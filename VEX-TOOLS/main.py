#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import os
import random
import string
import secrets
import uuid
import hashlib
import requests
import urllib.parse
import socket
import phonenumbers
from phonenumbers import carrier, geocoder, timezone, PhoneNumberType
from core.colors import Colors, LOGO
from core.utils import clear, header, error, info, success, warning
from core.actions import show_actions
from core.config import PHONE_API_KEY, EMAIL_API_URL

# ====== OSINT TOOLS ======
from modules.osint import OsintTools

# ====== INTRO ======
INTRO = """
⠀⠀⠀⢀⡤⢤⢄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⡅⠠⢀⡈⢀⣙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⠀⠀⠀⠈⠙⠿⣝⢇⠀⠀⣀⣠⠤⠤⠤⠤⣤⡤⠚⠁⠀⠀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢧⡀⠀⠀⠠⣄⠈⢺⣺⡍⠀⠀⠀⠀⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⡆⢀⠘⣔⠄⠑⠂⠈⠀⡔⠤⠴⠚⡁⠀⠀⢀⠀⠀⠀⣠⠔⢶⡢⡀⠀⠠⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣇⠀⢃⡀⠁⠀⠀⠀⡸⠃⢀⡴⠊⢀⠀⠀⠈⢂⡤⠚⠁⠀⠀⠙⢿⠀⠉⡇⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠾⣹⢤⢼⡆⠀⠀⠀⠀⠀⠀⠈⢀⠞⠁⠀⢠⣴⠏⠀⠀⠀⠀⠀⠀⠸⡇⠀⢇⠀⠀⠀⠀⠀
⠀⠀⣾⢡⣤⡈⠣⡀⠙⠒⠀⠀⠀⠀⣀⠤⠤⣤⠤⣌⠁⢛⡄⠀⠀⠀⠀⠀⠠⡀⢇⠀⠘⣆⠀⢀⡴⡆
⠀⠀⣿⢻⣿⣿⣄⡸⠀⡆⠀⠒⣈⣩⣉⣉⡈⠉⠉⠢⣉⠉⠀⠀⠀⠀⠀⠀⠀⢣⠈⠢⣀⠈⠉⢁⡴⠃
⠀⢀⢿⣿⣿⡿⠛⠁⠀⢻⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣸⢿⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⡇⠉⠉⠁⠀⠀
⣠⣞⠘⢛⡛⢻⣷⣤⡀⠈⡎⣿⣿⣿⣿⣿⣿⣿⣿⣿⠹⠏⠀⠀⠀⠀⠀⠀⠀⠀⠇⢰⡇⠀⠀⠀⠀⠀
⠻⣌⠯⡁⢠⣸⣿⣿⣷⡄⠁⠈⢻⢿⣿⣿⣿⣿⠿⠋⠃⠰⣀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⠀
⠀⠀⠉⢻⠨⠟⠹⢿⣿⢣⠀⠀⢨⡧⣌⠉⠁⣀⠴⠊⠑⠀⡸⠛⠀⠀⠀⠀⠀⣸⢲⡟⠀⠀⠀⠀⠀⠀
⠀⠀⣠⠏⠀⠀⠀⠉⠉⠁⠀⠐⠁⠀⠀⢉⣉⠁⠀⠀⢀⠔⢷⣄⠀⠀⠀⠀⢠⣻⡞⠀⠀⠀⠀⠀⠀⠀
⠀⢠⠟⡦⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢾⠉⠀⣹⣦⠤⣿⣿⡟⠁⠀⠀⠀⢀⣶⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠙⣦⣁⡎⢈⠏⢱⠚⢲⠔⢲⠲⡖⠖⣦⣿⡟⠀⣿⡿⠁⣠⢔⡤⠷⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⣟⠿⡿⠿⠶⢾⠶⠾⠶⠾⠞⢻⠋⠏⣸⠁⠀⡽⠓⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡏⠳⠷⠴⠣⠜⠢⠜⠓⠛⠊⠀⢀⡴⠣⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣏⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠁⢀⣀⣀⠴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⢀⣀⠴⠖⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠑⠒⠒⠐⠒⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

# ====== CLEAR ======
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ====== LOOKUPS MENU ======
def lookups_menu():
    while True:
        clear_screen()
        print(LOGO)
        header("LOOKUPS")
        print("""
╭ [1] Phone Lookup
│ [2] Gmail Lookup
│ [3] IP Lookup
╰ [0] Back - Osint
""")
        choice = input(f"{Colors.WHITE}> Choose: {Colors.RESET}")
        if choice == "1": OsintTools.phone()
        elif choice == "2": OsintTools.email()
        elif choice == "3": OsintTools.ip()
        elif choice == "0": return
        else: error("Invalid choice!")

# ====== DOX TRACKER MENU ======
def dox_menu():
    while True:
        clear_screen()
        print(LOGO)
        header("DOX TRACKER")
        print("""
╭ [1] Check Username
│ [2] Check Name
│ [3] Mobile Location
╰ [0] Back - Osint
""")
        choice = input(f"{Colors.WHITE}> Choose: {Colors.RESET}")
        if choice == "1": OsintTools.username()
        elif choice == "2": OsintTools.name()
        elif choice == "3": OsintTools.mobile()
        elif choice == "0": return
        else: error("Invalid choice!")

# ====== OSINT MENU ======
def osint_menu():
    while True:
        clear_screen()
        print(LOGO)
        header("OSINT")
        print("""
╭ [1] Lookups
│ [2] Dox Tracker
╰ [0] Back - Main
""")
        choice = input(f"{Colors.WHITE}> Choose: {Colors.RESET}")
        if choice == "1": lookups_menu()
        elif choice == "2": dox_menu()
        elif choice == "0": return
        else: error("Invalid choice!")

# ====== GENERATORS MENU ======
def generators_menu():
    while True:
        clear_screen()
        print(LOGO)
        header("GENERATORS")
        print("""
╭ [1] URL Shortener
│ [2] ID Shorter
╰ [0] Back - Main
""")
        choice = input(f"{Colors.WHITE}> Choose: {Colors.RESET}")
        if choice == "1":
            # URL Shortener direkt hier
            header("URL SHORTENER")
            print("")
            url = input(f"{Colors.WHITE}> Enter URL to shorten: {Colors.RESET}")
            if not url.startswith("http://") and not url.startswith("https://"):
                url = "https://" + url
            encoded_url = urllib.parse.quote(url, safe='')
            info(f"Shortening {url}...")
            try:
                response = requests.get(
                    f"https://is.gd/create.php?format=simple&url={encoded_url}",
                    timeout=10,
                    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                )
                if response.status_code == 200:
                    short_url = response.text.strip()
                    if short_url.startswith("http"):
                        print("")
                        print(f"{Colors.WHITE}{'Original URL:':<20}{url:>80}{Colors.RESET}")
                        print(f"{Colors.WHITE}{'Short URL:':<20}{short_url:>80}{Colors.RESET}")
                        print("")
                        print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
                        print("")
                    else:
                        error(f"Error: {short_url}")
                else:
                    error(f"API error: {response.status_code}")
            except Exception as e:
                error(f"Error: {e}")
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
        elif choice == "2":
            # ID Shorter direkt hier
            header("ID SHORTER")
            print("")
            print("""
╭ [1] Random String
│ [2] Secure String (Hex)
│ [3] UUID
│ [4] Nano ID
│ [5] Token (URL-safe)
│ [6] OTP (Numeric)
│ [7] Hash Generator
│ [8] All in One
╰ [0] Back
""")
            sub_choice = input(f"{Colors.WHITE}> Choose: {Colors.RESET}")
            if sub_choice == "1":
                length = input(f"{Colors.WHITE}> Length (default 8): {Colors.RESET}")
                if not length: length = 8
                else: length = int(length)
                result = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
                print("")
                print(f"{Colors.WHITE}{'Random String:':<20}{result:>80}{Colors.RESET}")
                print("")
            elif sub_choice == "2":
                length = input(f"{Colors.WHITE}> Length (default 8): {Colors.RESET}")
                if not length: length = 8
                else: length = int(length)
                result = secrets.token_hex(length)
                print("")
                print(f"{Colors.WHITE}{'Secure String:':<20}{result:>80}{Colors.RESET}")
                print("")
            elif sub_choice == "3":
                result = str(uuid.uuid4())
                print("")
                print(f"{Colors.WHITE}{'UUID:':<20}{result:>80}{Colors.RESET}")
                print("")
            elif sub_choice == "4":
                length = input(f"{Colors.WHITE}> Length (default 8): {Colors.RESET}")
                if not length: length = 8
                else: length = int(length)
                alphabet = '_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                result = ''.join(random.choice(alphabet) for _ in range(length))
                print("")
                print(f"{Colors.WHITE}{'Nano ID:':<20}{result:>80}{Colors.RESET}")
                print("")
            elif sub_choice == "5":
                length = input(f"{Colors.WHITE}> Length (default 16): {Colors.RESET}")
                if not length: length = 16
                else: length = int(length)
                result = secrets.token_urlsafe(length)
                print("")
                print(f"{Colors.WHITE}{'Token:':<20}{result:>80}{Colors.RESET}")
                print("")
            elif sub_choice == "6":
                length = input(f"{Colors.WHITE}> Length (default 6): {Colors.RESET}")
                if not length: length = 6
                else: length = int(length)
                result = ''.join(random.choice('0123456789') for _ in range(length))
                print("")
                print(f"{Colors.WHITE}{'OTP:':<20}{result:>80}{Colors.RESET}")
                print("")
            elif sub_choice == "7":
                text = input(f"{Colors.WHITE}> Text to hash: {Colors.RESET}")
                print("")
                print(f"{Colors.WHITE}{'MD5:':<20}{hashlib.md5(text.encode()).hexdigest():>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'SHA1:':<20}{hashlib.sha1(text.encode()).hexdigest():>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'SHA256:':<20}{hashlib.sha256(text.encode()).hexdigest():>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'SHA512:':<20}{hashlib.sha512(text.encode()).hexdigest():>80}{Colors.RESET}")
                print("")
            elif sub_choice == "8":
                print("")
                print(f"{Colors.WHITE}{'Random String:':<20}{''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8)):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Secure Hex:':<20}{secrets.token_hex(8):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'UUID:':<20}{str(uuid.uuid4()):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Nano ID:':<20}{''.join(random.choice('_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8)):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Token:':<20}{secrets.token_urlsafe(16):>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'OTP:':<20}{''.join(random.choice('0123456789') for _ in range(6)):>80}{Colors.RESET}")
                print("")
            elif sub_choice == "0":
                return
            else:
                error("Invalid choice!")
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
        elif choice == "0": return
        else: error("Invalid choice!")

# ====== MAIN ======
def main():
    clear_screen()
    print(INTRO)
    time.sleep(2)
    clear_screen()
    
    while True:
        clear_screen()
        print(LOGO)
        print("")
        print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
        print("")
        print("""
╭ [1] OSINT
│ [2] Generators
╰ [0] Exit
""")
        
        choice = input(f"{Colors.WHITE}> Choose: {Colors.RESET}")
        if choice == "1": osint_menu()
        elif choice == "2": generators_menu()
        elif choice == "0":
            print(f"\n{Colors.WHITE}Goodbye!{Colors.RESET}")
            sys.exit(0)
        else:
            error("Invalid choice!")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.WHITE}Interrupted by user.{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        error(f"Error: {e}")
        input("Press Enter...")