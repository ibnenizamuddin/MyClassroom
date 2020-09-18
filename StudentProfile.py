from Connectivity import mySQLConnection
import mysql.connector
import datetime
from base64 import b64encode


def getStudentProfile(RollNo):
    try:
        StudentRollNo = int(RollNo)
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "Select StudentFName,StudentMName,StudentLName,StudentAddress,StudentEmail,StudentContactInfo from students where  Student_id=%s;"
        val = (StudentRollNo, )
        dbcursor.execute(sql, val)
        myresult = dbcursor.fetchall()
        if myresult == []:
            return ''
        DBconnection.commit()
        DBconnection.close()
        return myresult

    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))


def getStudentProfileByName(RollNo):
    try:
        StudentName = str(RollNo)
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        StudentName = "%" + StudentName + "%"
        print(StudentName)
        sql = "Select Student_id,Studentfname,StudentMName,StudentLName from students where  StudentFName like %s or StudentLName like %s;"
        val = (StudentName, StudentName)
        dbcursor.execute(sql, val)
        myresult = dbcursor.fetchall()
        print(myresult)
        if myresult == []:
            return ''
        DBconnection.commit()
        DBconnection.close()
        return myresult

    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))
