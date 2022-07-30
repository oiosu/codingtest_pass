# 뒤집힌 덧셈
# 어떤 수 X가 주어졌을 때, 
# X의 모든 자리수가 역순이 된 수를 얻을 수 있다
# Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자.
# X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다.
# 두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램

x, y = map(str, input().split())
sum = str(int(x[::-1]) + int(y[::-1]))
print(int(sum[::-1]))
