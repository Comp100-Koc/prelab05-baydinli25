def add_binary(a, b):
    
    def myint(x, y) :
        intvalue = 0
        for i in range(-1, -len(x) + 1, -1) :
            power = -1 -i
            intvalue += y**power * int(x[i])
        return intvalue

    def mybin(k) :
        if k == 0 :
            return "0b0"
        binstr = ""
        while k > 0 :
            remainder = k%2 
            k = k//2
            binstr = str(remainder) + binstr
        return "0b" + binstr
    
    a = myint(a, 2)
    b = myint(b, 2)
    return mybin(a+b)