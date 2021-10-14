my_list = list(input())
c = 0
for e1 in range(1,len(my_list), 2):
  c = my_list[e1]
  my_list[e1] = my_list[e1 - 1]
  my_list[e1 - 1] = c
print(my_list)