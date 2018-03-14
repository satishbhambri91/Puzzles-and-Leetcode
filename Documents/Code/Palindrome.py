import re

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) == 0:
        return True

    else:
        start = 0

        s = s.lower()

        nS = re.sub(r"[^a-zA-Z0-9]", "", s)
        print(s)
        print(nS)
        end = len(nS) - 1

        while start < end:
            if nS[start] == nS[end]:
                start = start + 1
                end = end - 1
            else:
                return False
            return True


s = "A man, a plan, a canal: Panama"
a = isPalindrome(s)

print(a)

