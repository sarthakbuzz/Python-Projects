import phonenumbers
from phonenumbers import timezone,geocoder,carrier
#geocoder:to know the specific location to that phonenumber
#indian phonenumber example:+91******
#this will print the country name
#carrier:to know the name of service provider of that phone number
#timezone:timezone is defined as a geographical area or region throughout whice standard time is observed.
number=input("enter the phone number with +91--")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)
