from constants import welcome_msgPO
from toExcelPO import mariaDBtoExcelPO
from util import *


def mainPO():
    try:
        user_name, picked_date = userInput(welcome_msgPO)
        initExcelFile(user_name, picked_date, "PO")
        mariaDBtoExcelPO(picked_date)
        print("\n導入完成OuO")
    except KeyboardInterrupt:
        print("Bye Bye :)")
    except Exception as e:
        print("---------------- Error ----------------")
        catchError(e)


if __name__ == '__main__':
    mainPO()

