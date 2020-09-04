from PIL import Image
import sys
import os


# 1. grab the first and second argument


folder_to_convert = sys.argv[1] #path of the folder images to convert to png

folder_to_put = sys.argv[2] #path where the coverted pics need to be stored

#check if new folder exist if not create it
folder_to_convert_abs= os.path.abspath(folder_to_convert)
 
if not os.path.exists(folder_to_put):

	directory = folder_to_put

	parent_dir ="/home/himanshu/Documents/"
	try:
		new_path = os.path.join(parent_dir, directory)
		os.makedirs(new_path)

	except OSError as error:
		print(error)
#loop through entire folder and convert images to png
for filename in os.listdir(folder_to_convert):
	img = Image.open(f'{folder_to_convert_abs}/{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f"{new_path}/{clean_name}.png", 'png')
	print("All Done")








	
	#print("Directory '% s' created" % directory) 



#save to the new folder