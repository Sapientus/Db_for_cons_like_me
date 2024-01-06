DROP TABLE IF EXISTS students;
CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(30),
group_id_fk INT,
FOREIGN KEY (group_id_fk) REFERENCES groups(id_group));

DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
id_group INTEGER PRIMARY KEY AUTOINCREMENT,
group_name VARCHAR(30));

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
id_teacher INTEGER PRIMARY KEY AUTOINCREMENT,
teacher_name VARCHAR(30),
teacher_age TINYINT UNSIGNED);

DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
id_subject INTEGER PRIMARY KEY AUTOINCREMENT,
subject_name VARCHAR(30),
teacher_id_fk INT,
FOREIGN KEY (teacher_id_fk) REFERENCES teachers(id_teacher));

DROP TABLE IF EXISTS marks;
CREATE TABLE marks (
student_id_fk INT,
subject_id_fk INT,
mark INT CHECK (mark >= 0 AND mark <= 100),
mark_date DATE NOT NULL,
FOREIGN KEY (student_id_fk) REFERENCES students (id),
FOREIGN KEY (subject_id_fk) REFERENCES subjects (id_subject));