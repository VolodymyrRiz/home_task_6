-- Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT Subj.subject_ AS Subject_, t.teacher AS Teacher, avg(m.mark) as averageMark
FROM subjects_nnij AS Subj
LEFT JOIN marks_nnij AS m ON Subj.id=m.subjects_nnij_id
LEFT JOIN teachers_nnij AS t ON t.id=Subj.id