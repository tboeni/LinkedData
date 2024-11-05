### transform IDKDB int longdata
#type3 Indicators

import pandas as pd
import numpy as np
import os


#data = pd.read_csv("C:/Users/Bot3/OneDrive - Berner Fachhochschule/Files BAFU/IDKDB/Types_Indicateurs_type2.csv", sep = ";", encoding = "ANSI")

directory_start = "C:/Users/Bot3/OneDrive - Berner Fachhochschule/Files BAFU/IDKDB/Rawfiles_csv/"
directory_end = "C:/Users/Bot3/OneDrive - Berner Fachhochschule/Files BAFU/IDKDB/Long_csv/"


# check which number the title line with "Jahr" and the countries is


def remove_desc(data) :
    
    ind_year = np.where(data == 'Jahr')
    
    if len(ind_year[0]) >= 2: # check wether this identifier has more than one occurence in the data set
        
        print("No unique matching header was found")
        
        
    else :

        row_ind = int(ind_year[0])
        print("The header for 'Jahr' is found at line " + str(row_ind))
        data = data[row_ind:].reset_index(drop = True)
        new_header = data.iloc[0]
        data = data[1:]
        data.columns = new_header
        return data

    


# delete the rest above header

def clean_dat(data) :
    data = remove_desc(data)
    data = data.replace('\W+','',regex=True).astype(str)
    data = data.replace('nan', '')
    print("Data cleaned for special characters and NaN")
    return data

# transform the table into a long table

def make_long_table(data) :
    data = clean_dat(data)
    data = pd.melt(data, id_vars = data.columns.values[0], value_vars = data.columns.values[1:], var_name= "variable")
    data = data.dropna()
    return data
 

 
  
# pick all csv from the 'Rawfiles' folder, transform them and save it with a new name to the 'Long  files' folder

chdr_start = os.chdir(directory_start)
path_start = os.getcwd()

csv_list = os.listdir(directory_start)
for csv in csv_list :
    csv_file_path = os.path.join(path_start, csv) 
    data = pd.read_csv(csv_file_path, sep = ";", encoding = "ANSI")
    data = make_long_table(data)
    chdr_end = os.chdir(directory_end)
    path_end = os.getcwd()
    csv_save_path = os.path.join(path_end, "long_" + csv)
    data.to_csv(csv_save_path, sep = ";", encoding = "ANSI")
    chdr_start = os.chdir(directory_start)
    path_start = os.getcwd()


