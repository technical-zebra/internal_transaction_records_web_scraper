import string

from bs4 import BeautifulSoup
import requests
import pandas as pd

df = pd.DataFrame({'X': [], 'Filing Date': [], 'Trade Date': [], 'Ticker': [], 'Company Name': [], 'Insider Name': [],
                   'Title': [], 'Trade Type': [], 'Price': [], 'Qty': [], 'Owned': [], 'ΔOwn': [], 'ΔValue': []})

# column_names = []

stop_condition = False
num = 1;

while (stop_condition != True) and (num < 56):
    link = string.Formatter
    html_text = requests.get(f'https://www.mobile2date.com/?sy&o&fd=0&td=365&xp=1&ocl&och&sortcol=0&cnt=300&pg={num}').text
    soup = BeautifulSoup(html_text, 'lxml')
    table = soup.find('table', class_='tinytable')
    # table_head = table.find('thead').tr.find_all('th')
    # for column_name in table_head:
    #     column_names.append(column_name.h3.string)
    # print(column_names)
    table_body = table.find('tbody')
    table_rows = table_body.find_all('tr')

    for table_row in table_rows:
        table_columns = table_row.find_all('td')
        s = str("")
        for n in range(13):
            if table_columns[n].string == None and n == 0:
                s += "None"
            elif table_columns[n].string != None and n == 0:
                s += table_columns[n].string
            else:
                s = s + " / " + table_columns[n].string.strip()

        if s == "":
            stop_condition = True
            break
        else:
            columns = s.split(" / ")
            new_row = {'X': columns[0], 'Filing Date': columns[1], 'Trade Date': columns[2], 'Ticker': columns[3],
                       'Company Name': columns[4], 'Insider Name': columns[5], 'Title': columns[6],
                       'Trade Type': columns[7],
                       'Price': columns[8], 'Qty': columns[9], 'Owned': columns[10], 'ΔOwn': columns[11],
                       'ΔValue': columns[12]}
            df = df.append(new_row, ignore_index=True)

    print(f"{num} page done!")
    num += 1

df.to_csv('data_table.csv')




