import webbrowser
from googlesearch import search
import os
from tkinter import dialog
import tkinter as tk

# nimmt image von auswahl oder image url und geht zu google image search [selenium]
# +gibt ein site:aliexpress.com -- nimmt einfach imagepfad von tkinter
# nimmt mit google search einfach alle search results

# operate with image_url oder mit lokaler datei?

want_image = input("Do you want to use image urls or local image files? write url / file: ")

#main choice loop

while True:
    if want_image == "url":
        # logic für url

        image_url = input("Please input the image url: ")

        search_url = f'https://www.google.com/search?tbs=sbi:{image_url}=de&site=imghp&q=site:aliexpress.com&authuser=0'

        suppliers = []


        #google search
        for ali in search(search_url, tld='com', lang='en', num=30, stop=30, pause=2):
            if "aliexpress" in ali:
                suppliers.append(ali)
                print(f"{ali} was appended")
            
        print(suppliers)

        break


    elif want_image == "file":
        #logic für localfile


        break


    else:
        print("Instructions unclear.")
        want_image = input("please say url OR file: ")



#search_string_1 = f'https://www.google.de/search?tbs=sbi:{image_urö}=de&site=imghp&q=site:aliexpress.com&authuser=0'

