'''
문제 7] 아래와 같은 패턴의 별(*)을 출력하는 프로그램을 작성해 보세요.

    *
   ***
  *****
 *******
*********

'''

for i in range(0,6):
    print(' '* (5-i)+ "*"* (2*i-1))
