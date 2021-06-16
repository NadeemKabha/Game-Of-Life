from lxml import html
import requests
from openpyxl import Workbook
import random
from openpyxl.styles import Font
from timeit import default_timer as timer

size=10

# List Of Names
names=[]

# List Of Numbers
numbers=[]

# List Of Emails
emails=[]

# Start measuring time
start= timer()

# Random Names Generator
def ngen(size) :
    while len(names)!=size:
        page=requests.get("https://www.behindthename.com/random/random.php?number=2&sets=1&gender=both&surname=&usage_heb=1")
        tree=html.fromstring(page.content)
        name=tree.xpath('/html/body/div[2]/div/div/center/div[1]/span/a[1]/text()')
        lname=tree.xpath('/html/body/div[2]/div/div/center/div[1]/span/a[2]/text()')
        if len(name)==0:
            continue
        if name[0]+' '+lname[0] not in names:
            names.append(name[0]+' '+lname[0])
    return names

# Random Phone Number Generator
def numgen(size):
    for i in range(size):
        number=random.choice(['050','052','054','055'])
        for k in range(7):
            number=number+str(random.randint(0,9))
        if number not in numbers:
            numbers.append(number)
        else:
            i-=1
    return numbers

# Random E-mail addresses Generator
def emgen(size):

    for i in range(size):
        k=names[i].lower()
        k=k.strip()
        k=k.replace(" ","")
        email=k+str(random.randint(111,4444)) +random.choice(["@gmail.com","@yahoo.com","@hotmail.com","@outlook.com"])
        emails.append(email)
    return emails


book = Workbook()
sheet = book.active
# Headers Names
sheet['A1'] = 'Name'
sheet['B1'] = 'Phone number'
sheet['C1']='Email Address'
sheet['A1'].font = Font(bold=True)
sheet['B1'].font = Font(bold=True)
sheet['C1'].font = Font(bold=True)

# Enters The Data To Excel
names=ngen(size)
print(len(names))
numbers=numgen(size)
emails=emgen(size)
for i in range(2,len(names)+2):
    sheet['A'+str(i)]=str(names[i-2])
    sheet['B'+str(i)]=str(numbers[i-2])
    sheet['c' + str(i)] = str(emails[i - 2])
book.save("sample.xlsx")

end = timer()
print(end - start)