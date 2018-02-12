import os


def rename_files():
    file_list = os.listdir(r"C:\Users\Oss\Desktop\photos")
    print file_list
    os.chdir(r"C:\Users\Oss\Desktop\photos")
    for f in file_list:
        os.rename(f, f.translate(None, '0123456789'))


rename_files()
