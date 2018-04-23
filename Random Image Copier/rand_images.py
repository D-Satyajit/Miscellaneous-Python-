# This program copies random images (in bulk) to several subfolders [using Python3]

# First you have to create a folder having some subfolders (tested on 1 lakh subfolders).
# Then create an image folder having some images in that.
# Note : The name of subfolders and image files must be numeric. (Starting from 1, 2, 3, ....)

# Image Folder : Contains images - must be named as 1,2,3,4... 
# Destination Folder : This folder contains subfolders were random images (as set) will be copied from images folder.




import glob, os, shutil, random

count = 1 # ith Folder Name
while (count < 10): # Put the number of folder here
	dest_dir =("/home/satyajeet/Desktop/jit/"+str(count)) 


	img = [] # Empty List
	val = ''
	for i in range(0,10):
		# Getting path of random images from "images" folder.
		val = random.choice(os.listdir('/home/satyajeet/Desktop/images')) 
		img.insert(i,val)
		#print(val)


	for j in range(0,10):
		src_path = "/home/satyajeet/Desktop/images/"+img[j]
		#print(src_path)
		shutil.copy(src_path, dest_dir)

	#print(len(img))

	count = count + 1









