SELECT s.subject_name
FROM subjects AS s
JOIN teachers ON s.teacher_id_fk=teachers.id_teacher
JOIN marks ON s.id_subject=marks.subject_id_fk
WHERE marks.student_id_fk=? AND s.teacher_id_fk=?
GROUP BY s.subject_name