from sympy import *
import sys
import matplotlib.pyplot as plt
print("아폴리니우스의 원") #프로그램 소개
print("AP : BP = M : N") #사용 방법
a1 = int(input("A의 X 좌표 : ")) #입력
a2 = int(input("A의 Y 좌표 : "))
b1 = int(input("B의 X 좌표 : "))
b2 = int(input("B의 Y 좌표 : "))
m = int(input("비율 M : "))
n = int(input("비율 N : ")) #입력 
if a1==b1 and a2==b2: #A와 B의 좌표가 같을 수 없음
    print("A와 B의 좌표가 같으면 안됩니다.")
    sys.exit() #프로그램 종료
if m==n: #M과 N의 비율이 같으면 직선이 만들어짐 (1:1, 2:2)
    print("M과 N의 비율이 같으면 직선이 만들어집니다.")
    sys.exit()
print("작성한 좌표는 (",a1,",",a2,"),(",b1,",",b2,"), 비율은",m,":",n,"입니다") #입력 된 좌표 출력
powm = m * m #비율 제곱
pown = n * n #비율 제곱
x = Symbol('x') #미지수 사용
y = Symbol('y')
powap = expand((x - a1)**2 + (y - a2)**2) #비율을 곱하지 않은 선분 AP
powbp = expand((x - b1)**2 + (y - b2)**2) #비율을 곱하지 않은 선분 BP
AP = pown * powap #비율을 곱한 선분 AP
BP = powm * powbp #비율을 곱한 선분 BP
equ = AP - BP #우변을 좌변으로 이동(좌변을 우변으로)
pol= Poly(equ, x, y)
if pol.coeffs()[0] == 1: #방정식의 X 제곱이 1일 때
    if a1==b1==0: #두 점의 X 좌표가 서로 0으로 같을 때 (방정식의 X가 존재 안함)
        ry = -(pol.coeffs()[2] / 2)
        radius = sqrt(pol.coeffs()[2]**2 - 4*(pol.coeffs()[3])) / 2
        rx = a1
        print("(0,",ry,"), 반지름은 ",radius)
    elif a2==b2: #두 점의 Y 좌표가 서로 0으로 같을 때
        rx = -(pol.coeffs()[1] / 2)
        radius = sqrt(pol.coeffs()[1]**2 - 4*(pol.coeffs()[3])) / 2
        ry = a2
        print("(",rx,",0), 반지름은 ",radius)
    elif a1!=b1 and a2!=b2: #두 점의 X, Y 좌표가 서로 다를 때
        rx = -(pol.coeffs()[1] / 2)
        ry = -(pol.coeffs()[3] / 2)
        radius = sqrt(pol.coeffs()[1]**2 + pol.coeffs()[3]**2 - 4*(pol.coeffs()[4])) / 2
        print("(",rx,",",ry,"), 반지름은 ",radius)
    else: #예외 상황일 때
        radius = - pol.coeffs()[2]
        rx = 0
        ry = 0
        print("(0,0), 반지름은 ",radius)
elif pol.coeffs()[0] > 1: #방정식의 X 제곱이 1 이상일 때
    newequ = equ / pol.coeffs()[0]
    polnew = Poly(newequ, x, y)
    if a1==b1==0: #두 점의 X 좌표가 서로 0으로 같을 때 (방정식의 X가 존재 안함)
        ry = -(polnew.coeffs()[2] / 2)
        radius = sqrt(polnew.coeffs()[2]**2 - 4*(polnew.coeffs()[3])) / 2
        rx = a1
        print("(0,",ry,"), 반지름은 ",radius)
    elif a2==b2: #두 점의 Y 좌표가 서로 0으로 같을 때
        rx = -(polnew.coeffs()[1] / 2)
        radius = sqrt(polnew.coeffs()[1]**2 - 4*(polnew.coeffs()[3])) / 2
        ry = a2
        print("(",rx,",0), 반지름은 ",radius)
    elif a1!=b1 and a2!=b2: #두 점의 X, Y 좌표가 서로 다를 때
        rx = -(polnew.coeffs()[1] / 2)
        ry = -(polnew.coeffs()[3] / 2)
        radius = sqrt(polnew.coeffs()[1]**2 + polnew.coeffs()[3]**2 - 4*(polnew.coeffs()[4])) / 2
        print("(",rx,",",ry,"), 반지름은 ",radius)
    else: #예외 상황일 때
        radius = - polnew.coeffs()[2]
        rx = 0
        ry = 0
        print("(0,0), 반지름은 ",radius)
else: #방정식의 제곱이 음수일 때
    cequ = - (equ)
    polcequ = Poly(cequ, x, y)
    if polcequ.coeffs()[0] > 1: #방정식의 X 제곱이 1 초과일 때
        newequ = cequ / polcequ.coeffs()[0]
        polnew = poly(newequ, x, y)
        if a1==b1==0: #두 점의 X 좌표가 서로 0으로 같을 때 (방정식의 X가 존재 안함)
            ry = -(polnew.coeffs()[2] / 2)
            radius = sqrt(polnew.coeffs()[2]**2 - 4*(polnew.coeffs()[3])) / 2
            rx = a1
            print("(0,",ry,"), 반지름은 ",radius)
        elif a2==b2: #두 점의 Y 좌표가 서로 0으로 같을 때
            rx = -(polnew.coeffs()[1] / 2)
            radius = sqrt(polnew.coeffs()[1]**2 - 4*(polnew.coeffs()[3])) / 2
            ry = a2
            print("(",rx,",0), 반지름은 ",radius)
        elif a1!=b1 and a2!=b2: #두 점의 X, Y 좌표가 서로 다를 때
            rx = -(polnew.coeffs()[1] / 2)
            ry = -(polnew.coeffs()[3] / 2)
            radius = sqrt(polnew.coeffs()[1]**2 + polnew.coeffs()[3]**2 - 4*(polnew.coeffs()[4])) / 2
            print("(",rx,",",ry,"), 반지름은 ",radius)
        else: #예외 상황일 때
            radius = - polnew.coeffs()[2]
            rx = 0
            ry = 0
            print("(0,0), 반지름은 ",radius)
    else: #방정식의 X 제곱이 1일 때
        polnew = Poly(cequ, x, y)
        if a1==b1==0: #두 점의 X 좌표가 서로 0으로 같을 때 (방정식의 X가 존재 안함)
            ry = -(polnew.coeffs()[2] / 2)
            radius = sqrt(polnew.coeffs()[2]**2 - 4*(polnew.coeffs()[3])) / 2
            rx = a1
            print("(0,",ry,"), 반지름은 ",radius)
        elif a2==b2: #두 점의 Y 좌표가 서로 0으로 같을 때
            rx = -(polnew.coeffs()[1] / 2)
            radius = sqrt(polnew.coeffs()[1]**2 - 4*(polnew.coeffs()[3])) / 2
            ry = a2
            print("(",rx,",0), 반지름은 ",radius)
        elif a1!=b1 and a2!=b2: #두 점의 X, Y 좌표가 서로 다를 때
            rx = -(polnew.coeffs()[1] / 2)
            ry = -(polnew.coeffs()[3] / 2)
            radius = sqrt(polnew.coeffs()[1]**2 + polnew.coeffs()[3]**2 - 4*(polnew.coeffs()[4])) / 2
            print("(",rx,",",ry,"), 반지름은 ",radius)
        else: #예외 상황일 때
            radius = - polnew.coeffs()[2]
            rx = 0
            ry = 0
            print("(0,0), 반지름은 ",radius)
circle_center = (rx, ry) #원의 중심 설정
circle_radius = radius #원의 반지름 설정
a = plt.axes(xlim=(-10, 10), ylim=(-10, 10)) #좌표 설정
a.set_aspect('equal')
plt.axvline(x=0, color = 'r')
plt.axhline(y=0, color = 'r')
c = plt.Circle(circle_center, circle_radius, fc='w', ec='b') #원 설정
a.add_patch(c)
#plt.scatter(rx,ry) - 원의 중심, 점 오류
plt.plot([a1, b1], [a2, b2])
plt.grid()
plt.title('CircleofApollonios') #타이틀 설정
plt.show()
