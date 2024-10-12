# open the file only if it exists and is readable,
# print out some file information

# Name: Keane Kouchi
# Date: 10/9/24

import os

file = 'survey_1000.csv'

if file and os.access(file, os.R_OK):
    FileInfo = os.stat(file)
    FileSize = FileInfo.st_size

    print(f"The file is {FileSize} bytes")
else:
    print("Invalid file")