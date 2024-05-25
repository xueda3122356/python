import xlwt

wb = xlwt.Workbook()
sh = wb.add_sheet('数据')

ft = xlwt.Font()
ft.name = 'Times New Roman'    # set font
ft.colour_index = 2 # set color
ft.height = 11 * 20 # set font size
ft.italic = True
ft.bold = True
ft.underline = True

# set alignment
alg = xlwt.Alignment()
alg.horz = 2 # 1 left,2 middle,3 right
alg.vert = 1 # 0 up,1 middle,2 down 

# set height of row
sh.row(3).height_mismatch = True
sh.row(3).height = 10 * 256
# set width of col
sh.col(3).width = 20 * 256

# set boarder 
boarder = xlwt.Borders()

boarder.left = 1
boarder.right = 1
boarder.top = 1
boarder.bottom = 1

boarder.left_colour = 1
boarder.right_colour = 2
boarder.top_colour = 3
boarder.bottom_colour = 4

# set color of background
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 5

style = xlwt.XFStyle()
style.font = ft
style2 = xlwt.XFStyle()
style2.alignment = alg
style3 = xlwt.XFStyle()
style3.borders = boarder
style4 = xlwt.XFStyle()
style4.pattern = pattern

style5 = xlwt.easyxf('font: name Times New Roman, bold on, italic on, color_index 6; alignment: vert center, horiz center')


sh.write(1,1,'Hello World')
sh.write(2,2,'Hello World',style)
sh.write(3,3,'Hey dude',style2)
sh.write(4,4,'Good morning',style3)
sh.write(5,5,'Good afternoon',style4)
sh.write(6,6,'Bye',style5)

wb.save('./generate_data/04_font_style_modify.xlsx')

