from matplotlib import colors
from matplotlib.pyplot import axis
import pandas as pd
import matplotlib as plt
import os
from pathlib import Path
import numpy as np
import json
import re
import numpy as np 
orignal_files_len = []
modified_files_len = []

def reading_files_from_folder(): #This function is basically redaing all files from folder one by one.
    main_folder_path = r'/home/navgurukul/Desktop/dataValidation/archive'
    archive_file_list = os.listdir(main_folder_path)
    return archive_file_list

def read_file(file_name):  #This function is for reading data from file and check file size. if file size is zero so it will delete file. if not it will return file data
    sz = Path(file_name).stat().st_size
    if sz == 0 or '.csv' not in file_name:
        print ('File is deleted becouse it is empty or it is not csv file')
        os.remove(file_name)
        print('File is empty or not csv file')
        return
    else:
        df = pd.read_csv(file_name)
        orignal_files_len.append(len(df))
        return df

def read_json(fileName):  #This function is for redaing json data
    list = []
    json_data = open(fileName, 'r')
    data_in_py = json.load(json_data)
    for i in data_in_py:
        list.append(data_in_py[i])
    return list

#This function is for data type check confirms that the data entered has the correct data type or not.
#For example, a field might only accept numeric data. If this is the case, then any datacontaining other characters, it will be delete that row
def data_type_checking(fileName, Data):     
    csv_f = fileName 
    json_f = csv_f.replace('csv','json')
    dataType = read_json(json_f)
    z = 0
    for column in Data:
        i = 0
        for value in Data[column]:
            if dataType[z] == 'str':
                x = re.findall("[a-zA-Z]", value)
                if len(x) == 0 or value[0] == '-':
                    Data.drop(Data.index[i], inplace = True)
            elif dataType[z] == 'int':
                convert = str(value)
                x = re.findall("[a-zA-Z]", convert)
                if len(x) != 0 or convert[0] == '-':
                    Data.drop(Data.index[i], inplace = True)
            elif dataType[z] == 'float':
                convert = str(value)
                x = re.findall("[a-zA-Z]", convert)
                if len(x) != 0 or convert[0] == '-':
                    Data.drop(Data.index[i], inplace = True)
            i = i +1
        z = z+1
    return Data

def formate_checking():  #This function does format checing of data. if there is any raw/column with null/NaN/emty data, it will discard rows and columns and write modified data in existing file.
    allFiles = reading_files_from_folder()
    for file in allFiles:
        df = read_file('/home/navgurukul/Desktop/dataValidation/archive/'+file)
        df.replace(r'^\s*$', np.NaN, regex=True)
        df.dropna(how='all',inplace = True, axis = 1)
        df.dropna(how ='all',inplace = True, axis = 0)
        df.dropna(inplace = True)
        final_data = data_type_checking(file, df )
        modified_files_len.append(len(final_data))
        final_data.to_csv('/home/navgurukul/Desktop/dataValidation/archive/'+file,index = False)
    
formate_checking()
print()
print('All files data has validated succesfully')
print()
print("orignal data len file wise:", orignal_files_len)
print("modified data len diffrent file wise:", modified_files_len)

#This function is for showing graph of data difference, after validation. like before validation file length and after validation length difference.
def graph_of_four_files_data ():
    import matplotlib.pyplot as plt 
    no_of_files = np.array([1,2,3,4])
    orignal_f_data = np.array([4473, 350, 1050, 2449])      #this array's data i have write as fixed becouse i wanted to show before and after validation data lenght.
    modified_f_data = np.array([3138, 350, 1050, 2447])     #if you want to check with updated data, you can use these two varible - orignal_files_len, modified_files_len.
    plt.bar(no_of_files, orignal_f_data) 
    plt.bar(no_of_files,modified_f_data,color='red',width=0.2)
    plt.ylabel('Number of Files')
    plt.xlabel('Before modified and After modified Data')
    plt.title('CSV Files Validated Data')
    plt.show()
graph_of_four_files_data()









