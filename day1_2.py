n = 0
    
arr = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
    }
    
try:
    while 1:
        s = input()
        for k,v in arr.items():
            s = s.replace(k, k[0] + v + k[-1])
        first_number = -1
        last_number = -1
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                if first_number == -1:
                    first_number = int(c)
                last_number = int(c)
                
        if first_number != -1 and last_number != -1:
            n += (first_number * 10) + last_number
        
except:
    print(n)