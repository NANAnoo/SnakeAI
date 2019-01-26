from Snake import*
import numpy as np

class Group():
	"""docstring for Group"""
	def __init__(self, size):
		self.SIZE = size
		self.Snakes = []
		self.BestScores = []
		self.BestSnakes = []
		self.Scores = []
		self.ScoreSum = 0

	def Randomize(self,w,h):
		for i in range(self.SIZE):
			snk = Snake()
			snk.setSize(w,h)
			snk.Randamize()
			self.Snakes.append(snk)

	def NaturalSelection(self):
		for i in range(self.SIZE):
			while not self.Snakes[i].dead:
				self.Snakes[i].auto_play()
				self.Snakes[i].MOVE()
			self.Scores.append(self.Snakes[i].score())
			# Maxs = [[0,0]]*count
			# for i in range(SIZE):
			# 	for j in range(count):
			# 		if(self.Scores[i]>Maxs[j][0]):
			# 			Maxs.insert(j,[self.Scores[i],i])
			# 			Maxs.pop()
			# 
		self.BestScores.append(max(self.Scores))
		self.BestSnakes.append(self.Snakes[np.argmax(self.Scores)])
		self.ScoreSum = sum(self.Scores)

	def getParent(self):
		prob = random.uniform(0,self.ScoreSum)
		SUM = 0
		for i in range(self.SIZE):
			SUM += self.Scores[i]
			if SUM>=prob:
				return self.Snakes[i]

	def CrossMat(self,a,b):
		raw = a.shape[0]
		col = a.shape[1]
		Lw = random.randint(0,raw)
		Lc = random.randint(0,col)
		ans = np.zeros((raw,col))
		for i in range(raw):
			for j in range(col):
				x = 0
				if(i<Lw or(i==Lw and j<=Lc)):
					ans[i][j] = a[i][j]
				else:
					ans[i][j] = b[i][j]
		return ans

	def Cross(self,pa,ma):
		snk = Snake()
		snk.setSize(50,50)
		#w0 = self.CrossMat(pa.W0,ma.W0)
		#b0 = self.CrossMat(pa.B0,ma.B0)
		w1 = self.CrossMat(pa.W1,ma.W1)
		b1 = self.CrossMat(pa.B1,ma.B1)
		w2 = self.CrossMat(pa.W2,ma.W2)
		b2 = self.CrossMat(pa.B2,ma.B2)
		w3 = self.CrossMat(pa.W3,ma.W3)
		b3 = self.CrossMat(pa.B3,ma.B3)
		snk.init_with(w1,b1,w2,b2,w3,b3)
		return snk

	def nextGenerate(self):
		newGroup = []
		for i in range(self.SIZE):
			snk = self.Cross(self.getParent(),self.getParent())
			newGroup.append(snk)
		self.Snakes = newGroup
		self.Scores = []
		self.ScoreSum = 0

	def getAver(self):
		return self.ScoreSum / self.SIZE

	def Mutate(self,rate):
		for snk in self.Snakes:
			snk.mutate(rate)
