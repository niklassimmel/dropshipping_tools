
# testing directory creation
"""
import os

folder_name = 'user_txt_files'

# file_name = input("name the file: ")
# file_name_txt = file_name + '.txt'


path = "./competitor_list/user_files/txt_files"

os.makedirs(path)
"""
# looping through txt file and opening in webbrowser
# options: type yes to display next; display {input_number}; display top 1ß

import webbrowser

urls_array = []

with open("competitor_list/user_files/competitorlists_txt_files/lashkit.txt") as f1:
    for fil in f1:
        urls_array.append(fil)

print(urls_array)

länge = len(urls_array)

i = 0

# open link then ask if open next one
print(f"there are {länge} urls!")

while i <= länge:
    for link in urls_array:
        openyon = input("do you want to open the link in your browser: type 'yes' or 'no': ")
        if openyon == "yes":
            webbrowser.open(link)
        elif openyon == "no":
            print("the money isa gone")
        else:
            print("Unclear instructions")




     
