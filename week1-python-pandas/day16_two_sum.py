# Day 16 (July 16) — Two Sum (NeetCode #1)
# Pattern: Arrays & Hashing → Hash Map

# =============================================
# Brute Force (O(n²))
# =============================================
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# =============================================
# Hash Map (O(n)) — optimal
# =============================================
def two_sum(nums, target):
    seen = {}  # value → index
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i

# Test
nums = [2, 7, 11, 15]
target = 9
print(f"Input: nums={nums}, target={target}")
print(f"Output: {two_sum(nums, target)}")
print(f"Expected: [0, 1]")
assert two_sum(nums, target) == [0, 1]
print("Passed!")
