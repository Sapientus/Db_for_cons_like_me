from datetime import datetime
import faker
from random import randint
import sqlite3

STUDENTS_AMOUNT = (30, 50)
TEACHERS_AMOUNT = (3, 5)
GROUPS_AMOUNT = (3, 5)
SUBJECTS_AMOUNT = (6, 9)

fake_data = faker.Faker()


def create_fake_data():  # this creates names and ids of our main tables, we get tuple as a result
    fake_students = []
    fake_teachers = []
    fake_groups = []
    fake_subjects = []
    for _ in range(randint(STUDENTS_AMOUNT[0], STUDENTS_AMOUNT[1])):
        fake_students.append(fake_data.name())
    for _ in range(randint(TEACHERS_AMOUNT[0], TEACHERS_AMOUNT[1])):
        fake_teachers.append(fake_data.name())
    for _ in range(randint(GROUPS_AMOUNT[0], GROUPS_AMOUNT[1])):
        fake_groups.append(f"Group {randint(0, 20)}")
    for _ in range(randint(SUBJECTS_AMOUNT[0], SUBJECTS_AMOUNT[1])):
        fake_subjects.append(fake_data.word())
    return fake_students, fake_teachers, fake_groups, fake_subjects


def prepare_data(
    students, teachers, groups, subjects
) -> tuple:  # this fills tables with multiple info
    for_groups = []  # create tuple`s list of groups. I'll do it for other tables, too
    for group in groups:
        for_groups.append((group,))
    for_students = []
    for student in students:
        for_students.append((student, randint(1, len(groups))))
    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher, randint(25, 60)))
    for_subjects = []
    for subject in subjects:
        for_subjects.append((subject, randint(1, len(teachers))))
    for_marks = []
    for month in range(1, 13):
        mark_date = datetime(2023, month, randint(10, 20)).date()
        for key in range(1, len(students) + 1):
            for_marks.append(
                (key, randint(1, len(subjects)), randint(0, 100), mark_date)
            )
    return for_students, for_teachers, for_groups, for_subjects, for_marks


def insert_to_db(students, teachers, groups, subjects, marks): #this inserts all info into our tables
    with sqlite3.connect("school.db") as con:
        cur = con.cursor()

        sql_to_students = """INSERT INTO students(name, group_id_fk)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)

        sql_to_teachers = """INSERT INTO teachers(teacher_name, teacher_age)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_groups = """INSERT INTO groups(group_name)
                              VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_subjects = """INSERT INTO subjects(subject_name, teacher_id_fk)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_marks = """INSERT INTO marks(student_id_fk, subject_id_fk, mark, mark_date)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_marks, marks)

        con.commit()


def main():
    students, teachers, groups, subjects, marks = prepare_data(*create_fake_data())
    insert_to_db(students, teachers, groups, subjects, marks)


if __name__ == "__main__":
    main()
