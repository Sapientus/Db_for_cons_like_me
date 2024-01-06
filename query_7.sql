SELECT s.id, s.name, marks.mark
FROM students AS s
JOIN marks ON s.id=marks.student_id_fk
WHERE s.group_id_fk=? AND marks.subject_id_fk=?
