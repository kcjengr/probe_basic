#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TurBoss 2023

import sys
import json

import smtplib


from datetime import datetime

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage



class EmailNotifications:
    
    def __init__(self, conf):
        
        # email content
                
        self.from_email = conf.get('from_email')
        self.to_email = conf.get('to_email')
        self.subject = conf.get('subject')
        
        # create SMTP session
        
        self.smtp_server = conf.get('smtp_server')
        self.smtp_port = conf.get('smtp_port')
        self.smtp_username = conf.get('smtp_username')
        self.smtp_password = conf.get('smtp_password')

        
    def send(self, tool_no):
        
        # send mail
        
        current_date = datetime.now().strftime('%d-%m-%Y  %H:%M:%S')
        
        self.body = f"The Tool Nº {tool_no} has been probed broken\n{current_date}"
        
        self.message = MIMEMultipart()
        self.message['From'] = self.from_email
        self.message['To'] = self.to_email
        self.message['Subject'] = self.subject
        self.message.attach(MIMEText(self.body, 'plain'))
        
        self.smtp_session = smtplib.SMTP(self.smtp_server, self.smtp_port)
        self.smtp_session.starttls()
        self.smtp_session.login(self.smtp_username, self.smtp_password)
        self.smtp_session.sendmail(self.from_email, self.to_email, self.message.as_string())
        
        # terminate SMTP session
        
        self.smtp_session.quit()
        
def main():
    conf = None
    try:
        with open("config.json", "r") as data:
            conf_json = data.read()
            conf = json.loads(conf_json)
            
    except Exception as e:
        print("BROKEN TOOL COMP ERROR: ", e)
        sys.exit()
    
    email_notifications = EmailNotifications(conf)

    email_notifications.send(1)
    email_notifications.send(2)


if __name__ == "__main__":
    main()
