import Admin as a
import Exam as e
import pandas as pd
import time as t
import mysql.connector as sql

Acess_code = 123
import mysql.connector as sql

conn = sql.connect(host="localhost", user="root", password="root", database="student_info")

ac_check = int(input("Please Enter Access code"))

cursor = conn.cursor()

query = "SELECT access_code FROM access_code WHERE access_code = %s"
cursor.execute(query,(ac_check,))
rows = cursor.fetchall()
df1 = pd.DataFrame(rows , columns=['Access_code'])

if ac_check == Acess_code:
    while ac_check == Acess_code:
    
        print("Welcome to Admin")
        choice = int(input("Please enter your Choice \n 1 for Adding a student \n 2 for Updating a Student data \n 3 for deleting a student Data \n 4 for searching a Student User_ID \n 5 For showing Acceess code of student \n 6 For creating an Exam \n 7 TO exit the interface" ))
        if choice == 1:
            a.data_enter_student()
            t.sleep(5)
        elif choice == 2:
            a.update_student()
            t.sleep(5)
        elif choice == 3:
            a.delete_data_student()
            t.sleep(5)
        elif choice == 4:
            a.search_for_student()
            t.sleep(5)
        elif choice == 5:
            a.show_acces_code()
            t.sleep(5)
        elif choice == 6:       # ask_std_id = input("Enter student id for which you want to create an exam")
            choice = input("Enter the subject of which the exam you want to create \n for Maths type M \n for Physics type P \n for Chemistry type C\n")
            df = e.create_exam(choice)
            df.to_csv('exam_data.csv', index=False)
        elif choice == 7:
            break
    # elif ac_check in a.access_codes.values():
   
    else:
        print("Invalid access code. Please try again.")
        ac_check = int(input("Please Enter Access code"))
elif ac_check == df1['Access_code'][0]:
    
    print("Welcome to Student")
        
    choice1 = int(input("Enter 1 to take your saved exam or 2 to exit the interface"))
    if choice1 == 1:

        df = pd.read_csv('exam_data.csv')
        dff = pd.DataFrame(df)
            #print(dff)
        e.take_exam(dff)
    
cursor.close()
conn.close()
