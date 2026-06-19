#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from core.utils import header, info, error, warning
from core.colors import Colors
from core.config import EMAIL_API_URL
from core.actions import show_actions

def email_lookup():
    header("EMAIL LOOKUP")
    print("")
    email = input(f"{Colors.WHITE}> Email Address: {Colors.RESET}")
    info(f"Looking up {email}...")
    
    try:
        response = requests.get(f"{EMAIL_API_URL}?email={email}", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            print("")
            print(f"{Colors.WHITE}{'Email:':<15}{email:>85}{Colors.RESET}")
            
            status = data.get('status', 'unknown')
            if status == 'valid':
                print(f"{Colors.WHITE}{'Status:':<15}{'VALID':>85}{Colors.RESET}")
            elif status == 'invalid':
                print(f"{Colors.WHITE}{'Status:':<15}{'INVALID':>85}{Colors.RESET}")
            else:
                print(f"{Colors.WHITE}{'Status:':<15}{'UNKNOWN':>85}{Colors.RESET}")
            
            domain = data.get('domain', 'Unknown')
            print(f"{Colors.WHITE}{'Domain:':<15}{domain:>85}{Colors.RESET}")
            
            is_disposable = data.get('is_disposable', False)
            if is_disposable:
                print(f"{Colors.WHITE}{'Disposable:':<15}{'YES (Temp Mail)':>85}{Colors.RESET}")
            else:
                print(f"{Colors.WHITE}{'Disposable:':<15}{'NO':>85}{Colors.RESET}")
            
            is_role = data.get('is_role', False)
            if is_role:
                print(f"{Colors.WHITE}{'Role:':<15}{'YES (info@, admin@)':>85}{Colors.RESET}")
            else:
                print(f"{Colors.WHITE}{'Role:':<15}{'NO':>85}{Colors.RESET}")
            
            is_free = data.get('is_free', False)
            if is_free:
                print(f"{Colors.WHITE}{'Provider:':<15}{'Free (Gmail, Yahoo, etc.)':>85}{Colors.RESET}")
            else:
                print(f"{Colors.WHITE}{'Provider:':<15}{'Corporate/Business':>85}{Colors.RESET}")
            
            mx_records = data.get('mx_records', [])
            if mx_records:
                print(f"{Colors.WHITE}{'MX Records:':<15}{', '.join(mx_records[:2]):>85}{Colors.RESET}")
            else:
                print(f"{Colors.WHITE}{'MX Records:':<15}{'None found':>85}{Colors.RESET}")
            
            score = data.get('score', 0)
            print(f"{Colors.WHITE}{'Score:':<15}{f'{score}/100':>85}{Colors.RESET}")
            
            print("")
            print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
            print("")
            
            # ====== ACTIONS ======
            print(f"{Colors.WHITE}{'Actions:':<15}{'':>85}{Colors.RESET}")
            print("")
            print(f"{Colors.WHITE}{'╭ [1] Google Email':<20}{f'https://www.google.com/search?q={email}':>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'│ [2] LinkedIn':<20}{f'https://www.linkedin.com/search/results/people/?keywords={email}':>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'│ [3] Twitter':<20}{f'https://twitter.com/search?q={email}':>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'│ [4] Facebook':<20}{f'https://www.facebook.com/search/top?q={email}':>80}{Colors.RESET}")
            print(f"{Colors.WHITE}{'╰ [0] Done':<20}{'Back to Menu':>80}{Colors.RESET}")
            print("")
            
            choice = input(f"{Colors.WHITE}Choice: {Colors.RESET}")
            if choice == "1": 
                import webbrowser
                webbrowser.open(f"https://www.google.com/search?q={email}")
            elif choice == "2": 
                import webbrowser
                webbrowser.open(f"https://www.linkedin.com/search/results/people/?keywords={email}")
            elif choice == "3": 
                import webbrowser
                webbrowser.open(f"https://twitter.com/search?q={email}")
            elif choice == "4": 
                import webbrowser
                webbrowser.open(f"https://www.facebook.com/search/top?q={email}")
            
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
            
        else:
            error(f"API error: {response.status_code}")
            warning("Try using Hunter.io API instead")
            
    except Exception as e:
        error(f"Error: {e}")
    
    input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")