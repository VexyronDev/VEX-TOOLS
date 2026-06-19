#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import socket
import phonenumbers
from phonenumbers import carrier, geocoder, timezone, PhoneNumberType
from core.utils import header, info, error, warning, success
from core.colors import Colors
from core.actions import show_actions
from core.config import PHONE_API_KEY

def mobile_location():
    header("MOBILE LOCATION")
    print("")
    target = input(f"{Colors.WHITE}> Enter IP or Phone Number: {Colors.RESET}")
    
    is_phone = False
    phone_clean = target.replace("+", "").replace(" ", "").replace("-", "")
    if phone_clean.isdigit() and len(phone_clean) >= 6:
        is_phone = True
    
    if is_phone:
        info(f"Processing phone number: {target}...")
        try:
            number = phonenumbers.parse(target, None)
            if phonenumbers.is_valid_number(number):
                phone_str = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                country = f"{geocoder.description_for_number(number, 'en')} ({number.country_code})"
                carrier_name = carrier.name_for_number(number, "en") or "Unknown"
                
                num_type = phonenumbers.number_type(number)
                if num_type == phonenumbers.PhoneNumberType.MOBILE:
                    line_type = "mobile"
                elif num_type == phonenumbers.PhoneNumberType.FIXED_LINE:
                    line_type = "landline"
                elif num_type == phonenumbers.PhoneNumberType.VOIP:
                    line_type = "voip"
                else:
                    line_type = "other"
                
                print("")
                print(f"{Colors.WHITE}{'Phone:':<20}{phone_str:>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Country:':<20}{country:>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Carrier:':<20}{carrier_name:>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Line Type:':<20}{line_type:>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Google Maps:':<20}{f'https://www.google.com/maps?q={country}':>80}{Colors.RESET}")
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
                return
            else:
                error("Invalid phone number")
                input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
                return
        except phonenumbers.NumberParseException as e:
            error(f"Invalid format: {e}")
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
            return
    
    ip = target
    if not target.replace('.', '').isdigit():
        try:
            ip = socket.gethostbyname(target)
            info(f"Resolved {target} -> {ip}")
        except:
            error("Could not resolve domain")
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
            return
    
    info(f"Looking up location for {ip}...")
    
    try:
        response = requests.get(
            f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,zip,lat,lon,timezone,isp,org,as,query,mobile",
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                is_mobile = data.get('mobile', False)
                print("")
                print(f"{Colors.WHITE}{'Target:':<20}{target:>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Resolved IP:':<20}{data.get('query', ip):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Country:':<20}{data.get('country', 'N/A') + ' (' + data.get('countryCode', 'N/A') + ')':>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Region:':<20}{data.get('regionName', 'N/A'):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'City:':<20}{data.get('city', 'N/A'):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'ZIP:':<20}{data.get('zip', 'N/A'):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Latitude:':<20}{str(data.get('lat', 'N/A')):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Longitude:':<20}{str(data.get('lon', 'N/A')):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Timezone:':<20}{data.get('timezone', 'N/A'):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'ISP:':<20}{data.get('isp', 'N/A'):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'ORG:':<20}{data.get('org', 'N/A'):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'AS:':<20}{data.get('as', 'N/A'):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Mobile:':<20}{str(is_mobile):>80}{Colors.RESET}")
                lat = data.get('lat', '')
                lon = data.get('lon', '')
                if lat and lon:
                    print(f"{Colors.WHITE}{'Google Maps:':<20}{f'https://www.google.com/maps?q={lat},{lon}':>80}{Colors.RESET}")
                print("")
                print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
                print("")
                
                # ====== ACTIONS ======
                print(f"{Colors.WHITE}{'Actions:':<15}{'':>85}{Colors.RESET}")
                print("")
                print(f"{Colors.WHITE}{'╭ [1] Google IP':<20}{f'https://www.google.com/search?q={ip}':>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'│ [2] IP Tracker':<20}{f'https://www.iplocation.net/?query={ip}':>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'│ [3] WhatIsMyIP':<20}{f'https://www.whatismyip.com/ip/{ip}/':>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'╰ [0] Done':<20}{'Back to Menu':>80}{Colors.RESET}")
                print("")
                
                choice = input(f"{Colors.WHITE}Choice: {Colors.RESET}")
                if choice == "1": 
                    import webbrowser
                    webbrowser.open(f"https://www.google.com/search?q={ip}")
                elif choice == "2": 
                    import webbrowser
                    webbrowser.open(f"https://www.iplocation.net/?query={ip}")
                elif choice == "3": 
                    import webbrowser
                    webbrowser.open(f"https://www.whatismyip.com/ip/{ip}/")
                
                input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
                return
    except Exception as e:
        warning(f"ip-api.com failed: {e}")
    
    error("All APIs failed. Please try again later.")
    input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")