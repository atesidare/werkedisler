import os
a = (30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100)

def main():
    os.system('cls')
    while True:
        print()
        print("Yaklaşım ölçüsünü girin")
        yö = int(input("Tam sonuç için 1 - Yaklaşık sonuç için 100: "))
        print()
        fç = int(input("Formül çarpanını girin (144, 48 gibi): "))
        print()
        ds = int(input("Diş sayısını girin: "))

        for B in range(0,36):
            for D in range(0,36):
                for A in range(0,36):
                    for C in range(0,36):
                        x = fç * a[B] * a[D]
                        y = a[A] * a[C] * ds
                        z = a[A] * a[C]
                        k = x-y
                        t = x/z

                        if  (k < 0):
                             k = -1 * k
                        elif (k < yö):
                            print()
                            print("İstenilen diş sayısı : ",ds)
                            print(" A = ", a[A])
                            print(" B = ", a[B])
                            print(" C = ", a[C])
                            print(" D = ", a[D])
                            print(" En yakın diş : ",t)

        print()
        print("Tekrar denemek istermisiniz? ")
        yanıt = input("Çıkmak için Q (veya q) ya basın : ")
        if yanıt == "q" or yanıt == "Q":
            quit()
        else:
            pass


main()