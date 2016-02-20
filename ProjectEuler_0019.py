from sys import argv

# returns the number of days in month m (1=Jan, 12=Dec)
# during year y (ex: 1776 or 1990)
def numDaysIn(m,y):
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12: return 31
    if m==4 or m==6 or m==9 or m==11: return 30
    if m==2:
        if y%4==0 and (y%100!=0 or y%400==0):
            return 29
        return 28

# generator for the day of the week for the first of the month
# starting at or after the mth month on year y
# Monday=1, Tues=2, Wed=3, Th=4, Fri=5, Sat=6, Sun=0
def getDoWoFoM(m,y):
    w=1
    M,Y = 1,1900
    while True:
        if Y>y or (Y==y and M>=m):
            yield w, M, Y
        w = (w+numDaysIn(M,Y))%7
        if M==12:
            Y+=1
            M=1
        else:
            M+=1
        
# returns the number of sundays that fell on the first
# of the month during the span between the mth month
# of year y and m2th month of the year y2
def getAnswer(m,y,m2,y2):
    cnt=0
    for w,M,Y in getDoWoFoM(m,y):
        if Y>y2 or (Y==y2 and M>m2):
            break
        if w==0:
            cnt += 1
    return cnt

if __name__=="__main__":
    print(getAnswer(int(argv[1]),int(argv[2]),int(argv[3]),int(argv[4])))
