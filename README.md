# SYSCOM_5Gproject_mariaDBtoExcel

###### tags: `SYSCOM` `GitHub`



### 執行

> `mainAG.py` (run車種辨識統計)
> `mainPO.py` (run車種辨識)
> `mainSL.py` (run停等)
> [color=pink]



### 套件

<img width='800px' src='https://i.imgur.com/JZ37TzG.png'/>



### 檔案說明

> shell `tree /f`
> [color=orange]
```
C:.
│  constants.py (不重要的字串:3)
│  mainAG.py (run車種辨識統計)
│  mainPO.py (run車種辨識)
│  mainSL.py (run停等)
│  sqlFunction.py (連線至mariaDB)
│  toExcelAG.py (車種辨識統計函示)
│  toExcelPO.py (車種辨識函示)
│  toExcelSL.py (停等函示)
│  util.py (通用函式)
│  varible.py (各種參數: mariaDB、SQL指令...)
│
├─example_table
│      example_tableAG.xlsx
│      example_tablePO.xlsx
│      example_tableSL.xlsx
│
└─output
       (匯出的檔案會在這裡)
```
