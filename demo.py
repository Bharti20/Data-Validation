import json
import pandas as pd
import os 
import re

file = '/home/navgurukul/Desktop/dataValidation/nba.csv'
df = pd.read_csv(file)




def read_json(fileName):
    list = []
    json_data = open(fileName, 'r')
    data_in_py = json.load(json_data)
    for i in data_in_py:
        list.append(data_in_py[i])
    return list


def data_type_checking():
    z = 0
    dataType = read_json('demo.json')
    for column in df:
        i = 0
        for value in df[column]:
            if dataType[z] == 'str':
                x = re.findall("[a-zA-Z]", value)
                if len(x) == 0:
                    df.drop(df.index[i], inplace = True)
            elif dataType[z] == 'int':
                convert = str(value)
                x = re.findall("[a-zA-Z]", convert)
                if len(x) != 0:
                    df.drop(df.index[i], inplace = True)
            elif dataType[z] == 'float':
                convert = str(value)
                x = re.findall("[a-zA-Z]", convert)
                if len(x) != 0:
                    df.drop(df.index[i], inplace = True)
            i = i +1
        z = z+1
    print(df)
data_type_checking()

