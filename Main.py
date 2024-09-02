import Admin as a
import Exam as e
import pandas as pd
# df = pd.DataFrame()
Acess_code = 123
std_code = 567
ac_check = int(input("Please Enter Acess code"))
df = None
if ac_check == Acess_code:
    print("Welcome to Admin")
    choice = int(input("Please enter your Choice \n 1 for Adding a student \n 2 for Updating a Student data \n 3 for deleting a student Data \n 4 for searching a Student User_ID \n 5 For creating an Exam \n" ))
    if choice == 1:
        a.data_enter_student()
    elif choice == 2:
        a.update_student()
    elif choice == 3:
        a.delete_data_student()
    elif choice == 4:
        a.search_for_student()
    else:
        choice = input("Enter the subject of which the exam you want to create \n for Maths type M \n for Physics type P \n for Chemistry type C\n")
        df = e.create_exam(choice)
        df.to_csv('exam_data.csv', index=False)
elif ac_check == std_code:
    
    print("Welcome to Student")
    choice1 = int(input("Enter 1 to take your saved exam or 2 to exit the interface"))
    if choice1 == 1:

        df = pd.read_csv('exam_data.csv')
        dff = pd.DataFrame(df)
        #print(dff)
        e.take_exam(dff)

    else:
        pass
else:
    print("Wrong Acess code")
