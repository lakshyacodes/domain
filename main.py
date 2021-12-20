import whois
print("Enter URL without protocol(https://,http://)")
domain=input(">> ")
domain=whois.whois(domain)
print(domain)