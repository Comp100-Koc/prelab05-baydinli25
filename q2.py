def remove_adjacent_duplicates(s):
    
    def any_duplicate(s) :
        
        if len(s) < 2 :
            return False
        if s[len(s)-1] == s[len(s)-2] :
            return True        
        prex = 0
        for x in range(1, len(s)) :
            if s[x] == s[prex] :
                return True
            prex = x
        return False   
    
    while any_duplicate(s) :
        prei = 0  # previous iterations i
        i = 0
        while True :
            i += 1
            if s[i] == s[prei] :
                s = s[:i-1] + s[i+1:]
                break
            prei = i
            if i == len(s) :
                break
    return s