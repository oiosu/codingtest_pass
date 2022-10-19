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

print(result)