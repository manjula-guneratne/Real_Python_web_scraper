import requests
from bs4 import BeautifulSoup

url = "https://pythonjobs.github.io/"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find(id="container")

data = results.find_all('section', class_="job_list")
# job_element = soup.find_all('section', class_="job_list").text

python_jobs = results.find_all("h1", string=lambda text: "python" in text.lower())

python_job_element = [section_element.parent.parent for section_element in python_jobs]

counter = 1

for job_element in python_job_element:
    # title_element = job_element.find("h1",'')
    # company_element = job_element.find("i", class_="i-company")
    # location_element = job_element.find("a")

    # print('Job element ***',counter,'*** Added: ',job_element.find('h1'))
    counter = counter + 1


    # print("TITLE ----- ",title_element.text)

    # print(company_element)
    # print(location_element)

# print('DATA ************ ', data)

# print(python_jobs)
print(python_job_element)