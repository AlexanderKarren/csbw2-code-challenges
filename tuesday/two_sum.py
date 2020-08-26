def twoSum(self, nums, target):
        solution = []
        list_set = {}
        match = None
        
        for num in nums:
            if list_set.get(num):
                list_set.update({num: list_set.get(num) + 1})
            else:
                list_set.update({num: 1})
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if list_set.get(difference):
                match = target - nums[i]
                if list_set.get(difference) <= 1 and nums[i] == match:
                    continue
                solution.append(i)
            elif nums[i] == match:
                solution.append(i)
                
        
        return solution