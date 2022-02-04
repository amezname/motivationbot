import csv, random, os
import smtplib
import datetime, time
import sys
import textwrap
import config as cfg
from PIL import Image, ImageDraw, ImageFont
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

### FUNCTIONS ###

def getpath():

    return os.getcwd()

def send(phone,carrier):
     
    auth = ('apikey', cfg.api_key)

    # Establish a secure session with outgoing SMTP server 
    try:
        server = smtplib.SMTP( "smtp.sendgrid.net", 587 )
        server.starttls()
        server.login(auth[0], auth[1])
    except:
        logger("Unable to login to email server. Check API key.")
        pass

    # Add carrier smtp gateways to dictionary

    carr_dict = {'tmobile':'@tmomail.net', 'att':'@att.net','sprint': '@messaging.sprintpcs.com','verizon':'@vtext.com','boost':'@myboostmobile.com','virgin':'@vmobl.com','metropcs':'@mymetropcs.com'}

    # Can update from address to any email

    fromaddr = 'daily@quote.com'
    toaddr = f'{phone}{carr_dict.get(carrier)}'
    message = MIMEMultipart('related')
    message['From'] = fromaddr
    message['To'] = toaddr

    # Open and attach image. 
    abspath = getpath()
    fp = open(f'{abspath}/images/quote.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    message.attach(msgImage)
 
    # Send email and quit session
    try:
        server.sendmail(fromaddr, toaddr, message.as_string())
        server.quit()
    except:
        logger("An error occurred. Unable to send message")
        logger("Exit")
        sys.exit("Error: Unable to send message")

def logger(Message):
    abspath = getpath()
    LogFile = f'{abspath}/log_file.txt'
    now=datetime.datetime.now()
    logtime = str(now)
    with open(LogFile, "a") as Log:
        Log.write(logtime +"  "+ Message + "\n")

def quote_picker():
    # Open the csv file that contains quotes and add to list. Shuffle list and pick one quote.
    abspath = getpath()
    try:
        file = open(f'{abspath}/tweets.csv')
    except:
        logger("Quotes file not found")
        logger("Exit")
        sys.exit("Error: quotes file not found")
    else:
        data = csv.reader(file)
        data_lines = list(data)
        quotes = []
        for line in data_lines:
            l = line[2].split('#')[0]
            quotes.append(l)
        random.shuffle(quotes)
        return quotes[0]


def draw_image(quote):
    abspath = getpath()
    no = random.randint(1,10)
    img = Image.open(f'{abspath}/images/img{no}.jpg')
    text = textwrap.fill(quote,width=40)
    fnt = ImageFont.truetype('Impact.ttf', 48)
    x,y = 50,150
    d = ImageDraw.Draw(img)
    d.multiline_text((x-2,y-2), text, font=fnt, fill=(0, 0, 0))
    d.multiline_text((x+2,y-2), text, font=fnt, fill=(0, 0, 0))
    d.multiline_text((x-2,y+2), text, font=fnt, fill=(0, 0, 0))
    d.multiline_text((x+2,y+2), text, font=fnt, fill=(0, 0, 0))
    d.multiline_text((x,y), text, font=fnt, fill=(255, 255, 255))
    img.save(f'{abspath}/images/quote.jpg')

def set_delay():
    # Pick a random time in seconds for delay
    timer = random.randint(0,32400)
    now = datetime.datetime.now()
    future = now + datetime.timedelta(0,timer)
    return future, timer

if __name__ == "__main__":
    logger("Motivation Bot Activated")
    quote = quote_picker()
    draw_image(quote)
    t2, t1 = set_delay()
    logger("Next message going out @ " + t2.strftime("%H:%M:%S"))
    time.sleep(t1)
    send(cfg.phone,cfg.carrier)
    log_message = f'Sent this "{quote}" to {cfg.phone}'
    logger(log_message)
    logger("Exit")

