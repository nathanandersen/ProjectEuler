#import copy
def solve_all():
    total = 200
    coins = [1,2,5,10,20,50,100,200]
    solutions = solve(coins,total)

    print(solutions)


def solve(coins,target):
#    print('started recursing')
    if target == 0:
        return 1
#    total = 0
#    print(coins)
    total = int(target in coins)
#    if target in coins:
    cs = list(filter(lambda c: c < target, coins))
    for coin in cs:
#    for coin in filter(lambda c: c < target, coins):
#        print(coin)
#        next_coins = list(filter(lambda c: c <= coin and c <= target, coins))
#        print('next coins:', list(next_coins), 'next total:', target-coin)
        x = solve(cs,target - coin)
#        print('finished recursing')
#        x = solve(filter(lambda c: c <= coin and c <= target, coins), target - coin)
#        print(x)
        total += x

    return total
#    return sum(solve(coins[:index+1],target-coin) for index,coin in enumerate(coins))
#    for index,coin in enumerate(coins):
#        print(coin,target-coin)
#        x = solve(coins[:index+1],target-coin)

#    for coin in enumerate(filter(lambda c: c <= target, coins)):
#        print(target-coin)
#        x = solve(filter(lambda c: c <= coin, coins),target - coin)
#        print(x)
#            return solutions
#    return solutions


        # append to solutions
#    return solutions
solve_all()
#print(solutions)
