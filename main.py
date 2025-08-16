import random

Reset = '\033[0m'
Red = '\033[31m'

num = random.random() * 6

final_num = round(num, 0)

print(f'Your randomised die number is {Red} {final_num} {Reset}')
