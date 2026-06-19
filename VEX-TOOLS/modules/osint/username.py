#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from core.utils import header, info, error, warning, success
from core.colors import Colors
from core.actions import show_actions

def username_lookup():
    header("USERNAME DOX TRACKER")
    print("")
    username = input(f"{Colors.WHITE}> Enter Username: {Colors.RESET}")
    info(f"Searching for {username}...")
    
    # ====== PLATTFORMEN FÜR USERNAME-SUCHE ======
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "GitLab": f"https://gitlab.com/{username}",
        "Bitbucket": f"https://bitbucket.org/{username}",
        "HackerNews": f"https://news.ycombinator.com/user?id={username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Mixcloud": f"https://www.mixcloud.com/{username}",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "AppleMusic": f"https://music.apple.com/profile/{username}",
        "CodePen": f"https://codepen.io/{username}",
        "Replit": f"https://replit.com/@{username}",
        "HackerRank": f"https://www.hackerrank.com/{username}",
        "LeetCode": f"https://leetcode.com/{username}",
        "Dev.to": f"https://dev.to/{username}",
        "VK": f"https://vk.com/{username}",
        "OK": f"https://ok.ru/{username}",
        "Telegram": f"https://t.me/{username}",
        "Discord": f"https://discord.com/users/{username}",
        "Mastodon": f"https://mastodon.social/@{username}",
        "Keybase": f"https://keybase.io/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Behance": f"https://www.behance.net/{username}",
        "Fiverr": f"https://www.fiverr.com/{username}",
        "Upwork": f"https://www.upwork.com/freelancers/~{username}",
        "Freelancer": f"https://www.freelancer.com/u/{username}",
        "AngelList": f"https://angel.co/u/{username}",
        "ProductHunt": f"https://www.producthunt.com/@{username}",
    }
    
    print("")
    print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
    print("")
    print(f"{Colors.WHITE}{'Search Results for: ' + username:^100}{Colors.RESET}")
    print("")
    
    found = 0
    for platform, url in platforms.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"{Colors.WHITE}{'[✓]':<5}{platform + ':':<22}{url:>73}{Colors.RESET}")
                found += 1
            else:
                print(f"{Colors.WHITE}{'[ ]':<5}{platform + ':':<22}{'Not Found':>73}{Colors.RESET}")
        except:
            print(f"{Colors.WHITE}{'[?]':<5}{platform + ':':<22}{'Connection Error':>73}{Colors.RESET}")
    
    print("")
    print(f"{Colors.WHITE}{'Total profiles found: ' + str(found):^100}{Colors.RESET}")
    print("")
    print(f"{Colors.WHITE}{'─' * 100}{Colors.RESET}")
    print("")
    
    # ====== ACTIONS ======
    print(f"{Colors.WHITE}{'Actions:':<15}{'':>85}{Colors.RESET}")
    print("")
    print(f"{Colors.WHITE}{'╭ [1] Google Search':<20}{f'https://www.google.com/search?q={username}':>80}{Colors.RESET}")
    print(f"{Colors.WHITE}{'│ [2] GitHub':<20}{f'https://github.com/{username}':>80}{Colors.RESET}")
    print(f"{Colors.WHITE}{'│ [3] Twitter':<20}{f'https://twitter.com/{username}':>80}{Colors.RESET}")
    print(f"{Colors.WHITE}{'│ [4] Instagram':<20}{f'https://www.instagram.com/{username}':>80}{Colors.RESET}")
    print(f"{Colors.WHITE}{'│ [5] Facebook':<20}{f'https://www.facebook.com/{username}':>80}{Colors.RESET}")
    print(f"{Colors.WHITE}{'╰ [0] Done':<20}{'Back to Menu':>80}{Colors.RESET}")
    print("")
    
    choice = input(f"{Colors.WHITE}Choice: {Colors.RESET}")
    if choice == "1": 
        import webbrowser
        webbrowser.open(f"https://www.google.com/search?q={username}")
    elif choice == "2": 
        import webbrowser
        webbrowser.open(f"https://github.com/{username}")
    elif choice == "3": 
        import webbrowser
        webbrowser.open(f"https://twitter.com/{username}")
    elif choice == "4": 
        import webbrowser
        webbrowser.open(f"https://www.instagram.com/{username}")
    elif choice == "5": 
        import webbrowser
        webbrowser.open(f"https://www.facebook.com/{username}")
    
    input(f"{Colors.DIM}Press Enter to return...{Colors.RESET}")