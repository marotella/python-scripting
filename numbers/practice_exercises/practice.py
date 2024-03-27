hour_rate = 0.51
per_day = 24 * hour_rate
per_year = 365 * per_day
per_month = per_year / 12

print(f'It costs ${per_day} to run a day.')
print(f'It costs ${per_year} to run a year.')
print(f'It costs ${per_month} to run a month.')

multi_per_day = per_day * 20
multi_per_month = per_month * 20

print(f'It costs ${multi_per_day} to run 20 servers a day.')
print(f'It costs ${multi_per_month} to run 20 servers a month.')


days = 918 / per_day

print(f"With 912 dollars you can run the server for {days} days.")