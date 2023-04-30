import whois # pip install python-whois

def is_registered(domain_name):
    """
    A function that returns a boolean indicating 
    whether a `domain_name` is registered
    """
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)
    

#  اسم دامنه مورد نظر را بین دو کوتیشن در لیست زیر قرار دهید و برنامه را اجرا کنید 
domains = [
    "bing.com",
    "google.com",
    "aaaa.ir",
    "",
    ""
]
# برسی دامین ها 
for domain in domains:
    print(domain, "is registered" if is_registered(domain) else "is not registered")