#파이썬은 다중산속이 가능한 언어

class A:
    pass

class B:
    pass

class X(A):
    pass

class Y(B):
    pass

class Me(X, Y):
    pass

#상속관계확인(mro), object가 최상위 클래스
print(Me.mro())


