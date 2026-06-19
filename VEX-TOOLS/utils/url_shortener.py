#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import urllib.parse
from core.utils import header, info, error, warning
from core.colors import Colors

def url_shortener():
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