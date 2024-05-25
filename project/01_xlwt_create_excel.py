# pip install xlwt
import xlwt

# create a excel
wb = xlwt.Workbook()

# create a sheet
sh = wb.add_sheet('moive')

# write headers to the worksheet
sh.write(0, 0, 'Movie')
sh.write(0, 1, 'Total Box Office')
sh.write(0, 2, 'Box Office Share')
sh.write(0, 3, 'Screenings')

# Movie data
movies = [
    ('If Sound is Remembered', 361.57, 33.3, 95371),
    ('Mr. Red Fox', 194.23, 17.8, 79980),
    ('Clear Sky', 130.05, 11.8, 42457),
    ('Crazy Beginning 2', 120.72, 10.9, 40697)
]

# write movie data to worksheet
for row, (name, total_box_office, box_office_share, screenings) in enumerate(movies, start=1):
    sh.write(row,0,name)
    sh.write(row,1,total_box_office)
    sh.write(row,2,box_office_share)
    sh.write(row,3,screenings)


# save excel
wb.save('01_moive_data.xlsx')