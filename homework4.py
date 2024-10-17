# 201
def print_coin():
    print("비트코인")
print_coin()

# 202
print_coin()

# 203
for i in range(0, 100):
    print(i);print_coin()

# 204
def print_coins():
    for i in range(100):
        print("비트코인")
print_coins()

# 205
# 함수 정의 전에 호출했기 때문에

# 206
# A
# B
# C
# A
# B

# 207
# A
# C
# B

# 208
# A
# C
# B
# E
# D

# 209
# B
# A

# 210
# B
# C
# B
# C
# B
# C
# A

################################################################################# 211~220

# 211
# 안녕
# Hi

# 212
# 7
# 15

# 213
# print안의 문자열을 따옴표로 감싸지 않았기때문

# 214
# string와 integer는 더하기 연산을 할 수 없기 때문

# 215
def print_with_smile(문자):
    print(문자+':D')
print_with_smile('A')

# 216
print_with_smile('안녕하세요')

# 217
def print_upper_price(숫자):
    print(int(숫자)*1.3)
print_upper_price(2000)
# 알고보니 int변환을 안해도 되네? 답은 아래
# def print_upper_price(price) :
#     print(price * 1.3)

# 218
def print_sum(숫자1,숫자2):
    print(숫자1 + 숫자2)
print_sum(3, 5)

# 219
def print_arithmetic_operation(x, y):
    print(x, '+', y, '=', x + y)
    print(x, '-', y, '=', x - y)
    print(x, '*', y, '=', x * y)
    print(x, '/', y, '=', x / y)
print_arithmetic_operation(10,5)

# 220
def print_max(x, y, z):
    if x > y:
        if x > z:
            print(x)
        else:
            print(z)
    else:
        if y > z:
            print(y)
        else:
            print(z)
print_max(1, 2, 3)
# 아니 완전 답이 다른데? 답은 아래
# def print_max(a, b, c) :
#     max_val = 0
#     if a > max_val :
#         max_val = a
#     if b > max_val :
#         max_val = b
#     if c > max_val :
#         max_val = c
#     print(max_val)

################################################################################## 221~230

# 221
def print_reverse(string):
    print(string[::-1])
print_reverse('python')

# 222
def print_score(리스트):
    print(sum(리스트)/len(리스트))
print_score([3,3,3,3,3])

# 223
def print_even(리스트):
    for i in 리스트:
        if i%2 == 0:
            print(i)
print_even([1,2,3,4,5])

# 224
# di = {"이름":"김말똥", "나이":30, "성별":0}
# def print_keys(딕셔너리):
#     print(딕셔너리.keys())
# print_keys(di)
# 이거 답 이거나온다
# dict_keys(['이름', '나이', '성별'])
# 근데 이러면 안되고 답은
def print_keys(dic):
    for keys in dic.keys():
        print(keys)

# 225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(딕셔너리, 날짜):
    if 날짜 in 딕셔너리:
        print(딕셔너리[날짜])
print_value_by_key  (my_dict, "10/26")
# 사실은 엄청 엄청 간단했다. 답은
# def print_value_by_key (my_dict, key) :
#     print(my_dict[key])

# 226 어렵다어렵다어렵다어렵다어렵다어렵다어렵다어렵다어렵다어렵다어렵다어렵다어렵다어렵다어렵다어렵다어렵다어렵다어렵다어렵다어렵다
girl = "아이엠어보이유알어걸"
# def print_5xn(string):
#     for i in string:
#         print(i, end='')
#         if i%5 == 0:
#             print('\n')
# 내 코드는 택도 없었고, 답은 이건데 내 기준 어려웠다
def print_5xn(line):
    chunk_num = int(len(line) / 5)
    for i in range(chunk_num + 1) :
        print(line[i * 5: i * 5 + 5])
print_5xn(girl)

# num = 2
# for 0 in range(2+1):
#     print(line[0: 5])
# for 1 in range(2+1):
#     print(line[5: 10])
# for 2 in range(2+1):
#     print(line[10: 15])

# 227
def print_mxn(string, num):
    chunk_num = int(len(string)/num)
    for i in range(chunk_num+1):
        print(string[i * num: i * num + num])
print_mxn("아이엠어보이유알어걸", 3)


# 228
def calc_monthly_salary(annual_salary):
    print(round(annual_salary/12))
# 답은 아래건데, 내거는 답 안되려나?
# def calc_monthly_salary(annual_pay) :
#     monthly_pay = int(annual_pay / 12)
#     print(monthly_pay)
calc_monthly_salary(12030301)

# 229
# 타입에러가 날줄 알았는데 아니었다.
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)
my_print(a=100, b=200)
# 답은
# 왼쪽: 100
# 오른쪽: 200

# 230
# 왼쪽: 200
# 오른쪽: 100

##################################################################################### 231~240

# 231
# 4
# 틀렸고 답은 에러

# 232
def make_url(string):
    string = 'www.'+string+'.com'
    return string
make_url('naver')
# 이렇게 하면 된다는데 왜 return이 안될까. 파이참 문제인지 뭔지.

# 233
def make_list(string):
    return list(string)
make_list('abcd')

# 234
def pickup_even(li):
    temp = []
    for i in li:
        if i%2 == 0:
            temp.append(i)
    return temp
pickup_even([3, 4, 5, 6, 7, 8])

# 235
def convert_int(string):
    string = string.replace(',', '')
    return int(string)
convert_int("1,234,567")

# 236
# 22

# 237
# 22

# 238
# 140

# 239
# 16

# 240
# 28

################################################################################################ 문제

# 1
# 받은 문자열을 역순으로 한글자씩 리스트에 넣어 반환하는 함수 new_string(x) 만들

# 2
# 인풋을 받아 딕셔너리 value 중 매치하는 값이 있으면 그의 key값을 출력하는 함수 find_key(x) 만들
# 딕셔너리 = {'abc':[100,200,300], 'efg':[500,600,700], 'hij':[100,1000,10000]}
# find_key(100)

# 3
# 하나의 문자열과 100이하의 숫자를 입력받아 입력받은 숫자만큼 문자열을 출력하는 함수 mul_string(x, y) 만들

# 4
# 리스트의 맨 앞에 주어진 변수를 추가하는 함수 add_element(리스트, 변수) 만들

# 5
# 주어진 문자열을 주어진 변수로 split하는 spliting(문자열, 변수) 만들