"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))
<출력>
6

"""
def gcd(a,b):
    a_list = []
    b_list = []
    common_list = []
    
    for i in range(1,a+1):
        if a%i==0:
            a_list.append(i)

    for i in range(1,b+1):
        if b%i==0:
            b_list.append(i)

    for i in range(len(a_list)):
        for k in range(len(b_list)):
            if a_list[i] == b_list[k]:
                common_list.append(a_list[i])

    print(max(common_list))

gcd(12,6)
        
    
