import os
import time
ret = 1
while(1):
    print(time.time())
    ret = os.system(u'tasklist | find "NK.exe"')
    print(ret)
    print('-'*50)
    if ret==0:
       print('Netkeeper has been found and killed')  
       os.system('TASKKILL /F /IM NK.exe"')
       ret = 1
       break
    else:
       print('Netkeeper has not been found, and continue to search')   
