import random, re, os, sys
from zipfile import ZipFile

global isfound, random_lines
isfound = 0

def RL():
    random_lines = random.choice(open("bible.txt").readlines())
    random_lines = re.sub('<[^<]+?>', '', random_lines)
    return random_lines

if os.path.isfile('bible.txt'):
    isfound = 1
else:
    #extract our bible.txt
    zf = ZipFile('bible.zip', 'r')
    zf.extractall()
    zf.close()
    print(RL())
    input()

if isfound > 0:
   print(RL())
   input()
   