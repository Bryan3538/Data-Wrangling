import xlwt
import xlrd
from xlutils.copy import copy
datafile = "book1.xls"

def write_to_file(datafile):
	workbook = copy(xlrd.open_workbook(datafile))
	sheet = workbook.get_sheet(0)
	sheet.write(0, 0, 1)
	workbook.save(datafile)

	return

write_to_file(datafile)