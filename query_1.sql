SELECT s.id, s.name, AVG(marks.mark) as avm
FROM students as s
JOIN marks ON s.id=marks.student_id_fk
GROUP BY s.id, s.name
ORDER BY avm DESC
LIMIT 5