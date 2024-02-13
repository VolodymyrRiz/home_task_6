-- Знайти список курсів, які відвідує студент.
SELECT s.subject_, st.student AS teachers
FROM marks_nnij AS m 
LEFT JOIN subjects_nnij AS s ON m.id=m.students_nnij_id
LEFT JOIN students_nnij AS st ON m.id=m.students_nnij_id