# a.remove('가')
# del b[1]
# print(a, b)
#
# a.append('마')
# b[5] = '마'
# print(a,b)





# new = ('a','c','d')
# t = new





# print(f'{l[1]}가 {d[4]}을 좋아한다')





# score = input("score: ")
# score = int(score)
#
# if score < 0 or score > 100:
#     print("0에서 100 사이의 값을 입력하세요")
# else:
#     if 81 <= score <= 100:
#         print("grade is A")
#     elif 61 <= score <= 80:
#         print("grade is B")
#     elif 41 <= score <= 60:
#         print("grade is C")
#     elif 21 <= score <= 40:
#         print("grade is D")
#     else:
#         print("grade is E")







# weights = {
#     0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7,
#     6: 8, 7: 9, 8: 2, 9: 3, 10: 4, 11: 5
# }
#
# num = input("주민등록번호: ")
#
# cleaned_num = num.replace("-", "")
#
# num_list = [int(digit) for digit in cleaned_num]
#
# calc_sum = 0
#
# calc_sum = (
#     num_list[0] * weights[0] + num_list[1] * weights[1] +
#     num_list[2] * weights[2] + num_list[3] * weights[3] +
#     num_list[4] * weights[4] + num_list[5] * weights[5] +
#     num_list[6] * weights[6] + num_list[7] * weights[7] +
#     num_list[8] * weights[8] + num_list[9] * weights[9] +
#     num_list[10] * weights[10] + num_list[11] * weights[11]
# )
#
# remainder = calc_sum % 11
# check_digit = 11 - remainder
#
# if check_digit == num_list[12]:
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")
