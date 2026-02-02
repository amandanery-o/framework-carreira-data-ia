-- Query: Radar de Expectativas
-- Descrição: Dados para gráfico radar das 5 dimensões por nível
-- Uso no Superset: Chart tipo Radar

-- Parametrização no Superset:
-- {{ nivel_selecionado }} (default: 'SE II (Pleno)')

SELECT 
    dimensao as "Dimensão",
    nota_media as "Nota Esperada"
FROM radar_expectativas
WHERE nivel_nome = '{{ nivel_selecionado | default("SE II (Pleno)") }}'
ORDER BY 
    CASE dimensao
        WHEN 'Results' THEN 1
        WHEN 'Direction' THEN 2
        WHEN 'Talent' THEN 3
        WHEN 'Culture' THEN 4
        WHEN 'Craft' THEN 5
    END;

