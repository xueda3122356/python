# pip install xlutils
import xlrd
from xlutils.copy import copy

# open excel
read_book = xlrd.open_workbook('./generate_data/01_moive_data.xlsx')

# copy data
wb = copy(read_book)

# select sheet
sh2 = wb.get_sheet(0)

sh2.write(5,0,'保家卫国')
sh2.write(5,1,113)
sh2.write(5,2,5.1)
sh2.write(5,3,490)


# add sheet
sh3 = wb.add_sheet('汇总数据')

count = 0

rs = read_book.sheet_by_index(0)
for i in range(1, rs.nrows):
    num = rs.cell_value(i,3)
    count += num

sh3.write(0,0,'总票房')
sh3.write(1,0,count)
wb.save('./generate_data/03_movie_data(modified).xlsx')

