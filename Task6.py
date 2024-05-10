from datetime import datetime,timedelta
first_time = datetime.strptime(input(),"%d %m %Y")
Second_time = datetime.strptime(input(),"%d %m %Y")
print(first_time-Second_time)