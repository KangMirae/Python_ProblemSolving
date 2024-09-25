# print("Hello World")
from dataclasses import replace
from mailcap import subst
from operator import index

# print("Mary's cosmetics")

# print('''신씨가 소리질렀다. "도둑이야".''')

# print("C:\\Windows")

# print("안녕하세요.\n만나서\t\t반갑습니다.")
# \n은 줄바꿈, \t는 Tab

# print ("오늘은", "일요일")
# 콤마를 기점으로 한 칸 띄어쓰기 됨

# print('naver;kakao;sk;samsung')

# print('naver', 'kakao', 'sk', 'samsung', sep='/')

# print("first", end='');print("second")

# print(5/3)







# 11~20 -----------------------------------------------

# samsung = 50000
# print(10*samsung)


# cap = 298000000000000
# price = 50000
# per = 15.79
# print(cap, price, per, sep=', ')


# s = "hello"
# t = "python"
# print(s, t, sep='! ')


# print(2 + 2 * 3)
# 결과값 8


# a = "132"
# print(type(a))
# 타입값 String


# num_str = "720"
# num_str = int(num_str)
# print(type(num_str))


# num = 100
# num = str(num)
# print(type(num))


# a = "15.79"
# a = float(a)
# print(type(a))


# year = "2020"
# year = int(year)
# print(year-1, year-2, year-3)


# monthly_pay = 48584
# total_months = 36
# print(monthly_pay*total_months)



# 21~30 --------------------------------------------------------

# letters = 'python'
# print(letters[0], letters[2])


# license_plate = "24가 2210"
# print(license_plate[4:8])


# string = "홀짝홀짝홀짝"
# print(string[0], string[2], string[4], sep='')


# string = "PYTHON"
# print(string[-1:0])
# 못풀었음 정답은 print(string[::-1])


# phone_number = "010-1111-2222"
# print(phone_number.replace('-',' '))


# phone_number = "010-1111-2222"
# print(phone_number.replace('-',''))


# url = "http://sharebook.kr"
# print(url[-2:])


# lang = 'python'
# lang[0] = 'P'
# print(lang)
# 결과값 Python -> 틀렸음 문자열은 수정할 수 없음


# string = 'abcdfe2a354a32a'
# print(string.replace('a', 'A'))



# string = 'abcd'
# string.replace('b', 'B')
# print(string)
# 결과값 aBcd -> 역시나 틀렸음 젠장





# 31~40 ------------------------------------------------

# a = "3"
# b = "4"
# print(a + b)
# 결과값 34


# print("Hi" * 3)
# 결과값 HiHiHi


# print('-'*80)


# t1 = 'python'
# t2 = 'java'
# t3 = t1 + ' ' + t2 + ' '
# print(t3*4)


# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
#
# string1 = '이름: %s 나이: %i' %(name1, age1)
# string2 = '이름: %s 나이: %i' %(name2, age2)
# print(string1, string2, sep='\n')


# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
#
# string1 = '이름: {0} 나이: {1}'.format(name1, age1)
# string2 = '이름: {0} 나이: {1}'.format(name2, age2)
# print(string1, string2, sep='\n')



# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print(f'이름: {name1} 나이: {age1}')
# print(f'이름: {name2} 나이: {age2}')



# 상장주식수 = "5,969,782,550"
# print(type(int(상장주식수.replace(',',''))))


# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])


# data = "   삼성전자    "
# print(data.strip(' '))







# 41~50 =======================================================================

# ticker = "btc_krw"
# print(ticker.upper())



# ticker = "BTC_KRW"
# print(ticker.lower())


# string ='hello'
# print(string.capitalize())


# file_name = "보고서.xlsx"
# print(file_name.endswith('xlsx'))


# file_name = "보고서.xlsx"
# print(file_name.endswith(('xlsx', 'xls')))


# file_name = "2020_보고서.xlsx"
# print(file_name.startswith('2020'))


# a = "hello world"
# print(a.split(' '))



# ticker = "btc_krw"
# print(ticker.split('_'))


# date = "2020-05-01"
# year = date.split('-')[0]
# month = date.split('-')[1]
# day = date.split('-')[2]
# print(f'연도:{year} 월:{month} 일:{day}')


# data = "039490     "
# print(data.rstrip(' '))





# 51~60 ===================================================================


# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# print(movie_rank)



# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# movie_rank.append('배트맨')
# print(movie_rank)



# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, '슈퍼맨')
# print(movie_rank)



# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank.remove('럭키')
# print(movie_rank)



# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# movie_rank.remove('스플릿')
# movie_rank.remove('배트맨')
# print(movie_rank)
# 틀림 -> 정답은 del movie_rank[2]


# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# langs = lang1 + lang2
# print(langs)



# nums = [1, 2, 3, 4, 5, 6, 7]
# print(f'max: {max(nums)}')
# print(f'min: {min(nums)}')



# nums = [1, 2, 3, 4, 5]
# print(sum(nums))


# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook))



# nums = [1, 2, 3, 4, 5]
# print(sum(nums)/len(nums))







# 61~70 ========================================================


# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])



# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])


# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])



# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0], interest[2])



# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(' '.join(interest))


# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print('/'.join(interest))


# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print('\n'.join(interest))


# string = "삼성전자/LG전자/Naver"
# interest = string.split('/')
# print(interest)


# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)

