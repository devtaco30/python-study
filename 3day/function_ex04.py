
def korean_age(x) :
    from datetime import datetime
    today = datetime.today()
    return today.year - x + 1

print('User의 나이는 ', korean_age(int(input('태어난 해를 입력하세요: '))), '세 입니다')