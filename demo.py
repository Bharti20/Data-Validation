import json
import pandas as pd
import os 

file = '/home/navgurukul/Desktop/dataValidation/nba.csv'
df = pd.read_csv(file)


def read_json(fileName):
    json_data = open(fileName, 'r')
    data_in_py = json.load(json_data)
    return data_in_py

def data_type_checking():
    dataType = read_json('demo.json')
    list = []
    for i in dataType:
        list.append(dataType[i])
    print(list)
    i = 0
    for column in df:
        for value in df[column]:
            a = bool(int(value))
            print(a)
            # b = str(a)
            # print(b)
            # if list[i] in b:
            #     print('yes')
            # else:
            #     print('same')
        break

data_type_checking()
