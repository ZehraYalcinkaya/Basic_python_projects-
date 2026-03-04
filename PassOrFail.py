def pass_fail(score):
     if score > 50:
        print('PASSED')

     elif score < 50:
        print('FAİLED')

     else :
        print('Narrowly PASSED')



point = float(input('Enter what you got from exam: '))
pass_fail(point)
