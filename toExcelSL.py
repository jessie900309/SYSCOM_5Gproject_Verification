import pandas as pd
from sqlFunction import sqlConnect
from util import openExcelFile
from varible import *


excelFileGroup = len(time_ListSL)

SL_excel = {
    0: "G", # LaneID
    2: "I", # Volume
    1: "N", # Length
    3: "S"  # Occupy
}


def mariaDBtoExcelSL(date):
    conn, cur = sqlConnect()
    n = 0
    for nvr in cctvID_list:
        nvr_row = excelFileGroup*(2*n) + 6
        for ts in time_ListSL:
            sql = "SET @TS = '2022-{} {}';".format(date, ts)
            cur.execute(sql)
            sql = sql_searchSL.format(nvr)
            cur.execute(sql)
            fetch_data = cur.fetchall()
            df = pd.DataFrame(fetch_data)
            if df.empty:
                pass
            else:
                for df_row in range(len(df.index)):
                    row_laneID = df.iloc[df_row][0]
                    row_len = df.iloc[df_row][1]
                    row_vol = df.iloc[df_row][2]
                    row_occ = df.iloc[df_row][3]
                    ws, wb = openExcelFile(outputFileSL)
                    if row_laneID == "0":
                        col = str(nvr_row)
                    else: # row_laneID == "1"
                        col = str(nvr_row+1)
                    ws["N" + col].value = row_len
                    ws["I" + col].value = row_vol
                    ws["S" + col].value = row_occ
                    wb.save(outputFileSL)
            nvr_row += 2
        n += 1
    conn.close()





