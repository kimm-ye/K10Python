'''
튜플(Tuple)
    : 소괄호() 안에 콤마로 구분된 항목들이 나열되어 표현되는 시퀀스 자료형.
    서로 다른 자료형으로 구성할 수 있지만, 대입 연산자로 튜플의 항목을
    변경할 수 없는 데이터 타입이다.
    Immutable 데이터 타입이라고 한다.
'''

tu1 = tuple() #빈 튜플 생성
tu2 = (1, 2, 3, 4, 5) 
tu3 = 1, #1개의 항목을 갖는 튜플 생성. 뒤에 컴마가 없다면 단순한 변수선언 문장이 된다.
tu4 = (98,99,100) 
print(tu1, tu2, tu3)

print("===인덱싱/슬라이싱", "="*30)
print("tu2[0]:", tu2[0]) 
print("tu2[-1]:", tu2[-1]) #인덱스가 음수인 경우 마지막 항목을 출력함
print("tu2[-2]:", tu2[-2]) #즉, 마지막 인덱스로 돌아가서 순회한다.
print("tu2[1:3]:", tu2[1:3]) #1~2까지 슬라이싱

#해당 요소가 포함되었는지 확인
print("===포함여부확인", "="*30)
print("4 in tu2:", 4 in tu2) #4는 포함되었으므로 true
print("99 not in tu2:", 99 not in tu2) #99는 포함되지 않았으므로 true

print("===반복출력", "="*30)
print("tu2 * 3:", tu2 *3)

# 2개의 튜플을 하나로 합침
print("===병합", "="*30)
new_tu = tu2 + tu4
print("new_tu", new_tu)

# 튜플과 리스트간의 변환을 위한 함수
print("===튜플과 리스트 반환", "="*30)
my_list = [1,2,3]
my_tuple=('x', 'y', 'z')
print(tuple(my_list))
print(list(my_tuple))