import requests
from bs4 import BeautifulSoup



# theme finder 

test = 'https://glownglam.co/products/polygel-nail-kit'

req = requests.get(test).text

soup = BeautifulSoup(req, 'lxml')
soup_pretty = soup.prettify()


#sucht alle scripts im quelltext
scripts = soup.find_all('script')

conv_script_string = str(scripts)

print(type(conv_script_string))

for line in conv_script_string:
    print(line)



"""
with open('scripts.txt', 'w') as script_file:
    for line in conv_script_string:
        script_file.write(line)

    script_file.close()





find_theme = 'Shopify.theme' in scripts
print(find_theme)
"""
