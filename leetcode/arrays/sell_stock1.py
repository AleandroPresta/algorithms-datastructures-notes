from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
                
            profit = max(profit, p-buy_price)
        return profit
    
    
class Test:
    def test1(self):
        prices = [7,1,5,3,6,4]
        output = 5
        assert Solution().maxProfit(prices) == output
        
    def test2(self):
        prices = [7,6,4,3,1]
        output = 0
        assert Solution().maxProfit(prices) == output
        

def main() -> None:
    test = Test()
    
    test.test1()
    print('Test 1 passed')
    
    test.test2()
    print('Test 2 passed')
    
if __name__ == '__main__':
    main()