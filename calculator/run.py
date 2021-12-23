print('Instructions:\n+ plus \n- minus \n* multiplication  \n/ division \n** degree')
from calculator import f, a, b, c
with open('Result.txt', 'w') as u:
    u.write("" + str(a) + " " + str(c) + " " + str(b) + " = " + str(f(a, b)))