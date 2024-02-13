import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

f = open("data.txt", "a")
f.write(page.text)
f.close()

print("data added")
# print(page.text)