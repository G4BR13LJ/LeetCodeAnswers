# detects weather a string contains target substring
def isSubsequence(sub, string):
    sub_idx = 0
    for char in string:
        if char == sub[sub_idx]:
            sub_idx += 1
        if sub_idx == len(sub):
            print("true")
            return True
    print("false")
    return sub_idx == len(sub)


s = "axc"
t = "ahbgdc"
isSubsequence(s, t)
print()
u = "abc"
v = "ahbgdc"
isSubsequence(u, v)
print()
x = "bab"
y = "aaaba"
isSubsequence(x, y)
