recovers, new_cases, active_cases = int(input()),int(input()),int(input())
days = 0
while active_cases > 0:
    days += 1
    active_cases = active_cases-recovers+new_cases
print(days)