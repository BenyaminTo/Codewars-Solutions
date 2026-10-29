def domain_name(url):
    if "://" in url:
        url = url.split("://", 1)[1]
    
    if url.startswith("www."):
        url = url[4:]
    
    result = ""
    for char in url:
        if char == '.' or char == '/':
            break
        result += char
    
    return result
#//////////////////////////////////////////////////////////////////////////////
print(domain_name("https://123.net"))        # 123
print(domain_name("http://www.google.com"))  # google
print(domain_name("www.example.co.uk"))      # example
print(domain_name("http://codewars.com"))    # codewars
print(domain_name("http://google.co.jp"))    # google