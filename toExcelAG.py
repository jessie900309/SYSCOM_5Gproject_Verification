import pandas as pd
from sqlFunction import sqlConnect
from util import openExcelFile
from varible import *


excelFileGroup = len(time_ListAG)

AG_excel = {
    "02": 'I',
    "11": 'N',
    "21": 'X',
    "22": 'S',
    "30": 'AW'
}


def mariaDBtoExcelAG(date):
    conn, cur = sqlConnect()
    n = 1
    ws, wb = openExcelFile(outputFileAG)
    for nvr in cctvID_list:
        nvr_row = excelFileGroup*n - 5
        for ts in time_ListAG:
            sql = "SET @TS = '2022-{} {}';".format(date, ts)
            cur.execute(sql)
            sql = sql_searchAG.format(nvr)
            cur.execute(sql)
            fetch_data = cur.fetchall()
            df = pd.DataFrame(fetch_data)
            if df.empty:
                print("{} {} 查無資料".format(nvr, ts))
                # sql = sql_checkAG.format(nvr)
                # cur.execute(sql)
                # fetch_data = cur.fetchall()
                # df = pd.DataFrame(fetch_data)
                # if df.empty:
                #     print("{} {} 查無資料".format(nvr, ts))
                pass
            else:
                for df_row in range(len(df.index)):
                    row_type = df.iloc[df_row][4]
                    row_vol = df.iloc[df_row][5]
                    col = AG_excel[row_type]
                    cellID = col+str(nvr_row)
                    if ws[cellID].value != 0:
                        ws[cellID].value = int(ws[cellID].value) + int(row_vol)
                    else:
                        ws[cellID].value = row_vol

            nvr_row += 1
        n += 1
    wb.save(outputFileAG)
    conn.close()





