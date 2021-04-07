import requests
from bs4 import BeautifulSoup as bs

github_user = input("Github User: ")
url = "https://github.com/" + github_user
r = requests.get(url)
soup = bs(r.content, "html.parser")

try:
    profile_image = soup.find("img", {"alt": "Avatar"})['src']
    print(profile_image)
except TypeError:
    print("Incorrect User")
