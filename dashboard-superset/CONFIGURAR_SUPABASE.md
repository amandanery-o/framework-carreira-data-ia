## Passo 1: Pegar suas credenciais

1. Entre em: https://supabase.com
2. Selecione seu projeto
3. Vá em: **Settings → Database**
4. Role até **Connection string**
5. Copie a URI no formato:
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.xxxxx.supabase.co:5432/postgres
   ```

---

## Passo 2: Criar arquivo .env

No terminal:

```bash
cd "/Users/amandanery/Workspace/trilha de carreira data & ia/dashboard-superset"

# Criar .env
cat > .env << 'EOF'
DB_HOST=db.SEU-PROJECT-REF.supabase.co
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=SUA-SENHA-AQUI
EOF
```

**OU simplesmente:**

```bash
nano .env
```

E cole:
```
DB_HOST=db.xxxxx.supabase.co
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=sua_senha
```

Salve com: `Ctrl+O`, `Enter`, `Ctrl+X`

---

## Passo 3: Criar o schema no Supabase

Você tem 2 opções:

### Opção A: Pelo SQL Editor do Supabase (Mais fácil)

1. No Supabase: **SQL Editor → New Query**
2. Cole o conteúdo de: `sql/schema.sql`
3. Clique em **Run**

### Opção B: Pelo terminal (se quiser)

```bash
psql "postgresql://postgres:[SUA-SENHA]@db.xxxxx.supabase.co:5432/postgres" -f sql/schema.sql
```

---

## Passo 4: Carregar os dados

Depois de criar o schema:

```bash
python scripts/load_to_db.py
```

Quando perguntar se quer limpar tabelas, digite: **s**

---

## ✅ Pronto!

Depois disso você pode:
- Ver os dados no Supabase (Table Editor)
- Conectar o Superset
- Ou criar queries SQL direto no Supabase

---

**Me chame quando chegar no Passo 4!** 😊

