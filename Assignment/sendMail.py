import warnings
warnings.filterwarnings('ignore')
import os
import smtplib
# from _datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pandas as pd
import xlrd
import path
import pyodbc
from datetime import datetime
import TableView as d

#dirpath = os.path.dirname(os.path.realpath(_file_))
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=137.116.139.217;'
                      'DATABASE=ARCHIVESKF;'
                      'UID=sa;'
                      'PWD=erp@123;')

data_df = pd.read_sql_query("""
        declare @Rptdate DATE=getdate()-1
        declare @DaysInMonth  nvarchar(MAX)
        set @DaysInMonth = DAY(EOMONTH(@Rptdate))

        DECLARE @TotalDaysInMonth as Integer=(SELECT DATEDIFF(DAY, @Rptdate, DATEADD(MONTH, 1, @Rptdate)))
        DECLARE @totalDaysGone as integer =(SELECT DATEPART(DD, @Rptdate))

        DECLARE @DATE AS SMALLDATETIME = @Rptdate
        DECLARE @FIRSTDATEOFMONTH AS SMALLDATETIME = CONVERT(SMALLDATETIME, CONVERT(CHAR(4),YEAR(@DATE)) + '-' + CONVERT(CHAR(2),MONTH(@DATE)) + '-01')
        DECLARE @YESTERDAY AS SMALLDATETIME = DATEADD(d,-1,@DATE)
        DECLARE @This_month as CHAR(6)= CONVERT(VARCHAR(6), @Rptdate, 112)
        DECLARE @FIRSTDATEOFMONTH_STR AS CHAR(8)=CONVERT(VARCHAR(10), @FIRSTDATEOFMONTH , 112)
        DECLARE @YESTERDAY_STR AS CHAR(8)=CONVERT(VARCHAR(10), @Rptdate , 112)
        DECLARE @BEFOREYESTERDAY_STR AS CHAR(8)=CONVERT(VARCHAR(10), @YESTERDAY , 112)

        SELECT     dbo.OESalesDetails.ITEM, dbo.prinfoskf.[DESC] as [Item Name], SUM(dbo.OESalesDetails.QTYSHIPPED) AS Qty, SUM(dbo.OESalesDetails.EXTINVMISC)
                                AS Sales
        FROM         dbo.OESalesDetails LEFT OUTER JOIN
                                dbo.prinfoskf ON rtrim(OESalesDetails.ITEM) = rtrim(dbo.prinfoskf.ITEMNO)
        WHERE     (dbo.OESalesDetails.PRICELIST <> '00') AND  (dbo.OESalesDetails.TRANSDATE BETWEEN @FIRSTDATEOFMONTH_STR AND @YESTERDAY_STR)

        GROUP BY dbo.OESalesDetails.ITEM, dbo.prinfoskf.[DESC]
        order by [Item Name] """, conn)

date = datetime.today()
day = str(date.day) + '-' + str(date.strftime("%b")) + '-' + str(date.year)
data_df.to_excel(day + "_ItemWiseSales.xlsx", index=False, startrow=0)

msgRoot = MIMEMultipart('related')
me = 'erp-bi.service@transcombd.com'

to = ['dulal.halder@transcombd.com', '']
cc = ['', '']
bcc = ['', '']

recipient = to + cc + bcc

date = datetime.today()
today = str(date.day) + '-' + str(date.strftime("%b")) + '-' + str(date.year) + ' ' + date.strftime("%I:%M %p")
today1 = str(date.day) + '-' + str(date.strftime("%b")) + '-' + str(date.year)

# # ------------ Group email --------------------
subject = "Item Wise Sales Data " + today
email_server_host = '10.168.2.5'
port = 25

msgRoot['From'] = me
msgRoot['To'] = ', '.join(to)
msgRoot['Cc'] = ', '.join(cc)
msgRoot['Bcc'] = ', '.join(bcc)
msgRoot['Subject'] = subject

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)
b = open("./images/all_banner_ai.png", 'rb')
banner = MIMEImage(b.read())
b.close()
banner.add_header('Content-ID', '<banner>')
msgRoot.attach(banner)

msgText = MIMEText("""
             <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
        table {
            border-collapse: collapse;
            border: 1px solid black;
            padding: 1px;
            table-layout: fixed;

        }

        td {
            padding-top: 3px;

            border-bottom: 1px solid black;
            white-space: nowrap;
            border: 1px solid black;
            overflow: hidden;

        }

        .qty{
        text-align: right;
        }

        th.unit {

            border: 1px solid black;
            background-color: #58b9b9;
            font-size: 14px; 
        }


        </style>

    </head>
        <img src="cid:banner" width="100%;">

        <table  width: 100%;>
          <tr><th colspan='4' style=" background-color: #b2ff66; font-size: 20px; ">Dulal</th></tr>

                """ + d.my_data_viewer()+ """</table>
        <br>


        </br> </br>

        </body>

        </html>""", 'html')

msgAlternative.attach(msgText)
part = MIMEBase('application', "octet-stream")
file_location = str(day) + "_ItemWiseSales.xlsx"
filename = os.path.basename(file_location)
attachment = open(file_location, "rb")
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msgRoot.attach(part)

server = smtplib.SMTP(email_server_host, port)
server.ehlo()
print('\n-----------------')
print('Sending Mail')
server.sendmail(me, recipient, msgRoot.as_string())
print('Mail Send')
print('-------------------')
server.close()
