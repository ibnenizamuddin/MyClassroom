from Connectivity import mySQLConnection
import mysql.connector
import datetime


def removeSubject(*args):
    try:
        stdid = args[0]
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()

        sql = "delete from Subject_details where Subject_detailid=%s"
        val = (stdid,)
        dbcursor.execute(sql, val)

        DBconnection.commit()
        DBconnection.close()
    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))


def addSubject(*args):
    try:
        Std_detailsName = args[0]
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "insert into Subject_details (Subject_detailsName) values (%s);"
        val = (Std_detailsName,)
        dbcursor.execute(sql, val)

        DBconnection.commit()
        DBconnection.close()

    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))


def getSubject():
    try:
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "select Subject_detailid,Subject_detailsName from Subject_details;"
        dbcursor.execute(sql)
        myresult = dbcursor.fetchall()

        DBconnection.commit()
        DBconnection.close()

        return myresult
    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))


def mapSubjectPrice(*args):
    try:
        MappingData = list(*args)
        Std_detailid = int(MappingData[0])
        Subject_detailid = int(MappingData[1])
        PriceDetails = int(MappingData[2])
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "insert into Subject_Class_Mapping (Std_detailid,Subject_detailid,PriceDetails) values (%s,%s,%s)"
        val = (Std_detailid, Subject_detailid, PriceDetails)
        dbcursor.execute(sql, val)

        DBconnection.commit()
        DBconnection.close()

    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))


def getMapSubjectPrice(*args):
    try:
        DBconnection = mySQLConnection()
        dbcursor = DBconnection.cursor()
        sql = "Select sm.id as MappingID,sd.Std_detailsName as Std_name,sj.Subject_detailsName As SubjectName,sm.PriceDetails as Amount from  Subject_Class_Mapping sm , Std_details sd ,Subject_details sj where sm.Std_detailid=sd.Std_detailid and sm.Subject_detailid=sj.Subject_detailid order by (sd.Std_detailsName)"
        dbcursor.execute(sql)
        myresult = dbcursor.fetchall()
        DBconnection.commit()
        DBconnection.close()
        return myresult

    except mysql.connector.Error as err:
        print("Something went wrong while logging: {}".format(err))
