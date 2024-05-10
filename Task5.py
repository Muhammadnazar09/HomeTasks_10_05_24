from datetime import datetime, timedelta
to_day = datetime.now()
for i in range(5+1):
    after = to_day+timedelta(days=i)
    print(after)