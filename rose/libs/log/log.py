# -*- coding: utf-8 -*-
"""
Created on Wen Dec  1 17:40:30 2018

@author: white
"""

import re
import sys,os
import datetime
import logging.handlers
from datetime import datetime

class log_util:
    def __init__(self):

        #1. setting log format and debug info
        LOG_FORMAT = "%(asctime)s - %(levelname)s - [%(filename)s:(%(funcName)s:%(lineno)d)]: %(message)s"

        #2.1 define os platform
        linux_pat = re.compile(r'linux', re.I)
        win_pat = re.compile(r'win\d+', re.I)

        if( linux_pat.match(sys.platform) is not None ) :
            h='linux'
            log_dir='%s/%s'%(os.getenv('HOME'), 'heenoze/robotv2_log')
        elif( win_pat.match(sys.platform) is not None ) :
            h = 'win'
            log_dir='%s/%s'%(('D:/DailyLog'), 'RobotV2')
        else:
            h = None

        #2.2 check dir, create when nessary
        if(os.path.exists(log_dir) is False):
            os.makedirs(log_dir)

        #2.3 setting right log dir
        total_log= '%s/%s-total-log.txt'%(log_dir, datetime.now().strftime('%Y-%m-%d') )
        err_log= '%s/%s-err-log.txt'%(log_dir, datetime.now().strftime('%Y-%m-%d') )



        #3. setting total log file
        self.total_handler = logging.handlers.TimedRotatingFileHandler(total_log, when='midnight', interval=1, backupCount=7)
        #, atTime=datetime.time(0, 0, 0, 0))
        self.total_handler.setFormatter(logging.Formatter(LOG_FORMAT))

        #4. setting error log file
        self.err_handler = logging.FileHandler(err_log)
        self.err_handler.setLevel(logging.ERROR)
        self.err_handler.setFormatter(logging.Formatter(LOG_FORMAT))

