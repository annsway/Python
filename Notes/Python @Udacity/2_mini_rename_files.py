import os 
def rename_files():
	#1) Get the files from a folder 
	file_list=os.listdir("/Users/ann/Dropbox/Python/2_alphabet")
	
	saved_path=os.getcwd()
	print("The current working directory is"+saved_path)
	os.chdir("/Users/ann/Dropbox/Python/2_alphabet")

	#2) For each file, rename filename 
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir(saved_path)
	
rename_files()
