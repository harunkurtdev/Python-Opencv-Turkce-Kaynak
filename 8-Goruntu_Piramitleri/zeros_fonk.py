import cv2
import numpy as np

def main():
    zar=cv2.imread('zar.jpg')
    'resmin boyutunu öğrendil'
    print(zar.shape)

    'pyrup ile resmin boyutunu  2 katına cıkardık ve boyutlarını çğrendik'
    iki_kat_buyuk=cv2.pyrUp(zar)
    print(iki_kat_buyuk.shape)

    iki_kat_kucuk=cv2.pyrDown(zar)
    print(iki_kat_kucuk.shape)

    'bilindiği üzere resimleirmiz array şeklinde oljusmakta ' \
    'zeros fonksiyonu bize arrayimiz de ki yüm değerleri sıfırlamakta ve' \
    'böylelikle siyah bir görüntü elde etmekteyiz'
    resim_zeros=np.zeros((150,150,3)# resöim boyuları
                         ,dtype='uint8')# array intipi

    ' burada remimize beyaz bir kare çiziyoruz'
    cv2.rectangle(resim_zeros,(0,100),(10,110),color=(255,255,255),thickness=2)

    'resimlerimizi gösteriyoruz'
    cv2.imshow('Zar',zar)
    cv2.imshow('Iki kat buyuk zar',iki_kat_buyuk)
    cv2.imshow('Iki kat kucuk zar',iki_kat_kucuk)
    cv2.imshow('Resim Zeros',resim_zeros)

if __name__ =='__main__':
    main()

cv2.waitKey(0)
cv2.destroyAllWindows()