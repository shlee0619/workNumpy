import numpy as np

x = [2,4,6,8,10]      #시건합계 30/5   평균 6시간
y = [81,93,91,97,98]  #점수합계 460/5  평균 92점


sum_x = np.sum(x) 
sum_y = np.sum(y)
print('시간x 총점: ', sum_x) #시간 x 총점 30
print('점수y 총점: ', sum_y) #점수 y 총점 460


mean_x = np.mean(x) 
mean_y = np.mean(y)
print('시간x 평균: ', mean_x) #시간 x 평균:  6.0
print('점수y 평균: ', mean_y) #점수 y 평균:  92.0
print()


# x = [2,4,6,8,10]      #시건합계 30/5   평균 6시간
# y = [81,93,91,97,98]  #점수합계 460/5  평균 92점
# child= 76 / parent=40
child = sum([(x[idx]-mean_x) * (y[idx] - mean_y) for idx, value in enumerate(x)])
parent = sum([(i - mean_x)**2 for i in x])
a = child/parent        #76/40=1.9
b = mean_y-(mean_x*a)   #92-(6*1.9)=92-11.4=80.6  

print('분자 child:', child)
print('분모 parent:', parent)
print()
print('기울기(a):', a)
print('y 절편(b):', b)
print()
'''
분모 parent: 40.0
분자 child: 76.0
기울기(a): 1.9
y 절편(b): 80.6
'''
print( '- ' *50)
print()


my = []
for i in range(5):
    cal= int((a*x[i]+b))  #기울기(a): 1.9 y 절편(b): 80.6
    my.append(cal)

print(my) #예측점수 [84, 88, 92, 95, 99]
# x = [2,4,6,8,10]      #시건합계 30/5   평균 6시간
# y = [81,93,91,97,98]  #점수합계 460/5  평균 92점
print('5시간성적', int((a*5+b)) ) #90
print('6시간성적', int((a*6+b)) ) #92
print()
print()