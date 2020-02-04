# import libraries
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

# print start statement
print ("Choose image which you want to convert")

# open files and print path
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes = (("Image files *.jpg;*.jpeg;*.png", "*.jpg;*.jpeg;*.png"),("All files", "*.*")),multiple=True)
print("You selected " + str(len(file_path)) + " file(s) \r\n")

# print start statement
print ("Choose logo")

# open logo
root2 = tk.Tk()
root2.withdraw()
logo_file_path = filedialog.askopenfilename(filetypes = (("Image files *.jpg;*.jpeg;*.png", "*.jpg;*.jpeg;*.png"),("All files", "*.*")))
print("You selected logo file \r\n")
# open logo image
logo_image = Image.open(logo_file_path,"r")
# convert logo size
width, height = logo_image.size
new_width = 640
new_height = int(new_width / width * height)
logo_image = logo_image.resize((new_width, new_height))
logo_image = logo_image.convert(mode='RGBA')
new_image = Image.new(mode="RGBA", size=(1920,1080), color="#FFFFFF")
new_image.paste(logo_image,(int(1920/2 - new_width/2),int(1080/2 - new_height/2)))
logo_image = new_image

# find main path
print("In this folder you will find converted files")
destination = file_path[0]
destination_last = destination.rfind('/')
destination_file_path = destination[0:destination_last] + "/Converted"
print(destination_file_path + '\r\n')

# create destination folder
if (len(file_path) != 0):
    if not os.path.exists(destination_file_path):
        os.makedirs(destination_file_path)

# open, convert and save file(s)
for file in file_path:
    # extract file name
    file_name, ext_name = os.path.splitext(file)
    file_name = file_name[file.rfind('/')+1:len(file_name)]
    # open image
    this_image = Image.open(file)
    # convert image size
    width, height = this_image.size
    new_width = 1920
    new_height = int(new_width / width * height)
    this_image = this_image.resize((new_width,new_height))
    this_image = this_image.convert(mode='RGBA')
    new_image = Image.new(mode="RGBA", size=(1920, 1080), color="#000000")
    new_image.paste(this_image, (int(1920 / 2 - new_width / 2), int(1080 / 2 - new_height / 2)))
    this_image = new_image
    # composite 2 image
    r,g,b,alpha = logo_image.split()
    alpha = alpha.point(lambda i: i>0 and 30)
    final_image = Image.composite(logo_image,this_image,alpha)
    # save image
    final_image = final_image.convert(mode='RGB')
    final_image.save(destination_file_path + '/' + file_name + ".JPEG")

# end
print("Done")
