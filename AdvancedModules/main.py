import shutil

import shutil
import re
import os



def search(file, pattern=r'\d{3}-\d{3}-\d{3}'):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    return ''

if __name__ == '__main__':

    shutil.unpack_archive('unzip_me_for_instructions.zip','','zip')

    with open('extracted_content/Instructions.txt') as f:
        content = f.read()
        print(content)

    test_string = 'Here is a phone number 123-123-1234'

    results = []
    for folder, sub,files in os.walk(os.getcwd() + '\\extracted_content'):
        for f in files:
            fullpath = folder + '\\'+f
            print(fullpath)

            results.append(search(fullpath))

    for r in results:
        if r != '':
            print(r.group())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
