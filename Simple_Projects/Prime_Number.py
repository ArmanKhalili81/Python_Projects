def prime_number(num):
    count = 0
    for j in range(1,num+1):
            if num%j == 0:
                 count += 1
            
    if count <= 2 and num != 1:
            return num
    else :
        return "ISN'T PRIME"
#--------------------------------------

counter = 0
tmp = 1
ns = 2

while tmp <= 10001 :
        result = prime_number(ns)
        ns += 1
        if result ==  "ISN'T PRIME" :
            tmp += 1
            continue
        else:
            tmp += 1
            counter +=1
            print(result , f"-> {counter}")
