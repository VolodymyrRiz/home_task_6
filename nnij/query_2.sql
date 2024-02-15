-- Знайти студента із найвищим середнім балом з певного предмета.
SELECT st.student, Subj.subject_ AS Subject_, AVG(m.mark) as averageMark
FROM students_nnij AS st
LEFT JOIN marks_nnij AS m ON st.id=m.students_nnij_id
LEFT JOIN subjects_nnij AS Subj ON Subj.id=m.subjects_nnij_id
WHERE st.id>=1 AND st.id<=30
GROUP BY Subj.id