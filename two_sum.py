nums = eval(input('Enter the list of numbers'))
target = int(input('enter the target'))

for i in range(len(nums)):
    dif = target-nums[i]
    if dif in nums[i+1:]:
        a = nums.index(nums[i])
        b = nums.index(dif,i+1)
print(a,b)