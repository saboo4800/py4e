monthly_pay=input('how much do you make in a month?')
weekly_hours=input('how many hours do you work in a week?')
hourly_rate=int(monthly_pay)/(int(weekly_hours)*4)
print('your hourly rate is',hourly_rate)
