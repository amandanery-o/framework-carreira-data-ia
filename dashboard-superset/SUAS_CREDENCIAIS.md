## Criar arquivo .env

No terminal, execute:

```bash
cd "/Users/amandanery/Workspace/trilha de carreira data & ia/dashboard-superset"

# Criar o arquivo .env
cat > .env << 'EOF'
DB_HOST=aws-1-us-east-1.pooler.supabase.com
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres.kcttjldhmdjyvlyealfn
DB_PASSWORD=SUBSTITUA_PELA_SUA_SENHA_REAL
EOF
```

**IMPORTANTE:** Substitua `SUBSTITUA_PELA_SUA_SENHA_REAL` pela sua senha real do Supabase!

---

## Ou edite manualmente:

```bash
cd "/Users/amandanery/Workspace/trilha de carreira data & ia/dashboard-superset"
nano .env
```

Cole:
```
DB_HOST=aws-1-us-east-1.pooler.supabase.com
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres.kcttjldhmdjyvlyealfn
DB_PASSWORD=sua_senha_real_aqui
```

Salve: `Ctrl+O`, `Enter`, `Ctrl+X`

---

## 🗄️ Próximo: Criar Schema no Supabase

1. Entre em: https://supabase.com
2. Seu projeto
3. **SQL Editor → + New query**
4. Cole o conteúdo de: `sql/schema.sql`
5. Clique **RUN**

Depois volte aqui! ✅

