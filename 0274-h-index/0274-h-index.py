class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations = sorted(citations)
        h_index = 0
        for i in range(len(citations)-1, -1, -1): 

            if citations[i] > h_index: 
                h_index += 1
        
        return h_index