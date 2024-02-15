-- Список курсів, які певному студенту читає певний викладач.
SELECT s.subject_, t.teacher, st.student AS students 
FROM marks_nnij AS m 
LEFT JOIN subjects_nnij AS s ON m.id=m.students_nnij_id
LEFT JOIN teachers_nnij AS t ON m.id=s.teachers_nnij_id
LEFT JOIN students_nnij AS st ON m.id=m.students_nnij_id
GROUP BY s.id