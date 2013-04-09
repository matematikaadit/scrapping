import sys
import csv
from bs4 import BeautifulSoup
from jinja2 import Template

template_f = open('template.html', 'rb')
csv_f = open('result.csv', 'rb')
index_f = open('index.html', 'wb')

template = Template(template_f.read())
resultreader = csv.reader(csv_f)

results = []
for row in resultreader:
  results.append(row)

index_f.write(template.render(rs=results))

template_f.close()
csv_f.close()
index_f.close()
