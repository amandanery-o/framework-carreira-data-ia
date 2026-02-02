-- Query: Comparação entre Níveis
-- Descrição: Comparar expectativas entre nível atual e próximo nível
-- Uso no Superset: Chart tipo Table com formatação condicional

-- Parâmetro no Superset:
-- {{ nivel_selecionado }} (default: 'SE II (Pleno)')

SELECT 
    dimensao as "Dimensão",
    nota_atual as "Nível Atual",
    nota_proximo as "Próximo Nível",
    gap as "Gap",
    CASE 
        WHEN gap < -0.5 THEN '🔴 Crítico'
        WHEN gap < 0 THEN '🟡 Desenvolver'
        ELSE '🟢 Pronto'
    END as "Status"
FROM comparacao_niveis
WHERE nivel_atual = '{{ nivel_selecionado | default("SE II (Pleno)") }}'
ORDER BY gap ASC;

