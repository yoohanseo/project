import random as r


def make_question():
	'''문제를 만드는 함수'''
	#숫자를 랜덤으로 생성 *2
	#연산자를 랜덤으로 생성
	#숫자연산자숫자
	#return
	a=r.randint(1,100)
	b=r.randint(1,100)
	c=r.randint(1,3)
	if c==1:
		t='+'
	elif c==2:
		t='-'
	elif c==3:
		t='*'
	result=str(a)+t+str(b)
	return result
	
while True:
	y=make_question()
	u=input('그만하고 싶으면 stop을 타이핑 해주세요.'+y+'=')
	if u =='stop':break
	elif int(u) == eval(y):
		print('Correct!')
	else:
		print('NO')
		
	
	
	
	

