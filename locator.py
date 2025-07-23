import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import time

def start_phone_tracer(target):
    print(f"[+] PhoneTracer v1.0 - OSINT")
    print(f"[*] Target: {target}")
    print(f"[*] Initiating trace...")
    time.sleep(1)

    try:
        p = phonenumbers.parse(target, None)

        # Validity checks
        is_valid = phonenumbers.is_valid_number(p)
        is_possible = phonenumbers.is_possible_number(p)

        # Location
        location = geocoder.description_for_number(p, "en")

        # Carrier
        sim_carrier = carrier.name_for_number(p, "en")
        timezones = timezone.time_zones_for_number(p)
        # r = geocoder.description_for_number(p, "en")

        print(f"[+] Valid NUmber: {is_valid}")
        print(f"[+] Possible Number: {is_possible}")
        print(f"[+] Location: {location}")
        print(f"[+] Carrier: {sim_carrier}")
        print(f"[+] Timezone(s): {', '.join(timezones)}")
        print(f"[✓] Trace complete")
    except phonenumbers.NumberParseException as e:
        print(f"[!] Error: {e}")

phone_number = str(input("Enter your phone number here: \n"))

start_phone_tracer(phone_number)
