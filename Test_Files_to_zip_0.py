import os
import time

source = ["/Users/lishengmin/Downloads/文稿"]

# spaces in it

target_dir = '/Users/lishengmin/Desktop'

# using

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'Successful backup to' + target
else:
    print 'backup FAILED'
