import os
import sys
import shutil
import platform
import zipfile

def is_linux():
        return platform.system() == "Linux"

def is_windows():
        return platform.system() == "Windows"

def getListOfFiles(dirName):
        # create a list of file and sub directories 
        # names in the given directory 
        listOfFile = os.listdir(dirName)
        allFiles = list()
        # loop through all the entries
        for entry in listOfFile:
                # Create full path
                fullPath = os.path.join(dirName, entry)
                # If entry is a directory then get the list of files in this directory 
                if os.path.isdir(fullPath):
                        allFiles = allFiles + getListOfFiles(fullPath)
                else:
                        allFiles.append(fullPath)
        return allFiles




def get_folder_paths():
        if is_linux():
                print("Enter the full input and output paths e.g /home/ubuntu/folder1")
                input_path = input("Enter Input Path:")
                output_path = input("Enter Output Path:")
        elif is_windows():
                print("Enter the full input and output paths e.g C:/folder1 use foward slash / instead of backslash ")
                input_path = input("Enter Input Path:")
                output_path = input("Enter Output Path:")
        if not input_path.endswith("/"):
        	input_path = input_path + "/"
        if not output_path.endswith("/"):
        	output_path = output_path + "/"
        errors=[]
        if not os.path.isdir(input_path):
                errors.append("Sorry the input path "+input_path+" doest not exists")
                

        if not os.path.isdir(output_path):
                errors.append("Sorry the output path "+output_path+" doest not exists")
        if errors:
                for error in errors:
                        print(error)
                sys.exit()
        print("\n")
        return input_path,output_path
        


def copy_files(number_of_files):
        src_path,dst_root = get_folder_paths()
        all_files = getListOfFiles(src_path)
        files_to_copy = all_files[:number_of_files]
        for src in files_to_copy:
        	# file relative path
        	rel_path = src[len(src_path):]
        	# Build destination path
        	destination_path = dst_root + rel_path
        	# check if parent directory exists otherwise create one
        	parent_dir = destination_path[:destination_path.rindex("/")]
        	if not os.path.exists(parent_dir):
        		os.makedirs(parent_dir)
        	shutil.copy2(src, destination_path)
        	print("copying "+src+" to "+destination_path)
        print("\n"+str(len(files_to_copy))+" files copied to "+ dst_root)
        

def unzip_files(number_of_files):
	src_path,dst_root = get_folder_paths()
	all_files= getListOfFiles(src_path)
	extensions_supported = []
	filtered_list = [x for x in all_files if x.endswith('.zip')]
	files_to_unzip = filtered_list[:number_of_files]
	for file_path in files_to_unzip:
		# file relative path
		rel_path = file_path[len(src_path):]
		# Build destination path
		destination_path = dst_root + rel_path
		# check if parent directory exists otherwise create one
		parent_dir = destination_path[:destination_path.rindex("/")]
		print("unzipping "+file_path+" to "+parent_dir)
		if not os.path.exists(parent_dir):
			os.makedirs(parent_dir)
		with zipfile.ZipFile(file_path,"r") as zip_ref:
			zip_ref.extractall(parent_dir)
		print(file_path)
	print("\n"+str(len(files_to_unzip))+" files unzipped to "+dst_root)

def delete_files(number_of_files):
        del_dir_path = input("Enter Path to folder with files to delete:")
        if not os.path.isdir(del_dir_path):
                print("Sorry the folder doest not exists")
                sys.exit()
        all_files = getListOfFiles(del_dir_path)
        files_to_delete = all_files[:number_of_files]
        for file_path in files_to_delete:
                print("Deleting "+file_path)
                os.remove(file_path)
        print("file deletion completed")


def main():
        print("1. Copy files")
        print("2. Unzip files")
        print("3. Delete files")

        user_input = input("Select an option?\n")

        if user_input == "1":
                copy_files(int(input("How Many Files Do You want to Copy?:")))
        elif user_input == "2":
                unzip_files(int(input("How Many Files Do You want to Unzip?:")))
        elif user_input == "3":
                delete_files(int(input("How Many Files Do You want to Delete?:")))
        else:
                print("Invalid Option!")
        print()


if __name__ == '__main__':
    main()
