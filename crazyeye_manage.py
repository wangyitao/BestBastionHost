# -*- coding: utf-8 -*-
# @Author  : FELIX
# @Date    : 2018/2/22 19:30

import sys,os

if __name__=='__main__':

    """如果要访问django的数据库环境，添加下面三条命令"""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "堡垒机CrazyEye.settings")
    import django
    django.setup()



    from backend import main
    interactive_obj=main.Argvhandler(sys.argv)
    interactive_obj.call()

