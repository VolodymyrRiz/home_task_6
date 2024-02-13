-- Знайти які курси читає певний викладач.
SELECT t.teacher, s.subject_ AS subjects
FROM teachers_nnij AS t
INNER JOIN subjects_nnij AS s ON t.id = s.teachers_nnij_id
