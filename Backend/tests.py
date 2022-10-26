from datetime import datetime
import re

def extractDate(text):
    date = re.findall(r'(\d{2})/(\d{2})/(\d{4})', text)
    hour = re.findall(r'(\d{2}):(\d{2})', text)

    if len(date) > 0:
        date = date[0]
        date = '/'.join(date)
    if len(hour) > 0:
        hour = hour[0]
        hour = ':'.join(hour)
    
    if hour.__class__ == str:
        timeAndDate = date+" "+hour
        timeAndDate = datetime.strptime(timeAndDate, '%d/%m/%Y %H:%M')
    else:
        timeAndDate = date
        timeAndDate = datetime.strptime(timeAndDate, '%d/%m/%Y').date()
    return timeAndDate

d = extractDate("El 21/08/2020 fue un dia muy cansado, a las 13:45 horas yo ya estaba descansando.")

date_time = d.strftime("%d/%m/%Y %H:%M")
print("date:",date_time)