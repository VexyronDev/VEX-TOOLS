#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import phonenumbers
from phonenumbers import carrier, geocoder, timezone, PhoneNumberType
from core.utils import header, info, error
from core.colors import Colors
from core.actions import show_actions

def phone_lookup():
    header("PHONE LOOKUP")
    print("")
    phone = input(f"{Colors.WHITE}> Phone Number: {Colors.RESET}")
    print("")
    
    try:
        number = phonenumbers.parse(phone, None)
        
        if phonenumbers.is_valid_number(number):
            phone_clean = phone.replace("+", "").replace(" ", "").replace("-", "")
            phone_str = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            country = f"{geocoder.description_for_number(number, 'en')} ({number.country_code})"
            
            carrier_name = carrier.name_for_number(number, "en")
            carrier_str = carrier_name if carrier_name else "Not available"
            
            num_type = phonenumbers.number_type(number)
            if num_type == phonenumbers.PhoneNumberType.MOBILE:
                line_type = "mobile"
            elif num_type == phonenumbers.PhoneNumberType.FIXED_LINE:
                line_type = "landline"
            elif num_type == phonenumbers.PhoneNumberType.VOIP:
                line_type = "voip"
            else:
                line_type = "other"
            
            timezones = timezone.time_zones_for_number(number)
            timezone_str = ', '.join(timezones) if timezones else "Unknown"
            
            national = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL)
            international = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            e164 = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
            
            international_clean = international.replace(" ", "")
            
            print(f"{Colors.WHITE}{'Phone:':<15}{phone_str:>85}{Colors.RESET}")
            print(f"{Colors.WHITE}{'Country:':<15}{country:>85}{Colors.RESET}")
            print(f"{Colors.WHITE}{'Carrier:':<15}{carrier_str:>85}{Colors.RESET}")
            print(f"{Colors.WHITE}{'Line:':<15}{line_type:>85}{Colors.RESET}")
            print(f"{Colors.WHITE}{'Timezone:':<15}{timezone_str:>85}{Colors.RESET}")
            print(f"{Colors.WHITE}{'National:':<15}{national:>85}{Colors.RESET}")
            print(f"{Colors.WHITE}{'International:':<15}{international_clean:>85}{Colors.RESET}")
            print(f"{Colors.WHITE}{'E164:':<15}{e164:>85}{Colors.RESET}")
            
            print("")
            print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
            print("")
            
            # ====== ACTIONS ======
            print(f"{Colors.WHITE}{'Actions:':<15}{'':>85}{Colors.RESET}")
            print("")
            print(f"{Colors.WHITE}{'╭ [1] WhatsApp':<20}{f'https://wa.me/{phone_clean}':>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'│ [2] Telegram':<20}{f'https://t.me/+{phone_clean}':>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'│ [3] Signal':<20}{f'https://signal.me/#p/+{phone_clean}':>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'│ [4] Google Phone':<20}{f'https://www.google.com/search?q={phone_clean}':>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'╰ [0] Done':<20}{'Back to Menu':>80}{Colors.RESET}")
            print("")
            
            choice = input(f"{Colors.WHITE}Choice: {Colors.RESET}")
            if choice == "1": 
                import webbrowser
                webbrowser.open(f"https://wa.me/{phone_clean}")
            elif choice == "2": 
                import webbrowser
                webbrowser.open(f"https://t.me/+{phone_clean}")
            elif choice == "3": 
                import webbrowser
                webbrowser.open(f"https://signal.me/#p/+{phone_clean}")
            elif choice == "4": 
                import webbrowser
                webbrowser.open(f"https://www.google.com/search?q={phone_clean}")
            
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
            
        else:
            error("Invalid phone number")
            
    except phonenumbers.NumberParseException as e:
        error(f"Invalid format: {e}")
    except Exception as e:
        error(f"Error: {e}")
    
    input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")