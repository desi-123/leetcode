def minCostClimbingStairs(cost):
    n1 = cost[0]
    n2 = cost[1]

    for i in range(2, len(cost)):
        temp = cost[i] + min(n1, n2)
        n1 = n2
        n2 = temp
    return min(n1, n2)


if __name__ == '__main__':
    print(minCostClimbingStairs([1, 2, 4, 9, 13]))