"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-ways
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':  # 基本情况，直接返回 0
            return 0
        dp = [None] * len(s)  # 构建 dp 数组
        dp[0] = 1  # 只有一个数时肯定为 1
        if len(s) > 1:  # 为 dp[1] 填充值
            if s[1] == '0':  # s[i] 为 ‘0’ 时
                if int(s[0:2]) <= 26:  # 截取前两数，判断是否小于或等于 26
                    dp[1] = 1  # 因为 s[i] 为 ‘0’ 所以 dp[1] 只有 1 种可能
                else:
                    return 0  # 比如 60 , 此时该序列无法翻译
            else:  # s[i] 不为 ‘0’ 时
                if int(s[0:2]) <= 26:
                    dp[1] = 2  # 比如 16，有两种翻译结果
                else:
                    dp[1] = 1  # 比如 27，只有一种结果
        else:  # 只有一个数
            return 1

        for i in range(2, len(s)):  # 从 2 开始
            if s[i] == '0':  # s[i] 为 ‘0’ 时
                if s[i - 1] == '0':  # 前一个为 ‘0’
                    return 0  # 无解
                else:  # 前一个不为 ‘0’
                    if int(s[i - 1:i + 1]) <= 26:  # s[i-1] 和 s[i] 组成的数 <= 26
                        dp[i] = dp[i - 2]
                    else:
                        return 0
            else:  # s[i] 不为 ‘0’
                if s[i - 1] == '0':  # 前一个为 ‘0’
                    dp[i] = dp[i - 1]
                else:  # 前一个不为 ‘0’
                    if int(s[i - 1:i + 1]) <= 26:  # s[i-1] 和 s[i] 组成的数 <= 26
                        dp[i] = dp[i - 1] + dp[i - 2]
                    else:  # s[i-1] 和 s[i] 组成的数 > 26
                        dp[i] = dp[i - 1]

        return dp[len(s) - 1]
