from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl 
import pandas as pd

# Ignore SSL certificate errors 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# parse web by opening url
def process_id(id):
    if id < 10:
        return "0"
    return ""

# Create a dataframe
def CreateDataFrame(root_url, start_id, end_id):
    DataFrame = pd.DataFrame(columns=["ID", "Toán", "Lí", "Hóa", "Sinh","Văn","Ngoại ngữ", "GDCD", "Địa","Sử"])
    # DataFrame.astype(str)
    province_id = start_id[0] + start_id[1]
    province_id = process_id(int(province_id))
    
    for i in range(int(start_id), int(end_id) + 1):
        dict ={"ID": None,
            "Toán": None,
            "Lí": None,
            "Hóa": None,
            "Sinh": None,
            "Ngoại ngữ": None,
            "Văn": None,
            "GDCD": None,
            "Địa": None,
            "Sử": None
        }
        id = province_id + str(i)
        dict["ID"] = id
        url = root_url + id + ".html"
        print(url)
        s = Parse_web(url)
        if ( s != None):
            size = len(s)
            for j in range(size):
                if (j % 2 == 0):
                    dict[s[j]] = float(s[j + 1])  
            DataFrame.loc[len(DataFrame.index)] = dict
    # DataFrame.columns=["ID", "Toán", "Lí", "Hóa", "Sinh","Văn","Ngoại ngữ", "GDCD", "Địa","Sử"]
    DataFrame.index += 1
    return DataFrame
        
def Parse_web(url):
    try:
        # html = urlopen(url, context=ctx).read()
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup("td")
        s = []
        for tag in tags:
            newline = str(tag.contents[0]).replace("\n", "").replace("\t", "")
            s.append(newline)
        return s
    except:
        return None
# Collect data
class CollectData(object):
    def __init__(self, rooturl, startid, endid):
        self.dataframe = CreateDataFrame(rooturl, startid, endid)
        
    def SaveData(self, filename):
        self.dataframe.to_csv(filename)
url = "https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt"
# get id from 02000001 to 02001000

DataFrame2021 = CollectData(url + "/2021/", "02000001", "02000005")
DataFrame2021.SaveData("_2021.csv")
DataFrame2022 = CollectData(url + "/2022/", "02000001", "02000005")
DataFrame2022.SaveData("_2022.csv")