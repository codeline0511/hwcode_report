def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(n):
    value = n * n * 3.14
    return value

a = '넓이를 구하고자 하는 원의 반지름은?'
result = get_radius(a)
b = get_circle_area(result)
print('반지름이', result, '인 원의 넓이 = 3.14 *', result,'*', result,'=', b)
