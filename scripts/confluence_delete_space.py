#!/usr/bin/env python3
"""
Delete all Confluence pages in a space.

Safety:
- DRY_RUN=true by default (prints what would be deleted).
- Set CONFIRM_DELETE=YES to actually delete.
"""

import os
import sys
import requests
from requests.auth import HTTPBasicAuth

CONFLUENCE_URL = os.getenv("CONFLUENCE_URL", "").rstrip("/")
CONFLUENCE_USERNAME = os.getenv("CONFLUENCE_USERNAME", "")
CONFLUENCE_API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN", "")
CONFLUENCE_SPACE_KEY = os.getenv("CONFLUENCE_SPACE_KEY", "")

DRY_RUN = os.getenv("DRY_RUN", "true").lower() != "false"
CONFIRM_DELETE = os.getenv("CONFIRM_DELETE", "") == "YES"


def require_env():
    missing = []
    if not CONFLUENCE_URL:
        missing.append("CONFLUENCE_URL")
    if not CONFLUENCE_USERNAME:
        missing.append("CONFLUENCE_USERNAME")
    if not CONFLUENCE_API_TOKEN:
        missing.append("CONFLUENCE_API_TOKEN")
    if not CONFLUENCE_SPACE_KEY:
        missing.append("CONFLUENCE_SPACE_KEY")
    if missing:
        print("❌ ERRO: Variáveis de ambiente ausentes:")
        for name in missing:
            print(f"   - {name}")
        sys.exit(1)


def fetch_pages(space_key, auth):
    pages = []
    start = 0
    limit = 100
    while True:
        params = {
            "spaceKey": space_key,
            "type": "page",
            "limit": limit,
            "start": start,
        }
        url = f"{CONFLUENCE_URL}/wiki/rest/api/content"
        resp = requests.get(url, auth=auth, params=params, timeout=30)
        if resp.status_code != 200:
            print(f"❌ Erro ao listar páginas: {resp.status_code} - {resp.text[:200]}")
            sys.exit(1)
        data = resp.json()
        results = data.get("results", [])
        pages.extend(results)
        if len(results) < limit:
            break
        start += limit
    return pages


def delete_page(page_id, auth):
    url = f"{CONFLUENCE_URL}/wiki/rest/api/content/{page_id}"
    resp = requests.delete(url, auth=auth, timeout=30)
    if resp.status_code == 204:
        return True
    print(f"❌ Falha ao deletar {page_id}: {resp.status_code} - {resp.text[:200]}")
    return False


def main():
    require_env()

    auth = HTTPBasicAuth(CONFLUENCE_USERNAME, CONFLUENCE_API_TOKEN)
    pages = fetch_pages(CONFLUENCE_SPACE_KEY, auth)

    print(f"Encontradas {len(pages)} páginas no espaço {CONFLUENCE_SPACE_KEY}.")
    for p in pages:
        print(f"- {p.get('id')} | {p.get('title')}")

    if DRY_RUN:
        print("\nDRY_RUN ativo. Nenhuma página foi deletada.")
        print("Para deletar de fato, rode com DRY_RUN=false e CONFIRM_DELETE=YES.")
        return

    if not CONFIRM_DELETE:
        print("\nCONFIRM_DELETE!=YES. Nenhuma página foi deletada.")
        return

    print("\nIniciando deleção...")
    success = 0
    for p in pages:
        if delete_page(p.get("id"), auth):
            success += 1
            print(f"✅ Deletada: {p.get('title')}")

    print(f"\nConcluído. Deletadas {success}/{len(pages)} páginas.")


if __name__ == "__main__":
    main()
