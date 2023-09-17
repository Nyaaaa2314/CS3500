l = open("large-beads.in", "r")
nums = list()
i = 1
for line in l:
    nums.append((i, int(line)))
    i += 1
k = int(input("Enter the number of beads: "))
solution = list()
i = 0
while i < len(nums):
    t = nums[i]
    if t[1] < k:
        for j in range(i+1,len(nums)):
            if t[1] + nums[j][1] == k:
                solution.append((t[0],nums[j][0]))
                nums.remove(nums[j])
                break
    i += 1
print(solution)