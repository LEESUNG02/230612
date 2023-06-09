# 불(Bool)과 비교, 논리 연산자
## 불과 비교 연산자 사용하기
'''
* 프로그래밍 -> 참, 거짓 판단 -> 참(True) : 어떠한 조건이나 수식을 만족시키는가? / 거짓(False) : 만족시키지 못한다
* 불(Bool) 혹은 불리언(Boolean) : 참과 거짓으로 구성된 자료형. <- 조건이나 수식들이 존재하게 됨.
* 두 값의 관계를 판단하는 비교 연산자 / 두 값의 논리적 관계를 판단하는 논리 연산자
* if, while.. 구문을 작성.
'''
print(True, False)  # 다른 언어들은 대개 true, false
print(int(True), int(False))  # 1, 0

# 비교 연산자 - 판단 결과
## 등호(같다, 다르다)와 부등호(크다, 작다). -> 비교하는 식이 맞으면 True 아니면 False
print('10 > 5', '10이 5보다 크다, 10은 5를 초과한다', 10 > 5)  # 초과
print('10 < 5', '10이 5보다 작다, 10은 5의 미만이다', 10 < 5)  # 미만

## 숫자가 같은지 다른지 비교
'''
* 일반적 수학에서는 =(등호)로 쓰는데, 파이썬 등 프로그래밍에서는 ==을 등호(동등 연산자, equal)로 쓴다
* =은 파이썬 뭐에요? -> 대입 연산자 -> 특정한 변수에 값을 할당해주는 연산자
* 다를 때 !=(not equal)을 사용
'''
print("1 == 1 :", 1 == 1)
print("2 == 1 :", 2 == 1)
print("1 != 1 :", 1 != 1)

## 문자열 동등 여부 비교 (only)
print("'python' == 'python'", "python" == "python")  # java == X. equals -> 주소값을 비교하니까.
print("'Python' == 'python'", "Python" == "python")  # 대소문자가 다르면 다른 문자!!!!
print("'Python' != 'python'", "Python" != "python")  # 대소문자가 다르면 다른 문자!!!!

# 숫자 비교 : 부등호
print("10 > 20", 10 > 20)  # 초과 (왼쪽 값 기준으로 생각)
print("10 < 20", 10 < 20)  # 미만
print("10 >= 20", 10 >= 20)  # 이상
print("10 <= 20", 10 <= 20)  # 이하

# 객체가 같은지 다른지 비교하기
'''
* is, is not -> 연산자. ==, !=. 왜 is(~이다), is not(~는 ~가 아니다)?
* ==, != : 값 자체를 비교한다
* is, is not -> 객체를 비교한다, 객체 주소를 비교한다(타입) 
'''
# 정수 1과 실수 1.0은 까다롭게 생각하면 다른 애들.
print("1 == 1.0 :", 1 == 1.0)  # 1이라고 하는 '값'은 같아요 (상호 변환이 가능) - 같은 숫자형일 경우에는 같다고 침
print("'1' == 1 :", '1' == 1)  # 문자열과 숫자의 비교이므로 성립 안함
# a = 1 is 1.0 # 비교 연산의 결과값을 변수에 담을 수 있음
# print("1 is 1.0 :", a)
# b = (1 is not 1.0)
# print("1 is not 1.0 :")
# print(b)

# 논리 연산자 사용하기
## 논리 연산자는 and, or, not. (연산자가 꼭 특수문자나 기호일 필요는 없음)
'''
내가 알고 있던 and는 &? &&? 내가 알고 있던 or은 |? ||? 내가 알고 있는 not은 !인데??
'''
## 그리고(and) 연산 (&)
have_car = True
have_money = True
can_drive = have_car and have_money
print("have_car", have_car)
print("have_money", have_money)
print("can_drive", can_drive)
print()
have_car = False
have_money = True
can_drive = have_car and have_money # 하나라도 False면은 다 False 틀린다
print("have_car", have_car)
print("have_money", have_money)
print("can_drive", can_drive)
print()
have_car = True
have_money = False
can_drive = have_car and have_money # 하나라도 False면은 다 False / 틀린다
print("have_car", have_car)
print("have_money", have_money)
print("can_drive", can_drive)
print()
have_car = False
have_money = False
can_drive = have_car and have_money # 하나라도 False면은 다 False / 틀린다
print("have_car", have_car)
print("have_money", have_money)
print("can_drive", can_drive)

print("have_car & have_money", have_car & have_money)
# print("have_car && have_money", have_car && have_money) # 문법 오류

# or (또는) / a or b : or로 묶인 것들 중에 하나가 True라면 결과값 True (a | b)
hungry = True
study = True
eat_lunch = hungry or study
print("hungry?", hungry)
print("study?", study)
print("eat_lunch?", eat_lunch)
print()
hungry = False
study = True
eat_lunch = hungry or study
print("hungry?", hungry)
print("study?", study)
print("eat_lunch?", eat_lunch)
print()
hungry = True
study = False
eat_lunch = hungry or study
print("hungry?", hungry) # <-> 배부르다
print("study?", study)
print("eat_lunch?", eat_lunch)
print()
hungry = False
study = False
eat_lunch = hungry or study # 여기서 계산이 끝남
print("hungry?", hungry)
print("study?", study)
print("eat_lunch?", eat_lunch) # 하나라도 True라면 결과가 True -> OR
print()
print("hungry | study", hungry | study)

# not (논리값 -> bool) True -> False / False -> True
sleepy = True
print("sleepy", sleepy)
print("not sleepy", not sleepy) # 안 졸리다, 깨어있다~
boring = False
print("boring", boring)
print("not boring", not boring)
# print("not boring", !boring) -> ! 연산자 없음...

# and, or, not -> not (1), and (2), or (3) <- 우선순위 외우면 좋음.

print("not True and False or not False", not True and False or not False)
print("(not True) and False or (not False)", False and False or True)
print("((not True) and False) or (not False)", False or True)
# 논리 연산도 ()를 통해서 강제로 우선순위를 정해줄 수 있음.
# 논리 연산을 복잡하게 하는 것에 익숙하지 않다 / 못하겠다
# 1. 괄호 사용하기 2. 변수로 끊어서 연산하기

# 논리 연산자 + 비교 연산자 (무조건 비교 연산자가 먼저임)
# 비교 연산자를 통해서 값을 비교하고 이것을 통해 True 또는 False 결과값(Bool 값이 나옴)
# 그 후에 논리 연산자가 그것을 받아서 처리함
# 산술 -> 비교 -> 논리 연산자 순. (그래도 괄호와 변수로 표현된 건 먼저 처리가 된 상태임)
print("10 == 10 and 10 != 5 :", 10 == 10 and 10 != 5)
print("(10 == 10) and (10 != 5) :", True and True)  # True.
print("10 > 5 or 10 < 3", 10 > 5 or 10 < 3) # True
print("5 + 5 > 8 and 3 - 2 < 0", 5 + 5 > 8 and 3 - 2 < 0)
print("(5 + 5) > 8 and (3 - 2) < 0", 5 + 5 > 8 and 3 - 2 < 0)
print("not 10 > 5", not 10 > 5)
print("not 7 + 3 > 5", not 7 + 3 > 5)

# 정수, 실수, 문자열을 불(참,거짓)으로 만들기 / 판별
'''
정수, 실수, 문자열 -> 불(bool) => bool(1)
'''
print("bool(1)", bool(1))
print("bool(0)", bool(0))
print("bool(-1)", bool(-1)) # 정수, 실수나 => 숫자에서는 True/False 기준은 0이면 False. 0이 아니면 True
print("bool(0.1)", bool(0.1))
# number -> bool ???? number != 0

# 문자열
print("bool('아무거나')", bool("아무거나")) # True
print("bool('abadfafa')", bool("abadfafa")) # True
print("bool('')", bool("")) # False => 큰따옴표 혹은 작은따옴표로 감싸진 것만 있을 때
# string -> bool ???? len(string) > 0 # length(길이)
# 문자열
# "" 혹은 ''로 묶여진 글자들의 묶음 (0자 이상의 글자들의 집합)

text = "hello playdata!"
print(text) # 출력

# 한글 문자열
korean = "먹어도 먹어도 배고프다"
print(korean)

# 문자열 만들기 : " "(큰따옴표)로 묶기
double_quotation = "my name is python"
print(double_quotation)  # ctrl + space (자동완성 or 기능 추천)

# ' '(작은따옴표)로 묶기
single_quotation = 'your name is python'
print(single_quotation)

#  '''...'''로 묶거나 """..."""로 묶기
t1 = '''hello guys'''
t2 = """good lunch"""
print(t1, t2)

# 여러 줄로 된 문자열 사용
m1 = '''green red
red green
hello buy'''
print(m1)
print("green red\nred green\nhello buy")
m2 = """chicken pork
beef salad
desert""" # 큰따옴표도 똑같은 역할
print(m2)
# 여러 줄로 된 문자열은 큰따옴표나 작은따옴표 3개로 시작해서 3개로 마쳐주면 된다.
# 변수만 지우면? -> 무슨 모양?
"""chicken pork
beef salad
desert""" # 여러줄 주석 <- 실제로는 여러 줄 문자열인데... => 이걸 저장하는 변수나 실행하는 구문 없으므로 주석처럼 쓸 수 있는 것

# 큰따옴표로 묶었을 때, 중간에 큰 따옴표가 들어가면?
# text = "안녕" 안녕" # 따옴표들은 직전 따옴표와 직후 따옴표 간의 문자열을 묶는다고 인식
# text = '이름하여 '파이썬'!' # 2개의 문자열이 있다고 인식
text = "이름하여 '파이썬!'" # 전체적으로 큰따옴표로 묶였기 때문에, 안에 있는 작은 따옴표는 문자열 그 자체로 인식
print(text)
text2 = '큰따옴표("")'
print(text2)
text = "\"" # \" <- 큰따옴표이긴 큰따옴표인데... 큰따옴표 자체가 가지고 있는 문자열을 감싸주는 특수 기능 제거 (이스케이프)
print(text)
# 여러 줄 문자열에서는 작은따옴표나 큰 따옴표가 섞여서 들어가도 상관 없어요
t1 = '''
작은따옴표(')
큰따옴표(")
'''
print(t1)
t2 = """
작은따옴표(')
큰따옴표(")
"""
print(t2)
# 리스트와 튜플
## 리스트 : 1개 이상의 연속된 값들의 묶음
'''
지금까지 배운 변수와 다른 값들 -> 값을 한 개씩 다뤘음
'''
a = 10
b = 20
print(a, b)

# 30개의 숫자를 저장 (1~30)
'''
a1 = 1
a2 = 2
...
a30 = 30
'''

# 리스트(List) : 목록 -> 값을 일렬로 (순서가 있게) 늘어놓은 형태

# 리스트 만들기
'''
* 변수에 값을 저장할 때 [ ](대괄호)로 묶어주면 리스트가 됨. 각 값은 ,(콤마)로 구분
* 리스트 = [값1, 값2, ...]
'''
fruits = ["사과", "배", "귤"]
print(fruits)
numbers = [10, 40, 27]
print(numbers)

# 리스트에 여러 가지 자료형 저장
teacher = ["김강사", 180, 70.9, True]  # 리스트-나열 -> 다 같은 타입이 되도록 제한.
print(teacher) # 파이썬에서의 리스트는 여러 가지 자료형(타입)들을 편하게 넣을 수 있음.

# 빈 리스트 만들기
'''
* 빈 리스트를 만들 때는 [ ] 만 사용하거나, list()를 사용하면 됨.
* 리스트 = []
* 리스트 = list()
'''
a = []
print("a :", a)
b = list()
print("b :", b)

# range를 사용하여 리스트 만들기
'''
range는 연속된 숫자를 생성하는 기능
range(10) # 시작은 0부터 하고, 끝은 입력한 값 직전. (10->9)
0 ~ 9까지의 수의 나열
'''
print(range(10)) # range(n) : 0부터 n 직전까지의 숫자를 생성
# range(0, 10) <- 앞으로 사용 예정일 range로 대기 상태.
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 수를 나열한 리스트를 만들 때
# 리스트 = list(range(횟수)) : 횟수 -> 횟수 - 1의 값까지 숫자를 만들겠다 (0부터 시작해서)

# 시작점과 끝점이 모두 있는 range
r = range(8, 14) # range(시작점, 끝점) : 시작점으로부터 시작하고, 끝점-1까지 반복되는 정수들의 집합
print(r)
print(list(r)) # 8~13까지 연속되는 정수의 리스트를 가지고 싶다?? range(8, 13+1=14) => range(8, 14) => list(...)
# 시작점(포함), 끝점(포함X)

# 시작점, 끝점, 증가폭 range
r2 = range(100, 1000, 100)  # list(range(시작, 끝, 증가폭)) => 증가폭만큼 늘어나면서 숫자 리스트를 생성
print(r2)
print(list(r2)) # [100, 200, 300, 400, 500, 600, 700, 800, 900]
print(list(range(100, 950, 100))) # 끝점을 초과하면 멈추는 개념.

r3 = range(1000, 100, -100) # 증가폭은 음수를 쓸 수 있다
print(list(r3))
r4 = range(1000, 99, -100) # 증가폭은 음수를 쓸 수 있다
print(list(r4))
# 리스트와 튜플
## 리스트 : 1개 이상의 연속된 값들의 묶음
'''
지금까지 배운 변수와 다른 값들 -> 값을 한 개씩 다뤘음
'''
a = 10
b = 20
print(a, b)

# 30개의 숫자를 저장 (1~30)
'''
a1 = 1
a2 = 2
...
a30 = 30
'''

# 리스트(List) : 목록 -> 값을 일렬로 (순서가 있게) 늘어놓은 형태

# 리스트 만들기
'''
* 변수에 값을 저장할 때 [ ](대괄호)로 묶어주면 리스트가 됨. 각 값은 ,(콤마)로 구분
* 리스트 = [값1, 값2, ...]
'''
fruits = ["사과", "배", "귤"]
print(fruits)
numbers = [10, 40, 27]
print(numbers)

# 리스트에 여러 가지 자료형 저장
teacher = ["김강사", 180, 70.9, True]  # 리스트-나열 -> 다 같은 타입이 되도록 제한.
print(teacher) # 파이썬에서의 리스트는 여러 가지 자료형(타입)들을 편하게 넣을 수 있음.

# 빈 리스트 만들기
'''
* 빈 리스트를 만들 때는 [ ] 만 사용하거나, list()를 사용하면 됨.
* 리스트 = []
* 리스트 = list()
'''
a = []
print("a :", a)
b = list()
print("b :", b)

# range를 사용하여 리스트 만들기
'''
range는 연속된 숫자를 생성하는 기능
range(10) # 시작은 0부터 하고, 끝은 입력한 값 직전. (10->9)
0 ~ 9까지의 수의 나열
'''
print(range(10)) # range(n) : 0부터 n 직전까지의 숫자를 생성
# range(0, 10) <- 앞으로 사용 예정일 range로 대기 상태.
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 수를 나열한 리스트를 만들 때
# 리스트 = list(range(횟수)) : 횟수 -> 횟수 - 1의 값까지 숫자를 만들겠다 (0부터 시작해서)

# 시작점과 끝점이 모두 있는 range
r = range(8, 14) # range(시작점, 끝점) : 시작점으로부터 시작하고, 끝점-1까지 반복되는 정수들의 집합
print(r)
print(list(r)) # 8~13까지 연속되는 정수의 리스트를 가지고 싶다?? range(8, 13+1=14) => range(8, 14) => list(...)
# 시작점(포함), 끝점(포함X)

# 시작점, 끝점, 증가폭 range
r2 = range(100, 1000, 100)  # list(range(시작, 끝, 증가폭)) => 증가폭만큼 늘어나면서 숫자 리스트를 생성
print(r2)
print(list(r2)) # [100, 200, 300, 400, 500, 600, 700, 800, 900]
print(list(range(100, 950, 100))) # 끝점을 초과하면 멈추는 개념.

r3 = range(1000, 100, -100) # 증가폭은 음수를 쓸 수 있다
print(list(r3))
r4 = range(1000, 99, -100) # 증가폭은 음수를 쓸 수 있다
print(list(r4))
r5 = range(10, 0, 1) # 10 -> 시작점에서 검사를 해보니까 끝점을 추월해버림.
print(list(r5)) # []

# 튜플 (tuple)
'''
* 리스트처럼 요소(원소, element)들이 있다
* 튜플은 요소를 수정할 수 없음. 읽기 전용 (read-only)
* 리스트가 []라면, 튜플은 ()입니다. -> 각 값은 ,(콤마, 쉼표)로 구분.
* 변수 한 개에 => 여러 값을 (괄호 없이) ,로 구분해서 넣으면 => 역시나 튜플
* 튜플 = (값1, 값2, 값3..)
* 튜플 = 값1, 값2, 값3...
'''
# 숫자가 5개 들어있는 튜플
a1 = (23, 38, 12, 11, 7)
print("a1 :", a1)
a2 = 23, 38, 12, 11, 7
print("a2 :", a2)
a3 = "python", 123, 123.45, True
print("a3 :", a3) # 튜플도 리스트처럼 자료형의 혼합이 가능하다

# range를 사용해서 튜플 만들기
# list(...) => range => list
# tuple(...) => range => tuple
print(tuple(range(1, 100)))
# tuple(range(끝점))
# tuple(range(시작점, 끝점))
# tuple(range(시작점, 끝점, 증가폭))

# tuple을 list로 변환하고, list를 tuple로 변환하고 싶으면?
a = list(range(10)) # [0.... 9]
print(a)
b = tuple(a)
print(b) # (0....9)
c = tuple(range(5, 25, 5))
print(c)
d = list(c)
print(d)

# 리스트와 튜플로 변수 만들기
'''
* 리스트 또는 튜플을 사용하면 변수 여러 개를 한 번에 만들 수 있음
* 이 때 (만들려는) 변수의 개수와 리스트(튜플)의 요소 개수는 같아야 함
'''
l = [1, 2, 3]
a, b, c = l
print("a:", a, "b:", b, "c:", c)
t = ("dog", "cat", "cow", "bird")
d, e, f, g = t
print("d:", d, "e:", e, "f:", f, "g:", g)
d, e, f, g = ("dog", "cat", "cow", "bird") # d, e, f, g = t
d, e, f, g = "dog", "cat", "cow", "bird" # d, e, f, g = t
# 파이썬에서는 왼쪽 변수의 수와 오른쪽 값의 수가 맞으면 한 번에 변수에 값을 대입해줄 수 있다
# unpacking -> tuple unpacking

a, b, c = [1, 2, 3]  # 리스트를 분해해서 각각의 변수에 집어넣는것? : 리스트 언팩킹.

v = 10, 100, 1000 # 튜플 -> 묶어서 넣는 것 -> pack -> packing -> 튜플 패킹
l = [10, 100, 1000] # 리스트 패킹
