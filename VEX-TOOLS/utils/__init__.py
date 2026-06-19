from .url_shortener import url_shortener
from .short_id import short_id_menu

class UtilsTools:
    @staticmethod
    def url_shortener():
        from .url_shortener import url_shortener as _url_shortener
        _url_shortener()
    
    @staticmethod
    def short_id():
        from .short_id import short_id_menu as _short_id_menu
        _short_id_menu()