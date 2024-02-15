-- Знайти список курсів, які відвідує студент.
SELECT m.subjects_nnij_id, s.subject_, st.student
FROM marks_nnij AS m 
LEFT JOIN subjects_nnij AS s ON s.id=m.subjects_nnij_id
LEFT JOIN students_nnij AS st ON s.id=m.students_nnij_id
GROUP BY s.id