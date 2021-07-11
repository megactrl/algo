def knapsack(profit, weight, capacity):
  
    # array of profit/weight ratio
    ratio = [v / w for v, w in zip(profit, weight)]

    # a list of (0, 1, ..., n-1)
    index = list(range(len(profit)))

    # index is sorted according to ratio in descending order
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_profit = 0

    fraction = [0] * len(profit)

    for i in index:
        if weight[i] <= capacity:
            fraction[i] = 1
            max_profit += profit[i]
            capacity -= weight[i]
        else:
            fraction[i] = capacity / weight[i]
            max_profit += profit[i] * fraction[i]
            break

    return max_profit, fraction


def main():
    # profit is array of profit of the items
    # weight is array of weight of the items
    # capacity is capacity of the sack

    profit = [50, 60, 80]
    weight = [10, 30, 20]
    capacity = 50

    # max_profit is the maximum profit gained
    # fraction is the fraction in which items should be taken
    max_profit, fraction = knapsack(profit, weight, capacity)
    print('Maximum profit:', max_profit)
    print('Items should be taken in fraction of:', fraction)


if __name__ == '__main__':
    main()
