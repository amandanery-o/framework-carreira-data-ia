-- Query: Skills por Trilha e Nível
-- Descrição: Tabela de skills técnicas filtrada por nível e trilha
-- Uso no Superset: Chart tipo Table

-- Parâmetros no Superset:
-- {{ nivel_selecionado }} (default: 'SE II (Pleno)')
-- {{ trilha_selecionada }} (default: 'Data Engineering')

SELECT 
    categoria as "Categoria",
    skill as "Skill",
    nivel_esperado as "Nível Esperado",
    detalhes as "Detalhes"
FROM skills_consolidadas
WHERE 
    nivel_nome = '{{ nivel_selecionado | default("SE II (Pleno)") }}'
    AND trilha = '{{ trilha_selecionada | default("Data Engineering") }}'
ORDER BY categoria, skill;

