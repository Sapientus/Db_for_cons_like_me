SELECT g.id_group, g.group_name, subjects.subject_name, AVG(marks.mark) as avm
FROM groups AS g
JOIN students ON g.id_group=students.group_id_fk
JOIN marks ON students.id=marks.student_id_fk
JOIN subjects ON marks.subject_id_fk=subjects.id_subject
WHERE marks.subject_id_fk=?
GROUP BY g.id_group, g.group_name