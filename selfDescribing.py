number_to_be_checked = input('Please enter a number: ')
occurences = []
counter = 1
checkie = 0

def checkNumber (nums:str):
    for i in range(len(nums)):
        if int(nums[i]) == nums.count(f'{i}'):
            if i == len(nums)-1:
                print(f'The number {nums} is a self describing number')
        else:
            print(f'The number {nums} is not a self describing number')
            break

checker = checkNumber(number_to_be_checked)