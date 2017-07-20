import os
import time

source = ["/Users/lishengmin/Downloads/文稿"]

target_dir = '/Users/lishengmin/Desktop'

today = target_dir + os.sep + time.strftime('%Y%m%d')
#os.sep :   Win'\\'
#           Linux、Unix：’／‘
#           MacOS:':'
now = time.strftime('%H%M%S')

print today + now

if not os.path.exists(today):
    #改变的部分主要是使用 os.exists 函数检验在主备份 目录中是否有以当前日期作为名称的目录。
    os.mkdir(today)
    print('successfully created directory', today)

target = today + os.sep + now + '.zip'
print 'target==' + target

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

if os.system(zip_command) == 0
    print('successful backup to', target)
else:
    print('Backup FILED')

