import os
try:
    os.chdir(r'C:\Users\Oss\Desktop')
    os.makedirs('os/os2')

except Exception:
    print('dir already exist ')

print(os.listdir())

for dirpath, dirname, filename in os.walk(r'C:\Users\Oss\Desktop\WebDev'):
    print('current path: ', dirpath)
    print('dir', dirname)
    print('file : ', filename)


