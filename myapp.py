import requests
from bs4 import BeautifulSoup
from datetime import datetime
import mysql.connector
from sklearn import tree , preprocessing
mydb = mysql.connector.connect(
    user="kilid",
    password='123',
    host="127.0.0.1",
    database="db1"
)
x = []
y = []
now = datetime.now().strftime('%Y-%m-%d %H:%M:00')
mycursor = mydb.cursor()

r = requests.get('https://www.coindesk.com/price/bitcoin')
soup = BeautifulSoup(r.text, 'html.parser')
elements = soup.find('div', attrs={'class':'coin-info-list price-list'})

for item in elements:
   title = item.find('div', attrs={'class':'title'})
   price = item.find('div', attrs={'class':'data-definition'})
   #print(title.text ,'is: ', price.text)
   if (title.text).find('Price') != -1:
       price_save = price.text
   elif (title.text).find('24 Hour % Change') != -1:
       change_save = price.text
   elif (title.text).find('Market Cap') != -1:
       MArket_cap_save = price.text
   elif (title.text).find('Volume (24h)') != -1:
       Volume_24H_save = price.text
sql = "INSERT INTO btc (dates, price, 24H_change, Market_Cap, Volume_24H) VALUES (%s, %s, %s, %s, %s)"
val = (now, price_save, change_save, MArket_cap_save, Volume_24H_save)
mycursor.execute(sql, val)
mydb.commit()

mycursor.execute("select * from btc where id = '10'")
results = mycursor.fetchall()
for row in results:
    x.append(row[3:7])
    y.append(row[2])
print(x[0])
print(y[0])
clf = tree.DecisionTreeClassifier()
labelencoder = preprocessing.LabelEncoder()
clf = labelencoder.fit_transform(x , y)