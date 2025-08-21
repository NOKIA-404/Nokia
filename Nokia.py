#####apni 
 #coding=utf-8
import os, sys, platform
 
os.system('git pull')
 
try:
    if sys.argv[1]=='update':
        os.system('git pull')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    
        import ssb_enc
    
 
elif bit == '32bit':
    
        import ssb1_enc
 
