from datetime import datetime,timedelta
def addYear(date,year):
    return date+timedelta(days=365*year)


first_time = datetime.strptime(input(),"%d %m %Y")
n = int(input())
print(addYear(first_time,n))