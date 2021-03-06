# 0/1 Knapsack problem using DP.
import random as rd


def knapsack(c, val, wt, n):
    dp = [0] * (c+1)

    for i in range(1, n+1):
        for w in range(c, 0, -1):
            if wt[i-1] <= w:
                dp[w] = max(dp[w], dp[w - wt[i-1]] + val[i-1])

    return dp[c]


# Randomly generated values and weight.
# values = [rd.randint(50, 300) for i in range(150)]
# weight = [rd.randint(10, 100) for j in range(150)]
values = [236, 191, 122, 170, 110, 100, 161, 194, 151, 180, 78, 284, 144, 86, 296, 54,
          283, 200, 64, 279, 66, 56, 175, 136, 249, 184, 95, 200, 300, 253, 107, 266, 165,
          243, 183, 59, 144, 217, 204, 156, 163, 226, 73, 248, 131, 234, 226, 96, 171, 108,
          149, 234, 181, 191, 56, 212, 122, 82, 283, 146, 117, 102, 140, 94, 199, 289, 120,
          152, 218, 268, 238, 249, 235, 221, 62, 266, 294, 66, 250, 244, 272, 287, 156, 205,
          139, 133, 151, 116, 99, 98, 292, 122, 111, 193, 190, 116, 266, 123, 182, 139, 293,
          123, 243, 291, 68, 262, 167, 284, 100, 274, 63, 81, 227, 209, 132, 201, 215, 300,
          159, 174, 88, 292, 133, 115, 114, 141, 138, 75, 107, 292, 157, 157, 142, 68, 300,
          69, 76, 224, 136, 286, 153, 106, 218, 172, 50, 213, 139, 188, 51, 96]
weight = [13, 41, 86, 76, 57, 39, 16, 25, 92, 36, 43, 18, 81, 37, 100, 70, 59, 14, 87, 94, 54,
          40, 78, 47, 84, 45, 21, 32, 86, 48, 32, 67, 39, 93, 60, 81, 66, 29, 75, 87, 22, 72,
          53, 15, 70, 91, 33, 64, 69, 16, 60, 76, 75, 91, 83, 42, 27, 100, 92, 85, 12, 59, 31,
          25, 39, 54, 78, 19, 68, 41, 71, 67, 77, 32, 57, 86, 97, 60, 60, 96, 46, 15, 15, 39,
          73, 94, 48, 33, 49, 33, 48, 75, 61, 64, 95, 80, 27, 84, 99, 28, 38, 21, 93, 99, 77,
          68, 48, 31, 82, 68, 72, 52, 15, 54, 30, 72, 29, 78, 34, 57, 50, 100, 99, 80, 46, 60,
          16, 52, 88, 69, 15, 18, 84, 56, 19, 65, 48, 10, 63, 86, 86, 45, 82, 61, 51, 27, 35, 89, 98, 40]
capacity = 1000
values_len = len(values)

print("Knapsack capacity is:", knapsack(capacity, values, weight, values_len))

