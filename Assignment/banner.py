from datetime import  datetime
import pytz
from PIL import Image,ImageDraw,ImageFont

date = datetime.today()
day = "Upto" + str(date.day) + '/' + str(date.month) + '/' + str(date.year)
tz_NY = pytz.timezone('Asia/Dhaka')
datetime_BD = datetime.now(tz_NY)
time = datetime_BD.strftime("%I:%M %p")
#print(time)
date = datetime.today()
#x = dd.datetime.now()
#day = str(date.day) + '-' + str(x.strftime("%b")) + '-' + str(date.year)
tz_NY = pytz.timezone('Asia/Dhaka')
datetime_BD = datetime.now(tz_NY)
time = datetime_BD.strftime("%I:%M %p")
print(time)

img = Image.open("./images/new_ai.jpeg")
title = ImageDraw.Draw(img)
timestore = ImageDraw.Draw(img)
tag = ImageDraw.Draw(img)
branch = ImageDraw.Draw(img)
font = ImageFont.truetype("./Fonts/Stencil_Regular.ttf", 35, encoding="unic")
font1 = ImageFont.truetype("./Fonts/ROCK.ttf", 35, encoding="unic")
font2 = ImageFont.truetype("./Fonts/ROCK.ttf", 18, encoding="unic")
report_name = ''
#
# tag.text((18, 8), 'SK+F', (255, 255, 255), font=font)
branch.text((25, 130), report_name + "Assignment Banner (Dulal)", (255, 209, 0), font=font1)
timestore.text((175, 175), "Upto " + day + "," + time, (255, 255, 255), font=font2)
print(time)
img.save("./images/all_banner_ai.png")

print('Banner created for :All ')