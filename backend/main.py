# -*- coding: utf-8 -*-
# @Author  : FELIX
# @Date    : 2018/2/22 19:34

class Argvhandler(object):
    """
    接受用户参数，并调用相应的功能
    """
    def __init__(self,sys_args):
        self.sys_argv=sys_args

    def help_msg(self,error_msg=''):
        """打印帮助"""
        msgs="""
            {}
            run     启动用户交互程序
        """.format(str(error_msg))
        print(msgs)
        exit(msgs)
    def call(self):
        """
        根据用户参数，调用对应的方法
        :return:
        """
        if len(self.sys_argv)==1:
            self.help_msg()
        if hasattr(self,self.sys_argv[1]):
            func=getattr(self,self.sys_argv[1])
            func()
        else:
            self.help_msg('没有这个方法:%s'%self.sys_argv[1])

    def run(self):
        """启动用户交互程序"""
        from backend.ssh_interactive import SshHandler
        obj=SshHandler(self)
        obj.interactive()
