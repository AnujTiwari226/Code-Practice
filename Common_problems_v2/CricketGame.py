def noOfWays(totalScore):
    # Handle invalid inputs
    if totalScore < 0 or totalScore % 2 != 0:
        return 0
        
    # Create dp array
    dp = [0] * (totalScore + 1)
    
    # Base cases
    dp[0] = 1
    if totalScore >= 2:
        dp[2] = 1
    if totalScore >= 4:
        dp[4] = 2
        
    # Fill dp array
    for i in range(6, totalScore + 1, 2):
        dp[i] = dp[i-2] + dp[i-4] + dp[i-6]
    
    return dp[totalScore]

# Read input
totalScore = int(input())
print(noOfWays(totalScore))