from bs4 import BeautifulSoup
import requests
from googlesearch import search
import os
import webbrowser
import time

product_title = input("Please type Product Title: ")   #wird nacher automatisch gescrapt

final_title = product_title + ' .myshopify'
print(final_title)

result_urls = []

def GoogleResults():

    for j in search(final_title, tld='com', lang='en', num=30, stop=30, pause=2):
        if 'amazon' in j:
            return None
       # elif 'aliexpress' in j:
        #    return None
        else:
            result_urls.append(j)
            # print(j)

"""--------------------------------------------------------"""  #save function file
GoogleResults() # need to call function up here sonst ist len_array = 0

len_array = len(result_urls)
print(len_array)

folder_name = 'competitorlists_txt_files'

#schreiben einer txt datei mit allen links

def saveInDirectory():

    want_save = input("Do you want to save the links in a file? yes/no: ")

    if want_save == "yes" or want_save == "Yes":

        try:
            if os.path.exists(f'competitor_list/user_files/{folder_name}'):
                print("Path already exists!")
            else:
                os.makedirs(f'competitor_list/user_files/{folder_name}/')
            
            if not OSError:
                print(f"A new folder named {folder_name} was successfully created in the files folder !")

        except OSError:
            print("Error accured when creating path")

        """-----------------------------------------------------------"""
        #write the file

        filename = input("please choose a filename: ")


        while os.path.exists(f'competitor_list/user_files/{folder_name}/{filename}.txt') == True:
            print(f'{filename}.txt already exists!')
            filename = input("Please choose another filename: ")
            if os.path.exists(f'competitor_list/user_files/{folder_name}/{filename}.txt') == False:
                break



        with open(f'competitor_list/user_files/{folder_name}/{filename}.txt', 'w') as file:
            for f in result_urls:
                # print(f)
                file.write(f+'\n')

            file.close()
            print(f'{filename}.txt was successfully created in folder {folder_name} inside the user_files folder!')



    elif want_save == "no" or want_save == "No":
        print("Alright, no file was created")

    else:
        print("Instructions unclear. Please type yes or no!")


# webbrowser automatisches öffnen der links mit 5 sekunden abstand
def openLinks():
    want_open = input(f"do you want to open the {len_array} links? Type: yes or no: ")
    if want_open == "yes" or want_open == "Yes":
        for link in result_urls:
            webbrowser.open_new_tab(link)
            print(f"{link} successfully opened")
            time.sleep(2)
        print("all links successfully opened")
    elif want_open == "no" or want_open == "No":
        print("Links won't be opened")
    else:
        print("Unclear. Please type 'yes' or 'no'")



saveInDirectory()
openLinks()

"""----------------------------------------"""     # verify if the stores a shopifys #gehört for save in file


# fix 'bug': keine doppelten stores, keine aliexpress (mit shopify source varification) = 100% nur shopify stores
# neues tool: aliexpress supplier finder; scrape image url on page --> google image search -- fetch google search results -> array und ausgeben
#tool: content scraper kann dann txt datei lesen und durch loopen und alle diese Links verwenden (oder er verwendet raw arry)
# make option: scrape one speficic store or scrape whole list

