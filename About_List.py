my_list1 = [1,2,3]
my_list2 = my_list1 # 리스트가 새로 만들어지는 것이 아닌 둘 다 하나의 오브젝트를 바라보고 있는 것이다.

my_list2[0] = 0 # my_list2를 변경하면 my_list1도 같이 변경된다.

# print(my_list1) -> [0, 2, 3]
# print(my_list2) -> [0, 2, 3]

# 따라서 변수로 변수를 선언하는 것은 지양하자.
# 새로운 리스트를 만들어주기 위한 방법 -> list.copy() 이용

my_list1 = [1,2,3] 
my_list2 = my_list1.copy() # my_list2라는 새로운 오브젝트가 생성된다. 
my_list1[0] = 10
#  print(my_list1) -> [10,2,3], print(my_list2) -> [1,2,3]

# 출처: https://datamasters.co.kr/49 [데이터마스터]


