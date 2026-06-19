#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import socket
import re
from core.utils import header, info, error, warning
from core.colors import Colors
from core.actions import show_actions

def is_private_ip(ip):
    private_ranges = [
        '10.0.0.0/8',
        '172.16.0.0/12',
        '192.168.0.0/16',
        '127.0.0.0/8',
    ]
    import ipaddress
    try:
        ip_obj = ipaddress.ip_address(ip)
        for private_range in private_ranges:
            if ip_obj in ipaddress.ip_network(private_range):
                return True
        return False
    except:
        return False

def ip_lookup():
    header("IP LOOKUP")
    print("")
    target = input(f"{Colors.WHITE}> IP/Domain: {Colors.RESET}")
    
    ip = target
    domain = ""
    if not target.replace('.', '').isdigit():
        try:
            ip = socket.gethostbyname(target)
            domain = target
            info(f"Resolved {target} -> {ip}")
        except:
            error("Could not resolve domain")
            input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
            return
    
    info(f"Looking up {ip}...")
    
    if is_private_ip(ip):
        print("")
        print(f"{Colors.WHITE}{'IP/Domain:':<22}{target:>78}{Colors.RESET}")
        if domain:
            print(f"{Colors.WHITE}{'Domain:':<22}{domain:>78}{Colors.RESET}")
        print(f"{Colors.WHITE}{'Resolved IP:':<22}{ip:>78}{Colors.RESET}")
        print("")
        print(f"{Colors.WHITE}{'TYPE:':<22}{'LOCAL / PRIVATE IP':>78}{Colors.RESET}")
        print(f"{Colors.WHITE}{'STATUS:':<22}{'No public data available':>78}{Colors.RESET}")
        print("")
        print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
        print("")
        input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
        return
    
    net_name = ""
    cidr = ""
    abuse_email = ""
    reverse_dns = ""
    asn_name = ""
    org_name = ""
    
    try:
        whois_response = requests.get(f"https://api.hackertarget.com/whois/?q={ip}", timeout=10)
        if whois_response.status_code == 200:
            whois_text = whois_response.text
            netname_match = re.search(r'netname:\s*(.+)', whois_text, re.IGNORECASE)
            if netname_match:
                net_name = netname_match.group(1).strip()
            cidr_match = re.search(r'inetnum:\s*([\d.]+)\s*-\s*([\d.]+)', whois_text, re.IGNORECASE)
            if cidr_match:
                cidr = f"{cidr_match.group(1)} - {cidr_match.group(2)}"
            abuse_match = re.search(r'abuse-mailbox:\s*(\S+@\S+)', whois_text, re.IGNORECASE)
            if abuse_match:
                abuse_email = abuse_match.group(1)
            org_match = re.search(r'org-name:\s*(.+)', whois_text, re.IGNORECASE)
            if org_match:
                org_name = org_match.group(1).strip()
        
        try:
            reverse_dns = socket.gethostbyaddr(ip)[0]
        except:
            pass
        
        try:
            asn_response = requests.get(f"https://api.hackertarget.com/aslookup/?q={ip}", timeout=10)
            if asn_response.status_code == 200:
                asn_text = asn_response.text
                asn_match = re.search(r'AS\d+\s+(.+)', asn_text)
                if asn_match:
                    asn_name = asn_match.group(1).strip()
        except:
            pass
            
    except:
        pass
    
    try:
        response = requests.get(
            f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query,mobile,proxy,hosting",
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('status') == 'success':
                print("")
                print(f"{Colors.WHITE}{'IP/Domain:':<22}{target:>78}{Colors.RESET}")
                if domain:
                    print(f"{Colors.WHITE}{'Domain:':<22}{domain:>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Resolved IP:':<22}{data.get('query', ip):>78}{Colors.RESET}")
                
                if reverse_dns:
                    print(f"{Colors.WHITE}{'Reverse DNS:':<22}{reverse_dns:>78}{Colors.RESET}")
                
                print("")
                print(f"{Colors.WHITE}{'Country:':<22}{data.get('country', 'N/A') + ' (' + data.get('countryCode', 'N/A') + ')':>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Region:':<22}{data.get('regionName', 'N/A'):>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'City:':<22}{data.get('city', 'N/A'):>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'ZIP/Postal:':<22}{data.get('zip', 'N/A'):>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Latitude:':<22}{str(data.get('lat', 'N/A')):>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Longitude:':<22}{str(data.get('lon', 'N/A')):>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Timezone:':<22}{data.get('timezone', 'N/A'):>78}{Colors.RESET}")
                
                print("")
                print(f"{Colors.WHITE}{'ISP:':<22}{data.get('isp', 'N/A'):>78}{Colors.RESET}")
                if org_name:
                    print(f"{Colors.WHITE}{'Org Name:':<22}{org_name:>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'ORG:':<22}{data.get('org', 'N/A'):>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'ASN:':<22}{data.get('as', 'N/A'):>78}{Colors.RESET}")
                if asn_name:
                    print(f"{Colors.WHITE}{'ASN Name:':<22}{asn_name:>78}{Colors.RESET}")
                
                if net_name:
                    print(f"{Colors.WHITE}{'NET Name:':<22}{net_name:>78}{Colors.RESET}")
                if cidr:
                    print(f"{Colors.WHITE}{'Net Range:':<22}{cidr:>78}{Colors.RESET}")
                if abuse_email:
                    print(f"{Colors.WHITE}{'Abuse Email:':<22}{abuse_email:>78}{Colors.RESET}")
                
                print("")
                print(f"{Colors.WHITE}{'Mobile:':<22}{str(data.get('mobile', False)):>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Proxy:':<22}{str(data.get('proxy', False)):>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Hosting:':<22}{str(data.get('hosting', False)):>78}{Colors.RESET}")
                
                print("")
                print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
                print("")
                
                # ====== ACTIONS ======
                print(f"{Colors.WHITE}{'Actions:':<15}{'':>85}{Colors.RESET}")
                print("")
                print(f"{Colors.WHITE}{'╭ [1] Google IP':<20}{f'https://www.google.com/search?q={ip}':>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'│ [2] IP Tracker':<20}{f'https://www.iplocation.net/?query={ip}':>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'│ [3] WhatIsMyIP':<20}{f'https://www.whatismyip.com/ip/{ip}/':>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'╰ [0] Done':<20}{'Back to Menu':>80}{Colors.RESET}")
                print("")
                
                choice = input(f"{Colors.WHITE}Choice: {Colors.RESET}")
                if choice == "1": 
                    import webbrowser
                    webbrowser.open(f"https://www.google.com/search?q={ip}")
                elif choice == "2": 
                    import webbrowser
                    webbrowser.open(f"https://www.iplocation.net/?query={ip}")
                elif choice == "3": 
                    import webbrowser
                    webbrowser.open(f"https://www.whatismyip.com/ip/{ip}/")
                
                input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
                return
            else:
                warning(f"ip-api.com error: {data.get('message', 'Unknown error')}")
    except Exception as e:
        warning(f"ip-api.com failed: {e}")
    
    try:
        info("Trying fallback API...")
        response = requests.get(f"https://ipwhois.io/json/{ip}", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('success') != False:
                print("")
                print(f"{Colors.WHITE}{'IP/Domain:':<22}{target:>78}{Colors.RESET}")
                if domain:
                    print(f"{Colors.WHITE}{'Domain:':<22}{domain:>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Resolved IP:':<22}{data.get('ip', ip):>78}{Colors.RESET}")
                
                if reverse_dns:
                    print(f"{Colors.WHITE}{'Reverse DNS:':<22}{reverse_dns:>78}{Colors.RESET}")
                
                print("")
                print(f"{Colors.WHITE}{'Country:':<22}{data.get('country', 'N/A') + ' (' + data.get('country_code', 'N/A') + ')':>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Region:':<22}{data.get('region', 'N/A'):>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'City:':<22}{data.get('city', 'N/A'):>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'ZIP/Postal:':<22}{data.get('postal', 'N/A'):>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Latitude:':<22}{str(data.get('latitude', 'N/A')):>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Longitude:':<22}{str(data.get('longitude', 'N/A')):>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'Timezone:':<22}{data.get('timezone', 'N/A'):>78}{Colors.RESET}")
                
                print("")
                print(f"{Colors.WHITE}{'ISP:':<22}{data.get('isp', 'N/A'):>78}{Colors.RESET}")
                if org_name:
                    print(f"{Colors.WHITE}{'Org Name:':<22}{org_name:>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'ORG:':<22}{data.get('org', 'N/A'):>78}{Colors.RESET}")
                print(f"{Colors.WHITE}{'ASN:':<22}{data.get('as', 'N/A'):>78}{Colors.RESET}")
                
                print(f"{Colors.WHITE}{'Mobile:':<22}{str(data.get('type', '') == 'mobile'):>78}{Colors.RESET}")
                
                print("")
                print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
                print("")
                
                # ====== ACTIONS ======
                print(f"{Colors.WHITE}{'Actions:':<15}{'':>85}{Colors.RESET}")
                print("")
                print(f"{Colors.WHITE}{'╭ [1] Google IP':<20}{f'https://www.google.com/search?q={ip}':>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'│ [2] IP Tracker':<20}{f'https://www.iplocation.net/?query={ip}':>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'│ [3] WhatIsMyIP':<20}{f'https://www.whatismyip.com/ip/{ip}/':>80}{Colors.RESET}")
                print(f"{Colors.WHITE}{'╰ [0] Done':<20}{'Back to Menu':>80}{Colors.RESET}")
                print("")
                
                choice = input(f"{Colors.WHITE}Choice: {Colors.RESET}")
                if choice == "1": 
                    import webbrowser
                    webbrowser.open(f"https://www.google.com/search?q={ip}")
                elif choice == "2": 
                    import webbrowser
                    webbrowser.open(f"https://www.iplocation.net/?query={ip}")
                elif choice == "3": 
                    import webbrowser
                    webbrowser.open(f"https://www.whatismyip.com/ip/{ip}/")
                
                input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")
                return
    except Exception as e:
        warning(f"ipwhois.io failed: {e}")
    
    error("All APIs failed. Please try again later.")
    input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")