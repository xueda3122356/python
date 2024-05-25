# pip install xlrd
import xlrd

# open excel
wb = xlrd.open_workbook('./generate_data/01_moive_data.xlsx')

# select worksheet
print(wb.sheet_names())
sh1 = wb.sheet_by_index(0)
sh2 = wb.sheet_by_name('moive')

print(f'there are {sh1.nrows} rows, and {sh2.ncols} columns in the sheet')

# obtain data in the cell
print(f'The value in the first row and second column: {sh1.cell_value(0,1)}')
print(f'The value in the first row and second column: {sh1.cell(0,1).value}')
print(f'The value in the first row and second column: {sh1.row(0)[1].value}')

# obtain the whole row or the whole column's value
print(sh1.row_values(0))
print(sh2.col_values(1))

# obtain all value from the sheet
for r in range(sh1.nrows):
    for c in range(sh1.ncols):
        print(f'The value of the {r+1} row and the {c+1} col: {sh1.cell_value(r,c)}')
    print('\n')