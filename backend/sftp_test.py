import os,sys
import paramiko

t = paramiko.Transport(('192.168.27.128',22))
t.connect(username='felix',password='felixwang')

sftp = paramiko.SFTPClient.from_transport(t)

# 获取远程的文件
sftp.get('/home/felix/views.py','d:/views.py')
# 向远程传送文件
# sftp.put('d:/牛X的开机启动.jpg','/root/test.jpg')
t.close()

#
# import os,sys
# import paramiko
#
# t = paramiko.Transport(('182.92.219.86',22))
# t.connect(username='wupeiqi',password='123')
# sftp = paramiko.SFTPClient.from_transport(t)
# sftp.get('/tmp/test.py','/tmp/test2.py')
# t.close()