import tkinter as tk
from tkinter import filedialog
from PIL import Image


root = tk.Tk()
root.withdraw()

# file_path = filedialog.askopenfilename()

more_imgs = filedialog.askopenfilenames()  # gibt nur immer die paths

img_list = []

# array mit allen filepaths
for img in more_imgs:
    img_list.append(img)
    print(img)

print(img_list)

# check if files are webp
# slicing backwards
webp_list = []

# this is bad code ---- fucked up loop -- works now
for webp in img_list:
    if webp[-4:] == "webp":
        webp_list.append(webp)
        print(f"{webp} is a .webp file")

    while webp[-4:] != "webp":
        print("please select only .webp files")
        webp_files = filedialog.askopenfilenames()
        for webp_f in webp_files:
            if webp_f[-4:] == "webp":
                webp_list.append(webp_f)
        break
                

print(webp_list)
# convert alle images im array von webp -> jpg


# print(file_path)



