def countPalindromicSubsequence(s):
    result = 0
    
    for char in set(s):
        left = s.find(char)
        right = s.rfind(char)
        if right - left > 1:
            unique_chars = set(s[left + 1:right])
            result += len(unique_chars)
    
    return result
    