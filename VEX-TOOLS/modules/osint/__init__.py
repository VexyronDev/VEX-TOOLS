from .phone import phone_lookup
from .email import email_lookup
from .ip import ip_lookup
from .username import username_lookup
from .name import name_lookup

class OsintTools:
    @staticmethod
    def phone():
        from .phone import phone_lookup as _phone_lookup
        _phone_lookup()
    
    @staticmethod
    def email():
        from .email import email_lookup as _email_lookup
        _email_lookup()
    
    @staticmethod
    def ip():
        from .ip import ip_lookup as _ip_lookup
        _ip_lookup()
    
    @staticmethod
    def username():
        from .username import username_lookup as _username_lookup
        _username_lookup()
    
    @staticmethod
    def name():
        from .name import name_lookup as _name_lookup
        _name_lookup()

def osint_menu():
    from core.utils import clear, header, error
    from core.colors import Colors, LOGO
    clear()
    print(LOGO)
    header("OSINT TOOLS")
    print("""
[1] Phone Lookup
[2] Email Lookup
[3] IP Lookup
[0] Back
""")
    choice = input(f"{Colors.WHITE}> Choose: {Colors.RESET}")
    if choice == "1": OsintTools.phone()
    elif choice == "2": OsintTools.email()
    elif choice == "3": OsintTools.ip()
    elif choice == "0": return
    else: error("Invalid choice!")