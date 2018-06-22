'''def mul(i):
    for i in range(1, 11):
        if i>11:
            return
        print(n, 'x', i, '=', n * mul(i+1))

n=int(input("Enter number: "))'''

def mul(i):
    if i<=10:
      a=12*i
      print(a)
      i=i+1
      mul(i)

mul(1)