my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.extend([50,60,70])
my_list.remove(my_list[-1])
my_list.sort()
print(my_list.index(30))
