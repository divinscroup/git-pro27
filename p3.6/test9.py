import os
import re

os.chdir(r'C:\Users\Oss\Desktop\ved')
for d in os.listdir():
    f_path, f_ext = os.path.splitext(d)
    f_title, f_middle, f_sub, f_num = f_path.split('-')
    num = re.findall(r'\d+', f_num)

    f_new = '{:02} {}-{}{}'.format(int(num[0]), f_title.strip(), f_middle.strip(), f_ext)
    os.rename(d,f_new)
    
