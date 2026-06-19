from .phone import phone_lookup
from .email import email_lookup
from .ip import ip_lookup
from .username import username_lookup
from .name import name_lookup
from .mobile import mobile_location

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
    
    @staticmethod
    def mobile():
        from .mobile import mobile_location as _mobile_location
        _mobile_location()