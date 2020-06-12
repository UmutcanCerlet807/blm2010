#!/usr/bin/env python
# coding: utf-8

# In[1]:


# UMUTCAN CERLET 170401060
ithalat  matematik
 senfoni  sp olarak  içe aktar
sp . init_printing ()
x  =  sp . Sembol ( 'x' )
içinde = []
korelasyonlar = []
def  dosyaOku ():
    dosya  =  open ( 'burada.txt' , 'r' )
    için  Satir  içinde  dosya :
        altında . append ( int ( satir ))
    dosya . kapat ()


def  gauss ( A ):
    boyut  =  len ( A )
    için  I  içinde  aralığı ( 0 , boyut ):
        maxSutun  =  abs ( A [ i ] [ i ])
        maxSatir  =  i
        için  j  olarak  aralık ( i  +  1 , boyut ):
            Eğer  abs ( A [ j ] [ i ]) >  maxSutun :
                maxSutun  =  abs ( A [ j ] [ i ])
                maxSatir  =  j
        için  k  olarak  aralık ( i , boyut  +  1 ):
            temp  =  A [ maxSatir ] [ k ]
            A [ maxSatir ] [ k ] =  A [ i ] [ k ]
            A [ i ] [ k ] =  sıcaklık
            
        için  l  olarak  aralık ( i  +  1 , boyut ):
            c  =  - A [ l ] [ i ] /  A [ i ] [ i ]
            için  j  olarak  aralık ( i , boyut  +  1 ):
                eğer  i  ==  j :
                    A [ l ] [ j ] =  0
                başka :
                    A [ l ] [ j ] + =  c  *  A [ i ] [ j ]

    matris  = [ 0  için  I  içinde  aralığı ( boyut )]
    için  I  içinde  aralığı ( Boyut'tan  -  1 , - 1 , - 1 ):
        matris [ i ] =  A [ i ] [ boyut ] /  A [ i ] [ i ]
        için  k  olarak  aralık ( I  -  1 , - 1 , - 1 ):
            A [ k ] [ boyut ] - =  A [ k ] [ i ] *  matris [ i ]
    dönüş  matrisi

def  korelasyon ( kendiSonuclarim , ilk , son ):
    n = son - ilk
    yi  =  0
    için  I  içinde  aralığında ( birinci , bitiş ):
        il + = Veriler [ I ]
    y_ussu  =  yi / n   # y'lerin ortalamasi
    Sr  =  0
    için  I  içinde  aralığında ( birinci , bitiş ):
        Sr  = ( kendiSonuclarim [ I - ilk ] -  Veriler [ i ]) **  2  +  , Sr
    St  =  0
    için  I  içinde  aralığında ( birinci , bitiş ):
        St  =  St  + ( Veriler [ I ] -  y_ussu ) ** 2
    rkare =   abs (( St - Sr ) / St )
    r  =  matematik . sqrt ( rkare )
    dönüş  r

def  veriBulma ( ilk , son ):   # 10lu şekilde alip 6. dereceye kadar hesaplatıyoruz en iyi dereceyi buluyoruz veya bütün verili burda hesapliyoruz.
    dizi = []
    n  =  son - ilk
    için  DERECE  olarak  aralık ( 1 , 7 ):
        xValue  = []
        için  I  içinde  aralığı ( n ):
            xValue . ekle ( i + 1 )
        # MATRIS Olustururmamız lazım    
        matris  = [[ 0  için  i  içinde  aralığı ( Dereceli + 1 )] için  j  olarak  aralık ( Dereceli + 1 )]
        boyut  =  len ( matris )
    
        için  I  içinde  aralığı ( Boyut'tan ):
            için  j  olarak  aralık ( Boyut'tan ):
                xToplamlari = 0
                için  k  olarak  aralık ( n ):
                    matris [ 0 ] [ 0 ] =  len ( xValue ) # matrisin 0,0 x veri sayisi kadar olması lazım
                    xToplamlari = xValue [ k ] ** ( i + j ) +  xToplamlari  
                    matris [ i ] [ j ] =  xToplamları
                
        
        
        # y, y * x, y * x kare, y * x kup gibi ifadeleri bulmamız lazım. 
        xySonuclari  = []
        için  I  içinde  aralığı ( Boyut'tan ):
            toplam = 0
            için  j  olarak  aralık ( birinci , bitiş ):
                Toplam  =  Toplam  + ( Veriler [ j ] * ( xValue [ j - ilk ] ** i ))    
            xySonuclari . append ( toplam )
        
        # Buldugumuz sonuclari matrisin en sutununa atarız.
        k  =  0        
        için  i  de  matrise :
            i . append ( xySonuclari [ k ])
            k = k + 1
    
    
            
        katSayilar = gauss ( matris )
        
        kendiSonuclarim = []
        için  I  içinde  aralığı ( n ):
            toplam  =  0
            için  j  olarak  aralık ( len ( katSayilar )):
                toplam  =  toplam  +  katSayilar [ j ] * (( i + 1 ) ** j )
                eğer  j  ==  DERECE :
                    kendiSonuclarim . append ( int ( toplam ))
        r  =  korelasyon ( kendiSonuclarim , ilk , son )
        dizi . ek ( r )
        

    eniyisi  =  100
    dizin = 0
    için  i  içinde  aralığı ( len ( dizi )):
        temp  =  abs ( 1 - dizi [ i ])
        eğer  geçici < eniyisi :
            eniyisi  =  sıcaklık
            dizin  =  i + 1

    print ( "En iyi dereceli polinom:" , dizin )
    tr İ yiPolinomVeIntegralYazdir ( endeks , 0 , len ( Veriler ))
    

def  en İ yiPolinomVeIntegralYazdir ( derece , first , end ):
        n  =  son  -  ilk 
        xValue  = []
        için  I  içinde  aralığı ( n ):
            xValue . ekle ( i + 1 )
        # MATRIS Olusturmamız lazım    
        matris  = [[ 0  için  i  içinde  aralığı ( Dereceli + 1 )] için  j  olarak  aralık ( Dereceli + 1 )]
        boyut  =  len ( matris )
    
        için  I  içinde  aralığı ( Boyut'tan ):
            için  j  olarak  aralık ( Boyut'tan ):
                xToplamlari = 0
                için  k  olarak  aralık ( n ):
                    matris [ 0 ] [ 0 ] =  len ( xValue ) # matrisin 0,0 x veri sayisi kadar olmak zorunda
                    xToplamlari = xValue [ k ] ** ( i + j ) +  xToplamlari  
                    matris [ i ] [ j ] =  xToplamları
                
        
        
        # y, y * x, y * xkare, y * xkup gibi ifadeleri bulmamız lazım. 
        xySonuclari  = []
        için  I  içinde  aralığı ( Boyut'tan ):
            toplam = 0
            için  j  olarak  aralık ( birinci , bitiş ):
                Toplam  =  Toplam  + ( Veriler [ j ] * ( xValue [ j - ilk ] ** i ))    
            xySonuclari . append ( toplam )
        
        # Buldugumuz sonuclari da matrisin en sutunlarina atarız.
        k  =  0        
        için  i  de  matrise :
            i . append ( xySonuclari [ k ])
            k = k + 1
        katSayilar = gauss ( matris )
        eğer  len ( katSayilar ) <  7 :
            ise  len ( katSayilar ) ! = 7 :
                katSayilar . ekle ( 0 )
        
        print ( "POLİNOM DENKLEMİ: \ n " )       
        denklem = katSayilar [ 6 ] * x ** 6 + katSayilar [ 5 ] * x ** 5 + katSayilar [ 4 ] * x ** 4 + katSayilar [ 3 ] * x ** 3 + katSayilar [ 2 ] * X ** 2 + katSayilar [ 1 ] * x + katSayilar [0 ]
        sp . pprint ( denklem )
        
        integral  =  0
        a = 10   # 17040106 (0)
        b = uzunluk ( Veriler )
        deltax = 0.01
        n  =  int (( b - a ) / deltax )
        için  I  içinde  aralığı ( n ):
            entegre + = DELTAX * ( denklem . subs ({ x : a }) + denklem . subs ({ x : Bir + DELTAX })) / 2
            a + = deltax
        
        print ( "İntegral Değeri:" , integral )


Def  polinomsuzIntegral ():
        integral  =  0
        a = 10   # 17040106 (0)
        b = uzunluk ( Veriler )
        deltax = 1
        n  =  int (( b - a ) / deltax )
        için  I  içinde  aralığı ( n - 1 ):
            entegre + = DELTAX * ( Veriler [ a ] + Veriler [ a + DELTAX ]) / 2
            a + = deltax
        print ( "Polinomsuz İntegral Değeri:" , integral )
    
def  yorumYap ():
    dosya  =  open ( '170401007_yorum.txt' , 'w' , kodlama = 'UTF8' )
    dosya . write ( '2 İntegral Sonucunun Farklı Çıkmasına Nedeni: \ n ' )
    dosya . yazma ( 'İntegral Hesabi yapılırken verilen polinom küçük dikdörtgenlere bölerek ve bunların alanlarını toplayarak hesaplamaya çalışırız \ n ' )
    dosya . yazma ( 'Aldığımız dikdörtgenlerin eni ne kadar küçük olursa o kadar fazla dikdörtgen alanı hesaplamış ve bir o kadar da istedğimize yakın değer elde edilir \ n ' )
    dosya . yazma ( 'Deltax dedimizin ise bizim dikdörtgenlerimizin enidir \ n ' )
    dosya . yazma ( 'Polinomlu Dettax i 0.1 arasında bizim 2 sayı arasında 10 tane diködrtgen alanı hesplamış oluruz \ n ' )
    dosya . write ( 'Polinomsuz hespalama dedektörünün şartlarında deltaks i 1 alıp odasındale integral hesaplamaktır \ n ' )
    dosya . write ( 'Polinomlu kısımda daha çok alan hesabı yapıldığından polinomsuza göre farklı sonuç vermesi doğaldır. \ n ' )
    dosya . yazma ( 'Polinomlu integral sonucu polinomsuza göre istediğimiz sonuca daha yakın bir sonuç verir.' )
    dosya . yazma ( 'Deltax arttıkça hespalacak dikdörtgen artacağından işlem daha uzun sürer \ n ' )
    dosya . kapat ()

    
dosyaOku ()    
veriBulma ( 0 , len ( Veriler ))
Integral ()
yorumYap ()


# In[ ]:




