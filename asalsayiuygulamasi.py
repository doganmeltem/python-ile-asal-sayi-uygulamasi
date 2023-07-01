sayi=int(input("sayiyi giriniz"))
asalMi=True

if(sayi==1):
    print("1 sayisi asal degildir")
for i in range(2,sayi):
    if(sayi%i==0):
        asalMi=False
        break

if(asalMi==True):
    print("asal sayidir")
else:
    print("asal sayi degildir")