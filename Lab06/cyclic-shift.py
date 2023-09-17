nums = list(range(1,101))
k = input("Enter k: ")
for i in range(int(k)):
    nums.insert(0, nums.pop())
print(nums)