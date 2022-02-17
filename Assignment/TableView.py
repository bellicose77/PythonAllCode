import xlrd
def choseRandom(x):
    color = ''
    if(x>=1 and x<=25):
        color = '#f65b5b'
    elif(x>=26 and x<=50):
        color = "#ffff00"
    elif(x>=51 and x<=75):
        color = "#90ee90"
    else:
        color ="#169016"
    return color

def my_data_viewer():
    from datetime import datetime
    date = datetime.today()
    day = str(date.day) + '-' + str(date.strftime("%b")) + '-' + str(date.year)
    xl = xlrd.open_workbook(day + "_ItemWiseSales.xlsx")
    sh = xl.sheet_by_name('Sheet1')
    th = ""
    td = ("")
    # Select all columns header name and placed All name in serial
    for i in range(0, 1):
        th = th + "<tr>\n"
        # th = th + "<th class=\"unit\">ID</th>"

        for j in range(0, 4):
            th = th + "<th class=\"unit\">" + str(sh.cell_value(i, j)) + "</th>\n"
        th = th + "</tr>\n"

    # Now placed all data
    for i in range(1, sh.nrows):
        # td = td + "<tr>\n"
        # td = td + "<td class=\"unit\">" + str(i) + "</td>"

        for j in range(0, 1):
            # fftr
            td = td + "<td id=\"\" style=\"background-color:"  "\">" + str(((sh.cell_value(i, j)))) + "</td>\n"

        for j in range(1, 2):
            # fftr
            td = td + "<td id=\"\" style=\"background-color:"  "\">" + str(((sh.cell_value(i, j)))) + "</td>\n"

        for j in range(2, 3):
            # fftr
            td = td + "<td class=\"qty\" style=\"background-color:" + str((choseRandom(int(sh.cell_value(i, j))))) + "\">" + str(((int(sh.cell_value(i, j))))) + "</td>\n"
        for j in range(3, 4):
            # fftr
            td = td + "<td class=\"qty\" style=\"background-color:"  "\">" + str(((sh.cell_value(i, j)))) + "</td>\n"

        td = td + "</tr>\n"
    html = th + td
    return html