import matplotlib
import re
import os


config_file = matplotlib.matplotlib_fname()

# Make some change in the config file for matplotlib

with open(config_file) as f:
    data = f.read()

regex = r"#axes\.unicode_minus"
subst = "axes.unicode_minus"
data = re.sub(regex, subst, data, 0)


regex = r"#(font\.sans-serif\s+:\s+)(\S)"
subst = "\\1WenQuanYi Micro Hei, \\2"
data = re.sub(regex, subst, data, 0)

with open(config_file, 'w') as f:
    f.write(data)

# move wenquanyi open source TTF font file in 

import shutil

ttf_font_path = config_file.replace('/matplotlibrc', '/fonts/ttf')

shutil.copy2("wenquanyi-micro-hei.ttf", ttf_font_path)


# clear fontlist

import glob

try:

    dot_matplotlib_path = os.path.expanduser("~/.matplotlib")

    fontlist_files = glob.glob(dot_matplotlib_path+"/fontList*")

    for file in fontlist_files:
        os.remove(file)

    print("Please restart the kernel in Jupyter Notebook and rerun plot command. Enjoy Chinese Display!")

except:

    print('Can not delete font list files in ~/.matplotlib')
