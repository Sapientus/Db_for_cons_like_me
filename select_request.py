import sqlite3


def read_sql(num):  # it allows us to read scripts of needed request
    with open(f"query_{num}.sql", "r") as f:
        query = f.read()

    return query


def execute_query(
    sql: str,
) -> list:  # this one checks the request's number and execute operations
    with sqlite3.connect("school.db") as con:
        cur = con.cursor()
        sentence_for_input = ""
        # I f*cked myself again just because I wanted to be more clear for uses so I did a lot of checks
        if sql in ["2", "3"]:
            sentence_for_input = input("Input subject id: ")
        elif sql == "5":
            sentence_for_input = input("Input teacher`s id: ")
        elif sql == "6":
            sentence_for_input = input("Input group`s id: ")
        elif sql == "7":
            sentence_for_input = input(
                f'Input subject`s id: {input("Input group`s id: ")}'
            )
        elif sql == "9":
            sentence_for_input = input("Input student`s id: ")
        elif sql == "10":
            sentence_for_input = input(
                f'Input teacher`s id: {input("Input student`s id: ")}'
            )
        cur.execute(read_sql(sql), sentence_for_input)
    return cur.fetchall()

def main():
    select_input = input("Input request number from 1 to 10: ")
    print(execute_query(select_input))

if __name__ == "__main__":
    main()