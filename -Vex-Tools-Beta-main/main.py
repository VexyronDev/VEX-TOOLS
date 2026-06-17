#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
from core.colors import Colors, LOGO
from core.utils import clear, header, error
from modules.osint import OsintTools

def osint_menu():
    clear()
    print(LOGO)
    header("OSINT TOOLS")
    print("""
[1] Phone Lookup
[2] Email Lookup
[0] Back
""")
    choice = input(f"{Colors.WHITE}> Choose: {Colors.RESET}")
    if choice == "1": OsintTools.phone()
    elif choice == "2": OsintTools.email()
    elif choice == "0": return
    else: error("Invalid choice!")

def main():
    while True:
        clear()
        print(LOGO)
        print("")
        print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
        print("")
        print("[1] OSINT Tools")
        print("[0] Exit")
        print("")
        
        choice = input(f"{Colors.WHITE}> Choose: {Colors.RESET}")
        if choice == "1": osint_menu()
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