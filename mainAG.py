from constants import welcome_msgAG
from toExcelAG import mariaDBtoExcelAG
from util import *


def mainAG():
    try:
        user_name, picked_date = userInput(welcome_msgAG)
        initExcelFile(user_name, picked_date, "AG")
        mariaDBtoExcelAG(picked_date)
        print("\n導入完成OuO")
    except KeyboardInterrupt:
        print("Bye Bye :)")
    except Exception as e:
        print("---------------- Error ----------------")
        catchError(e)


if __name__ == "__main__":
    mainAG()
