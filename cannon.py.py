import turtle as t
import random as r
def up ():
	t.left(2)
	
def down ():
	t.right(2)

def go ():
	ang=t.heading()
	#포물선 날아가기
	while t.ycor()>0:
		t.fd(15)
		t.right(5)
	
	d=t.distance(target,0)
	t.sety(r.randint(10,100))
	#타겟에 닿으면 굿 아니면 배드
	if d <= 25:
		t.pencolor('green')
		t.write("Good!",False,"center",("",15))
		t.pencolor('black')
	else:
		t.pencolor('red')
		t.write("Bad!",False,"center",("",15))
		t.pencolor('black')
		
				
	t.goto(-200,10)
	t.setheading(ang)
	
#거북이 발사
#땅에 닿을때까지 계속
#바닥에 닿으면 점수계산
#다시 돌아오기

t.goto(-300,0)
t.down()
t.goto(300,0)	
target=r.randint(50,150)
t.up()
t.pencolor('green')
t.pensize(8)
t.goto(target-25,0)
t.down()
t.goto(target+25,0)
t.up()
t.goto(-200,10)
t.onkeypress(up,"Up")
t.onkeypress(down,"Down")
t.onkeypress(go,"space")
t.listen()
t.mainloop()
