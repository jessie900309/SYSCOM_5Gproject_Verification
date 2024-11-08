# ----- Connect to MariaDB Platform -----

myUser = "YOUR_USERNAME"
myPassword = "YOUR_PASSWORD"
myHost = "HOST_ADDRESS"
myPort = 3306
myDatabase = "DB_NAME"

# ----- file -----

inputFileAG = "example_table/example_tableAG.xlsx"
outputFileAG = "output/output_ag.xlsx"
inputFilePO = "example_table/example_tablePO.xlsx"
outputFilePO = "output/output_po.xlsx"
inputFileSL = "example_table/example_tableSL.xlsx"
outputFileSL = "output/output_sl.xlsx"

# ----- api -----

BaseURL = "https://opendata.cwb.gov.tw/api"
sun_data_url = "/v1/rest/datastore/A-B0062-001"
payload = {
    "Authorization": "YOUR_AUTH_TOKEN",
    "limit": 1,
    "format": "JSON",
    "locationName": ["花蓮縣"],
}

# ----- select -----

cctvID_list = ["165K-1", "165K-2", "166K-1", "166K-2", "168K-1", "168K-2", "170K-1"]

time_ListAG = [
    "04:00:35",
    "05:00:00",
    "06:00:00",
    "07:00:00",
    "11:01:00",
    "12:00:00",
    "15:00:00",
    "17:00:00",
    "18:00:00",
    "19:00:00",
    "20:00:00",
]
sql_searchAG = "SELECT * from VehicleRecResultAG ag where cctvid IN ('{}') and DATE_FORMAT(ImageCaptureTime, '%Y-%m-%d %H:%i:%s') >= @TS and DATE_FORMAT(ImageCaptureTime, '%Y-%m-%d %H:%i:%s') <= @TS;"
sql_checkAG = "SELECT * FROM MQRecvAggAG where DeviceID IN ('{}') and DATE_FORMAT(DataCollectTime, '%Y-%m-%d %H:%i') >= @TS and DATE_FORMAT(DataCollectTime, '%Y-%m-%d %H:%i') <= @TE order by DataCollectTime;"

time_startListPO = [
    "04:00:00",
    "05:00:00",
    "06:00:00",
    "07:00:00",
    "11:01:00",
    "12:00:00",
    "15:00:00",
    "17:00:00",
    "18:00:00",
    "19:00:00",
    "20:00:00",
]
time_endListPO = [
    "04:05:00",
    "05:05:00",
    "06:05:00",
    "07:05:00",
    "11:06:00",
    "12:05:00",
    "15:05:00",
    "17:05:00",
    "18:05:00",
    "19:05:00",
    "20:05:00",
]
sql_searchPO = "SELECT po.cctvid, po.VehicleType, count(po.ObjectId) as cnt from VehicleRecResultPO po where cctvid IN ('{}') and DATE_FORMAT(ImageCaptureTime, '%Y-%m-%d %H:%i') >= @TS and DATE_FORMAT(ImageCaptureTime, '%Y-%m-%d %H:%i') <= @TE group by po.cctvid , po.VehicleType order by po.cctvid , po.VehicleType;"

time_ListSL = [
    "04:00:00",
    "05:00:00",
    "06:00:00",
    "07:00:00",
    "11:00:00",
    "12:00:00",
    "15:00:00",
    "17:00:00",
    "18:00:00",
    "19:00:00",
    "20:00:00",
]
sql_searchSL = "SELECT st.LaneID, st.Length, st.Volume, st.Occupy from StopLen st where cctvid IN ('{}') and DATE_FORMAT(ImageCaptureTime, '%Y-%m-%d %H:%i:%s') >= @TS and DATE_FORMAT(ImageCaptureTime, '%Y-%m-%d %H:%i:%s') <= @TS order by st.ImageCaptureTime;"
