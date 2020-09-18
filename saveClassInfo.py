from Connectivity import mySQLConnection
import mysql.connector
import datetime


def updateClassInfo(*args):
    try:
        ClassData = list(*args)
        Classname = str(ClassData[0])
        Email = str(ClassData[1])
        Address1 = str(ClassData[2])
        Contact = str(ClassData[3])
        Logo = ClassData[5]
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        LastModified = datetime.datetime.now()

        sql = "update classinfo set Classname=%s,Address1=%s ,Email=%s,ContactInfo=%s,Logo=%s,LastModified=%s"
        val = (Classname, Address1, Email, Contact, Logo, LastModified)
        dbcursor.execute(sql, val)

        DBconnection.commit()
        DBconnection.close()
    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))


def selectClassInfo():
    try:
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "select  Classname,Address1,Email,ContactInfo,Logo,LastModified from classinfo "
        dbcursor.execute(sql)
        myresult = dbcursor.fetchall()

        DBconnection.commit()
        DBconnection.close()

        return myresult
    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))
