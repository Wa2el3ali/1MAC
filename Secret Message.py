import os


def rename_files():
    files_list = os.listdir(r"C:\Users\wa2el\Desktop\prank")
    print files_list

    saved_path = os.getcwd()
    # print saved_path
    os.chdir(r"C:\Users\wa2el\Desktop\prank")
    for file_name in files_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print "old_name - " + file_name + " --->" + "new_name - " + file_name.translate(None, "0123456789")

    os.chdir(saved_path)

rename_files()

