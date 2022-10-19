<<<<<<< HEAD
n = int(input())

result = n
for i in range(n) :
  value = input()
  for j in range(len(value) - 1) :
    if value[j] == value[j + 1] :
      pass
    elif value[j] in value[j+1:] :
      result -= 1
      break

=======
n = int(input())

result = n
for i in range(n) :
  value = input()
  for j in range(len(value) - 1) :
    if value[j] == value[j + 1] :
      pass
    elif value[j] in value[j+1:] :
      result -= 1
      break

>>>>>>> ffba77d72193687ce75e356a6d29096d959d5789
print(result)