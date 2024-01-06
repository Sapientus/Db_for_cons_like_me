SELECT s.id, s.name, subjects.subject_name, AVG(marks.mark) as avm
FROM students AS s
JOIN marks ON s.id=marks.student_id_fk
JOIN subjects ON marks.subject_id_fk=subjects.id_subject
WHERE marks.subject_id_fk=?
GROUP BY s.id, s.name
ORDER BY avm DESC
LIMIT 1