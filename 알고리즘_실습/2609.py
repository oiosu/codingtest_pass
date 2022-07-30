a, b = map(int, input().split())
a_value = a
b_value = b

while b_value != 0 :
 a_value = a_value % b_value
 a_value, b_value = b_value, a_value

print(a_value)
print(a * b // a_value)