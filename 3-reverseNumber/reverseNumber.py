a           = int(input())
ones        = a%10
tens        = (int(a/10))%10
hundreds    = int(a/100)
print(ones, tens, hundreds)
print(2*((100*ones)+(10*tens)+(hundreds)))