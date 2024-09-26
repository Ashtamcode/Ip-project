import mysql.connector as sql
import pandas as pd
import time as t
import matplotlib.pyplot as py
import numpy as np


def phy_exam():
    conn=sql.connect(host="localhost",user="root",password="root",database="Exam_questions")
    Cursor = conn.cursor()
    Cursor.execute("select * from phy" )
    rows = Cursor.fetchall()
    df = pd.DataFrame(rows, columns=['S.no','Q','A'])
    r = df.sample(n=5)
    print("Exam Created and Saved")
    return r
    

def chem_exam():
    conn=sql.connect(host="localhost",user="root",password="root",database="Exam_questions")
    Cursor = conn.cursor()
    Cursor.execute("select * from chem" )
    rows = Cursor.fetchall()
    df = pd.DataFrame(rows, columns=['S.no','Q','A'])
    r = df.sample(n=5)
    print("Exam Created and Saved")
    return r


def Maths_exam():
    conn=sql.connect(host="localhost",user="root",password="root",database="Exam_questions")
    Cursor = conn.cursor()
    Cursor.execute("select * from Maths" )
    rows = Cursor.fetchall()
    df = pd.DataFrame(rows, columns=['S.no','Q','A'])
    r = df.sample(n=5)
    print("Exam Created and Saved")
    return r
    
   
def create_exam(choice):
    if choice.upper() == "M":
        return Maths_exam()
    elif choice.upper() == 'P':
        return phy_exam()
    else:
        return chem_exam()


def take_exam(dff):
    total = 5
    t_for_q = []
    q_done = []
    count = 0
    score = 0

    for index, rows in dff.iterrows():
        count += 1
        print(f"Q {count}: {rows['Q']}")

        start_time = t.time()
        ans = input("Enter your answer (True/False): ")
        print('\n')

        if ans.lower() == 'true' and rows['A']:
            score += 1
        elif ans.lower() == 'false' and not rows['A']:
            score += 1
        else:
            # print("Wrong")
            pass

        end_time = t.time()
        t_for_q.append(int(end_time - start_time))
        q_done.append(count)
    
    print("Your Score is :",score ,'/', total)
    # print("Time taken to do 1 q",t_for_q ,"score",q_done)
    # df1 = pd.DataFrame(score)
    anly = input("Do you want to Analyse your questions?(Y/N)")
    if anly.upper() == 'Y':

        py.plot(q_done,t_for_q , 'r')
        py.xlabel('No. of questions Done')
        py.ylabel('Time taken to do 1 question')
        py.show() 
    else:
        pass

