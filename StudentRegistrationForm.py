from Connectivity import mySQLConnection
import mysql.connector
import datetime
from base64 import b64encode


def getLogoImg():
    try:
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "select Logo from classinfo "
        dbcursor.execute(sql)
        myresult = dbcursor.fetchall()
        myresult = myresult[0][0]
        image = b64encode(myresult).decode("utf-8")

        DBconnection.commit()
        DBconnection.close()

        return image
    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))


def registerNewStudent(*args):
    try:
        StudentData = list(*args)
        StudentFName = StudentData[0]
        StudentMName = StudentData[1]
        StudentLName = StudentData[2]
        StudentAddress = StudentData[3]
        StudentEmail = StudentData[4]
        StudentContactInfo = StudentData[5]
        Student_Dob = StudentData[6]
        Student_gender = StudentData[7]
        Student_AadhaarNo = StudentData[8]
        Student_Reference = StudentData[9]
        Student_FatherName = StudentData[10]
        Student_FatherContactNo = StudentData[11]
        Student_MotherName = StudentData[12]
        Student_MotherContactNo = StudentData[13]
        Student_ProfilePic = StudentData[14]
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "insert into Students (StudentFName,StudentMName,StudentLName,StudentAddress,StudentEmail,StudentContactInfo,Student_Dob,Student_gender,Student_AadhaarNo,Student_Reference,Student_FatherName,Student_FatherContactNo,Student_MotherName,Student_MotherContactNo,Student_ProfilePic) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (StudentFName, StudentMName, StudentLName, StudentAddress, StudentEmail, StudentContactInfo, Student_Dob, Student_gender, Student_AadhaarNo,
               Student_Reference, Student_FatherName, Student_FatherContactNo, Student_MotherName, Student_MotherContactNo, Student_ProfilePic)
        dbcursor.execute(sql, val)
        StudentRollNo = dbcursor.lastrowid

        DBconnection.commit()
        DBconnection.close()
        return StudentRollNo

    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))


def getSubjectList(*args):
    try:
        StdId = args[0]
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "Select sm.Subject_detailid as MappingID,sj.Subject_detailsName As SubjectName,sm.PriceDetails as Amount from  Subject_Class_Mapping sm , Std_details sd ,Subject_details sj where sm.Std_detailid=sd.Std_detailid and sm.Subject_detailid=sj.Subject_detailid and sd.Std_detailid=%s;"
        val = (StdId, )
        dbcursor.execute(sql, val)
        myresult = dbcursor.fetchall()

        DBconnection.commit()
        DBconnection.close()

        return myresult
    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))


def getSelStdList(*args):
    try:
        StdId = args[0]
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "select Std_detailid,Std_detailsName from Std_details where Std_detailid=%s;"
        val = (StdId, )
        dbcursor.execute(sql, val)
        myresult = dbcursor.fetchall()

        DBconnection.commit()
        DBconnection.close()

        return myresult
    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))


def StudentRegistration_Fess_Subject(*args):
    try:
        StudentData = list(*args)
        Student_id = StudentData[0]
        TotalFees = StudentData[1]
        Discount = StudentData[2]
        FinalTotalFees = StudentData[3]
        Std_detailid = StudentData[4]
        Subject_detailid = StudentData[5]
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "insert into student_fees_details (Student_id,TotalFees,Discount,FinalTotalFees) values (%s,%s,%s,%s);"
        val = (Student_id, TotalFees, Discount, FinalTotalFees)
        dbcursor.execute(sql, val)
        for x in Subject_detailid:
            sql = "insert into Student_Subject_Class_Mapping (Student_id,Std_detailid,Subject_detailid) values (%s,%s,%s);"
            val = (Student_id, Std_detailid, x)
            dbcursor.execute(sql, val)

        DBconnection.commit()
        DBconnection.close()

    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))


def getStudentRegistrationFullSubject(*args):
    try:
        StudentData = list(*args)
        Student_id = int(StudentData[0])
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "select sd.std_detailsname,sb.subject_detailsname,sm.PRICEDETAILS from subject_details sb, std_details sd,subject_class_mapping sm join student_subject_class_mapping scm  on (sm.Std_detailid=scm.Std_detailid and sm.Subject_detailid=scm.Subject_detailid) where scm.subject_detailid=sb.subject_detailid and sd.std_detailid=scm.std_detailid and student_id=%s;"
        val = (Student_id, )
        dbcursor.execute(sql, val)
        myresult = dbcursor.fetchall()

        DBconnection.commit()
        DBconnection.close()

        return myresult

    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))


def getStudentProfileImg(StudentRollNo):
    try:
        Student_id = int(StudentRollNo)
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "select Student_ProfilePic from students where student_id=%s"
        val = (Student_id,)
        dbcursor.execute(sql, val)
        myresult = dbcursor.fetchall()
        if myresult == []:
            return ''

        myresult = myresult[0][0]
        image = b64encode(myresult).decode("utf-8")

        DBconnection.commit()
        DBconnection.close()

        return image
    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))
