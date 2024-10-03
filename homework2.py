from calendar import calendar


# 71
# my_variable = ()

# 72
# movie_rank = ('닥터 스트레인지', '스플릿', '럭키')

# 73
# one = (1, )

# 74
# t = (1, 2, 3)
# t[0] = 'a'
# 튜플은 수정 불가능한 자료구조이기 때문에

# 75
# t = 1, 2, 3, 4
# t의 데이터 타입은 리스트이다
# -> 틀림, 튜플은 괄호안에 적지 않아도 됨

# 76
# t = ('a', 'b', 'c')
# r = ('A', 'b', 'c')
# t = r
# print(t)

# 77
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# interest = [interest[0], interest[1], interest[2]]
# print(type(interest))
# -> 틀림 답은
# data = list(interest)

# 78
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# data = tuple(interest)
# print(type(data))

# 79
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)
# a에는 apple, b에는 banana, c에는 cake

# 80 -> 모르겠음
# data = tuple(range(2,100,2))
# print(data)

# 81~90 =================================================================================

# 81
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a, b, *valid_score = tuple(scores)
# print(a); print(b); print(valid_score)
# 틀림 문제는 좌측부터 저장임. 고로 답은
#
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, _, _= scores
# print(valid_score)


# 82
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# _, _, *valid_score = scores
# print(valid_score)


#83
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# _, *valid_score, _= scores
# print(valid_score)


# 84
# temp = {}
# 그러니까 정리하자면 1. 리스트 [] / 2. 튜플 () / 3. 딕셔너리 {}


# 85
# 메로나, 폴라포, 빵빠레 = {1000, 1200, 1800}
# print(메로나); print(폴라포); print(빵빠레)
# 틀림. 해보니 메로나1000 폴라포 1800 빵빠레 1200 으로 나옴. 이유는 당연히 모름. 답은
# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# print(ice)


# 86
# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# ice = {'죠스바': 1200, '월드콘': 1500}
# print(ice)
# 위의 답은 틀림. 이렇게 되면 ice딕셔너리를 overwrite하게 됨
# 답은
# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# ice["죠스바"] = 1200
# ice["월드콘"] = 1500
# print(ice)


# 87
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# print(f"메로나 가격 : {ice['메로나']}")


# 88
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# ice['메로나'] = 1300
# print(ice)


# 89
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# ice['메로나'] = 0
# print(ice)
# 틀림. 답은
# del ice["메로나"]
# print(ice)


# 90
# 해당 딕셔너리에 '누가바' key가 존재하지 않기 때문



# 91~100 ===================================================================

# 91
# inventory = {"메로나": (300,20), "비비빅": (400,3), "죠스바": (250, 100)}
# print(inventory)
# 틀림, value 값을 묶을땐 []Square Brackets를 사용
# inventory = {"메로나": [300, 20],
#              "비비빅": [400, 3],
#              "죠스바": [250, 100]}
# print(inventory)



# 92
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# print(f'{inventory["메로나"][0]} 원')


# 93
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# print(f'{inventory["메로나"][1]} 개')



# 94
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# inventory['월드콘'] = [500,7]
# print(inventory)


# 95
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# ice = [icecream.keys()]
# print(ice)
# 틀림
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# ice = list(icecream.keys())
# print(ice)


# 96
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# ice = list(icecream.values())
# print(ice)


# 97
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# total = sum(icecream.values())
# print(total)


# 98
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# icecream = new_product
# print(icecream)
# 틀림.
# 답은
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# icecream.update(new_product)
# print(icecream)



# 99
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# result = {keys[0]: vals[0], keys[1]: vals[1], keys[2]: vals[2]}
# print(result)
# 답은 나왔는데 틀림. 답은
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# result = dict(zip(keys, vals))
# print(result)



# 100
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# close_table = dict(zip(date, close_price))
# print(close_table)



# 101~110 ============================================================

# 101
# boolean
# 틀림 답은 bool


# 102
# print(3 == 5)
# False


# 103
# print(3 < 5)
# True



# 104
# x = 4
# print(1 < x < 5)
# True



# 105
# print ((3 == 3) and (4 != 3))
# True



# 106
# print(3 => 4)
# print(3 >= 4)



# 107
# if 4 < 3:
#     print("Hello World")
# 아무일도 일어나지 않음


# 108
# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")
# Hi, there. 가 출력됨


# 109
# if True :
#     print ("1")
#     print ("2")
# else :
#     print("3")
# print("4")
# 1
# 2
# 틀림, 답은
# 1
# 2
# 4



# 110
# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")
# 3
# 5



# 111~120 ====================================================================

# 111
# string = input('문자열 입력: ')
# print(string)
# 틀렸네. input을 받으면 바로 출력되지 않나봐
# 답은
# print(string * 2)


# 112
# number = input('숫자 입력: ')
# print(int(number)+10)



# 113
# number = int(input('숫자 입력: '))
# if number%2 == 0:
#     print('짝수')
# else:
#     print('홀수')


# 114
# number = int(input('숫자 입력: '))
# if number <= 235:
#     print(number+20)
# else:
#     print(255)


# 115
# number = int(input('숫자 입력: '))
# number = number-20
# if 0 <= number <= 255:
#     print(number)
# else:
#     if number < 0:
#         print(0)
#     else:
#         print(255)



# 116
# string = input('현재 시간: ')
# minute = int(string[-2:])
# if minute > 0:
#     print("정각이 아닙니다")
# else:
#     print("정각입니다")


# 117
# fruit = ["사과", "포도", "홍시"]
# string = input('좋아하는 과일은? ')
# if string in fruit:
#     print('정답입니다')
# else:
#     print('오답입니다')



# 118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# string = input('종목명: ')
# if string in warn_investment_list:
#     print('투자 경고 종목입니다')
# else:
#     print('투자 경고 종목이 아닙니다.')




# 119
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# string = input('제가좋아하는계절은: ')
# if string in fruit.keys():
#     print('정답입니다')
# else:
#     print('오답입니다')
# 값은 나오는데... 답은
# if string in fruit:
# 라고만 해도 됨.


# 120
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# string = input('제가좋아하는과일은: ')
# if string in fruit.values():
#     print('정답입니다')
# else:
#     print('오답입니다')



# 121~130 =================================================================


# 121
# character = input('문자 입력: ')
# if character.islower():
#     print(character.upper())
# else:
#     print(character.lower())


# 122
# score = int(input('성적 입력: '))
# grade = 'E'
# if score > 80:
#     grade = 'A'
# elif score > 60:
#     grade = 'B'
# elif score > 40:
#     grade = 'C'
# elif score > 20:
#     grade = 'D'
# print(f'grade is {grade}')


# 123
# string = input('금액과 통화명: ')
# 구분자 = list(string.split(' '))
# price = int(구분자[0])
# if 구분자[1] == "달러":
#     price = price * 1167
# elif 구분자[1] == "엔":
#     price = price * 1.096
# elif 구분자[1] == "유로":
#     price = price * 1268
# elif 구분자[1] == "위안":
#     price = price * 171
# print(f'{price} 원')
#
# 답은 나왔는데 딕셔너리를 이용한게 정답이네. 그래서 답은,
# 환율 = {"달러": 1167,
#         "엔": 1.096,
#         "유로": 1268,
#         "위안": 171}
# user = input("입력: ")
# num, currency = user.split()
# print(float(num) * 환율[currency], "원")



# 124
# input1 = int(input("number1: "))
# input2 = int(input("number2: "))
# input3 = int(input("number3: "))
# print(max(input1, input2, input3))
# 내 답이 더 쉬운것 같은데 그래도 답은,
# num1 = input("input number1: ")
# num2 = input("input number2: ")
# num3 = input("input number3: ")
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)
#
# if num1 >= num2 and num1 >= num3:
#     print(num1)
# elif num2 >= num1 and num2 >= num3:
#     print(num2)
# else:
#     print(num3)



# 125
# 휴대폰통신사 = {"011": "SKT", "016": "KT", "019": "LGU", "010": "알수없음"}
# user = input("휴대전화번호 입력: ")
# 앞자리 = user[:3]
# if 앞자리 in 휴대폰통신사 :
#     print(f'당신은 {휴대폰통신사[앞자리]} 사용자입니다.')



# 126
# string = input('우편번호: ')
# integer = int(string[2])
# if integer < 3:
#     print('강북구')
# elif integer < 6:
#     print('도봉구')
# else:
#     print('노원구')



# 127
# string = input('주민등록번호: ')
# if string[7] == '1' or string[7] == '3':
#     print("남자")
# else:
#     print("여자")



# 128
# string = input('주민등록번호: ')
# if int(string[8:10]) < 9:
#     print('서울 입니다.')
# else:
#     print('서울이 아닙니다.')



# 129
# string = input('주민등록번호: ')
# 유효성검사 = [2,3,4,5,6,7,0,8,9,2,3,4,5]
# 주민번호 = list(string)
# print(f'주민번호: {주민번호}')
# user = dict(zip(유효성검사,주민번호))
# print(user)
# 여기까지 했는데 왜 안될까. 정답 보러감.
# 이런 노가다를 왜하지?
# num = input("주민등록번호: ")
# 계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
#         int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
#         int(num[11])* 4 + int(num[12]) * 5
# 계산2 = 11 - (계산1 % 11)
# 계산3 = str(계산2)
#
# if num[-1] == 계산3[-1]:
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")


# 130
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# 비교값 = int(btc['opening_price']) + (int(btc['max_price']) - int(btc['min_price']))
# if 비교값 >= int(btc['max_price']) :
#     print('상승장')
# else:
#     print('하락장')
# 틀림. 기본적으로 integer를 안쓰네.
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#
# 변동폭 = float(btc['max_price']) - float(btc['min_price'])
# 시가 = float(btc['opening_price'])
# 최고가 = float(btc['max_price'])
#
# if (시가+변동폭) > 최고가:
#     print("상승장")
# else:
#     print("하락장")



# =======================================================================

# 문제 1
a = ['가', '나', '다', '라']
b = {1:'가', 2:'나', 3:'다', 4:'라'}
# a와 b의 '가'를 삭제하고 '마'를 추가하라


# 문제 2
t = ('b','c','d')
# t의 원소 'b'를 'a'로 대체하라


# 문제 3
d = {1: '봄', 2: '여름', 3: '가을', 4: '겨울'}
l = ['하니', '민지', '해린', '다니엘', '혜인']
# 딕셔너리와 리스트의 원소를 이용해 "민지가 겨울을 좋아한다" 를 출력하라


# 문제 4
# 문제 122번에 점수 범위에 있지 않은 숫자를 걸러내는 예외처리를 하라.


# 문제 5
# 문제 129번을 딕셔너리와 리스트를 이용하여 다시 풀어본다면?
weights = {
    0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7,
    6: 8, 7: 9, 8: 2, 9: 3, 10: 4, 11: 5
}
num = input("주민등록번호: ")
cleaned_num = num.replace("-", "")
num_list = [int(digit) for digit in cleaned_num]
# 이를 이용하여 풀이
