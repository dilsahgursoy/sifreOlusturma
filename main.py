def PassGenerator(uzunluk):
    sonuc = ""
    import random
    import string
    liste = [string.ascii_lowercase,string.ascii_uppercase,string.digits,string.punctuation]
    getir = lambda x: random.choice(x)
    def PassKontrol(metin):
        import string
        liste = [string.ascii_lowercase, string.ascii_uppercase,
                string.digits, string.punctuation]
        def fonk(x, liste): return x in liste
        sozluk = {}
        sozluk.update(zip(liste,[False,False,False,False]))
        for item in metin:
            for key,value in sozluk.items():
                if fonk(item,key):
                    sozluk[key] = True
                    break
        kontr =list(sozluk.items())
        return all(map(lambda x:x[1]==False,sonuc))

    while not PassKontrol(sonuc) and len(sonuc)<uzunluk:
        sonuc+= getir(random.choice(liste))

    return sonuc

        

print(*PassGenerator(12),sep="")
