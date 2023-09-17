# def valid_list():
#     valid = open("primes-million.txt", "r")
#     i = 0
#     while i < len(valid):
#         if valid[i] != list[i]:
#             return False
#         i += 1
#     return True


#lobal list
nums = list(range(2,1000001))
i = 0
nprimes = set()
primes = set()
while i < len(nums):
    if nums[i] not in nprimes:
       for j in range(nums[i] * nums[i], 1000001, nums[i]):
           nprimes.add(j)
    else:
        primes.add(nums[i])
    i+= 1
print("Done")
# primes = list()
# primes.append(2)
# while i < len(nums):
#     for j in primes:
#         if nums[i] % j == 0:
#             break
#         else:
#             primes.append(nums[i])
#     i += 1




# while i < len(list):
#     j = i + 1
#     while j < len(list):
#         if list[j] % list[i] == 0:
#             list.remove(j)
#         else:
#             j += 1
#     i += 1
# i = 0
# primes = list()
# primes.append(2)
# while i < len(nums):
#     for j in primes:
#         if nums[i] % j == 0:
#             break
#         else:
#             primes.append(nums[i])
#     i += 1
# print(len(primes))
