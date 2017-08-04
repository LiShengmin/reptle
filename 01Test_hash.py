

from hashlib import md5  
from hashlib import sha1  
from hashlib import sha224  
from hashlib import sha384  
from hashlib import sha512  
import hashlib  
  
#__all__ = ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'new', 'algorithms_guaranteed', 'algorithms_available', 'pbkdf2_hmac')  
#Python计算字符串的hash值  
def hashForString(method,srcbyte):  
    #将字符串和汉字转化成byte类型  
    # srcbyte = srcbyte.encode("gb2312")  
        
    #new(name, data=b'')  
    # testnew = hashlib.new(method,data=srcbyte).hexdigest()  
    # print(testnew)  
      
    if method == 'md5':   
        m = md5()  
        m.update(srcbyte)  
        srcbyte = m.hexdigest()  
    elif method == 'sha1':  
        s = sha1()  
        s.update(srcbyte)  
        srcbyte = s.hexdigest()  
    elif method == 'sha224':  
        s = sha224()  
        s.update(srcbyte)  
        srcbyte = s.hexdigest()  
    elif method == 'sha384':  
        s = sha384()  
        s.update(srcbyte)  
        srcbyte = s.hexdigest()  
    elif method == 'sha512':  
        s = sha512()  
        s.update(srcbyte)  
        srcbyte = s.hexdigest()  
    return srcbyte  
   
if __name__ == "__main__":
    print (hashForString("md5","屏幕快照 2017-08-01 下午11.49.01"))