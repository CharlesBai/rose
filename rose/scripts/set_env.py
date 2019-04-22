# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:12:00 UTC 2019

auto init system enviroment module

@author: white
"""

import re
import sys,os
class set_env(object):
    __sys_plat ='' #linux'
    __LINUX_HOST = 'linux'
    __WIN_HOST = 'win'
    def __init__(self):
        #1 define os platform
        fplatform='platform.txt'
        if(os.path.exists(fplatform) == False):
            linux_pat = re.compile(r'linux', re.I)
            win_pat = re.compile(r'win\d+', re.I)
            if( linux_pat.match(sys.platform) is not None ) :
                self.__sys_plat = self.__LINUX_HOST
            elif( win_pat.match(sys.platform) is not None ) :
                self.__sys_plat = self.__WIN_HOST
            with open(fplatform, 'w+') as f:
                f.write('%s'%(self.__sys_plat))
            print('platform init success !')
        else:
            with open(fplatform, 'r') as f:
                self.__sys_plat=f.readline()

    def set_pythonpath(self):
        python_path=os.getenv('PYTHONPATH')
        if(self.__sys_plat == self.__LINUX_HOST):
            profile='%s/.profile'%(os.getenv('HOME'))
            prj_dir=os.getenv('PWD')
            if(None == python_path):
                with open(profile, 'a+') as f:
                    f.write('export PYTHONPATH=%s\n'%(prj_dir))

            elif(0 == python_path.count(prj_dir)):
                with open(profile, 'a+') as f:
                    f.write('export PYTHONPATH=${PYTHONPATH}:%s\n'%(prj_dir))
            #print('Setting PYTHONPATH success!')
        #elif(self.__sys_plat == self.__WIN_HOST):
            #home_dir = os.getenv('HOMEPATH')


if __name__=="__main__":
    #1. check current dir is root dir
    if(os.path.exists('scripts/set_env.py') is False):
        print('\tPlease run scripts/set_env.py under the project root(rose) dir!')
        quit(-1)
    a=set_env()
    a.set_pythonpath()
    print('system init success!')
