-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT st.student, AVG(m.mark) as averageMark
FROM students_nnij AS st
LEFT JOIN marks_nnij AS m ON st.id=m.students_nnij_id
GROUP BY st.id
HAVING st.id < 6