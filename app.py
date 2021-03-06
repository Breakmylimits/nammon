
from flask_sqlalchemy import SQLAlchemy 
from flask import Flask, request, abort
import requests
import json
from Config import *
import urllib.parse


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'





db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    score = db.Column(db.Integer)
    password = db.Column(db.String(50))
    teacher = db.Column(db.String(50))

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    token = db.Column(db.String(50))


url = "https://notify-api.line.me/api/notify" 

def line_text(message, LINE_ACCESS_TOKEN):	
	msg = urllib.parse.urlencode({"message":message})
	LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
	session = requests.Session()
	a=session.post(url, headers=LINE_HEADERS, data=msg)

@app.route('/<fname>/<lname>/<score>/<teacher>')
def index(fname, lname):
    user = User(fname=fname, lname=lname, score=score, teacher=teacher  )
    db.session.add(user)
    db.session.commit()

    return '<h1>Added New User!</h1>'

@app.route('/<fname>')
def get_user(fname):
    user = User.query.filter_by(fname=name).first()

    return f'<h1>The user is located in: { user.score }</h1>'

@app.route('/delete/<name>')
def get_delete(name):
    user = User.query.filter_by(fname=fname, lname=lname).first()
    db.session.delete(user)
    db.session.commit()

    return '<h1>Delete</h1>'


@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json

        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        message = payload['events'][0]['message']['text']
        print(message)
        if '??????????????????' in message :
            Reply_messasge='??????????????????????????? ????????????????????????????????????????????????????????????'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        
        elif"/" in message :
            ma=message.split("/")
            print(ma)
            user = User.query.filter_by(fname=ma[1], lname=ma[2], password=ma[3]).first()
            Reply_messasge = f'???????????? {user.fname} { user.lname } ????????????????????? {user.score}?????????'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
                    
        elif"????????????????????????" in message :
            Reply_messasge = '''??????????????????????????????????????????????????????????????????
            ???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????(???????????????????????????????????????)?????????
            '''
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif"?????????????????????????????????????????????????????????" in message :
            Reply_messasge ='''??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
    ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????  ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
    ????????????????????????????????? - ???????????????????????????????????????????????????????????????????????????????????????????????????????????????-???????????????????????????????????????????????????-????????????4??????????????????????????????????????????????????????????????? ???????????????????????????????????? ??????????????????????????????????????? ???????????? ????????????????????????????????????????????????????????????????????????????????????????????? -Akara-Alisara-7892 ????????? 
    ????????????????????????????????????????????????????????????????????????????????????????????? ??????????????? ?????????????????? ?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? +???????????????????????????????????????????????????????????????????????????????????????????????????????????????+???????????????????????????????????????????????????+????????????4???????????????????????????????????????????????????????????????+?????????????????????????????????????????? ??????????????? ??????????????????+?????????????????????????????????????????????????????????????????????????????????????????????????????????????????? ???????????????????????????????????? +Akara+Alisara+7892+??????????????????????????????+?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? 3 ????????? ?????????'''
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif"??????????????????" in message :
            ReplyButtons(Reply_token, Channel_access_token)

        elif"+" in message :
            ma=message.split("+")
            print(ma)
            user = User.query.filter_by(fname=ma[1], lname=ma[2], password=ma[3]).first()
            teacher1=user.teacher
            teacher = Teacher.query.filter_by(fname=teacher1).first()
            Reply_messasge = f'??????????????????????????????????????????????????????{user.teacher} ????????????????????? {user.fname} { user.lname }????????? {ma[4]}?????????'
            notify=f'??????????????????????????????{user.fname} { user.lname }{ma[4]} ?????????????????????????????????????????????{ma[5]}?????????'
            print(f'{teacher.token}')
            LINE_ACCESS_TOKEN=f'{teacher.token}'
            print(LINE_ACCESS_TOKEN)
            line_text(notify, LINE_ACCESS_TOKEN)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token) 
        elif"*" in message :
            ma=message.split("*")
            print(ma)
            user = User.query.filter_by(fname=ma[1], lname=ma[2], password=ma[3]).first()
            teacher1=user.teacher
            teacher = Teacher.query.filter_by(fname=teacher1).first()
            Reply_messasge = f'??????????????????????????????????????????????????????{user.teacher} ????????????????????? {user.fname} { user.lname }????????? {ma[4]}?????????'
            notify=f'??????????????????????????????{user.fname} { user.lname }{ma[4]}?????????'
            print(f'{teacher.token}')
            LINE_ACCESS_TOKEN=f'{teacher.token}'
            print(LINE_ACCESS_TOKEN)
            line_text(notify, LINE_ACCESS_TOKEN)
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif"-" in message :  
            ma=message.split("-")
            user = User.query.filter_by(fname=ma[1], lname=ma[2], password=ma[3]).first()
            SFNAME=f'{user.fname}'
            SLNAME=f'{user.lname}'
            SPASS=f'{user.password}'
            teacher1=user.teacher
            teacher = Teacher.query.filter_by(fname=teacher1).first()
            TFNAME=f'{teacher.fname}'
            TLNAME=f'{teacher.fname}'
            Studentname(Reply_token, Channel_access_token, SFNAME, SLNAME, SPASS, TFNAME, TLNAME)

        elif'???????????????' in message :
            Reply_messasge='??????????????????????????? ????????????????????????????????????????????????????????????'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif'??????????????????' in message :
            Reply_messasge='??????????????????????????? ????????????????????????????????????????????????????????????'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif'hello' in message :
            Reply_messasge='??????????????????????????? ????????????????????????????????????????????????????????????'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif'Hello' in message :
            Reply_messasge='??????????????????????????? ????????????????????????????????????????????????????????????'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif'Hi' in message :
            Reply_messasge='??????????????????????????? ????????????????????????????????????????????????????????????'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        elif'hi' in message :
            Reply_messasge='??????????????????????????? ????????????????????????????????????????????????????????????'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)

            
        else:
            Reply_messasge ='????????????????????????????????????????????????????????????????????????????????????????????????'
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
            return request.json, 5000
        
          

            
            
       



        

    elif request.method == 'GET' :
        return 'this is method GET!!!' , 5000

    else:
        
        abort(400)

@app.route('/')




def Replycarousel(Reply_token, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) ##?????????????????????
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
  "type": "template",
  "altText": "this is a image carousel template",
  "template": {
      "type": "image_carousel",
      "columns": [
          {
            "imageUrl": "https://1.bp.blogspot.com/-o4YPhRQT1d0/XbMR1EyCETI/AAAAAAAAAHY/IXYTSuJfvsocbuEVgIhBVbcGUCy9eOi6gCLcBGAsYHQ/s320/38119647_743758185794879_5544365706084089856_n.png",
            "action": {
                "type":"message",
                "label":"???????????????????????????",
                "text":"???????????????????????????"
            }
          },
          {
            "imageUrl": "https://1.bp.blogspot.com/-gyoHrHQa8-U/XbMR1Y8j19I/AAAAAAAAAHc/-0YM-gEMVPsKphTKAO55BrqPXmCynvU-gCLcBGAsYHQ/s320/38121000_744071645763533_4895872695754817536_n.png",
            "action": {
               "type":"message",
                "label":"???????????????????????????",
                "text":"???????????????????????????"
            }
          },
          {
            "imageUrl": "https://1.bp.blogspot.com/-ZY53QZAJe1s/XbMR0ru5CAI/AAAAAAAAAHQ/zrq7D2QLVn4y2rhkrs2ipdaDvvQ4iqwMQCLcBGAsYHQ/s320/34700779_696039347233430_3850755295479332864_n.png",
            "action": {
              "type":"message",
                "label":"???????????????????????????",
                "text":"???????????????????????????"
            }
            
          },
          {
            "imageUrl": "https://1.bp.blogspot.com/-s_ovnRQXf3I/XbMR0vT09gI/AAAAAAAAAHM/AoAgOWO91UYrDBpvQFRt1vcVPXbaYc4hwCLcBGAsYHQ/s320/34811345_695621193941912_3209420582588252160_n.jpg",
            "action": {
              "type":"message",
                "label":"???????????????????????????",
                "text":"???????????????????????????"
            }
            
          },
          {
            "imageUrl": "https://1.bp.blogspot.com/-FQiie01yVJ0/XbMR0wshrQI/AAAAAAAAAHU/YPgGQDK35c0uK7cwlvbq8_TXO516fcGngCLcBGAsYHQ/s320/35643171_706262076211157_922758527951306752_n.png",
            "action": {
              "type":"message",
                "label":"???????????????????????????",
                "text":"???????????????????????????"
            }
            
          }
      ]
  }
}]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    e = requests.post(LINE_API, headers=headers, data=data) 
    return 200






@app.route('/')
def Studentname(Reply_token, Line_Acees_Token, SFNAME, SLNAME, SPASS, TFNAME, TLNAME):
    Fullname=f'????????????{SFNAME} {SLNAME}'
    Commandill=f'*{SFNAME}*{SLNAME}*{SPASS}*??????????????????'
    Commandbiz=f'*{SFNAME}*{SLNAME}*{SPASS}*???????????????'
    Commandlern=f'/{SFNAME}/{SLNAME}/{SPASS}'
    Commandacc=f'*{SFNAME}*{SLNAME}*{SPASS}*??????????????????????????????????????????'
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) 
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
  "type": "template",
  "altText": "??????????????????????????????????????????",
  "template": {
      "type": "buttons",
      "thumbnailImageUrl": "https://1.bp.blogspot.com/-nSrpGCpruoc/XbRr-NIyOEI/AAAAAAAAAIA/br78BKoZlNM7VlsjwxhNNevQYi6WVb7qgCLcBGAsYHQ/s400/80107965_0_20160213-173903.jpg",
      "imageAspectRatio": "rectangle",
      "imageSize": "cover",
      "imageBackgroundColor": "#FFFFFF",
      "title": "??????????????????????????????????????????????????????????????????",
      "text": Fullname,
      "defaultAction": {
          "type": "uri",
          "label": "?????????????????????????????????????????????",
          "uri": "https://bit.ly/37ar4nD"
      },
      "actions": [
           {
            "type":"message",
            "label":"??????????????????????????????",
            "text":Commandlern
          },
          {
            "type":"message",
            "label":"??????????????????",
            "text":Commandill
          },
          {
            "type":"message",
            "label":"???????????????",
            "text":Commandbiz
          },
          {
            "type":"message",
            "label":"??????????????????????????????????????????????????????????????????",
            "text":Commandacc
          },
          
      ]
  }
}]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    e = requests.post(LINE_API, headers=headers, data=data) 
    return 200

@app.route('/')
def ReplyButtons(Reply_token, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) ##?????????????????????
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
  "type": "template",
  "altText": "??????????????????????????????????????????",
  "template": {
      "type": "buttons",
      "thumbnailImageUrl": "https://1.bp.blogspot.com/-nSrpGCpruoc/XbRr-NIyOEI/AAAAAAAAAIA/br78BKoZlNM7VlsjwxhNNevQYi6WVb7qgCLcBGAsYHQ/s400/80107965_0_20160213-173903.jpg",
      "imageAspectRatio": "rectangle",
      "imageSize": "cover",
      "imageBackgroundColor": "#FFFFFF",
      "title": "?????????????????????????????????????????????????????????????????????????????????????????????????????????",
      "text": "?????????????????????????????????????????????",
      "defaultAction": {
          "type": "uri",
          "label": "?????????????????????????????????????????????",
          "uri": "https://bit.ly/37ar4nD"
      },
      "actions": [
           {
            "type":"message",
            "label":"?????????????????????????????????????????????????????????",
            "text":"?????????????????????????????????????????????????????????"
          },
          {
            "type":"message",
            "label":"????????????????????????????????????????????????????????????",
            "text":"????????????????????????"
          },
          {
            "type": "uri",
            "label": "????????????????????????????????????????????????",
            "uri": "https://bit.ly/37ar4nD"
          },
          {
            "type": "uri",
            "label": "facebook fanpage",
            "uri": "https://www.facebook.com/pg/huasaireunprachabanschool/posts/"
          }
      ]
  }
}]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    e = requests.post(LINE_API, headers=headers, data=data) 
    return 200




def ReplyPic(Reply_token, PicUrl,Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) ##?????????????????????
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data ={
        "replyToken":Reply_token,
        "messages": [{
            "type": "image",
            "originalContentUrl": PicUrl,
            "previewImageUrl": PicUrl,
            
        }]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    e = requests.post(LINE_API, headers=headers, data=data) 
    return 200

def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) ##?????????????????????
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        }]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    e = requests.post(LINE_API, headers=headers, data=data) 
    return 5000
