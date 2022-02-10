from matplotlib.pyplot import axis
import pandas as pd
import matplotlib as plt
import os
from pathlib import Path
import numpy as np
import json
import re

def reading_files_from_folder(): #This function is basically redaing all files from folder.
    main_folder_path = r'/home/navgurukul/Desktop/dataValidation/archive'
    archive_file_list = os.listdir(main_folder_path)
    return archive_file_list

def read_file(file_name):  #This function is for reading data from file and check file size. if file size is zero so it will delete file. if not it will return file data
    sz = Path(file_name).stat().st_size
    if sz == 0 or '.csv' not in file_name:
        print ('File is deleted becouse it is empty or it is not csv file')
        os.remove(file_name)
        return 'File is empty or not csv file'
    else:
        df = pd.read_csv(file_name)
        return df

def read_json(fileName):
    list = []
    json_data = open(fileName, 'r')
    data_in_py = json.load(json_data)
    for i in data_in_py:
        list.append(data_in_py[i])
    return list

def data_type_checking(fileName, Data): 
    dataType = read_json(fileName)
    z = 0
    for column in Data:
        i = 0
        for value in Data[column]:
            if dataType[z] == 'str':
                x = re.findall("[a-zA-Z]", value)
                if len(x) == 0:
                    Data.drop(Data.index[i], inplace = True)
            elif dataType[z] == 'int':
                convert = str(value)
                x = re.findall("[a-zA-Z]", convert)
                if len(x) != 0:
                    Data.drop(Data.index[i], inplace = True)
            elif dataType[z] == 'float':
                convert = str(value)
                x = re.findall("[a-zA-Z]", convert)
                if len(x) != 0:
                    Data.drop(Data.index[i], inplace = True)
            i = i +1
        z = z+1
    return Data

def formate_checking():  #This function does format checing of data one by one, all file and write modified data in existing file.
    allFiles = reading_files_from_folder()
    for file in allFiles:
        file_data = read_file(file)
        file_data.dropna(inplace = True)
        final_data = data_type_checking(file, file_data )
        print(file_data)
        # file_data.to_csv(file,index = False)

formate_checking()





