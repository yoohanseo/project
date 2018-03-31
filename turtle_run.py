#화면구성
#위,아래,옆 이동하는 키
#먹이 먹고나면 또 랜덤으로 생성
#잡히면 죽음
import turtle as t
import random as r

Devil=t.Turtle()
Devil.shape('turtle')
Devil.color('black')
Devil.speed(0)
Devil.up()
Devil.goto(r.randint(-299,229),r.randint(-299,299))

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
	t.fd(10)
	ang=t.towards(t.pos())
	Devil.setheading(ang)
	Devil.fd(8)
	


t.shape('turtle')
t.setup(500,500)
t.bgcolor('gray')
t.speed(3)
t.color('white')
t.up()
t.onkeypress(turn_up,'Up')
t.onkeypress(turn_down,'Down')
t.onkeypress(turn_right,'Right')
t.onkeypress(turn_left,'Left')
t.listen()
t.mainloop()
