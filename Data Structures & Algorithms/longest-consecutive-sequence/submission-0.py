class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # O(1) lookups, removes duplicates
        longest = 0

        for num in num_set:
            # only start counting if this is the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # count consecutive elements
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest

