from datetime import date
import holidays
  
# Select country
CA_holidays = holidays.Canada()
  
# Print all the holidays in canada in year 2018
for ptr in holidays.Canada(years = 2018).items():
    print(ptr)
    
