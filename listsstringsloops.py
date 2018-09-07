def vowelcount (str):
    #instantiate the string and duplicate counter
    strcontainer = " " 
    dup = 0
    #loop through the string and capture vowels or their duplicates for a in str
    if a in ('a', 'e', 'i', 'o', 'u'):
        if a in strcontainer:
            dup += 1
        else:
            strcontainer += a 
            return (strcontainer, dup)