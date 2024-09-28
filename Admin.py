import mysql.connector as sql
import random as r
access_codes = {}
def data_enter_student():
    conn = sql.connect(host="localhost", user="root", password="root", database="student_info")
    cursor = conn.cursor()
    User_Id = str(input("Please Enter your student Email ID:"))
    Name = str(input('Please enter your name:'))
    DOB = str(input('Enter your Date of Birth in YYYY-MM-DD Format: '))
    Phone_no = str(input("Please enter you Phone number:"))
    qry = ('INSERT INTO Student_info values(%s,%s,%s,%s)')
    access_codes_for_student = r.randint(100, 999)  # Generate a unique access code
    print(Name, access_codes_for_student)
    access_codes[Name] = access_codes_for_student  # Store the access code in the dictionary
    data = (User_Id, Name, DOB, Phone_no)
    cursor.execute(qry, data)
    conn.commit()
    
    # Insert access code into Access_codes table
    qry_access_codes = ('INSERT INTO access_code values(%s, %s)')
    data_access_codes = (Name, access_codes_for_student)
    cursor.execute(qry_access_codes, data_access_codes)
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
    if data.lower() == 'user_id':
        n_user_Id = str(input("Please Enter new User_ID"))
        qry = ("UPDATE student_info SET User_ID=%s WHERE User_ID = %s")
        new = (n_user_Id,User_ID)
        Cursor.execute(qry,new)
    elif data.lower() == 'name':
       n_Name = str(input('Please enter your name:'))
       qry = ("UPDATE student_info SET Name=%s WHERE User_ID = %s")
       new = (n_Name,User_ID)
       Cursor.execute(qry,new)
    elif data.lower() == 'dob' or data.strip().lower() == 'dateofbirth':
        n_DOB = str(input('Enter your Date of Birth in YYYY-MM-DD Format '))
        qry = ("UPDATE student_info SET DOB=%s WHERE User_ID = %s")
        new = (n_DOB,User_ID)
        Cursor.execute(qry,new)
    elif data.strip().lower() == 'phone_no':
        n_Phone_no = str(input("Please enter you Phone number:"))
        qry = ("UPDATE student_info SET Phone_no=%s WHERE User_ID = %s")
        new = (n_Phone_no,User_ID)
        Cursor.execute(qry,new)
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
    for (User_Id,Name,DOB,Phone_no) in Cursor:
        print("User_Id: ", User_Id)
        print("Name: ", Name)
        print("DOB: ", DOB)
        print("Phone_no: ", Phone_no)
    conn.commit()
    Cursor.close()
    conn.close()

def show_acces_code():
    conn = sql.connect(host="localhost", user="root", password="root", database="student_info")
    Cursor = conn.cursor()
    name = input("Enter the name of the student")
    qry = ("SELECT * FROM access_code where name= %s")
    data = (name,)
    Cursor.execute(qry,data)
    for (Name , access_code) in Cursor:
        print("Name: ", Name)
        print("Access code :" , access_code)
    conn.commit()
    Cursor.close()
    conn.close()

