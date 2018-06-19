import csv
import re
import pandas as pd

def get_unique_addr(rows):
    mails = []
    for row in rows:
        #print (row[0].split('$')[1])
        if row[0].split('$')[1] not in mails:
            mails.append(row[0].split('$')[1])
    return mails

def get_last_date(rows):
    dates = []
    for row in rows:
        date = row[0].split('$')[0]
        date = date[:6] + '20' + date[6:]
        if date not in dates and not re.search('[a-zA-Z]', date):
            dates.append(date)
    from datetime import datetime
    last_date = sorted(dates, key = lambda d: datetime.strptime(d, '%d/%m/%Y'), reverse=True)[0]
    last_dateObj = datetime.strptime(last_date, '%d/%m/%Y')
    import datetime
    today = datetime.datetime.now()
    days_gone = today - last_dateObj
    return last_date, days_gone.days

def get_word_hits(rows, csvreader, fields):
    words = ['Python','OpenCV','deadline', 'details', 'Computer Vision', 'Data', 'Machine Learning']
    content = []
    for row in rows:
        line = row[0].split('$')[2]
        if line not in content:
            content.append(line)
    words_to_add = []
    for word in words:
        for line in content:
            if word in line and word not in words_to_add:
                words_to_add.append(word)
    return words_to_add

filename = "data.csv"
fields = []
rows = []

with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
 
    print("Total no. of rows: %d"%(csvreader.line_num))

mails = get_unique_addr(rows)
last_date, days_gone = get_last_date(rows)
words = get_word_hits(rows, csvreader, fields)
print ("Unique addresses: {}\nlast date of conversation = {}\ndays elapsed = {}\n\
Frequent Words = {}".format(mails, last_date, days_gone, words))

