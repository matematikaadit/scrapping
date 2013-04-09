import sys
import csv
from xlrd import open_workbook,XL_CELL_TEXT,XL_CELL_NUMBER

def check_rows(r, sheet):
  rowtypes = [ x.ctype for x in sheet.row_slice(r,0,4) ]
  tabtypes = [ XL_CELL_NUMBER, XL_CELL_TEXT ] * 2
  return rowtypes == tabtypes

def check_hidden(r, sheet):
  rows_info = sheet.rowinfo_map
  if r in rows_info:
    return rows_info[r].hidden
  return 0

def inside_table(r, sheet):
  return check_rows(r, sheet) and not(check_hidden(r, sheet))

def normal(x):
  if x.ctype == XL_CELL_NUMBER:
    return int(x.value)
  return x.value

def process(source, target='result.csv'):
  book = open_workbook(source,formatting_info=True)
  sheet = book.sheet_by_index(0)
  parse(sheet, target)

def parse(sheet, target):
  with open(target, 'ab') as csv_file:
    tb_writer = csv.writer(csv_file)
    for r in range(sheet.nrows):
      if inside_table(r, sheet):
        tb_writer.writerow([ normal(x) for x in sheet.row_slice(r,0,4)])

if __name__ == '__main__':
  for source in sys.argv[1:]:
    process(source)
