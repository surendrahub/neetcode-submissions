class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0 
        min_arr = prices[0]
        for i in range(1,len(prices)):
            if min_arr > prices[i]:
                min_arr = prices[i]
            else :
                current_profit = prices[i]- min_arr
                max_sum = max(current_profit,max_sum)
        return max_sum