from core import create_app
from flask import jsonify,request
import openpyxl
from datetime import date,datetime
from flask_apscheduler import APScheduler
import time
from pywhatkit.whats import sendwhats_image,sendwhatmsg_instantly

app = create_app()
app.debug = True
scheduler = APScheduler()
scheduler.init_app(app)


if __name__ == "__main__":
    app.run

def hello():
    print(hello)

# @app.route('/index',methods=['GET'])
def index(persons):
    birth_day_persons = []
    today = date.today()
    for i in persons:
        if isinstance(i['dob'],str):
            print(i['dob'])
            i['dob'] = datetime.strptime(i['dob'],'%d/%m/%Y')
        if i['dob'].day == today.day and i['dob'].month == today.month:
            birth_day_persons.append(i)

    print(birth_day_persons ,'hi')
    for i in birth_day_persons:
        image_path = 'E:\Programming\profile pics\profile2.jpg'
        sendwhats_image("EaEFItUHCXA6qDtGQm8Utu",image_path,'hi',90)

# def print_date_time():
#     print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

# to start sheduler path to xl file and time message
@app.route('/start',methods=['POST'])
def start():
    data = request.json
    folder = 'E:\Programming\profile pics'
    group = 'Project batch 7'
    xml_file = (openpyxl.load_workbook("details.xlsx")).active
    persons = []
    keys =[]
    h = list(xml_file.rows)[0]
    for i in h:
        keys.append(i.value)
    print(h,keys)
    for row in xml_file.iter_rows(2, xml_file.max_row):
        data = {}
        for i in range(0,len(row)):
            data[keys[i]] = row[i].value
        persons.append(data)
                
    print(persons)
    scheduler.remove_all_jobs()
    if data['job'] == 'stop'  and scheduler.state:
        scheduler.shutdown()
        return data
    file_path = data['path']
    hour = data['time'][:2]
    minute = data['time'][3:5]
    app.apscheduler.add_job(func=index(persons), trigger='cron',day_of_week='mon-sun',hour=hour,minute=minute,id='dob message')  
    if not scheduler.state:
        scheduler.start()
    return data
