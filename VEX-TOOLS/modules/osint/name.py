#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core.utils import header, info, error
from core.colors import Colors
from core.actions import show_actions

def name_lookup():
    header("NAME DOX TRACKER")
    print("")
    first_name = input(f"{Colors.WHITE}> First Name: {Colors.RESET}")
    last_name = input(f"{Colors.WHITE}> Last Name: {Colors.RESET}")
    
    if not first_name or not last_name:
        error("Both first and last name are required!")
        input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
        return
    
    info(f"Searching for {first_name} {last_name}...")
    
    max_width = 85
    
    print("")
    print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
    print("")
    print(f"{Colors.WHITE}{'Name:':<15}{first_name + ' ' + last_name:>{max_width}}{Colors.RESET}")
    print(f"{Colors.WHITE}{'First Name:':<15}{first_name:>{max_width}}{Colors.RESET}")
    print(f"{Colors.WHITE}{'Last Name:':<15}{last_name:>{max_width}}{Colors.RESET}")
    print("")
    print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
    print("")
    
    # ====== ACTIONS ======
    print(f"{Colors.WHITE}{'Actions:':<15}{'':>85}{Colors.RESET}")
    print("")
    
    full_name = f"{first_name} {last_name}"
    print("")
    print(f"{Colors.WHITE}{'╭ [1] Google Search':<20}{f'https://www.google.com/search?q={full_name}':>80}{Colors.RESET}")
    print(f"{Colors.WHITE}{'│ [2] LinkedIn':<20}{f'https://www.linkedin.com/search/results/people/?keywords={full_name}':>80}{Colors.RESET}")
    print(f"{Colors.WHITE}{'│ [3] Facebook':<20}{f'https://www.facebook.com/search/top?q={full_name}':>80}{Colors.RESET}")
    print(f"{Colors.WHITE}{'│ [4] Twitter':<20}{f'https://twitter.com/search?q={full_name}':>80}{Colors.RESET}")
    print(f"{Colors.WHITE}{'│ [5] Instagram':<20}{f'https://www.instagram.com/search/?q={full_name}':>80}{Colors.RESET}")
    print(f"{Colors.WHITE}{'╰ [0] Done':<20}{'Back to Menu':>80}{Colors.RESET}")
    print("")
    
    choice = input(f"{Colors.WHITE}Choice: {Colors.RESET}")
    if choice == "1": 
        import webbrowser
        webbrowser.open(f"https://www.google.com/search?q={full_name}")
    elif choice == "2": 
        import webbrowser
        webbrowser.open(f"https://www.linkedin.com/search/results/people/?keywords={full_name}")
    elif choice == "3": 
        import webbrowser
        webbrowser.open(f"https://www.facebook.com/search/top?q={full_name}")
    elif choice == "4": 
        import webbrowser
        webbrowser.open(f"https://twitter.com/search?q={full_name}")
    elif choice == "5": 
        import webbrowser
        webbrowser.open(f"https://www.instagram.com/search/?q={full_name}")
    
    input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")