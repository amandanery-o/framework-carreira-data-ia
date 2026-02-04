#!/usr/bin/env python3
"""
Script para ajustar termos para versões mais comuns em português brasileiro
"""

import os
import re
from pathlib import Path

# Mapeamento de ajustes (termos mais comuns em português brasileiro)
AJUSTES = {
    # Retroalimentação → Feedback (mais comum em PT-BR)
    r'\bretroalimentação\b': 'feedback',
    r'\bRetroalimentação\b': 'Feedback',
    r'\bretroalimentações\b': 'feedbacks',
    r'\bRetroalimentações\b': 'Feedbacks',
    r'\bretroalimentação técnica\b': 'feedback técnico',
    r'\bRetroalimentação Técnica\b': 'Feedback Técnico',
    r'\bretroalimentação construtiva\b': 'feedback construtivo',
    r'\bRetroalimentação Construtiva\b': 'Feedback Construtivo',
    r'\bretroalimentação específica\b': 'feedback específico',
    r'\bRetroalimentação Específica\b': 'Feedback Específico',
    r'\bretroalimentação frequente\b': 'feedback frequente',
    r'\bRetroalimentação Frequente\b': 'Feedback Frequente',
    
    # Iteração → Sprint (mais comum em PT-BR)
    r'\biteração\b': 'sprint',
    r'\bIteração\b': 'Sprint',
    r'\biterações\b': 'sprints',
    r'\bIterações\b': 'Sprints',
    
    # Roteiro → Roadmap (mais comum em PT-BR)
    r'\broteiro\b': 'roadmap',
    r'\bRoteiro\b': 'Roadmap',
    r'\broteiros\b': 'roadmaps',
    r'\bRoteiros\b': 'Roadmaps',
}

# Arquivos para processar
ARQUIVOS_PRIORITARIOS = [
    'docs/levels/',
    'docs/competencies/',
    'docs/culture/',
]

def ajustar_arquivo(caminho_arquivo):
    """Ajusta termos em um arquivo"""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        conteudo_original = conteudo
        
        # Aplica todos os ajustes
        for padrao, substituicao in AJUSTES.items():
            conteudo = re.sub(padrao, substituicao, conteudo)
        
        # Só escreve se houve mudança
        if conteudo != conteudo_original:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo)
            return True
        
        return False
    except Exception as e:
        print(f"Erro ao processar {caminho_arquivo}: {e}")
        return False

def main():
    """Processa arquivos do framework"""
    base_dir = Path(__file__).parent.parent
    
    arquivos_processados = 0
    arquivos_modificados = 0
    
    # Processa arquivos prioritários
    for pasta in ARQUIVOS_PRIORITARIOS:
        pasta_path = base_dir / pasta
        if pasta_path.exists():
            for arquivo in pasta_path.rglob('*.md'):
                arquivos_processados += 1
                if ajustar_arquivo(arquivo):
                    arquivos_modificados += 1
                    print(f"✅ Ajustado: {arquivo.relative_to(base_dir)}")
    
    print(f"\n📊 Resumo:")
    print(f"   Arquivos processados: {arquivos_processados}")
    print(f"   Arquivos modificados: {arquivos_modificados}")

if __name__ == "__main__":
    main()
