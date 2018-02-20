import datetime


days=["ΔΕΥΤΕΡΑ","ΤΡΙΤΗ","ΤΕΤΑΡΤΗ","ΠΕΜΠΤΗ","ΠΑΡΑΣΚΕΥΗ","ΣΑΒΒΑΤΟ","ΚΥΡΙΑΚΗ"]
y = int(input("ΔΩΣΕ ΧΡΟΝΟ: "))
m = int(input("ΔΩΣΕ ΜΗΝΑ: "))
if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    x=31
elif m==2:
    if y%4==0:
        x=29
    else:
        x=28
else:
    x=30

for i in range(1,x+1):
    a=datetime.date(y,m,i)

    b=(a.weekday())


    print (a)
    print (days[a.weekday()])
