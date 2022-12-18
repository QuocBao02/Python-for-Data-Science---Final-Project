import pandas as pd
import numpy as np


# read data from 2 files.
def readfile(filename):
    file = pd.read_csv(filename, index_col= False, dtype = {'ID': 'str'})
    return file

def main():
    source = input("Enter the list name of source file (speperated by comma ): ")
    destination = input("Enter the name of destination file: ")
    
    list_source = source.split(', ')
    newdataframe = pd.DataFrame()
    for file in list_source:
        file1 = readfile(filename = file)
        # file1.reset_index(drop = True)
        newdataframe = pd.concat([newdataframe, file1], ignore_index= True)
        newdataframe = newdataframe[["ID", "Toán", "Lí", "Hóa", "Sinh","Văn","Ngoại ngữ", "GDCD", "Địa","Sử"]]
    newdataframe.index += 1
    newdataframe.to_csv(destination)
if __name__ == "__main__":
    main()