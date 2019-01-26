import random
import numpy as np

class Snake():
	"""docstring for Snake"""
	def __init__(self):
		self.head = [25,25]
		self.body = [[24,25],[23,25],[22,25]]
		self.dead = False
		self.Width = 50
		self.Height = 50
		self.food_count = 0
		self.left_step = 200
		self.lifetime = 0
		self.nextfood()
		self.move_right()

	def init_with(self,w1,b1,w2,b2,w3,b3):
		#self.W0 = w0
		#self.B0 = b0
		self.W1 = w1
		self.B1 = b1
		self.W2 = w2
		self.B2 = b2
		self.W3 = w3
		self.B3 = b3

	def Mmutate(self,m,rate):
		for i in range(m.shape[0]):
			for j in range(m.shape[1]):
				r = random.random()
				if r<rate :
					m[i][j] += np.random.normal()/7.0
					if m[i][j]>1 :
						m[i][j] = 1
					else:
						if m[i][j]<-1:
							m[i][j] = -1


	def auto_play(self):
		INPUT = self.See()
		res = np.argsort(self.think(INPUT))[0][3]
		if res == 0:
			self.move_up()
		if res == 1:
			self.move_down()
		if res == 2:
			self.move_left()
		if res == 3:
			self.move_right()


	def See(self):
		Looks = []
		Looks.append(self.look([0,1]))
		Looks.append(self.look([1,1]))
		Looks.append(self.look([1,0]))
		Looks.append(self.look([1,-1]))
		Looks.append(self.look([0,-1]))
		Looks.append(self.look([-1,-1]))
		Looks.append(self.look([-1,0]))
		Looks.append(self.look([-1,1]))
		return np.array(Looks).reshape([1,24])

	def look(self,pos):
		distance = 1.0
		look = []
		point = [self.head[0]+pos[0],self.head[1]+pos[1]]
		a = 0
		b = 0
		while not self.CollisionWall(point):
			if self.CollisionFood(point):
				a = 1.0
			if self.CollisionSelf(point) and b==0:
				b = 1.0/distance
			distance +=1.0
			point = [point[0]+pos[0],point[1]+pos[1]]

		return [a,b,1.0/distance]

	def relu(self,m):
		return (np.abs(m)+m)/2

	def think(self,input):
		#L0 = self.relu(np.matmul(input,self.W0) + self.B0)

		L1 = self.relu(np.matmul(input,self.W1) + self.B1)
		#print(L1)
		L2 =  self.relu(np.matmul(L1,self.W2) + self.B2)
		#print(L2)
		return  self.relu(np.matmul(L2,self.W3) + self.B3)

	def mutate(self,rate):
		#self.Mmutate(self.W0,rate)
		#self.Mmutate(self.B0,rate)
		self.Mmutate(self.W1,rate)
		self.Mmutate(self.B1,rate)
		self.Mmutate(self.W2,rate)
		self.Mmutate(self.B2,rate)
		self.Mmutate(self.W3,rate)
		self.Mmutate(self.B3,rate)

	def Randamize(self):
		#self.W0 = np.random.uniform(-1,1,(24,18))
		#self.B0 = np.random.uniform(-1,1,(1,18))
		self.W1 = np.random.uniform(-1,1,(24,18))
		self.B1 = np.random.uniform(-1,1,(1,18))
		self.W2 = np.random.uniform(-1,1,(18,18))
		self.B2 = np.random.uniform(-1,1,(1,18))
		self.W3 = np.random.uniform(-1,1,(18,4))
		self.B3 = np.random.uniform(-1,1,(1,4))


	def setSize(self,Width,Height):
		self.Width = Width
		self.Height = Height

	def nextfood(self):
		self.food = [random.randint(1,self.Width-1),random.randint(1,self.Height-1)]
		go = True
		while go :
			go = False
			if(self.CollisionFood(self.head)):
				go = True
			for point in self.body:
				if(self.CollisionFood(point)):
					go = True
					break
			if(go):
				self.food = [random.randint(1,self.Width-1),random.randint(1,self.Height-1)]

	def CollisionFood(self,point):
		return point[0]==self.food[0] and point[1]==self.food[1]

	def CollisionWall(self,point):
		return point[0]==0 or point[0]==self.Width or point[1]==0 or point[1]==self.Height

	def CollisionSelf(self,p):
		for point in self.body:
			if(point[0]==p[0] and point[1]==p[1]):
				return True
		return False

	def reburn(self):
		self.dead = False
		self.head = [25,25]
		self.body = [[24,25],[23,25],[22,25]]
		self.food_count = 0
		self.left_step = 200
		self.lifetime = 0
		self.nextfood()
		self.move_right()

	def MOVE(self):
		if(self.left_step==1):
			self.dead = True
		if(self.dead):
			return
		self.lifetime+=1
		self.head[0] += self.V_x
		self.head[1] += self.V_y
		if(self.CollisionWall(self.head) or self.CollisionSelf(self.head)):
			self.dead = True

		if(self.CollisionFood(self.head)):
			#eat
			self.body.append(self.body[len(self.body)-1])
			length = len(self.body)
			for i in range(0,length-1):
				self.body[length-1-i] = [self.body[length-2-i][0],self.body[length-2-i][1]]

			self.body[0][0] = self.head[0] - self.V_x
			self.body[0][1] = self.head[1] - self.V_y
			self.nextfood()
			self.food_count +=1
			if self.left_step < 500 :
				if self.left_step>400:
					self.left_step = 500
				else:
					self.left_step +=100
		else:
			length = len(self.body)
			for i in range(0,length-1):
				self.body[length-1-i][0] = self.body[length-2-i][0]
				self.body[length-1-i][1] = self.body[length-2-i][1]
			self.body[0][0] = self.head[0] - self.V_x
			self.body[0][1] = self.head[1] - self.V_y

	def score(self):
		if self.food_count<10:
			return self.lifetime*self.food_count*self.food_count
		else:
			return self.lifetime*(self.food_count-9)*100

	def move_up(self):
		self.left_step -=1
		if(self.head[1]-self.body[0][1]!=1):
			self.V_y = -1
			self.V_x = 0

	def move_down(self):
		self.left_step -=1
		if(self.head[1]-self.body[0][1]!=-1):
			self.V_y = 1
			self.V_x = 0

	def move_left(self):
		self.left_step -=1
		if(self.head[0]-self.body[0][0]!=1):
			self.V_y = 0
			self.V_x = -1

	def move_right(self):
		self.left_step -=1
		if(self.head[0]-self.body[0][0]!=-1):
			self.V_y = 0
			self.V_x = 1

	def save(self):
		name = str(random.random())[2:] + ".npy"
		brain = [self.W1,self.B1,self.W2,self.B2,self.W3,self.B3]
		np.save(name,brain)