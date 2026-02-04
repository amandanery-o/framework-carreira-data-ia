#!/usr/bin/env python3
"""
Script para traduzir termos em inglês para português nos arquivos do framework
"""

import os
import re
from pathlib import Path

# Mapeamento de traduções
TRADUCOES = {
    # Termos técnicos comuns
    r'\bcode review\b': 'revisão de código',
    r'\bCode Review\b': 'Revisão de Código',
    r'\bcode reviews\b': 'revisões de código',
    r'\bCode Reviews\b': 'Revisões de Código',
    
    r'\bpair programming\b': 'programação em par',
    r'\bPair Programming\b': 'Programação em Par',
    
    r'\btech talk\b': 'palestra técnica',
    r'\bTech Talk\b': 'Palestra Técnica',
    r'\btech talks\b': 'palestras técnicas',
    r'\bTech Talks\b': 'Palestras Técnicas',
    
    r'\bonboarding\b': 'integração',
    r'\bOnboarding\b': 'Integração',
    
    r'\bstandup\b': 'reunião diária',
    r'\bStandup\b': 'Reunião Diária',
    r'\bstandups\b': 'reuniões diárias',
    
    r'\bdaily\b': 'diária',  # quando usado como substantivo (daily meeting)
    r'\bDaily\b': 'Diária',
    r'\bdailies\b': 'diárias',
    
    # Termos de gestão (manter alguns que são muito usados)
    r'\bstakeholder\b': 'parte interessada',
    r'\bStakeholder\b': 'Parte Interessada',
    r'\bstakeholders\b': 'partes interessadas',
    r'\bStakeholders\b': 'Partes Interessadas',
    
    # Performance pode ser mantido em alguns contextos, mas traduzir quando usado como "desempenho"
    # Vou ser cuidadoso aqui - só traduzir quando claramente significa "desempenho"
    
    # Roadmap - traduzir para roteiro
    r'\broadmap\b': 'roteiro',
    r'\bRoadmap\b': 'Roteiro',
    r'\broadmaps\b': 'roteiros',
    r'\bRoadmaps\b': 'Roteiros',
    
    # Feedback - traduzir para retroalimentação (mas manter em alguns contextos técnicos)
    r'\bfeedback\b': 'retroalimentação',
    r'\bFeedback\b': 'Retroalimentação',
    r'\bfeedbacks\b': 'retroalimentações',
    
    # Sprint - termo muito usado em ágil, mas podemos traduzir
    r'\bsprint\b': 'iteração',
    r'\bSprint\b': 'Iteração',
    r'\bsprints\b': 'iterações',
    r'\bSprints\b': 'Iterações',
    
    # Performance - traduzir quando usado como "desempenho"
    r'\bperformance\b': 'desempenho',
    r'\bPerformance\b': 'Desempenho',
    
    # Check-in - pode manter ou traduzir
    r'\bcheck-in\b': 'acompanhamento',
    r'\bCheck-in\b': 'Acompanhamento',
    r'\bcheck-ins\b': 'acompanhamentos',
    r'\bCheck-ins\b': 'Acompanhamentos',
}

# Arquivos para processar (focando nos principais do framework)
ARQUIVOS_PRIORITARIOS = [
    'docs/levels/',
    'docs/competencies/',
    'docs/culture/',
]

def traduzir_arquivo(caminho_arquivo):
    """Traduz termos em um arquivo"""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        conteudo_original = conteudo
        
        # Aplica todas as traduções
        for padrao_en, traducao_pt in TRADUCOES.items():
            conteudo = re.sub(padrao_en, traducao_pt, conteudo, flags=re.IGNORECASE)
        
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
                if traduzir_arquivo(arquivo):
                    arquivos_modificados += 1
                    print(f"✅ Traduzido: {arquivo.relative_to(base_dir)}")
    
    print(f"\n📊 Resumo:")
    print(f"   Arquivos processados: {arquivos_processados}")
    print(f"   Arquivos modificados: {arquivos_modificados}")

if __name__ == "__main__":
    main()
