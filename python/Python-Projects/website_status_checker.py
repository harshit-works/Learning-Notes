import requests
import time
url = input("Enter the url of the website you want to chack:")
if not url.startswith("https://"):
    url = "https://" + url
for i in range(3):
    time.sleep(0.7)
    print ("Checking" + "." * (i + 1))
time.sleep(2.5)
try:
    result = requests.get(url)
    if result.status_code ==200:
        print("website is online")
    elif result.status_code ==404:
        print("page not found")
    elif result.status_code ==403:
        print("access forbidden")
    elif result.status_code ==301:
        print("redirected")
    else:
        print("The website responded with a status code I didn't specifically handle.")
except:
    print("There might be some connection issue from my end")
