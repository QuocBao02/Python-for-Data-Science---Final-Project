from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def Parse_web(url):
    try:
        # html = urlopen(url, context=ctx).read()
        html = urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup.find_all("td")
        s = []
        for tag in tags:
            newline = str(tag.contents).replace("\n", "").replace("\t", "")
            s.append(newline)
        result = []
        result = s[-2:-12:-1]
        for i in range(len(result)):
            if result[i] == '[]':
                result[i] = result[i].replace("[]", "-1")
            result[i] = result[i].replace("]", "").replace('[', "").replace("'", '')
        return list(reversed(result))
    except:
        return None
def process_id(id):
    if id < 10:
        return "0"
    return ""

# Create a dataframe
def Add_value_into_DataFrame(root_url, start_id, end_id):
    DataFrame = pd.DataFrame(columns=["ID", "Toán", "Lí", "Hóa", "Sinh","Văn","Ngoại ngữ", "GDCD", "Địa","Sử"])
    # DataFrame.astype(str)
    province_id = start_id[0] + start_id[1]
    province_id = process_id(int(province_id))
    
    for i in range(int(start_id), int(end_id) + 1):
        dict = {"ID": None,
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
        subject = ["Toán","Văn", "Ngoại ngữ", "Lí", "Hóa", "Sinh","Sử", "Địa", "GDCD"]
        id = province_id + str(i)
        dict["ID"] = id
        url = root_url + id + "&v_ten=&v_cum_thi=00&547960"
        print(url)
        s = Parse_web(url)
        if (s != None and s != []):
            s.pop(6)
            for j in range(len(subject)):
                dict[subject[j]] = s[j] 
            DataFrame.loc[len(DataFrame.index)] = dict
    DataFrame.columns=["ID", "Toán", "Lí", "Hóa", "Sinh","Văn","Ngoại ngữ", "GDCD", "Địa","Sử"]
    DataFrame.index += 1
    return DataFrame

url = "https://diemthi.24h.com.vn/?v_page=1&v_sbd="

# from 1 to 20k 
DataFrame2020 = Add_value_into_DataFrame(url, "02000001", "02020000")
# print(DataFrame)


DataFrame2020.to_csv("2020_1_20k.csv")

