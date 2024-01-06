import create_db
import fill_data
import select_request


if __name__ == "__main__":
    talk_to_user = input('Do you wanna create database? Type "yes" or "no". ')
    if talk_to_user == "yes":
        create_db.create_db()
        fill_data.main()
        print(
            'Database with name "school" was created. Now you may connect it with you application.'
        )
        select_request.main()
    elif talk_to_user == "no":
        print("Ok, have a nice day!")
    else:
        print('The answer should be "yes" or "no"!')
