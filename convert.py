import csv
import json
import re
import pandas as pd

# open csv
with open('sampledata.csv', encoding="utf-8-sig") as csv_file:
    # read csv file
    reader = csv.reader(csv_file, delimiter=';')
    # convert csv data to list
    rows = list(reader)

    tmp_data = []
  
    for x in rows:
      # save all col in a dict / row
      tmp_col = {}
      
      for i, val in enumerate(x):
          if i == 0:
            tmp_col["VIN"] = val # re.sub('\W+','', val) => menghilangkan special chars
          if i == 1:
            tmp_col["TRIP_ID"] = val
          if i == 2:
            tmp_col["DS"] = json.loads(val) # convert string to json / dict
            tmp_data.append(tmp_col)

      tmp_data.append(tmp_col)

    # dataframe = pd.DataFrame.from_dict(json.loads(val)) # => convert dict to dataframe, ref: https://stackoverflow.com/questions/21104592/json-to-pandas-dataframe
    # normalize json, ref: https://stackoverflow.com/questions/6027558/flatten-nested-dictionaries-compressing-keys
    f = pd.json_normalize(tmp_data)

    # f.to_csv("result.csv",encoding='utf-8')
    # save dataframe to excel, ref: https://stackoverflow.com/questions/55170300/how-to-save-a-pandas-dataframe-to-an-excel-file
    f.to_excel("output.xlsx")