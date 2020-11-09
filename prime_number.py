
def prime_list(stop):
    a=1
    b=0
    counter=0
    while b<stop:
        for i in range(2,a):
            counter=i
            if a%i==0:
                break
            else:
                continue
        if counter==a-1:
            print(a)
            b+=1
        a+=1


def is_prime(a):
    for i in range(2,a):
        counter=i
        if a%i==0:
            break
        else:
            continue
    if counter==a-1:
        return "Yes"
    return "No"


# prime_list(100)
prime_list(100)