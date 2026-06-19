import os
import platform

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header(text: str):
    from .colors import Colors
    print(f"\n{Colors.WHITE}{'─' * 100}{Colors.RESET}")
    print(f"{Colors.WHITE}{text:^100}{Colors.RESET}")
    print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")

def error(text: str):
    from .colors import Colors
    print(f"{Colors.WHITE}[ERROR] {text}{Colors.RESET}")

def info(text: str):
    from .colors import Colors
    print(f"{Colors.WHITE}[INFO] {text}{Colors.RESET}")

def success(text: str):
    from .colors import Colors
    print(f"{Colors.WHITE}[SUCCESS] {text}{Colors.RESET}")

def warning(text: str):
    from .colors import Colors
    print(f"{Colors.WHITE}[WARNING] {text}{Colors.RESET}")