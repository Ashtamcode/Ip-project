import mysql.connector as sql

def data_enter_student():
    conn=sql.connect(host="localhost",user="root",password="root",database="student_info")
    cursor = conn.cursor()
    User_Id = str(input("Please Enter your student Email ID:"))
    Password = str(input("Enter your password:"))
    Name = str(input('Please enter your name:'))
    DOB = str(input('Enter your Date of Birth in YYYY-MM-DD Format: '))
    Phone_no = str(input("Please enter you Phone number:"))
    qry = ('INSERT INTO Student_info values(%s,%s,%s,%s,%s)')
    data = (User_Id,Password,Name,DOB,Phone_no)
    cursor.execute(qry,data)
    conn.commit()
    conn.close()
    print("Record Inserted")

def delete_data_student():
    conn=sql.connect(host="localhost",user="root",password="root",database="student_info")
    Cursor = conn.cursor()
    User_ID = input("Enter User_ID of Student to be deleted : ")
    Qry = ("""DELETE FROM Student_info WHERE User_ID = %s""")
    del_rec = (User_ID,)
    Cursor.execute(Qry, del_rec)
    conn.commit()
    Cursor.close()
    conn.close()
    print("Record Deleted")

def update_student():
    conn = sql.connect(host="localhost", user="root", password="root", database="student_info")
    Cursor = conn.cursor()
    User_ID = input("Enter User_ID of Student to be updated : ")
    data = input("Enter the field of which data is to be updated")
    if data.upper == 'User_ID':

        n_user_Id = str(input("Please Enter your student Email ID:"))
 
    n_Password = str(input("Enter your password:"))
    n_Name = str(input('Please enter your name:'))
    n_DOB = str(input('Enter your Date of Birth in YYYY-MM-DD Format '))
    n_Phone_no = str(input("Please enter you Phone number:"))
    data = (n_user_Id,n_Password,n_Name,n_DOB,n_Phone_no , User_ID)
    qry = ("UPDATE student_info SET User_ID=%s, Password=%s, Name= %s, DOB = %s , Phone_no=%s WHERE User_ID  = %s")
    Cursor.execute(qry,data)
    conn.commit()
    Cursor.close()
    conn.close()
    print("Record Updated")

def search_for_student():
    conn = sql.connect(host="localhost", user="root", password="root", database="student_info")
    Cursor = conn.cursor()
    User_ID = input("Enter User_ID of Student to be searched : ")
    qry = ("SELECT * FROM Student_info WHERE User_ID = %s")
    data = (User_ID,)
    Cursor.execute(qry, data)
    for (User_Id,Password,Name,DOB,Phone_no) in Cursor:
        print("User_Id: ", User_Id)
        print("Password: ", Password)
        print("Name: ", Name)
        print("DOB: ", DOB)
        print("Phone_no: ", Phone_no)
    conn.commit()
    Cursor.close()
    conn.close()


