import cv2
import numpy as np


'ana fonksiyonumuz'
def main():
    'kameradan alınan bilgiyi oku 0 bizim kendi kameramız oluyor '\
    'eğer kği video istersek video nun yerini belirtmek gerekiyor'
    kamera=cv2.VideoCapture(0)

    'videowriter_fourcc bize hanghi tipte kaydecegimizi yardımcı oluyor biz aşapıda avi olarak kaydettil'
    fourcc=cv2.VideoWriter_fourcc(*"XVID")

    'video writer ise bize kaydımızı nasıl özelliklere sahip oldugunu söylüyorız'
    kayit=cv2.VideoWriter('kayit.avi'# kayit ismi
                          ,fourcc#hangi tpite olacgı
                          ,30#kaç fps oldugu
                          ,(640,480))# kaça kaç pixel oldugu
    'belilemiş oluyoruz'

    'sonsuz bir dongu olusturmus olduk kameradan alınan bilgileri kare ye aktarmak için'
    while(True):
        'kameradan bilgi alıyoruz ret bize kameranın çalısıp çalısmadıgını kare ise kameradan alınan pixelleri söylüyor'
        ret,kare=kamera.read()

        'ekranı ters yapabilmek için flip fonk kullanıyourz'
        ters_ekran=cv2.flip(kare #ters cevirelecek kare
                            ,1)
        '0 olursa ters ekran 1 olursa aynalanmıs ekran '

        'eğer kamera çalsısoyr ise true bilgisini dönüyoruz'
        if ret==True:
            'kosul sağlandı ise kareden aldıgın bilgileri kayit içerisine katdet diyoruz'
            kayit.write(kare)

        'kareden alınan bilgileri ekran da göstermiş oluyoruz'
        cv2.imshow('Kare',kare)
        cv2.imshow('Ters Kare',ters_ekran)

        'burada waitkey biizm beklemeizi sağlıyor ord ise Q ya basılırsa yani söyle' \
        '25 ms içeirisnde Q ya basılırsa video dan cık'
        if cv2.waitKey(25)&0xFF==ord('q'):
            break
    'burada kamerayı serbest bırakıyoruz'
    kamera.release()
    cv2.destroyAllWindows()

'burada ise programa ilk başlarken burada ki yerdne başla diyoruz'
if __name__ == '__main__':
    main()