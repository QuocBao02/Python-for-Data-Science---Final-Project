import pandas as pd

dataframe = pd.read_csv("result.csv", index_col= False)

def CountStudentOfSubject(subject,dataframe):
    df = dataframe.loc[dataframe[subject] >= 0]
    df = df.loc[subject].array
    return len(df)
def PiePlot(list_subject, dataframe):
    y = []
    for index in range(len(list_subject)):
        len_sub = CountStudentOfSubject(list_subject[index], dataframe)
        print(list_subject[index])
        # y.append(len_sub)
    # plt.pie(y, labels = list_subject, shadow= True)
    pass
    
list_subject = ["Toán", "Lí", "Hóa", "Sinh", "Ngoại ngữ"]
print(CountStudentOfSubject(list_subject[3], dataframe))