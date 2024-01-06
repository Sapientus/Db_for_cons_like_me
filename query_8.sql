SELECT s.subject_name, AVG(marks.mark) AS avm
FROM subjects AS s
JOIN marks ON s.id_subject=marks.subject_id_fk
JOIN teachers ON s.teacher_id_fk=teachers.id_teacher
WHERE s.teacher_id_fk=?