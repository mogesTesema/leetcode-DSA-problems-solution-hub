class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count the frequency of each element in the array
        freq_element = Counter(nums)
       
    
        # assign threshold freqency to be majority element once not to recomputer on every iteration of elment while majority element checking stage.
        majority_threshold = len(nums)/2
        
        # clear memory
        del nums

        
       # iterate through freqency countered elements
        for element in freq_element:
            # check for eligibility to be majority element
            if freq_element[element] >= majority_threshold:
                # return majority element you get
                return element
            



        
