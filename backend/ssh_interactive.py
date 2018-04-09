# -*- coding: utf-8 -*-
# @Author  : FELIX
# @Date    : 2018/2/22 20:07

from django.contrib.auth import authenticate
from backend import paramiko_ssh
from web import models


class SshHandler(object):
    """堡垒机交互脚本"""

    def __init__(self, argv_handler_instance):
        self.argv_handler_instance = argv_handler_instance
        self.models = models

    def auth(self):
        """认证程序"""
        count = 0
        while count < 3:
            username = input("堡垒机账号:").strip()
            password = input("Password:").strip()
            user = authenticate(username=username, password=password)
            if user:
                self.user = user
                return True
            else:
                count += 1

    def interactive(self):
        """启动交互脚本"""
        if self.auth():
            print("Ready to print all the authorized hosts...to this user ...")
            while True:
                # 获取所有的组名
                host_group_list = self.user.host_groups.all()
                for index, host_group_obj in enumerate(host_group_list):
                    print("%s.\t%s[%s]" % (index, host_group_obj.name, host_group_obj.host_to_remote_users.count()))
                print("z.\t未分组主机[%s]" % (self.user.host_to_remote_users.count()))
                while True:
                    choice = input("请选择主机组>>:").strip()
                    if choice.isdigit():
                        try:
                            choice = int(choice)
                            selected_host_group = host_group_list[choice]
                            break
                        except Exception as e:
                            print('请输入正确的数字')
                    elif choice == 'z':
                        selected_host_group = self.user
                        break
                    else:
                        print('请输入正确的数字')

                while True:
                    for index, host_to_user_obj in enumerate(selected_host_group.host_to_remote_users.all()):
                        print("%s.\t%s" % (index, host_to_user_obj))
                    while True:
                        choice = input("请选择主机>>:").strip()
                        if choice == "b":
                            break
                        if choice.isdigit():
                            try:
                                choice = int(choice)
                                selected_host_to_user_obj = selected_host_group.host_to_remote_users.all()[choice]
                                print("going to logon  %s" % selected_host_to_user_obj)
                                paramiko_ssh.ssh_connect(self, selected_host_to_user_obj)
                                break
                            except Exception as e:
                                print('请输入正确的数')
