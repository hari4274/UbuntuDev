# Phone number validation and basic details

# pip3 install phonenumbers
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
 

msg = ''
res = tz = False
pn = "9659094562"
try:
 x = phonenumbers.parse("+" + pn, None)
 tz = timezone.time_zones_for_number(x)
 if tz:
 	tz = tz[0]
 msg, res = 'SUCCESS', phonenumbers.is_valid_number(x)
except Exception as e:
 msg, res = 'ERROR', e.__str__()

print(pn, msg, res, tz)



def localScan(InputNumber, print_results=True):
    print("Running local scan...")

    # FormattedPhoneNumber = "+" + formatNumber(InputNumber)
    FormattedPhoneNumber = "+" + InputNumber

    try:
        PhoneNumberObject = phonenumbers.parse(FormattedPhoneNumber, None)
    except Exception as e:
        print(e)
    else:
        if not phonenumbers.is_valid_number(PhoneNumberObject):
            return False

        number = phonenumbers.format_number(PhoneNumberObject, phonenumbers.PhoneNumberFormat.E164).replace("+", "")
        numberCountryCode = phonenumbers.format_number(PhoneNumberObject, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split(" ")[0]
        numberCountry = phonenumbers.region_code_for_country_code(int(numberCountryCode))

        localNumber = phonenumbers.format_number(PhoneNumberObject, phonenumbers.PhoneNumberFormat.E164).replace(numberCountryCode, "")
        internationalNumber = phonenumbers.format_number(PhoneNumberObject, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        country = geocoder.country_name_for_number(PhoneNumberObject, "en")
        location = geocoder.description_for_number(PhoneNumberObject, "en")
        carrierName = carrier.name_for_number(PhoneNumberObject, "en")

        if print_results:
            print("International format: {}".format(internationalNumber))
            print("Local format: {}".format(localNumber))
            print("Country found: {} ({})".format(country, numberCountryCode))
            print("City/Area: {}".format(location))
            print("Carrier: {}".format(carrierName))
            for timezoneResult in timezone.time_zones_for_number(PhoneNumberObject):
                print("Timezone: {}".format(timezoneResult))

            if phonenumbers.is_possible_number(PhoneNumberObject):
                print("The number is valid and possible.")
            else:
                print("The number is valid but might not be possible.")

    numberObj = {}
    numberObj["input"] = InputNumber
    numberObj["default"] = number
    numberObj["local"] = localNumber
    numberObj["international"] = internationalNumber
    numberObj["country"] = country
    numberObj["countryCode"] = numberCountryCode
    numberObj["countryIsoCode"] = numberCountry
    numberObj["location"] = location
    numberObj["carrier"] = carrierName

    return numberObj 


ss = localScan(pn)
print(ss)

# Result:

# 919659094562 SUCCESS True Asia/Calcutta
# Running local scan...
# International format: +91 96590 94562
# Local format: 9659094562
# Country found: India (+91)
# City/Area: India
# Carrier: Aircel
# Timezone: Asia/Calcutta
# The number is valid and possible.
# {'input': '919659094562', 'default': '919659094562', 'local': '9659094562', 'international': '+91 96590 94562', 'country': 'India', 'countryCode': '+91', 'countryIsoCode': 'IN', 'location': 'India', 'carrier': 'Aircel'}
