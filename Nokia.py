import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
Nokia=platform.architecture()[0]
if Nokia=="32bit":__import__("Nokia32")
elif Nokia=="64bit":__import__("Nokia64")
