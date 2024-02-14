-- Знайти середній бал у групах з певного предмета.
SELECT sub.subject_, g.id AS groupID, avg(m.mark) as averageMark
FROM marks_nnij AS m
LEFT JOIN subjects_nnij AS sub ON sub.id=m.subjects_nnij_id
LEFT JOIN groups_nnij AS g ON g.id=sub.id
WHERE g.id IN (SELECT id
FROM groups_nnij
WHERE id=2)