# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        longestlenth = 1  # 非空子字符串的长度最小为1
        substr = ""  # 子字符串
        for item in s:
            if item not in substr:
                substr += item
            else:
                if len(substr) > longestlenth:
                    longestlenth = len(substr)
                # 应该从重复的下一个字符开始继续判断
                substr += item
                substr = substr[substr.index(item) + 1:]
        if len(substr) > longestlenth:
            longestlenth = len(substr)
        return longestlenth


if __name__ == '__main__':

    str = Solution.lengthOfLongestSubstring("abccdef")
    print(str)










