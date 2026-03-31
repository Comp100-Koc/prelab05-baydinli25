def longest_palindromic_substring(s):
    def is_palindrome(t):
        for x in range(len(t)) :
            if t[x] != t[len(t)-1-x] :
                return False
        return True
    
    final = ""
    for i in range(len(s)) :
        longest = ""
        for k in range(i, len(s)) :
            if is_palindrome(s[i:k+1]) and len(s[i:k+1]) > len(longest) :
                longest = s[i:k+1]
        if len(longest) > len(final) :
            final = longest
    if len(final) < 2 :
        return ""
    return final