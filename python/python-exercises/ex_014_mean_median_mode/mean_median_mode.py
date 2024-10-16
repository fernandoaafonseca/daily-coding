'''
I challenged myself to code functions for the mean, median and mode measures without using any external modules.
The mode was the trickiest one to implement by iterating over a dictionary but in the end, everything worked out.
'''

def main():
    list_of_nums = []
    continue_to_add = True

    while continue_to_add:
        num = ''
        add_more = '_'

        while type(num) != 'float':
            try:
                num = float(num)
                list_of_nums.append(num)
                break
            except:
                num = input('\nWrite a number:\n')

        answer = ''
        valid_answers = ['y', 'n']
        while answer not in valid_answers:
            answer = input('\nDo you want to add more numbers?\nType "yes" or "no":\n').lower()
            add_more = answer[0]

            if add_more == 'n':
                continue_to_add = False
                break
            elif add_more == 'y':
                break

    measure = ''
    valid_measures = [1, 2, 3, 4]
    while measure not in valid_measures:
        measure = int(input('\nWhat measure of central tendency do you want to calculate?\
                \n1: mean\
                \n2: median\
            \n3: mode\
            \n4: all of the above\n'))
        
        calculate(measure, list_of_nums)
            
            
def calculate(measure, list_of_nums):
    def mean():
        mean = sum(list_of_nums) / len(list_of_nums)
        print(f'\nThe mean of {list_of_nums} is: \n{mean:.2f}')

    def median():
        list_of_nums.sort()
        length = len(list_of_nums)

        if length % 2 == 0:
            m1 = list_of_nums[length // 2]
            m2 = list_of_nums[length // 2 - 1]
            median = (m1 + m2) / 2
        else:
            median = list_of_nums[length // 2]
        print(f'\nThe median of {list_of_nums} is: \n{median}')

    def mode():
        temp = 0
        num_counter = {}
        
        for num in list_of_nums:
            if num in num_counter:
                num_counter[num] += 1
            else:
                num_counter[num] = 1

        mode = {}
        while True:
            for k, v in num_counter.items():
                if v > temp:
                    mode.clear()
                    mode[k] = num_counter[k]
                    temp = v
                elif v == temp:
                    mode[k] = num_counter[k]
                    temp = v
                else:
                    continue
            
            print(f'\nThe mode(s) of {list_of_nums} are:')
            for k, v in mode.items():
                print(f'{k}, which appeared {v} times.')
            break

    if measure == 1:
        mean()
    elif measure == 2:
        median()
    elif measure == 3:
        mode()
    else:
        mean()
        median()
        mode()
        
        
if __name__== "__main__":
    main()