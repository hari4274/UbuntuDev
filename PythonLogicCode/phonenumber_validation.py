# Phone number validation 

# pip3 install phonenumbers
import phonenumbers
from phonenumbers import timezone

msg = ''
res = tz = False
pn = "+18316859999"
try:
 x = phonenumbers.parse(pn, None)
 tz = timezone.time_zones_for_number(x)
 if tz:
 	tz = tz[0]
 msg, res = 'SUCCESS', phonenumbers.is_valid_number(x)
except Exception as e:
 msg, res = 'ERROR', e.__str__()

print(pn, msg, res, tz)


# +40721234567 SUCCESS True ('Europe/Bucharest',)
