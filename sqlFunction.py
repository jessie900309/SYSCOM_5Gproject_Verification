import mariadb
from util import catchError
from varible import myUser, myPassword, myHost, myPort, myDatabase


def sqlConnect():
    try:
        print("----- Connect to MariaDB Platform -----")
        conn = mariadb.connect(
            user=myUser,
            password=myPassword,
            host=myHost,
            port=myPort,
            database=myDatabase,
        )
        print("------- Connect to ICC Database -------")
        curr = conn.cursor()
        sql = "use {};".format(myDatabase)
        curr.execute(sql)
        print("----------- Connect Success -----------")
        return conn, curr
    except mariadb.Error as e:
        print("------------- Connect Error -----------")
        catchError(e)
    except Exception as e:
        print("---------------- Error ----------------")
        catchError(e)
