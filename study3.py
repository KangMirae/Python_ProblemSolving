ex_li = ['안녕', '미래']
ex_dic = {'age': 11, 'name': '미란'}
ex_dic2 = {'age1': 20, 'age2': 30}
ex_str = 'python'

# 1. 문자열이 들어있는 리스트를 입력받아 문자열로 바꾸어 출력하는 함수를  작성하라
# print_strlist(["안녕", "미래"])
# 안녕 미래
def print_strlist(li):
    print(' '.join(li))
print_strlist(ex_li)

# 2. 숫자하나(단)를 입력받아 구구단을 출력하는 함수를 작성하라
def mul_table(숫자):
    for i in range(1, 10):
        print(숫자, 'x', i, '=', i*int(숫자))
mul_table(2)

# 3. 딕셔너리를 입력받아 value만 출력하는 함수를 작성하라
def print_val(dic):
    for i in dic:
       return dic[i]
print_val(ex_dic)

# 4. 문자열을 입력받아 'i'가 있는지 없는지 true, false를 반환하는 함수를 작성하라
# return_bool_i("python")
# false
def return_bool_i(str):
    return 'i' in str
# return_bool_i("python")
print(return_bool_i("pithon"))

# 5. 다음 딕셔너리를 입력받아 합계를 리턴하는 함수를 작성하라 #########################################################################
#
# op_sum({age1: 20, age2: 30})
#
# 50
def print_sum(dict1):
    temp = sum(dict1.values())
    print(temp)
print_sum(ex_dic2)

# 1
# 받은 문자열을 역순으로 한글자씩 리스트에 넣어 반환하는 함수 new_string(x) 만들
def new_string(x):
    li = list(x[::-1])
    print(li)
new_string(ex_str)

# 2 ###############################################################################################
# 딕셔너리 value 중 매치하는 값이 있으면 그의 key값을 출력하는 함수 find_key(x) 만들
딕셔너리 = {'abc':[100,200,300], 'efg':[500,600,700], 'hij':[100,1000,10000]}
def find_key(x):
    for i,j in 딕셔너리.items():
        if x in j:
            print(i)
find_key(100)

# 3
# 하나의 문자열과 100이하의 숫자를 입력받아 입력받은 숫자만큼 문자열을 출력하는 함수 mul_string(x, y) 만들
def mul_string(x, y):
    print(x*y)
mul_string('안녕', 3)

# 4
# 리스트의 맨 앞에 주어진 변수를 추가하는 함수 add_element(리스트, 변수) 만들
def add_element(리스트, 변수):
    리스트.insert(0, 변수)
add_element(ex_li, '변수')
print(ex_li)

# 5
# 주어진 문자열을 주어진 변수로 split하는 spliting(문자열, 변수) 만들
def spliting(문자열, 변수):
    temp = 문자열.split(변수)
    print(temp)
spliting(ex_str, 'y')