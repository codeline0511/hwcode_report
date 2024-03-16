def get_radius(prompt):
    print('\n반지름의 값을 한번 더 입력해주세요.')
    r = int(input(prompt))
    return r

def get_circle_area(n):
    value = n * n * 3.14
    return value

a = '넓이를 구하고자 하는 원의 반지름은?'
result = get_radius(a)
b = get_circle_area(result)
print('반지름이', result, '인 원의 넓이 = 3.14 *', result,'*', result,'=', b)
