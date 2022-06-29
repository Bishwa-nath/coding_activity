# Longest Common Subsequence

def print_lcs(str1, str2, dp):
    i = len(str1)
    j = len(str2)
    lcs_str = ""
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs_str += str1[i-1]
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    lcs_str = lcs_str[::-1]
    print(lcs_str)


def lcs(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[0] * (m+1) for i in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print_lcs(s1, s2, dp)
    return dp[n][m]


s1 = "correspondent"
s2 = "response"
print("Length of LCS: {}".format(lcs(s1, s2)))
