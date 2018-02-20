import datetime
from datetime import datetime
mondays = 0
months = range(1,12)
for year in range(2018, 2028):
    for month in months:
        if datetime(year, month, 8).weekday() == 0:
            mondays += 1
print(" Οι Δευτέρες που θα εχουν 8 και θα ειναι και δευτερα ειναι: ")           
print(mondays)
