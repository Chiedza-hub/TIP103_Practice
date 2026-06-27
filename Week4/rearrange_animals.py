def rearrange_animal_names(s):
    
    j = s.find(")")
    
    while j != -1 :
        for i in range(j - 1, -1, -1):
            if s[i] == "(":
                break

        # slice while removing the braces
        first_half = s[:i]
        second_half = s[j + 1:]

        # reverse the text inbetween
        stack = []
        for k in range(i+1, j):
            stack.append(s[k])
        reversed = ""

        while stack:
            reversed += stack.pop()
        s = first_half + reversed + second_half
        j = s.find(")")
        
    return s 


print(rearrange_animal_names("(dribtacgod)"))
print(rearrange_animal_names("(!(love(stac))I)")) 
print(rearrange_animal_names("adopt(yadot(a(tep)))!")) 