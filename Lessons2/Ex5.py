my_list = [7, 5, 3, 3, 2]
print(my_list)
print('введите натуральное чило ')
number = int(input())
i = 0
for n in my_list:
  if number <= n:
    i = i + 1
  else:
    break
my_list.insert(i, number)
print('новый рейтинг')
print(my_list)