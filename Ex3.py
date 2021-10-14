month_dict = {1: 'jenuary', 2:'february', 3: 'mach', 4:'april', 5:'may', 6:'june', 7:'july',8:'august', 9:'septenber', 10:'oktober', 11:'november', 12: 'desember'}
month_list = ['jenuary', 'february', 'mach', 'april', 'may', 'june', 'july', 'august', 'septenber', 'oktober', 'november', 'desember']
print('введите чисто от 1 до 12')
num = int(input())
if num in month_dict:
  print(num,'month - is',month_list[num - 1])
else:
  print('error')
winter_dict = {1: 'jenuary', 2:'february', 12: 'desember'}
spring_dict = {3: 'mach', 4:'april', 5:'may'}
summer_dict = {6:'june', 7:'july',8:'august'}
autum_dict = {9:'septenber', 10:'oktober', 11:'november'}
season_list = ['winter', 'spring', 'summer', 'autum']
if num in winter_dict:
  print ('it is',season_list[0])
else:
  if num in spring_dict:
    print('it is', season_list[1])
  else:
    if num in summer_dict:
      print('it is', season_list[2])
  print('it is', season_list[3])