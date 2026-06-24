import time
import os

ascii_art = r"""
     .-:                                   ...  
    -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+.
    =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=
    +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:
   .***#######%@@@@%#%#%#%@###%##%*%%#########+.
      .=+##############%###**##*++=*****+-++++-.
       .=*#########*#@@@     -#.                
       .########%%**.=%@#:   .*.                
       =+####%#@@@*%#: .+*. .+#.                
      -+*##%%##%#+- ..----:::::.                
     :+*#%###%##++                              
    :+*#%%%%%##*+                               
   -+##%%%#%%%#+.                               
  -+#%%%%%%%%#+-                                
 :+*%%%%%%%%#+=                                 
 -+#%%%%%%%%*+.                                 
 -+#########*+                                  
 :-#%%%%%%%%*-                                  
   loadin...              
"""

# Violet ANSI
print("\033[95m" + ascii_art + "\033[0m")

time.sleep(4)

os.system("cls" if os.name == "nt" else "clear")
print("Tool lancé.")
import os
import socket
import requests
import dns.resolver
import ssl
import time
import webbrowser

# ---------------- COLOR SYSTEM ----------------
current_color = "5"

def apply_color():
    os.system(f"color {current_color}")

# ---------------- ASCII ----------------
ASCII = r"""
             :::::::::  :::::::::  ::::::::::: :::    :::      ::::::::::: ::::::::   ::::::::  :::        :::::::: 
            :+:    :+: :+:    :+:     :+:     :+:    :+:          :+:    :+:    :+: :+:    :+: :+:       :+:    :+: 
           +:+    +:+ +:+    +:+     +:+      +:+  +:+           +:+    +:+    +:+ +:+    +:+ +:+       +:+         
          +#++:++#+  +#++:++#:      +#+       +#++:+            +#+    +#+    +:+ +#+    +:+ +#+       +#++:++#++   
         +#+    +#+ +#+    +#+     +#+      +#+  +#+           +#+    +#+    +#+ +#+    +#+ +#+              +#+    
        #+#    #+# #+#    #+#     #+#     #+#    #+#          #+#    #+#    #+# #+#    #+# #+#       #+#    #+#     
       #########  ###    ### ########### ###    ###          ###     ########   ########  ########## ########              
"""

def clean(x):
    return x if x else "N/A"

# ---------------- IP INFO ----------------
def ip_info():
    ip = input("IP > ")

    try:
        r = requests.get(f"https://ipwho.is/{ip}", timeout=5).json()

        print("\n=== IP INFO ===")
        print("IP      :", clean(r.get("ip")))
        print("Country :", clean(r.get("country")))
        print("City    :", clean(r.get("city")))
        print("ISP     :", clean(r.get("connection", {}).get("isp")))
        print("ASN     :", clean(r.get("connection", {}).get("asn")))

    except:
        print("API error")

# ---------------- DNS ----------------
def dns_lookup():
    d = input("Domain > ")

    for t in ["A", "MX", "TXT", "NS"]:
        try:
            print(f"\n[{t}]")
            for r in dns.resolver.resolve(d, t):
                print(r.to_text())
        except:
            pass

# ---------------- DOMAIN -> IP ----------------
def domain_to_ip():
    d = input("Domain > ")

    try:
        print(socket.gethostbyname(d))
    except:
        print("Error")

# ---------------- WEBSITE CHECK ----------------
def website_check():
    url = input("URL > ")

    try:
        r = requests.get(url, timeout=10)

        print("\nStatus:", r.status_code)
        print("Server:", r.headers.get("Server"))

    except:
        print("Error")

# ---------------- HEADERS ----------------
def headers():
    url = input("URL > ")

    try:
        r = requests.get(url, timeout=10)

        print("\n=== HEADERS ===")
        for k, v in r.headers.items():
            print(k, ":", v)

    except:
        print("Error")

# ---------------- SPEED TEST ----------------
def speed_test():
    url = input("URL > ")

    try:
        start = time.time()
        requests.get(url, timeout=10)
        end = time.time()

        print("Response time:", round(end - start, 2), "sec")

    except:
        print("Error")

# ---------------- SSL CHECK ----------------
def ssl_check():
    host = input("Domain > ")

    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
            s.connect((host, 443))
            cert = s.getpeercert()

        print("\n=== SSL ===")
        print("Issuer :", cert.get("issuer"))
        print("Expire :", cert.get("notAfter"))

    except:
        print("SSL error")

# ---------------- REVERSE DNS ----------------
def reverse_dns():
    ip = input("IP > ")

    try:
        print(socket.gethostbyaddr(ip)[0])
    except:
        print("Error")

# ---------------- USERNAME TRACKER ----------------
def username_tracker():
    username = input("Username > ")

    sites = {
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Twitter/X": f"https://twitter.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
    }

    print("\n=== USERNAME TRACKER ===\n")

    headers = {"User-Agent": "Mozilla/5.0"}

    for site, url in sites.items():
        try:
            r = requests.get(url, headers=headers, timeout=5)

            if r.status_code == 200:
                print(f"[+] FOUND -> {site}")
                print(f"    {url}")
            else:
                print(f"[-] NOT FOUND -> {site}")

        except:
            print(f"[!] ERROR -> {site}")

# ---------------- VIRUSTOTAL ----------------
def virustotal():
    query = input("IP / Domain / URL / Hash > ")
    webbrowser.open(f"https://www.virustotal.com/gui/search/{query}")

# ---------------- WEBSITE SCANNER ----------------
def website_scanner():
    url = input("URL > ")

    try:
        r = requests.get(url, timeout=10)

        print("\n=== WEBSITE SCAN ===")
        print("Status Code:", r.status_code)
        print("Server:", r.headers.get("Server"))
        print("Content-Type:", r.headers.get("Content-Type"))
        print("Length:", len(r.text))

        headers_check = [
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Referrer-Policy"
        ]

        print("\n=== SECURITY HEADERS ===")

        for h in headers_check:
            if r.headers.get(h):
                print(f"[+] {h}")
            else:
                print(f"[-] {h} MISSING")

    except:
        print("Scan error")

# ---------------- SETTINGS ----------------
def settings():
    global current_color

    print("""
=== SETTINGS - COLORS ===

[0] Black
[1] Dark Blue
[2] Dark Green
[3] Dark Cyan
[4] Dark Red
[5] Purple
[6] Dark Yellow
[7] Gray
[8] Dark Gray
[9] Blue
[A] Green
[B] Cyan
[C] Red
[D] Pink
[E] Yellow
[F] White
""")

    c = input("Choose color > ").upper()

    colors = {
        "0": "0","1": "1","2": "2","3": "3",
        "4": "4","5": "5","6": "6","7": "7",
        "8": "8","9": "9","A": "A","B": "B",
        "C": "C","D": "D","E": "E","F": "F"
    }

    if c in colors:
        current_color = colors[c]
        apply_color()
        print("Color updated!")
    else:
        print("Invalid choice")

# ---------------- INFO ----------------
def info():
    print("""
=================================
        TOOL INFORMATION
=================================

Creator        : Brix
Tool Type      : Multi-Tools Platform
Language       : English (EN)
Coding         : Python 3
Supported OS   : Windows 10 / 11 / Linux

=================================
""")

# ---------------- MENU ----------------
while True:
    apply_color()
    os.system("cls")

    print(ASCII)

    print("""
[1] IP Info
[2] DNS Lookup
[3] Domain -> IP
[4] Website Check
[5] HTTP Headers
[6] Speed Test
[7] SSL Check
[8] Reverse DNS
[9] Username Tracker
[10] VirusTotal
[11] Website Scanner
[12] Settings (Colors)
[13] Tool Info
[0] Exit
""")

    c = input("> ")

    if c == "1":
        ip_info()
    elif c == "2":
        dns_lookup()
    elif c == "3":
        domain_to_ip()
    elif c == "4":
        website_check()
    elif c == "5":
        headers()
    elif c == "6":
        speed_test()
    elif c == "7":
        ssl_check()
    elif c == "8":
        reverse_dns()
    elif c == "9":
        username_tracker()
    elif c == "10":
        virustotal()
    elif c == "11":
        website_scanner()
    elif c == "12":
        settings()
    elif c == "13":
        info()
    elif c == "0":
        break

    input("\nENTER...")