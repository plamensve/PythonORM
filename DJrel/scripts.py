from datetime import *

numb = [[1, 2, 3], [9, 8, 7]]

result = [i
          for x in numb
          for i in x]

print(*result)


print(f"{datetime.now():%H-%M-%m-%Y}")