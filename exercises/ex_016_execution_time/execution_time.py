from time import time
import os


start = time()
num = 0
while num < 1000:
    num += 1
    os.system('cls' if os.name=='nt' else 'clear')
    print(num)
end = time()
execution_time = end - start
print(f'Execution time: {execution_time:.5f} seconds')