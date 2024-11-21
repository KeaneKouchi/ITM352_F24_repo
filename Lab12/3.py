# Inspect the website https://shidler.hawaii.edu/itm/people and note the HTML that displays the people.
# Keane Kouchi
# 10/30/24

from bs4 import BeautifulSoup as BS
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://shidler.hawaii.edu/itm/people"

print(f"Opening {url}...")
itm_html = urllib.request.urlopen(url)

# a.Using BeautifulSoup, parse the page to extract the HTML. Use prettify() to print out 
# the HTML (only put the first few lines here). You will need to install beautifulsoup4.

html_to_parse = BS(itm_html, "html.parser")
pretty_html = html_to_parse.prettify()

lines = pretty_html.splitlines()
lines_to_print = 10

for line in lines[:lines_to_print]:
    print(line)

# b. Create a list of the people retrieved. Print out the people and the number of people found. 
list_of_people = html_to_parse.find_all("h2", class_ = "title")

itm_people = []
for element in list_of_people:
    itm_people.append(element.text)
    print(element.text)

print("Number of ITM faculty: ", len(itm_people))