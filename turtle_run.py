#화면구성
#위,아래,옆 이동하는 키
#먹이 먹고나면 또 랜덤으로 생성
#잡히면 죽음
import turtle as t
import random as r

score=0
playing=False

t.title('Turtle Run!!')

Devil=t.Turtle()
Devil.shape('turtle')
Devil.color('black')
Devil.speed(0)
Devil.up()
Devil.goto(r.randint(-299,229),r.randint(-299,299))

evil=t.Turtle()
evil.shape('turtle')
evil.color('red')
evil.speed(0)
evil.up()
evil.goto(r.randint(-299,229),r.randint(-299,299))


prey=t.Turtle()
prey.shape('circle')
prey.color('violet')
prey.up()
prey.goto(r.randint(-299,229),r.randint(-299,299))


def turn_up ():
	t.setheading(90)
def turn_down ():
	t.setheading(270)
def turn_right ():
	t.setheading(0)
def turn_left ():
	t.setheading(180)
def play ():
	global score
	global playing
	t.fd(16.7)
	ang1=Devil.towards(t.pos())
	Devil.setheading(ang1)
	ang2=evil.towards(t.pos())
	evil.setheading(ang2)
	Devil.fd(13)
	evil.fd(12.5)

	
	
	if t.distance(prey)<15:
		score+= 5
		prey.goto(r.randint(-229,229),r.randint(-229,229))
		t.write(score)
		if score == 10:
			Devil.fd(14)
			evil.fd(13.5)
	
		if score == 20:
			Devil.fd(16.5)
			evil.fd(16.5)
	
	if t.distance(Devil)>10 or t.distance(evil)>10 :
		t.ontimer(play,50)
	else:
		message('Game Over','score='+str(score))
		score=0

def message(m1,m2):
	t.up()
	t.goto(0,100)
	t.write(m1, False, "center", ("",20))
	t.up()
	t.goto(0,-100)
	t.write(m2, False, "center", ("",15))

message('TURTLE RUN!!','space를 누르면 시작합니다')


def start():
	global playing
	if playing == False:
		plaing=True
		play()
		t.clear()
	


	


t.shape('turtle')
t.setup(500,500)
t.bgcolor('gray')
t.speed(0)
t.color('white')
t.up()
t.onkeypress(turn_up,'Up')
t.onkeypress(turn_down,'Down')
t.onkeypress(turn_right,'Right')
t.onkeypress(turn_left,'Left')
t.onkeypress(start,'space')


t.listen()
t.mainloop()

