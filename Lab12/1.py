#
#
# Keane Kouchi
# 10/30/24

import urllib.request
import ssl

# a.Open the URL using  urllib.request.urlopen(url) and print out the response you get. 
# Set ssl._create_default_https_context = ssl._create_unverified_context
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"
encoding = "utf-8"

print(f"Opening {url}...")
webpage = urllib.request.urlopen(url)
print(webpage)

# b.Use the opened URL to get the HTML as lines. Decode each 
# line .decode('utf-8') and print out the line only if it has a <title> tag.
for line in webpage:
    line = line.decode(encoding)
    if "<title>" in line:
        print(line)


# print(type(webpage))
