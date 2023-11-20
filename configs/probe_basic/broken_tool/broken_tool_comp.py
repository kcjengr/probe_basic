#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# TurBoss 2023


import sys
import json
import time
import datetime

from send_email import EmailNotifications
from hal import component, HAL_BIT, HAL_U32, HAL_IN, HAL_OUT

def main():

    print("INIT BROKEN TOOL COMP")


    notify_flag = False
    
    comp = component("broken_tool_comp")

    comp.newpin("broken_tool_in", HAL_BIT, HAL_IN)
    comp.newpin("msg_sent_out", HAL_BIT, HAL_OUT)

    email_notifications = EmailNotifications(conf)

    comp.ready()


    print("BROKEN TOOL COMP READY")


    while True:
 
        current_time = time.time()

        broken_tool_in = comp["broken_tool_in"]
        msg_sent_out = comp["msg_sent_out"]

		if notify_flag == True:
			if broken_tool_in == True:
				email_notifications.send(1)
				notify_flag = False

if __name__ == "__main__":
    main()
