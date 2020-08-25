# Time complexity O(n)
# Space complexity O(n)

class Solution:
    def containsDuplicate(self, nums):
        num_hash = {}
        
        # iterate through the loop
        for i in range(len(nums)):
            # if num in hash table, duplicate found
            if num_hash.get(nums[i]):
                return True
            # otherwise, store in hash table
            else:
                num_hash.update({nums[i]: 1})
                
        return False