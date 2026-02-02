#!/usr/bin/env python3
"""
Script para traduzir termos restantes em inglês nos arquivos de levels
"""

import os
import re
from pathlib import Path

# Mapeamento de traduções adicionais
TRADUCOES = {
    # Títulos de seções - remover inglês e manter só português
    r'### Scope \(Escopo de atuação\)': '### Escopo de Atuação',
    r'### Collaborative Reach \(Alcance colaborativo\)': '### Alcance Colaborativo',
    r'### Impact Levers \(Alavancas de impacto\)': '### Alavancas de Impacto',
    r'## 🏆 Results \(Resultados\)': '## 🏆 Resultados',
    r'### Impact \(Impacto\)': '### Impacto',
    r'### Ownership \(Responsabilidade\)': '### Responsabilidade',
    r'### Decision Making \(Tomada de decisão\)': '### Tomada de Decisão',
    r'## 🌟 Direction \(Direção\)': '## 🌟 Direção',
    r'### Agility \(Agilidade\)': '### Agilidade',
    r'### Innovation \(Inovação\)': '### Inovação',
    r'### Strategy \(Estratégia\)': '### Estratégia',
    r'## 🌳 Talent \(Talento\)': '## 🌳 Talento',
    r'### Personal Growth \(Crescimento pessoal\)': '### Crescimento Pessoal',
    r'### Team Development \(Desenvolvimento do time\)': '### Desenvolvimento do Time',
    r'## 🌈 Culture \(Cultura\)': '## 🌈 Cultura',
    r'### Collaboration \(Colaboração\)': '### Colaboração',
    r'### Organizational Health \(Saúde organizacional\)': '### Saúde Organizacional',
    r'### Communication \(Comunicação\)': '### Comunicação',
    r'### Culture Leader \(Liderança cultural\)': '### Liderança Cultural',
    r'## 🛠️ Craft \(Habilidades Técnicas\)': '## 🛠️ Habilidades Técnicas',
    r'### Strategy and Change Management \(Estratégia e gestão de mudança\)': '### Estratégia e Gestão de Mudança',
    
    # Termos técnicos
    r'\bownership\b': 'responsabilidade',
    r'\bOwnership\b': 'Responsabilidade',
    r'\baccountability\b': 'prestação de contas',
    r'\bAccountability\b': 'Prestação de Contas',
    r'\bpeer\b': 'par',
    r'\bPeer\b': 'Par',
    r'\bpeers\b': 'pares',
    r'\bPeers\b': 'Pares',
    r'\bboard\b': 'diretoria',
    r'\bBoard\b': 'Diretoria',
    r'\bhands-on\b': 'prático',
    r'\bHands-on\b': 'Prático',
    r'\bpeople management\b': 'gestão de pessoas',
    r'\bPeople Management\b': 'Gestão de Pessoas',
    r'\bIC track\b': 'trilha IC',
    r'\bIC Track\b': 'Trilha IC',
    r'\bManagement Track\b': 'Trilha de Gestão',
    r'\bPR\b': 'Pull Request',
    r'\bsprint planning\b': 'planejamento de sprint',
    r'\bSprint Planning\b': 'Planejamento de Sprint',
    r'\bquarter\b': 'trimestre',
    r'\bQuarter\b': 'Trimestre',
    r'\bquarters\b': 'trimestres',
    r'\bQuarters\b': 'Trimestres',
    
    # Termos compostos
    r'\bIndustry Leadership\b': 'Liderança da Indústria',
    r'\bTechnical Leadership\b': 'Liderança Técnica',
    r'\bExecution\b': 'Execução',
    r'\bTechnical Excellence\b': 'Excelência Técnica',
    
    # Termos específicos que aparecem em contextos técnicos
    r'\bboard members\b': 'membros da diretoria',
    r'\bBoard Members\b': 'Membros da Diretoria',
    r'\bC-level\b': 'C-level',
    r'\bopen source\b': 'código aberto',
    r'\bOpen Source\b': 'Código Aberto',
}

# Arquivos para processar
ARQUIVOS_PRIORITARIOS = [
    'levels/',
]

def traduzir_arquivo(caminho_arquivo):
    """Traduz termos em um arquivo"""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        conteudo_original = conteudo
        
        # Aplica todas as traduções
        for padrao_en, traducao_pt in TRADUCOES.items():
            conteudo = re.sub(padrao_en, traducao_pt, conteudo)
        
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
