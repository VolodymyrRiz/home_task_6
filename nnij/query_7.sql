-- Знайти оцінки студентів у окремій групі з певного предмета.
SELECT st.student, sub.subject_, m.mark AS Marks
FROM students_nnij AS st
JOIN subjects_nnij AS sub ON sub.id=1
LEFT JOIN marks_nnij AS m ON st.id=m.id
WHERE st.groups_nnij_id IN (SELECT id
FROM groups_nnij
WHERE name_="0")
