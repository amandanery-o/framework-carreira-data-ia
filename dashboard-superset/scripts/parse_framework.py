#!/usr/bin/env python3
"""
Parse Framework Markdowns → CSV

Lê os arquivos markdown do framework e gera CSVs para carga no banco.

Uso:
    python parse_framework.py

Saída:
    ../data/niveis.csv
    ../data/expectativas.csv
    ../data/skills.csv
    ../data/valores_gupy.csv
"""

import os
import re
import csv
from pathlib import Path
from typing import List, Dict, Any

# Caminhos
REPO_ROOT = Path(__file__).parent.parent.parent
LEVELS_DIR = REPO_ROOT / "levels"
TRACKS_DIR = REPO_ROOT / "tracks"
CULTURE_DIR = REPO_ROOT / "culture"
OUTPUT_DIR = Path(__file__).parent.parent / "data"

# Criar pasta de output se não existir
OUTPUT_DIR.mkdir(exist_ok=True)

# ============================================
# Mapeamento de níveis
# ============================================
NIVEIS_MAPPING = {
    "SE_I_junior.md": {"nome": "SE I (Junior)", "ordem": 1, "tipo": "IC"},
    "SE_II_pleno.md": {"nome": "SE II (Pleno)", "ordem": 2, "tipo": "IC"},
    "SE_III_senior.md": {"nome": "SE III (Senior)", "ordem": 3, "tipo": "IC"},
    "Lead_engineer.md": {"nome": "Lead Engineer", "ordem": 4, "tipo": "IC"},
    "Staff_engineer.md": {"nome": "Staff Engineer", "ordem": 5, "tipo": "IC"},
    "Staff_II_senior_staff.md": {"nome": "Staff II (Senior Staff)", "ordem": 6, "tipo": "IC"},
    "Principal_engineer.md": {"nome": "Principal Engineer", "ordem": 7, "tipo": "IC"},
    "Tech_lead.md": {"nome": "Tech Lead", "ordem": 8, "tipo": "Management"},
    "Engineering_manager.md": {"nome": "Engineering Manager", "ordem": 9, "tipo": "Management"},
}

# Notas esperadas por nível (baseline)
NOTAS_BASELINE = {
    1: 2.0,  # SE I
    2: 3.0,  # SE II
    3: 4.0,  # SE III
    4: 4.5,  # Lead
    5: 5.0,  # Staff
    6: 5.0,  # Staff II
    7: 5.0,  # Principal
    8: 4.5,  # Tech Lead
    9: 4.5,  # EM
}


# ============================================
# Parse de Níveis
# ============================================
def parse_niveis() -> List[Dict[str, Any]]:
    """Parse informações básicas dos níveis."""
    niveis = []
    
    for filename, info in NIVEIS_MAPPING.items():
        filepath = LEVELS_DIR / filename
        
        if not filepath.exists():
            print(f"⚠️  Arquivo não encontrado: {filepath}")
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extrair escopo, alcance, alavancas (se disponível no markdown)
        # Por enquanto, deixar vazio - pode ser melhorado depois
        escopo = ""
        alcance = ""
        alavancas = ""
        
        niveis.append({
            "id": info["ordem"],
            "nome": info["nome"],
            "ordem": info["ordem"],
            "escopo": escopo,
            "alcance_colaborativo": alcance,
            "alavancas": alavancas,
            "tipo": info["tipo"]
        })
    
    return niveis


# ============================================
# Parse de Expectativas (Dimensões)
# ============================================
def parse_expectativas() -> List[Dict[str, Any]]:
    """Parse expectativas por dimensão."""
    expectativas = []
    id_counter = 1
    
    dimensoes = ["Results", "Direction", "Talent", "Culture"]
    
    for filename, info in NIVEIS_MAPPING.items():
        nivel_id = info["ordem"]
        nota_base = NOTAS_BASELINE.get(nivel_id, 3.0)
        
        for dimensao in dimensoes:
            expectativas.append({
                "id": id_counter,
                "nivel_id": nivel_id,
                "dimensao": dimensao,
                "subdimensao": None,
                "descricao": f"Expectativas de {dimensao} para {info['nome']}",
                "nota_esperada": nota_base,
                "ordem": None
            })
            id_counter += 1
    
    return expectativas


# ============================================
# Parse de Skills (Trilhas Técnicas)
# ============================================
def parse_skills() -> List[Dict[str, Any]]:
    """Parse skills técnicas das trilhas."""
    skills = []
    id_counter = 1
    
    trilhas = {
        "data_engineering.md": "Data Engineering",
        "analytics_engineering.md": "Analytics Engineering",
        "cientista_de_dados.md": "Cientista de Dados"
    }
    
    # Mapeamento de títulos de nível nos arquivos para nível_id
    nivel_patterns = {
        r'##\s+SE\s+I\s*[–-]\s*Junior': 1,
        r'##\s+SE\s+II\s*[–-]\s*Pleno': 2,
        r'##\s+SE\s+III\s*[–-]\s*Senior': 3,
        r'##\s+Lead\s+Engineer': 4,
        r'##\s+Staff\s+Engineer': 5,
        r'##\s+Staff\s+II\s*[–-]\s*Senior\s+Staff': 6,
        r'##\s+Principal\s+Engineer': 7
    }
    
    for filename, trilha_nome in trilhas.items():
        filepath = TRACKS_DIR / filename
        
        if not filepath.exists():
            print(f"⚠️  Arquivo não encontrado: {filepath}")
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Para cada nível, encontrar sua seção
        for pattern, nivel_id in nivel_patterns.items():
            # Encontrar a seção do nível (até o próximo ## ou fim do arquivo)
            match = re.search(rf'{pattern}(.*?)(?=^##\s+\S|\Z)', content, re.DOTALL | re.IGNORECASE | re.MULTILINE)
            
            if not match:
                continue
            
            nivel_section = match.group(1)
            
            # Extrair categorias (### Categoria)
            categorias = re.findall(r'###\s+(.*?)\n(.*?)(?=###|##|$)', nivel_section, re.DOTALL)
            
            for categoria_nome, categoria_content in categorias:
                categoria_nome_clean = categoria_nome.strip().replace(' (SE I+)', '').replace(' (SE II+)', '')
                
                # Extrair bullets (-) de cada categoria
                bullets = re.findall(r'^[-*]\s+(.+)$', categoria_content, re.MULTILINE)
                
                for bullet in bullets:
                    bullet_clean = bullet.strip()
                    
                    # Extrair "skill" (primeira parte até : ou –)
                    skill_match = re.match(r'(\*\*([^*]+)\*\*|([^:–]+))', bullet_clean)
                    if skill_match:
                        skill_nome = skill_match.group(2) or skill_match.group(3) or skill_match.group(1)
                        skill_nome = skill_nome.strip().replace('**', '')
                    else:
                        skill_nome = bullet_clean[:50]
                    
                    skills.append({
                        "id": id_counter,
                        "nivel_id": nivel_id,
                        "trilha": trilha_nome,
                        "categoria": categoria_nome_clean,
                        "skill": skill_nome,
                        "nivel_esperado": None,  # Não especificado explicitamente
                        "detalhes": bullet_clean,
                        "ordem": None
                    })
                    id_counter += 1
    
    return skills


# ============================================
# Parse de Valores Gupy
# ============================================
def parse_valores_gupy() -> List[Dict[str, Any]]:
    """Parse valores Gupy por nível do arquivo culture/mapping_to_gupy_culture.md."""
    valores = []
    id_counter = 1
    
    cultura_file = REPO_ROOT / "culture" / "mapping_to_gupy_culture.md"
    
    if not cultura_file.exists():
        print(f"⚠️  Arquivo não encontrado: {cultura_file}")
        return []
    
    with open(cultura_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Valores Gupy com seus emojis
    valores_patterns = [
        (r'##\s*🎯\s*Obsessão pelo Cliente', 'Obsessão pelo Cliente'),
        (r'##\s*💡\s*Paixão por Inovar', 'Paixão por Inovar'),
        (r'##\s*⚡\s*Agilidade para Resultado', 'Agilidade para Resultado'),
        (r'##\s*💰\s*Fazer Mais com Menos', 'Fazer Mais com Menos'),
        (r'##\s*🤝\s*Juntos!', 'Juntos!')
    ]
    
    # Mapeamento de nomes na tabela para os nomes dos níveis no sistema
    level_mapping = {
        'SE I-II': ['SE I (Junior)', 'SE II (Pleno)'],
        'SE III': ['SE III (Senior)'],
        'Lead': ['Lead Engineer'],
        'Staff': ['Staff Engineer', 'Staff II (Senior Staff)'],
        'Principal': ['Principal Engineer'],
        'TL': ['Tech Lead'],
        'EM': ['Engineering Manager']
    }
    
    for ordem, (pattern, valor_nome) in enumerate(valores_patterns, start=1):
        # Encontrar seção do valor
        match_section = re.search(rf'{pattern}(.*?)(?=##\s*[🎯💡⚡💰🤝]|$)', content, re.DOTALL)
        
        if not match_section:
            continue
        
        section_content = match_section.group(1)
        
        # Extrair linhas da tabela markdown
        table_lines = re.findall(r'\|\s*\*\*(.*?)\*\*\s*\|\s*(.*?)\s*\|', section_content)
        
        for table_nivel, manifestacao in table_lines:
            table_nivel_clean = table_nivel.strip()
            manifestacao_clean = manifestacao.strip()
            
            # Mapear para níveis no sistema
            mapped_levels = level_mapping.get(table_nivel_clean, [])
            
            for nivel_nome in mapped_levels:
                # Encontrar o nivel_id correto
                for filename, info in NIVEIS_MAPPING.items():
                    if info['nome'] == nivel_nome:
                        valores.append({
                            "id": id_counter,
                            "nivel_id": info['ordem'],
                            "valor": valor_nome,
                            "manifestacao": manifestacao_clean,
                            "exemplos": None,
                            "ordem": ordem
                        })
                        id_counter += 1
                        break
    
    return valores


# ============================================
# Exportar para CSV
# ============================================
def export_to_csv(data: List[Dict[str, Any]], filename: str):
    """Exporta lista de dicts para CSV."""
    if not data:
        print(f"⚠️  Nenhum dado para exportar: {filename}")
        return
    
    filepath = OUTPUT_DIR / filename
    
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    
    print(f"✅ Exportado: {filepath} ({len(data)} linhas)")


# ============================================
# Main
# ============================================
def main():
    print("🚀 Parseando framework...")
    print(f"📂 Repo root: {REPO_ROOT}")
    print(f"📂 Output: {OUTPUT_DIR}")
    print()
    
    # Parse
    niveis = parse_niveis()
    expectativas = parse_expectativas()
    skills = parse_skills()
    valores = parse_valores_gupy()
    
    # Export
    export_to_csv(niveis, "niveis.csv")
    export_to_csv(expectativas, "expectativas.csv")
    export_to_csv(skills, "skills.csv")
    export_to_csv(valores, "valores_gupy.csv")
    
    print()
    print("✅ Parse completo!")
    print()
    print("📊 Resumo:")
    print(f"   - Níveis: {len(niveis)}")
    print(f"   - Expectativas: {len(expectativas)}")
    print(f"   - Skills: {len(skills)}")
    print(f"   - Valores Gupy: {len(valores)}")
    print()
    print("🎯 Próximo passo: python scripts/load_to_db.py")


if __name__ == "__main__":
    main()

