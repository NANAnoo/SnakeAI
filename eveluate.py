from Snake import*
import os 

w = 50
h = 50
l = 10

TIMES = 100

def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.npy':  
                L.append(file_dir + file)  
    return L 

brains = file_name('/home/nano/BestSnakes/DATA/')
snk = Snake()
snk.setSize(w,h)

size = len(brains)

SCORES = []

for brain in brains:
	snk.load_from(brain)
	snk.reburn()
	timeout = 0.0
	wall = 0.0
	Self = 0.0
	scoresum = 0.0
	for i in range(TIMES):
		while not snk.dead:
			snk.auto_play()
			snk.MOVE()
		if snk.deadReason == 'time out':
			timeout+=1
		if snk.deadReason == 'collisionWall':
			wall+=1
		if snk.deadReason == 'collisionSelf':
			Self+=1
		scoresum += snk.food_count
		snk.reburn()
	SCORES.append(scoresum)
	print("Snake:",brain,"timeout:",timeout/TIMES,'collisionWall:',wall/TIMES,'collisionSelf:',Self/TIMES,'score:',scoresum/TIMES)

Rank = np.argsort(SCORES)
lens = len(Rank)
for i in range(lens):
	print('RANK',i,'NAME',brains[Rank[lens-1-i]])