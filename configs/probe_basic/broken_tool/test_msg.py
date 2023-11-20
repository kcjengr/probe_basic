#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

from send_email import EmailNotifications


def main():
    conf = None
    try:
        with open("config.json", "r") as data:
            conf_json = data.read()
            conf = json.loads(conf_json)
            
    except Exception as e:
        print("PUMPS COMP ERROR: ", e)
        sys.exit()
        
    from_email = conf.get("from_email")
    to_email = conf.get("to_email")
    subject = conf.get("subject")

    email_notifications = EmailNotifications(conf)

    email_notifications.send(1)
    email_notifications.send(2)


if __name__ == "__main__":
    main()
