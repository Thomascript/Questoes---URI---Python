a, b = input().split()

a = int(a)
b = int(b)

if(a == 1):

    quantidade = b * 4.00

elif(a == 2):

    quantidade = b * 4.50

elif(a == 3):

    quantidade = b * 5.00

elif(a == 4):

    quantidade = b * 2.00

elif(a == 5):

    quantidade = b * 1.50

print("Total: R$ {0:.2f}".format(quantidade))
