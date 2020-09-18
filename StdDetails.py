from Connectivity import mySQLConnection
import mysql.connector
import datetime


def removeStd(*args):
    try:
        stdid = args[0]
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()

        sql = "delete from Std_details where Std_detailid=%s"
        val = (stdid,)
        dbcursor.execute(sql, val)

        DBconnection.commit()
        DBconnection.close()
    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))


def addStd(*args):
    try:
        Std_detailsName = args[0]
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "insert into Std_details (Std_detailsName) values (%s);"
        val = (Std_detailsName,)
        dbcursor.execute(sql, val)

        DBconnection.commit()
        DBconnection.close()

    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))


def getStd():
    try:
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "select Std_detailid,Std_detailsName from Std_details;"
        dbcursor.execute(sql)
        myresult = dbcursor.fetchall()

        DBconnection.commit()
        DBconnection.close()

        return myresult
    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))
