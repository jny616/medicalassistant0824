#Flex_msg.py
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import *

from IT_help.models import *


def records_progress(uid):
    contents=dict()
    contents['type']='carousel'
    bubbles=[]
    datas = records.objects.filter(uid=uid)
    for data in datas:
        date = data.mdt
        text = data.description
        bubble= {   "type": "bubble",
                    "size": "nano",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "日期：", date,
                            "color": "#ffffff",
                            "align": "start",
                            "size": "md",
                            "gravity": "center"
                            }
                           ],
                           "backgroundColor": "#27ACB2",
                           "paddingTop": "19px",
                           "paddingAll": "12px",
                           "paddingBottom": "16px"
                          },
                          "body": {
                           "type": "box",
                           "layout": "vertical",
                           "contents": [
                            {
                             "type": "box",
                             "layout": "horizontal",
                             "contents": [
                              {
                                "type": "text",
                                "text": "身體狀況：", text,
                                "color": "#8C8C8C",
                                "size": "sm",
                                "wrap": true
                               }
                             ],
                             "flex": 1
                            }
                          ],
                          "spacing": "md",
                          "paddingAll": "12px"
                        },
                        "styles": {
                         "footer": {
                          "separator": false
                         }
                        }
                       },
                       {
                        "type": "bubble",
                        "size": "nano",
                        "header": {
                         "type": "box",
                         "layout": "vertical",
                         "contents": [
                           {
                            "type": "text",
                            "text": "日期：", date,
                            "color": "#ffffff",
                            "align": "start",
                            "size": "md",
                            "gravity": "center"
                           }
                         ],
                         "backgroundColor": "#FF6B6E",
                         "paddingTop": "19px",
                         "paddingAll": "12px",
                         "paddingBottom": "16px"
                        },
                        "body": {
                         "type": "box",
                         "layout": "vertical",
                         "contents": [
                          {
                           "type": "box",
                           "layout": "horizontal",
                           "contents": [
                            {
                              "type": "text",
                              "text": "身體狀況：", text,
                              "color": "#8C8C8C",
                              "size": "sm",
                              "wrap": true
                            }
                           ],
                           "flex": 1
                         }
                        ],
                        "spacing": "md",
                        "paddingAll": "12px"
                    },
                    "styles": {
                     "footer": {
                      "separator": false
                     }
                    }
                   },
                   {
                    "type": "bubble",
                    "size": "nano",
                    "header": {
                     "type": "box",
                     "layout": "vertical",
                     "contents": [
                      {
                        "type": "text",
                        "text": "日期：", date,
                        "color": "#ffffff",
                        "align": "start",
                        "size": "md",
                        "gravity": "center"
                       }
                      ],
                      "backgroundColor": "#A17DF5",
                      "paddingTop": "19px",
                      "paddingAll": "12px",
                      "paddingBottom": "16px"
                     },
                     "body": {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                       {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                         {
                            "type": "text",
                            "text": "身體狀況：", text,
                            "color": "#8C8C8C",
                            "size": "sm",
                            "wrap": true
                           }
                          ],
                          "flex": 1
                         }
                        ],
                        "spacing": "md",
                        "paddingAll": "12px"
                      },
                      "styles": {
                       "footer": {
                        "separator": false
                        }
                      }
                    }
        bubbles.append(bubble)
    contents['contents']=bubbles
    message=FlexSendMessage(alt_text='身體紀錄',contents=contents)
    return message