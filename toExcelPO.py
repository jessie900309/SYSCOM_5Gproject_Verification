import pandas as pd
from sqlFunction import sqlConnect
from util import openExcelFile
from varible import *


excelFileGroup = len(time_startListPO)

PO_excel = {
    "02": 'K',
    "11": 'P',
    "21": 'Z',
    "22": 'U',
    "30": 'AY'
}

def mariaDBtoExcelPO(date):
    conn, cur = sqlConnect()
    n = 1
    ws, wb = openExcelFile(outputFilePO)
    for nvr in cctvID_list:
        nvr_row = excelFileGroup*n - 5
        for timeStep in range(excelFileGroup):
            sql = "SET @TS = '2022-{} {}';".format(date, time_startListPO[timeStep])
            cur.execute(sql)
            sql = "SET @TE = '2022-{} {}';".format(date, time_endListPO[timeStep])
            cur.execute(sql)
            sql = sql_searchPO.format(nvr)
            cur.execute(sql)
            fetch_data = cur.fetchall()
            df = pd.DataFrame(fetch_data)
            if df.empty:
                print("{} {} 查無資料".format(nvr, time_startListPO[timeStep]))
                pass
            else:
                for df_row in range(len(df.index)):
                    row_type = df.iloc[df_row][1]
                    row_vol = df.iloc[df_row][2]
                    col = PO_excel[row_type]
                    cellID = col+str(nvr_row)
                    if ws[cellID].value != 0:
                        ws[cellID].value = int(ws[cellID].value) + int(row_vol)
                    else:
                        ws[cellID].value = row_vol
            nvr_row += 1
        n += 1
    wb.save(outputFilePO)
    conn.close()





