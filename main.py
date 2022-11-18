from core import create_app
import threading
import asyncio
from flask import jsonify
import pandas as pd
import openpyxl
from datetime import date,datetime
from dateutil.parser import parse

app = create_app()
app.debug = True

if __name__ == "__main__":
    app.run()

def hello():
    print(hello)

@app.route('/index',methods=['GET'])
async def index():
    # df = pd.read_excel(r'details.xlsx')
    df = openpyxl.load_workbook("details.xlsx")
    df1 = df.active
    print(df,df.active)
    # for row in range(0, df1.max_row):
    for col in df1.iter_cols(1,df1.max_column):
        for i in col:
            print(i.value)
            if i.value == 'dob':
                date_of_birthlist = col
        

    for row in df1.iter_rows(1, df1.max_row):
        print(row)
        for i in row:
            print(i.value)
    # print(date_of_birthlist)
    # for i in date_of_birthlist:
    #     print(i.coordinate)
    print(date.today())
    for i in date_of_birthlist:
        if i.value != 'dob':
            date_of_birth = datetime.strptime(i.value, '%b %d').replace(year=date.today.year)
            await (date_of_birth == date.today(),hello())
            print('hi')