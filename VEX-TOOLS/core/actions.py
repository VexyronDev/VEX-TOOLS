#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import webbrowser
from core.colors import Colors

def open_url(url):
    try:
        webbrowser.open(url)
        return True
    except:
        return False

def show_actions(phone_clean=None, email=None, ip=None, username=None, first_name=None, last_name=None):
    
    # ====== PHONE ACTIONS ======
    if phone_clean:
        print("")
        print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
        print("")
        print(f"{Colors.WHITE}{'Actions:':<15}{'':>85}{Colors.RESET}")
        print("")
        
        print(f"{Colors.WHITE}{'[1] WhatsApp':<20}{f'https://wa.me/{phone_clean}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[2] Telegram':<20}{f'https://t.me/+{phone_clean}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[3] Signal':<20}{f'https://signal.me/#p/+{phone_clean}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[4] Google Phone':<20}{f'https://www.google.com/search?q={phone_clean}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[0] Done':<20}{'Back to Menu':>80}{Colors.RESET}")
        print("")
        
        choice = input(f"{Colors.WHITE}Choice: {Colors.RESET}")
        if choice == "1": open_url(f"https://wa.me/{phone_clean}")
        elif choice == "2": open_url(f"https://t.me/+{phone_clean}")
        elif choice == "3": open_url(f"https://signal.me/#p/+{phone_clean}")
        elif choice == "4": open_url(f"https://www.google.com/search?q={phone_clean}")
    
    # ====== EMAIL ACTIONS ======
    elif email:
        print("")
        print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
        print("")
        print(f"{Colors.WHITE}{'Actions:':<15}{'':>85}{Colors.RESET}")
        print("")
        
        print(f"{Colors.WHITE}{'[1] Google Email':<20}{f'https://www.google.com/search?q={email}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[2] LinkedIn':<20}{f'https://www.linkedin.com/search/results/people/?keywords={email}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[3] Twitter':<20}{f'https://twitter.com/search?q={email}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[4] Facebook':<20}{f'https://www.facebook.com/search/top?q={email}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[0] Done':<20}{'Back to Menu':>80}{Colors.RESET}")
        print("")
        
        choice = input(f"{Colors.WHITE}Choice: {Colors.RESET}")
        if choice == "1": open_url(f"https://www.google.com/search?q={email}")
        elif choice == "2": open_url(f"https://www.linkedin.com/search/results/people/?keywords={email}")
        elif choice == "3": open_url(f"https://twitter.com/search?q={email}")
        elif choice == "4": open_url(f"https://www.facebook.com/search/top?q={email}")
    
    # ====== IP ACTIONS ======
    elif ip:
        print("")
        print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
        print("")
        print(f"{Colors.WHITE}{'Actions:':<15}{'':>85}{Colors.RESET}")
        print("")
        
        print(f"{Colors.WHITE}{'[1] Google IP':<20}{f'https://www.google.com/search?q={ip}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[2] IP Tracker':<20}{f'https://www.iplocation.net/?query={ip}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[3] WhatIsMyIP':<20}{f'https://www.whatismyip.com/ip/{ip}/':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[0] Done':<20}{'Back to Menu':>80}{Colors.RESET}")
        print("")
        
        choice = input(f"{Colors.WHITE}Choice: {Colors.RESET}")
        if choice == "1": open_url(f"https://www.google.com/search?q={ip}")
        elif choice == "2": open_url(f"https://www.iplocation.net/?query={ip}")
        elif choice == "3": open_url(f"https://www.whatismyip.com/ip/{ip}/")
    
    # ====== USERNAME ACTIONS ======
    elif username:
        print("")
        print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
        print("")
        print(f"{Colors.WHITE}{'Actions:':<15}{'':>85}{Colors.RESET}")
        print("")
        
        print(f"{Colors.WHITE}{'[1] Google Search':<20}{f'https://www.google.com/search?q={username}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[2] GitHub':<20}{f'https://github.com/{username}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[3] Twitter':<20}{f'https://twitter.com/{username}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[4] Instagram':<20}{f'https://www.instagram.com/{username}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[5] Facebook':<20}{f'https://www.facebook.com/{username}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[0] Done':<20}{'Back to Menu':>80}{Colors.RESET}")
        print("")
        
        choice = input(f"{Colors.WHITE}Choice: {Colors.RESET}")
        if choice == "1": open_url(f"https://www.google.com/search?q={username}")
        elif choice == "2": open_url(f"https://github.com/{username}")
        elif choice == "3": open_url(f"https://twitter.com/{username}")
        elif choice == "4": open_url(f"https://www.instagram.com/{username}")
        elif choice == "5": open_url(f"https://www.facebook.com/{username}")
    
    # ====== NAME ACTIONS (VORNAME + NACHNAME) ======
    elif first_name and last_name:
        full_name = f"{first_name} {last_name}"
        print("")
        print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
        print("")
        print(f"{Colors.WHITE}{'Actions:':<15}{'':>85}{Colors.RESET}")
        print("")
        
        print(f"{Colors.WHITE}{'[1] Google Search':<20}{f'https://www.google.com/search?q={full_name}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[2] LinkedIn':<20}{f'https://www.linkedin.com/search/results/people/?keywords={full_name}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[3] Facebook':<20}{f'https://www.facebook.com/search/top?q={full_name}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[4] Twitter':<20}{f'https://twitter.com/search?q={full_name}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[5] Instagram':<20}{f'https://www.instagram.com/search/?q={full_name}':>80}{Colors.RESET}")
        print(f"{Colors.WHITE}{'[0] Done':<20}{'Back to Menu':>80}{Colors.RESET}")
        print("")
        
        choice = input(f"{Colors.WHITE}Choice: {Colors.RESET}")
        if choice == "1": open_url(f"https://www.google.com/search?q={full_name}")
        elif choice == "2": open_url(f"https://www.linkedin.com/search/results/people/?keywords={full_name}")
        elif choice == "3": open_url(f"https://www.facebook.com/search/top?q={full_name}")
        elif choice == "4": open_url(f"https://twitter.com/search?q={full_name}")
        elif choice == "5": open_url(f"https://www.instagram.com/search/?q={full_name}")