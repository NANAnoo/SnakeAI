from Snake import*
from show import*
import os  

w = 50
h = 50
l = 15


def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.npy':  
                L.append(file_dir + file)  
    return L  
path = '/home/nano/BestSnakes/DATA/'
brains = file_name(path)
print(brains)

SHOW = Show(w,h,l)

snk = Snake()
snk.setSize(w,h)
snk.load_from(brains[0])

SHOW.addPlayer(snk)
#SHOW.Run(False)
SHOW.demo(brains,100)