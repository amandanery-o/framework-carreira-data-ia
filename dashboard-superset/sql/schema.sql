-- Schema para Dashboard Superset - Framework de Carreira
-- PostgreSQL

-- ============================================
-- Tabela: niveis
-- Armazena informações básicas de cada nível
-- ============================================
CREATE TABLE IF NOT EXISTS niveis (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE, -- Ex: "SE II (Pleno)"
    ordem INT NOT NULL, -- Para ordenação: 1=SE I, 2=SE II, etc
    escopo TEXT,
    alcance_colaborativo TEXT,
    alavancas TEXT,
    tipo VARCHAR(20) DEFAULT 'IC', -- 'IC' ou 'Management'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices
CREATE INDEX idx_niveis_ordem ON niveis(ordem);
CREATE INDEX idx_niveis_tipo ON niveis(tipo);

-- ============================================
-- Tabela: expectativas
-- Expectativas por dimensão e nível
-- ============================================
CREATE TABLE IF NOT EXISTS expectativas (
    id SERIAL PRIMARY KEY,
    nivel_id INT NOT NULL REFERENCES niveis(id) ON DELETE CASCADE,
    dimensao VARCHAR(50) NOT NULL, -- "Results", "Direction", "Talent", "Culture"
    subdimensao VARCHAR(50), -- "Impact", "Ownership", "Decision Making"
    descricao TEXT NOT NULL,
    nota_esperada DECIMAL(2,1) CHECK (nota_esperada >= 0 AND nota_esperada <= 5),
    ordem INT, -- Para manter ordem das subdimensões
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices
CREATE INDEX idx_expectativas_nivel ON expectativas(nivel_id);
CREATE INDEX idx_expectativas_dimensao ON expectativas(dimensao);

-- ============================================
-- Tabela: skills
-- Skills técnicas por trilha e nível
-- ============================================
CREATE TABLE IF NOT EXISTS skills (
    id SERIAL PRIMARY KEY,
    nivel_id INT NOT NULL REFERENCES niveis(id) ON DELETE CASCADE,
    trilha VARCHAR(50) NOT NULL, -- "Data Engineering", "Analytics Engineering", "Cientista de Dados"
    categoria VARCHAR(100) NOT NULL, -- "SQL", "Python", "dbt", "ML", etc
    skill VARCHAR(200) NOT NULL, -- Skill específica
    nivel_esperado VARCHAR(50), -- "Básico", "Intermediário", "Avançado", "Expert"
    detalhes TEXT, -- Descrição detalhada da skill
    ordem INT, -- Para manter ordem de exibição
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices
CREATE INDEX idx_skills_nivel ON skills(nivel_id);
CREATE INDEX idx_skills_trilha ON skills(trilha);
CREATE INDEX idx_skills_categoria ON skills(categoria);

-- ============================================
-- Tabela: valores_gupy
-- Como valores Gupy se manifestam por nível
-- ============================================
CREATE TABLE IF NOT EXISTS valores_gupy (
    id SERIAL PRIMARY KEY,
    nivel_id INT NOT NULL REFERENCES niveis(id) ON DELETE CASCADE,
    valor VARCHAR(100) NOT NULL, -- "Obsessão pelo Cliente", etc
    manifestacao TEXT NOT NULL, -- Como o valor se manifesta nesse nível
    exemplos TEXT, -- Exemplos práticos
    ordem INT, -- Para manter ordem dos 5 valores
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices
CREATE INDEX idx_valores_nivel ON valores_gupy(nivel_id);
CREATE INDEX idx_valores_valor ON valores_gupy(valor);

-- ============================================
-- View: radar_expectativas
-- View consolidada para gráfico radar
-- ============================================
CREATE OR REPLACE VIEW radar_expectativas AS
SELECT 
    n.id as nivel_id,
    n.nome as nivel_nome,
    n.ordem as nivel_ordem,
    e.dimensao,
    AVG(e.nota_esperada) as nota_media
FROM niveis n
LEFT JOIN expectativas e ON n.id = e.nivel_id
GROUP BY n.id, n.nome, n.ordem, e.dimensao
ORDER BY n.ordem, e.dimensao;

-- ============================================
-- View: skills_consolidadas
-- View para tabela de skills
-- ============================================
CREATE OR REPLACE VIEW skills_consolidadas AS
SELECT 
    n.id as nivel_id,
    n.nome as nivel_nome,
    n.ordem as nivel_ordem,
    s.trilha,
    s.categoria,
    s.skill,
    s.nivel_esperado,
    s.detalhes
FROM niveis n
LEFT JOIN skills s ON n.id = s.nivel_id
ORDER BY n.ordem, s.trilha, s.categoria, s.ordem;

-- ============================================
-- View: comparacao_niveis
-- View para comparar níveis adjacentes
-- ============================================
CREATE OR REPLACE VIEW comparacao_niveis AS
SELECT 
    n1.id as nivel_atual_id,
    n1.nome as nivel_atual,
    n1.ordem as nivel_atual_ordem,
    n2.id as nivel_proximo_id,
    n2.nome as nivel_proximo,
    n2.ordem as nivel_proximo_ordem,
    e1.dimensao,
    e1.nota_esperada as nota_atual,
    e2.nota_esperada as nota_proximo,
    (e2.nota_esperada - e1.nota_esperada) as gap
FROM niveis n1
JOIN niveis n2 ON n2.ordem = n1.ordem + 1 AND n2.tipo = n1.tipo
LEFT JOIN expectativas e1 ON n1.id = e1.nivel_id
LEFT JOIN expectativas e2 ON n2.id = e2.nivel_id AND e2.dimensao = e1.dimensao
WHERE e1.subdimensao IS NULL -- Apenas notas gerais por dimensão
ORDER BY n1.ordem, e1.dimensao;

-- ============================================
-- View: valores_por_nivel
-- View consolidada dos valores Gupy
-- ============================================
CREATE OR REPLACE VIEW valores_por_nivel AS
SELECT 
    n.id as nivel_id,
    n.nome as nivel_nome,
    n.ordem as nivel_ordem,
    v.valor,
    v.manifestacao,
    v.exemplos
FROM niveis n
LEFT JOIN valores_gupy v ON n.id = v.nivel_id
ORDER BY n.ordem, v.ordem;

-- ============================================
-- Comentários nas tabelas (documentação)
-- ============================================
COMMENT ON TABLE niveis IS 'Níveis de carreira (SE I → Principal, TL, EM)';
COMMENT ON TABLE expectativas IS 'Expectativas comportamentais por dimensão e nível';
COMMENT ON TABLE skills IS 'Skills técnicas por trilha (Data Eng, Analytics, Cientista)';
COMMENT ON TABLE valores_gupy IS 'Como valores Gupy se manifestam em cada nível';

COMMENT ON COLUMN niveis.ordem IS 'Ordem hierárquica: 1=SE I, 2=SE II, ..., 7=Principal';
COMMENT ON COLUMN expectativas.nota_esperada IS 'Nota esperada 0-5 para a dimensão/subdimensão';
COMMENT ON COLUMN skills.nivel_esperado IS 'Nível de proficiência: Básico/Intermediário/Avançado/Expert';

-- ============================================
-- Grants (ajustar conforme necessário)
-- ============================================
-- GRANT SELECT ON ALL TABLES IN SCHEMA public TO superset_user;
-- GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO superset_user;

