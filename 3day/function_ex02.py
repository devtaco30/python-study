input_num = int(input('1 이상 10 이하의 정수 1개를 입력하세요: '))
korean_num_list = ['일','이','삼','사','오','육','칠','팔','구','십']


# print(korean_num_list[input_num + 1])

def korean_number(num):
    return korean_num_list[num - 1]

print(korean_number(input_num))



    