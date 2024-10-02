from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_total = 0
        # Search a day to buy
        for i in range(0, len(prices)): 
            max_profit_i = 0
            current_buy_price = prices[i]
            # Seach a day to sell
            for j in range(i+1, len(prices)):
                if self.convenient_price(prices[j], current_buy_price, max_profit_i):
                    max_profit_i = prices[j] - current_buy_price
            if max_profit_i > max_profit_total:
                max_profit_total = max_profit_i
        return max_profit_total

    
    def convenient_price(self, sell_price, buy_price, max_profit):
        profit = sell_price - buy_price
        return True if sell_price > buy_price and profit > max_profit else False
    
    
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