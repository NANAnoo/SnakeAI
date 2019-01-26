from Group import*
from Snake import*


GENERATTION = 200
SIZE = 2000

group = Group(SIZE)
group.Randomize(50,50)
RATE = 0.05
Last = 0
Current =0

for i in range(GENERATTION):
	group.NaturalSelection()
	Current = group.getAver()
	print("GENERATTION: ",i,"averageScore: ",Current," BestScore: ",group.BestScores[i]," BestEat:" ,group.BestSnakes[i].food_count)
	if 1 != GENERATTION-1:
		group.nextGenerate()
		# rate = 2/(Current-Last+21.121151)
		# if rate > 0.2 or Current-Last<0:
		# 	rate = 0.2
		group.Mutate(RATE)
	Last = Current

MAX = 0
INDEX = 0
for i in range(GENERATTION):
	if(group.BestScores[i]>MAX):
		MAX = group.BestScores[i]
		INDEX = i
snk = group.BestSnakes[i]

args = np.argsort(group.BestScores)
for i in range(100):
	group.BestSnakes[args[GENERATTION-1-i]].save()
