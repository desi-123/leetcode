def maxProfit(prices):
    left, right = 0, 1
    maxProfit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        else:
            left = right
        right += 1
    return maxProfit


if __name__ == '__main__':
    print(maxProfit([7, 1, 5, 3, 6, 4]))