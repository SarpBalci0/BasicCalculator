print('Hesap Makinesine Hoşgeldiniz')

sayi1=float(input('1.Sayıyı Giriniz=  '))
sayi2=float(input('2.Sayıyı Giriniz=  '))
islem=input('Yapmak İstediğiniz İşlemi Giriniz (+, -, *, /, %)=  ')

if islem=='+':
    cevap=sayi1+sayi2
    print('İşlem Sonucu=',cevap)

elif islem=='-':
    cevap=sayi1-sayi2
    print('İşlem Sonucu=',cevap)

elif islem=='*':
        cevap=sayi1*sayi2
        print('İşlem Sonucu=',cevap)

elif islem=='/':
            cevap=sayi1/sayi2
            print('İşlem Sonucu=',cevap)
elif islem=='%':
                cevap=sayi1*sayi2/100
                print('İşlem Sonucu=',cevap)

else:
     print('Hatalı Giriş yapıldı, tekrar deneyin')

