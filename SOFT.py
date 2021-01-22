import os
a = input("enter software name")
if a == "GOM":
    c = os.system('cd / && cd /Program Files (x86)/GRETECH/GOMPlayer/ && GOM.exe')
if a == "firefox":
    d = os.system(' cd / && cd /Program Files/Mozilla Firefox && firefox.exe')
else:
    print("error")