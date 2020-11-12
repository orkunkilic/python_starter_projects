def asal(sayi):
    i=2
    lista=[]
    listb=[]

    while i <= sayi:
        lista.append(i)
        i+=1

    a=0
    while a < (len(lista)-1):
        c=lista[a]
        listb.append(c)
        n=1
        while (c*n)<=lista[-1]:
            try:
                lista.remove(c*n)
            except:
                 pass
            n=n+1
        a=0

    listb.append(lista[0])
    lista.pop()


    return listb

giris=int(input("Kaça kadar olan asal sayıların bulunmasını istiyorsunuz?"))

print(giris,"'e kadar olan asal sayılar:",asal(giris))
