from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl 
import pandas

# Ignore SSL certificate errors 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# parse web by opening url
def Parse_web(url):
    try:
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup("td")
        s = []
        for tag in tags:
            newline = str(tag.contents[0]).replace("\n", "").replace("\t", "")
            s.append(newline)
        return s
    except:
        return None
# parse web by cmd
# def Parse_web_cmd(id, url):
#     html = subprocess.


# Create Dataframe
def Add_value_into_DataFrame(root_url, start_id, end_id):
    DataFrame = pandas.DataFrame(columns=["ID", "Toán", "Lí", "Hóa", "Sinh","Văn","Ngoại ngữ", "GDCD", "Địa","Sử"])
    # DataFrame.astype(str)
    province_id = start_id[0] + start_id[1]
    province_id = process_id(int(province_id))
    
    for i in range(int(start_id), int(end_id) + 1):
        dict ={"ID": None,
            "Toán": -1,
            "Lí": -1,
            "Hóa": -1,
            "Sinh": -1,
            "Ngoại ngữ": -1,
            "Văn": -1,
            "GDCD": -1,
            "Địa": -1,
            "Sử": -1
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
    DataFrame.columns=["ID", "Toán", "Lí", "Hóa", "Sinh","Văn","Ngoại ngữ", "GDCD", "Địa","Sử"]
    DataFrame.index += 1
    # DataFrame.loc[:, "ID"].astype(str)
    return DataFrame
def process_id(id):
    if id < 10:
        return "0"
    return ""
    
url = "https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt/2022/"
# get id from 02000001 to 02001000
DataFrame = Add_value_into_DataFrame(url, "02000001", "02000005")
print(DataFrame)
DataFrame.to_csv("result.csv")