#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string
import secrets
import uuid
import hashlib
from core.utils import header, info, error
from core.colors import Colors, LOGO

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_random_string(length=8, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))

def generate_secure_string(length=8):
    return secrets.token_hex(length)

def generate_uuid():
    return str(uuid.uuid4())

def generate_nano_id(length=8):
    alphabet = '_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(alphabet) for _ in range(length))

def generate_token(length=16):
    return secrets.token_urlsafe(length)

def generate_otp(length=6):
    return ''.join(random.choice('0123456789') for _ in range(length))

def generate_hash(text, algo='sha256'):
    if algo == 'md5':
        return hashlib.md5(text.encode()).hexdigest()
    elif algo == 'sha1':
        return hashlib.sha1(text.encode()).hexdigest()
    elif algo == 'sha256':
        return hashlib.sha256(text.encode()).hexdigest()
    elif algo == 'sha512':
        return hashlib.sha512(text.encode()).hexdigest()
    return None

def short_id_menu():
    while True:
        clear()
        print(LOGO)
        header("SHORT ID GENERATOR")
        print("""
[1] Random String
[2] Secure String (Hex)
[3] UUID (Universally Unique)
[4] Nano ID
[5] Token (URL-safe)
[6] OTP (Numeric)
[7] Hash Generator
[8] All in One
[0] Back
""")
        choice = input(f"{Colors.WHITE}> Choose: {Colors.RESET}")
        if choice == "1": 
            header("RANDOM STRING")
            length = input(f"{Colors.WHITE}> Length (default 8): {Colors.RESET}")
            if not length:
                length = 8
            else:
                length = int(length)
            result = generate_random_string(length)
            print("")
            print(f"{Colors.WHITE}{'Random String:':<20}{result:>80}{Colors.RESET}")
            print("")
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
        elif choice == "2": 
            header("SECURE STRING (HEX)")
            length = input(f"{Colors.WHITE}> Length in bytes (default 8): {Colors.RESET}")
            if not length:
                length = 8
            else:
                length = int(length)
            result = generate_secure_string(length)
            print("")
            print(f"{Colors.WHITE}{'Secure String:':<20}{result:>80}{Colors.RESET}")
            print("")
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
        elif choice == "3": 
            header("UUID GENERATOR")
            result = generate_uuid()
            print("")
            print(f"{Colors.WHITE}{'UUID:':<20}{result:>80}{Colors.RESET}")
            print("")
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
        elif choice == "4": 
            header("NANO ID")
            length = input(f"{Colors.WHITE}> Length (default 8): {Colors.RESET}")
            if not length:
                length = 8
            else:
                length = int(length)
            result = generate_nano_id(length)
            print("")
            print(f"{Colors.WHITE}{'Nano ID:':<20}{result:>80}{Colors.RESET}")
            print("")
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
        elif choice == "5": 
            header("TOKEN GENERATOR (URL-SAFE)")
            length = input(f"{Colors.WHITE}> Length in bytes (default 16): {Colors.RESET}")
            if not length:
                length = 16
            else:
                length = int(length)
            result = generate_token(length)
            print("")
            print(f"{Colors.WHITE}{'Token:':<20}{result:>80}{Colors.RESET}")
            print("")
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
        elif choice == "6": 
            header("OTP GENERATOR (NUMERIC)")
            length = input(f"{Colors.WHITE}> Length (default 6): {Colors.RESET}")
            if not length:
                length = 6
            else:
                length = int(length)
            result = generate_otp(length)
            print("")
            print(f"{Colors.WHITE}{'OTP:':<20}{result:>80}{Colors.RESET}")
            print("")
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
        elif choice == "7": 
            header("HASH GENERATOR")
            text = input(f"{Colors.WHITE}> Text to hash: {Colors.RESET}")
            print("")
            print(f"{Colors.WHITE}{'MD5:':<20}{generate_hash(text, 'md5'):>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'SHA1:':<20}{generate_hash(text, 'sha1'):>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'SHA256:':<20}{generate_hash(text, 'sha256'):>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'SHA512:':<20}{generate_hash(text, 'sha512'):>80}{Colors.RESET}")
            print("")
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
        elif choice == "8": 
            header("ALL IN ONE")
            print("")
            print(f"{Colors.WHITE}{'Random String:':<20}{generate_random_string(8):>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'Secure Hex:':<20}{generate_secure_string(8):>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'UUID:':<20}{generate_uuid():>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'Nano ID:':<20}{generate_nano_id(8):>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'Token:':<20}{generate_token(16):>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'OTP:':<20}{generate_otp(6):>80}{Colors.RESET}")
            print("")
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
        elif choice == "0": 
            return
        else: 
            error("Invalid choice!")