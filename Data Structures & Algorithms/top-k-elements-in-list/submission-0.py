class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        final_list = []
        for num in nums:
            # create a entry in the dict if it doesnt alr have one
            # otherwise, increment dict count by 1
            if num not in group:
                group[num] = 1
            else:
                group[num]+=1
        #sort groups based on value, then add them descending to sorted_groups (aka largest first)
        sorted_groups = sorted(group, key=group.get, reverse=True)
        for i in range(k):
            final_list.append(sorted_groups[i])
            #make a final list and append however many of the elements we want
        return(final_list)
