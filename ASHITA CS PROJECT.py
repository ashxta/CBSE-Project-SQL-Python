title='COMPUTER INSTITUTE MANAGEMENT'
d='--**************--'
x=title.center(80)
y=d.center(85)
print(x)
print(y)

import mysql.connector as con
def db_setup():
    mydb=con.connect(host='localhost',user='root',passwd='root')
    cur=mydb.cursor()
    try:
       cur.execute('create database if not exists computer_institute_management')
       print("Database created")
    except:
        print("Database computer_institute_management already exits")
    mydb.close()

def tb_setup():
    mydb=con.connect(host='localhost', user='root', passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    try:
        cur.execute('create table if not exists course(course_id int primary key,course_name varchar(80),course_duration varchar(20), course_fees varchar(20))')
        print("Course Table setup done")
        cur.execute('create table if not exists student(student_id int primary key,student_name varchar(30),phone_no int, student_course varchar(50))')
        print("Student Table setup done")
        cur.execute('create table if not exists faculty(faculty_id int primary key,faculty_name varchar(30),phone_no int, faculty_course varchar(50))')
        print("Faculty Table setup done")
    except:
        print("Tables already exist")
    mydb.close()

def database_setup():
    while True:
        print("\npress 1 to setup database")
        print("Press 2 to setup tables")
        print("Press 3 to go back main menu\n")
        ch=int(input("Enter your choice"))
        if ch==1:
            db_setup()
        elif ch==2:
            tb_setup()
        elif ch==3:
            return
        else:
            exit()

def add_course():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    
    course_id=int(input('Enter course id'))
    course_name=input('Enter course name')
    course_duration=int(input('Enter the duration of the course (in weeks)'))
    course_fees=int(input('Enter the total fees of the course'))
    z="insert into course values(%s,%s,%s,%s)"
    y=(course_id,course_name,course_duration,course_fees)
    cur.execute(z,y)
    print("Course added Successfully")
    mydb.commit()
    mydb.close()
def delete_course ():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    course_id=int(input("Enter course id that you want to delete"))
    z="Delete from course where course_id=%s"
    y=(course_id,)
    cur.execute(z,y)
    if cur.rowcount<=0:
        print("Enter the correct id")
    else:
        print(cur.rowcount,"Course Successfully Deleted")
    mydb.commit()
    mydb.close()
def update_course():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    course_id=int(input("Enter course id for which you want to update name"))
    course_name=input("Enter Updated course name")
    z="update course set course_name=%s where course_id=%s"
    y=(course_name,course_id)
    cur.execute(z,y)
    if cur.rowcount<=0:
        print("Enter the correct id")
    else:
        print(cur.rowcount,"Detail Successfully Updated")
    mydb.commit()
    mydb.close()
def update_duration_course():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    course_id=int(input("Enter course id for which you want to update duration"))
    course_duration=input("Enter Updated course duration")
    z="update course set course_duration=%s where course_id=%s"
    y=(course_duration,course_id)
    cur.execute(z,y)
    if cur.rowcount<=0:
        print("Enter the correct id")
    else:
        print(cur.rowcount,"Detail Successfully Updated")
    mydb.commit()
    mydb.close()
def update_fees_course():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    course_id=int(input("Enter course id for which you want to update fees"))
    course_fees=input("Enter Updated course fees")
    z="update course set course_fees=%s where course_id=%s"
    y=(course_fees,course_id)
    cur.execute(z,y)
    if cur.rowcount<=0:
        print("Enter the correct id")
    else:
        print(cur.rowcount,"Detail Successfully Updated")
    mydb.commit()
    mydb.close()
def display_course():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    while True:    
        print('\nPress 1 to display all the records')
        print('Press 2 to display a certain course')
        print('Press 3 to return\n')
        nd=eval(input("Enter no."))
        if nd==1:
            mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
            cur=mydb.cursor()
            cur.execute("Select * from course")
            records=cur.fetchall()
            print('|COURSEID|','|NAME|','|DURATION|','|FEES|')
            for i in records:
                print(i[0],'\t  ',i[1],'   ',i[2],'     ',i[3])
            print("Course list successfully displayed")
        elif nd==2:  
            mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
            cur=mydb.cursor()
            course_id=eval(input("Enter the id of the course for which you want to see the data"))
            y=(course_id,)
            z="select * from course where course_id=%s"
            cur.execute(z,y)
            records=cur.fetchall()
            print('|COURSEID|','|NAME|','|DURATION|','|FEES|')
            for i in records:
                print(i[0],'\t  ',i[1],'   ',i[2],'     ',i[3])
                print("Course Successfully Displayed")
        elif nd==3:
            
            return()
        else:
            print('Error, Use the correct numbers')
    mydb.commit()
    mydb.close()
    
def course():

    while True:
        print("Press 1 to add a course")
        print("Press 2 to delete a course")
        print("Press 3 to update the name of a course")
        print("Press 4 to update the duration of a course")
        print("Press 5 to update the fees of a course")
        print("Press 6 to display course data")
        print("Press 7 to go back main menu")

        ch=eval(input("Enter your choice"))
        if ch==1:
            add_course()
        elif ch==2:
            delete_course()
        elif ch==3:
            update_course()
        elif ch==4:
            update_duration_course()
        elif ch==5:
            update_fees_course()
        elif ch==6:
            display_course()
        elif ch==7:
            return()
        else:
            exit()
            
def add_student():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    student_id=int(input('Enter id'))
    student_name=input('Enter student name')
    phone_no=int(input('Enter student phone no'))
    student_course=input('Enter the course of the student')
    z="insert into student values(%s,%s,%s,%s)"
    y=(student_id,student_name,phone_no,student_course)
    cur.execute(z,y)
    print("Student added Successfully")
    mydb.commit()
    mydb.close()
def delete_student():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    student_id=input("Enter student id that you want to delete")
    z="Delete from student where student_id=%s"
    y=(student_id,)
    cur.execute(z,y)
    if cur.rowcount<=0:
        print("Enter the correct id")
    else:
        print(cur.rowcount,"Student Successfully Deleted")
    mydb.commit()
    mydb.close()
def update_name_student():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    student_id=int(input("Enter student id"))
    student_name=(input("Enter Updated Detail for name"))
    z="update student set student_name=%s where student_id=%s"
    y=(student_name,student_id)
    cur.execute(z,y)
    if cur.rowcount<=0:
        print("Enter the correct id")
    else:
        print(cur.rowcount,"Detail Successfully Updated")
    mydb.commit()
    mydb.close()
def update_phone_student():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    student_id=int(input("Enter student id"))
    phone_no=int(input("Enter Updated Detail for phone no"))
    z="update student set phone_no=%s where student_id=%s"
    y=(phone_no,student_id)
    cur.execute(z,y)
    if cur.rowcount<=0:
        print("Enter the correct id")
    else:
        print(cur.rowcount,"Detail Successfully Updated")
    mydb.commit()
    mydb.close()
def update_course_student():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    student_id=int(input("Enter student id"))
    student_course=(input("Enter Updated Detail for course"))
    z="update student set student_course=%s where student_id=%s"
    y=(student_course,student_id)
    cur.execute(z,y)
    if cur.rowcount<=0:
        print("Enter the correct id")
    else:
        print(cur.rowcount,"Detail Successfully Updated")
    mydb.commit()
    mydb.close()

def display_student():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    while True:    
        print('\nPress 1 to display all the records')
        print('Press 2 to display a certain student')
        print('Press 3 to return\n')
        nd=eval(input("Enter no."))
        if nd==1:
            mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
            cur=mydb.cursor()
            cur.execute("Select * from student")
            records=cur.fetchall()
            print('|STUDENT_ID|','|NAME|','|PHONE_NO|','|COURSE|')
            for i in records:
                print(i[0],'\t  ',i[1],'   ',i[2],'     ',i[3])
                print("Student Successfully Displayed")
        elif nd==2:  
            mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
            cur=mydb.cursor()
            student_id=eval(input("Enter the id of the student for which you want to see the data"))
            y=(student_id,)
            z="select * from student where student_id=%s"
            cur.execute(z,y)
            records=cur.fetchall()
            print('|STUDENT_ID|','|NAME|','|PHONE_NO|','|COURSE|')
            for i in records:
                print(i[0],'\t  ',i[1],'   ',i[2],'     ',i[3])
                print("Student Successfully Displayed")
        
        elif nd==3:
            
            return()
        else:
            print('Error, Use the correct numbers')
    mydb.commit()
    mydb.close()
    

    
def student():

    while True:
        print("Press 1 to add a student")
        print("Press 2 to delete a student")
        print("Press 3 to update the name of a student")
        print("Press 4 to update the phone no. of a student")
        print("Press 5 to update the course of a student")
        print("Press 6 to dispay student data")
        print("Press 7 to go back main menu")

        ch=eval(input("Enter your choice"))
        if ch==1:
            add_student()
        elif ch==2:
            delete_student()
        elif ch==3:
            update_name_student()
        elif ch==4:
            update_phone_student()
        elif ch==5:
            update_course_student()
        elif ch==6:
            display_student()
        elif ch==7:
            return()
        else:
            exit()

def add_faculty():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    faculty_id=int(input('Enter id'))
    faculty_name=input('Enter faculty name')
    phone_no=int(input('Enter faculty phone no'))
    faculty_course=input('Enter the course taught by the faculty')
    z="insert into faculty values(%s,%s,%s,%s)"
    y=(faculty_id,faculty_name,phone_no,faculty_course)
    cur.execute(z,y)
    print(cur.rowcount,"Faculty added Successfully")
    mydb.commit()
    mydb.close()
def delete_faculty():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    faculty_id=int(input("Enter faculty id that you want to delete"))
    z="Delete from faculty where faculty_id=%s"
    y=(faculty_id,)
    cur.execute(z,y)
    if cur.rowcount<=0:
        print("Enter the correct id")
    else:
        print(cur.rowcount,"Faculty Successfully Deleted")
    mydb.commit()
    mydb.close()
def update_name_faculty():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    faculty_id=int(input("Enter faculty id"))
    faculty_name=(input("Enter Updated Detail for name"))
    z="update faculty set faculty_name=%s where faculty_id=%s"
    y=(faculty_name,faculty_id)
    cur.execute(z,y)
    if cur.rowcount<=0:
        print("Enter the correct id")
    else:
        print(cur.rowcount,"Detail Successfully Updated")
    mydb.commit()
    mydb.close()
def update_phone_faculty():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    faculty_id=int(input("Enter faculty id"))
    phone_no=int(input("Enter Updated Detail for phone no"))
    z="update faculty set phone_no=%s where faculty_id=%s"
    y=(phone_no,faculty_id)
    cur.execute(z,y)
    if cur.rowcount<=0:
        print("Enter the correct id")
    else:
        print(cur.rowcount,"Detail Successfully Updated")
    mydb.commit()
    mydb.close()
def update_course_faculty():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    faculty_id=int(input("Enter faculty id"))
    faculty_course=(input("Enter Updated Detail for course"))
    z="update faculty set faculty_course=%s where faculty_id=%s"
    y=(faculty_course,faculty_id)
    cur.execute(z,y)
    if cur.rowcount<=0:
        print("Enter the correct id")
    else:
        print(cur.rowcount,"Detail Successfully Updated")
    mydb.commit()
    mydb.close()
def display_faculty():
    mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
    cur=mydb.cursor()
    while True:    
        print('\nPress 1 to display all the records')
        print('Press 2 to display a certain faculty')
        print('Press 3 to return\n')
        nd=eval(input("Enter no."))
        if nd==1:
            mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
            cur=mydb.cursor()
            cur.execute("Select * from faculty")
            records=cur.fetchall()
            print('|FACULTY_ID|','|NAME|','|PHONE_NO|','|COURSE|')
            for i in records:
                  print(i[0],'\t  ',i[1],'   ',i[2],'     ',i[3])
                  print("Faculty list successfully displayed")
        elif nd==2:  
            mydb=con.connect(host='localhost',user='root',passwd='root',database='computer_institute_management')
            cur=mydb.cursor()
            faculty_id=eval(input("Enter the id of the faculty for which you want to see the data"))
            y=(faculty_id,)
            z="select * from faculty where faculty_id=%s"
            cur.execute(z,y)
            records=cur.fetchall()
            print('|FACULTY_ID|','|NAME|','|PHONE_NO|','|COURSE|')
            for i in records:
                print(i[0],'\t  ',i[1],'   ',i[2],'     ',i[3])
                print("Faculty Successfully Displayed")
        elif nd==3:
            
            return()
        else:
            print('Error, Use the correct numbers')
    mydb.commit()
    mydb.close()
    
def faculty():

    while True:
        print("Press 1 to add a faculty")
        print("Press 2 to delete a faculty")
        print("Press 3 to update the name of a faculty")
        print("Press 4 to update the phone number of a faculty")
        print("Press 5 to update the course of a faculty")
        print("Press 6 to display faculty data")
        print("Press 7 to go back main menu")

        ch=eval(input("Enter your choice"))
        if ch==1:
            add_faculty()
        elif ch==2:
            delete_faculty()
        elif ch==3:
            update_name_faculty()
        elif ch==4:
            update_phone_faculty()
        elif ch==5:
            update_course_faculty()
        elif ch==6:
            display_faculty()
        elif ch==7:
            return()
        else:
            exit()


while True:
    print("\n\t\t\t PLEASE SELECT AN OPERATION \n")
    print ("\t\t\t1. Press 1 to setup database")
    print ("\t\t\t2. Press 2 to setup course database")
    print ("\t\t\t3. Press 3 to setup student database")
    print ("\t\t\t4. Press 4 to setup faculty database")
    print("Press any key for exit")

    ch=eval(input("Enter your choice"))

    if ch==1:
       database_setup()
    elif ch==2:
         course()
    elif ch==3:
        student()
    elif ch==4:
        faculty()
    else:
        exit()
