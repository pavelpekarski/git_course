def convert_to_python_case(txt):
    s = list(txt)
    for i in range(len(s)):
        if s[i] == s[i].upper():
            s.insert(i - 1, '_')
    return s        

txt = input()
print(convert_to_python_case(txt))