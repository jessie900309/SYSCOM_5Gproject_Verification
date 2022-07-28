from constants import welcome_msgSL
from toExcelSL import mariaDBtoExcelSL
from util import *


def mainSL():
    try:
        user_name, picked_date = userInput(welcome_msgSL)
        initExcelFile(user_name, picked_date, "SL")
        mariaDBtoExcelSL(picked_date)
        print("\n導入完成OuO")
    except KeyboardInterrupt:
        print("Bye Bye :)")
    except Exception as e:
        print("---------------- Error ----------------")
        catchError(e)


if __name__ == '__main__':
    mainSL()

