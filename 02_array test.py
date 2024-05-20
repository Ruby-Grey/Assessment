# li = ["a", "b", "c", "d", "e", "f"]
#
# choice = -1
# is_valid = False
#
# while is_valid == False:
#
#     print(f"Choose and option (type a number from 1 to {len(li)})")
#
#     for index in range(0, len(li)):
#         print(index + 1, " - ", li[index])
#
#     choice = int(input())
#
#     if choice < 0 or choice >= len(li):
#         print("Please enter an integer between 1 and ", {len(li)})
#
#     else:
#         is_valid = True
#
# print("You chose option: ", choice)

list = ["a", "b", "c"]

option_count = len(list)

while True:

   print(f"Select an option. (Type an integer between 1 and {option_count})")

   option_number = 1

   for option in list:

      print(f"{option_number} - {option}")

      option_number = option_number + 1


   choice = input()

   print(f"you chose {choice}")

   break














