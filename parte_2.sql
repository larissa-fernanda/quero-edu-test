-- pergunta 1
SELECT
    cursos.name,
    ROUND(SUM(compras.mensalidade), 2) as somatoria
FROM
    cursos
INNER JOIN
    compras ON
    cursos.id = compras.course_id
GROUP BY
    cursos.name

-- pergunta 2
SELECT
    *
FROM
    compras
WHERE
    mensalidade > 110

-- pergunta 3
SELECT
    cursos.*
FROM
    cursos
LEFT JOIN
    compras ON
    cursos.id = compras.course_id
WHERE
    compras.id IS NULL
