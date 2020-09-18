import mysql.connector
import configparser
import base64


def mySQLConnection():
    try:

        config = configparser.ConfigParser()
        config.read('conf/ClassRoomConfig.properties')
        dbuser = config.get('mysql', 'user').replace("'", "")
        dbpassword = config.get('mysql', 'password').replace("'", "")
        dbpassword = base64.b64decode(dbpassword)
        dbhost = config.get('mysql', 'host').replace("'", "")
        db = config.get('mysql', 'database').replace("'", "")
        dbport = int(config.get('mysql', 'port').replace("'", ""))

        cnx = mysql.connector.MySQLConnection(user=dbuser, password=dbpassword,
                                              host=dbhost,
                                              database=db, port=dbport)

        return cnx

    except mysql.connector.Error as err:
        print(err)
