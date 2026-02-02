#!/usr/bin/env python3
"""
Load CSVs → PostgreSQL

Carrega CSVs gerados no banco de dados.

Uso:
    # Configurar variáveis de ambiente primeiro:
    export DB_HOST=localhost
    export DB_PORT=5432
    export DB_NAME=framework_carreira
    export DB_USER=postgres
    export DB_PASSWORD=sua_senha
    
    python load_to_db.py

Ou criar arquivo .env na raiz do projeto dashboard-superset/
"""

import os
import sys
import csv
from pathlib import Path
import psycopg2
from psycopg2.extras import execute_batch
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Paths
DATA_DIR = Path(__file__).parent.parent / "data"

# Configuração do banco
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "framework_carreira"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "")
}


def connect_db():
    """Conecta ao PostgreSQL."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print(f"✅ Conectado ao banco: {DB_CONFIG['database']}")
        return conn
    except Exception as e:
        print(f"❌ Erro ao conectar: {e}")
        raise


def load_csv_to_table(conn, csv_file: Path, table_name: str):
    """Carrega CSV para tabela."""
    if not csv_file.exists():
        print(f"⚠️  CSV não encontrado: {csv_file}")
        return
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    if not rows:
        print(f"⚠️  CSV vazio: {csv_file}")
        return
    
    # Preparar query
    columns = rows[0].keys()
    placeholders = ', '.join(['%s'] * len(columns))
    insert_query = f"""
        INSERT INTO {table_name} ({', '.join(columns)})
        VALUES ({placeholders})
        ON CONFLICT DO NOTHING
    """
    
    # Converter valores None para NULL
    data = []
    for row in rows:
        values = []
        for col in columns:
            val = row[col]
            if val == '' or val == 'None':
                values.append(None)
            else:
                values.append(val)
        data.append(tuple(values))
    
    # Executar batch insert
    cursor = conn.cursor()
    try:
        execute_batch(cursor, insert_query, data)
        conn.commit()
        print(f"✅ Carregado: {table_name} ({len(data)} linhas)")
    except Exception as e:
        conn.rollback()
        print(f"❌ Erro ao carregar {table_name}: {e}")
        raise
    finally:
        cursor.close()


def truncate_tables(conn):
    """Limpa tabelas antes de carregar (opcional)."""
    cursor = conn.cursor()
    try:
        print("🗑️  Limpando tabelas existentes...")
        cursor.execute("TRUNCATE TABLE valores_gupy, skills, expectativas, niveis RESTART IDENTITY CASCADE")
        conn.commit()
        print("✅ Tabelas limpas")
    except Exception as e:
        conn.rollback()
        print(f"⚠️  Erro ao limpar tabelas: {e}")
    finally:
        cursor.close()


def main():
    print("🚀 Carregando CSVs no banco...")
    print(f"📂 Data dir: {DATA_DIR}")
    print(f"🗄️  Database: {DB_CONFIG['database']} @ {DB_CONFIG['host']}")
    print()
    
    # Conectar
    conn = connect_db()
    
    try:
        # Opcional: Limpar tabelas
        # Use --truncate para limpar tabelas antes de carregar
        if len(sys.argv) > 1 and sys.argv[1] == '--truncate':
            truncate_tables(conn)
            print()
        
        # Carregar na ordem correta (por causa de foreign keys)
        load_csv_to_table(conn, DATA_DIR / "niveis.csv", "niveis")
        load_csv_to_table(conn, DATA_DIR / "expectativas.csv", "expectativas")
        load_csv_to_table(conn, DATA_DIR / "skills.csv", "skills")
        load_csv_to_table(conn, DATA_DIR / "valores_gupy.csv", "valores_gupy")
        
        print()
        print("✅ Carga completa!")
        print()
        print("🎯 Próximo passo: Configurar Superset")
        
    finally:
        conn.close()
        print("🔌 Conexão fechada")


if __name__ == "__main__":
    main()

