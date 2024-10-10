# 131
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)

# 132
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#   print("#####")

# 133
# for 변수 in ["A", "B", "C"]:
#   print(변수)
#
# li = ["A", "B", "C"]
# for 변수 in li:
#     print(변수)

# 134
# for 변수 in ["A", "B", "C"]:
#   print("출력:", 변수)
#
# print("출력: A")
# print("출력: B")
# print("출력: C")

# 135
# for 변수 in ["A", "B", "C"]:
#   b = 변수.lower()
#   print("변환:", b)
#
# print("변환:", "A".lower())
# print("변환:", "B".lower())
# print("변환:", "C".lower())

# 136
# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)
#
# for 변수 in [10,20,30]:
#     print(변수)

# 137
# print(10)
# print(20)
# print(30)
#
# for 변수 in [10,20,30]:
#     print(변수)

# 138
# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")
#
# for 변수 in [10,20,30]:
#     print(변수);print("-------")

# 139
# print("++++")
# print(10)
# print(20)
# print(30)
#
# print("++++")
# for 변수 in [10,20,30]:
#     print(변수)

# 140
# print("-------")
# print("-------")
# print("-------")
# print("-------")
#
# for 변수 in [1,2,3,4]:
#     print("-------")

# ---------------------------------------------------------------------------------141~150

# 141
# 부가세 = 10
# 리스트 = [100, 200, 300]
# for 변수 in 리스트:
#     print(변수+부가세)

# 142
# 리스트 = ["김밥", "라면", "튀김"]
# for 변수 in 리스트:
#     print("오늘의 메뉴:", 변수)

# 143
# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# for 변수 in 리스트:
#     print(len(변수))

# 144
# 리스트 = ['dog', 'cat', 'parrot']
# for 변수 in 리스트:
#     print(변수, len(변수))

# 145
# 리스트 = ['dog', 'cat', 'parrot']
# for 변수 in 리스트:
#     print(변수[0])

# 146
# 리스트 = [1, 2, 3]
# for 변수 in 리스트:
#     print("3 x", 변수)

# 147
# 리스트 = [1, 2, 3]
# x = 3
# for 변수 in 리스트:
#     print(f'{x} x {변수} = {x*변수}')

# 148
# 리스트 = ["가", "나", "다", "라"]
# for 변수 in 리스트[1:]:
#     print(변수)

# 149
# 리스트 = ["가", "나", "다", "라"]
# for 변수 in 리스트[::2]:
#     print(변수)

# 150
# 리스트 = ["가", "나", "다", "라"]
# for 변수 in 리스트[::-1]:
#     print(변수)

# -------------------------------------------------------------------151~160

# 151
# 리스트 = [3, -20, -3, 44]
# for 변수 in 리스트:
#     if 변수 < 0:
#         print(변수)

# 152
# 리스트 = [3, 100, 23, 44]
# for 변수 in 리스트:
#     if 변수%3 == 0:
#         print(변수)

# 153
# 리스트 = [13, 21, 12, 14, 30, 18]
# for 변수 in 리스트:
#     if 20 > 변수:
#         if 변수%3 == 0:
#             print(변수)
# 코드 간소화. 답은
# 리스트 = [13, 21, 12, 14, 30, 18]
# for 변수 in 리스트:
#   if (변수 < 20) and (변수 % 3 == 0):
#     print(변수)

# 154
# 리스트 = ["I", "study", "python", "language", "!"]
# for 변수 in 리스트:
#     if len(변수) >= 3:
#         print(변수)

# 155
# 리스트 = ["A", "b", "c", "D"]
# for 변수 in 리스트:
#     if 변수.isupper():
#         print(변수)

# 156
# 리스트 = ["A", "b", "c", "D"]
# for 변수 in 리스트:
#     if 변수.islower():
#         print(변수)

# 157
# 리스트 = ['dog', 'cat', 'parrot']
# for 변수 in 리스트:
#     변수[0].upper()
#     print(변수)
# 이렇게하면 틀림. 소문자로만 나옴. 답은,
# 리스트 = ['dog', 'cat', 'parrot']
# for 변수 in 리스트:
#     첫글자 = 변수[0]              # 1)
#     대문자 = 첫글자.upper()     # 2)
#     print(대문자 + 변수[1:])      # 3)
# 혹은
# for 변수 in 리스트:
#   print(변수[0].upper() + 변수[1:])

# 158
# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# for 변수 in 리스트:
#     새변수 = 변수.split('.')
#     print(새변수[0])
# 답은 나오지만 아래걸 또 해봤는데
# for 변수 in 리스트:
#     print(변수.split('.')[0])
# 답이 또 나왔다.

# 159
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for 변수 in 리스트:
#     새리스트 = 변수.split('.')
#     if 새리스트[1] == 'h':
#         print(변수)

# 160
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for 변수 in 리스트:
#     새리스트 = 변수.split('.')
#     if (새리스트[1] == 'h') or (새리스트[1] == 'c'):
#         print(변수)

# -----------------------------------------------------------------------------161~170

# 161
# for i in range(100):
#     print(i)

# 162
# for i in range(2002, 2051, 4):
#     print(i)

# 163
# for i in range(3, 31, 3):
#     print(i)

# 164
# for i in range(99, -1, -1):
#     print(i)
# 답은 나왔는데, 원래는 이거라네
# for i in range(100):
#     print(99 - i)
# 말이 되네

# 165
# for i in range(10):
#     print(f'0.{i}')
# 헉 답은 이거였음
# for num in range(10) :
#     print(num / 10)
# 이건 좀.. 나에겐 너무 수학적인걸..

# 166
# for i in range(1, 10):
#     print(f'3x{i} = {i*3}')

# 167
# for i in range(1, 10):
#     if i%2 != 0 :
#         print(f'3x{i} = {i*3}')
# 또 다른 답은,
# num = 3
# for i in range(1, 10, 2) :
#     print (num, "x", i, " = ", num * i)

# 168
# s = 0
# for i in range(1, 11):
#     s += i
# print(s)

# 169
# s = 0
# for i in range(1, 11, 2):
#     s += i
# print(s)

# 170
# s = 1
# for i in range(1, 11):
#     s *= i
# print(s)

# -------------------------------------------------------------- 171~180

# 171
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(price_list[i])

# 172
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(i, price_list[i])

# 173
# price_list = [32100, 32150, 32000, 32500]
# l = len(price_list)
# for i in range(len(price_list)):
#     l-=1
#     print(l, price_list[i])
# 흠... 답은..
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print((len(price_list) - 1) - i, price_list[i])

# 174
# price_list = [32100, 32150, 32000, 32500]
# j = 100
# for i in range(len(price_list)-1):
#     print(j, price_list[i+1])
#     j+=10
# 답은 이거라는데, 진짜 왜 이렇게 해야하는건지
# for i in range(1, 4):
#     print(90 + 10 * i, price_list[i])

# 175
# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list)-1):
#     print(my_list[i], my_list[i+1])

# 176
# my_list = ["가", "나", "다", "라", "마"]
# for i in range(len(my_list)-2):
#     print(my_list[i], my_list[i+1], my_list[i+2])

# 177
# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list), 1, -1):
#     print(my_list[i-1], my_list[i-2])
# 다른 답은,
# for i in range(len(my_list) - 1, 0, -1):
#     print(my_list[i], my_list[i-1])

# 178
# my_list = [100, 200, 400, 800]
# for i in range(len(my_list)-1):
#     print(my_list[i+1]- my_list[i])

# 179
# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(len(my_list)-2):
#     print((my_list[i]+my_list[i+1]+my_list[i+2])/3)
# 답은 이거래.
# for i in range(1, len(my_list) - 1):
#     print(abs(my_list[i-1] + my_list[i] + my_list[i+1]) / 3)

# 180
# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# volatility = []
# for i in range(len(low_prices)):
#     volatility.append(high_prices[i]-low_prices[i])
# print(volatility)

# ---------------------------------------------------------------------------------------181~190

# 181
# apart =[[101,102], [201,202], [301,302]]
# print(apart)

# 182
# stock = [[100,200,300],[80,210,330]]
# print(stock)

# 183
# stock = {'시가':[100,200,300], '종가':[80,210,330]}
# print(stock)

# 184
# stock = {'10/10':[80,110,80,90], '10/11':[210,230,190,200]}
# print(stock)

# 185
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart:
#     for j in i:
#         print(j,'호')

# 186
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart[::-1]:
#     for j in i:
#         print(j, '호')

# 187
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart[::-1]:
#     for j in i[::-1]:
#         print(j, '호')

# 188
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart:
#     for j in i:
#         print(j,'호')
#         print('-----')

# 189
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart:
#     for j in i:
#         print(j,'호')
#     print('-----')

# 190
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart:
#     for j in i:
#         print(j,'호')
# print('-----')

# -------------------------------------------------------------------------191~200

# 191~194
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

# 191
# charge = 0.014
# for i in data:
#     for j in i:
#         temp = (j*charge)/100
#         print(j + temp)
# 이것의 답은 간단하게 이것이었음
# for line in data:
#     for column in line:
#         print(column * 1.00014)

# 192
# for line in data:
#     for column in line:
#         print(column * 1.00014)
#     print('----')

# 193
# result = []
# for line in data:
#     for column in line:
#         result.append(column * 1.00014)
# print(result)

# 194
# result = []
# for line in data:
#     temp = []
#     for column in line:
#         temp.append(column * 1.00014)
#     result.append(temp)
# print(result)

# 195~
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

# 195
# 못풀었음. 사실 굉장히 쉬운문제였군..
# for row in ohlc[1:]:
#     print(row[3])

# 196
# for row in ohlc[1:]:
#     if row[3] > 150:
#         print(row[3])

# 197
# for row in ohlc[1:]:
#     if (row[3] >= row[0]):
#         print(row[3])

# 198
# volatility = []
# for row in ohlc[1:]:
#     volatility.append(row[1] - row[2])
# print(volatility)

# 199
# for row in ohlc[1:]:
#     if (row[3] > row[0]):
#         print(row[1]-row[2])

# 200
# s = 0
# for row in ohlc[1:]:
#     s += (row[0] - row[3])
# print('총 수익금:', s)


# ===========================================================================================

# 1
# 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라. 단 부가세는 금액의 10%로 가정한다.
# 리스트 = [100, 200, 300, 400, 500]
#
# 2
# for 문과 분기문을 사용하여 오늘메뉴에 '토스트'가 있는지 확인하고 있으면 '오예'를 출력하라.
# 오늘메뉴 = ['흑미밥', '코다리조림', '감자채볶음', '소고기무국', '토스트', '요구르트']
#
# 3
# 다음 리스트를 활용하여 아래와 같이 출력하라. 단 for문을 사용할 것.
# 애국가 = ['동해물과', '백두산이', '마르고', '닳도록', '하느님이보우하사우리나라만세']
#
# 출력 예시)
# 물과
# 산이
# 고
# 록
# 님이보우하사우리나라만세
#
# 4
# 1~100까지의 숫자 중 4의 배수의 합을 출력하는 프로그램을 for 문과 range 함수를 사용하여 작성하라.
#
# 5
# for 문을 이용하여 다음 이차원리스트에서 국에 해당하는 메뉴만 출력하라.
# 메뉴 = [['디저트', '국', '찌개'],
#         ['화채', '김칫국', '된장찌개'],
#         ['소보로빵', '버섯국', '김치찌개'],
#         ['푸딩', '미역국', '고추장찌개'],
#         ['에끌레어', '육개장', '참치찌개']]