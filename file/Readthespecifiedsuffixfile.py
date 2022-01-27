import os
import re
filePath = 'C:\\Boost\\lib'
files = os.listdir(filePath)
pattern = "-x64-1_78.lib"
lenPattern = len(pattern)
for file in files:
    lenFile = len(file)
    if(file[lenFile-lenPattern:lenFile]==pattern):
        print(file+";")
    