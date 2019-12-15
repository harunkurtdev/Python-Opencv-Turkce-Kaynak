import cv2
import numpy as np

def main():
    # 0=> dersek pc nin kendisine ait camera
    # 1=> dersek usb de ki kamara
    # 2=> dersek video calıstırır
    '''biz kameradan kare sayısını okuyabilmek için videocapture olayını
    kullanırız ve böylelikle hangi kameraya baglanmak istiyorsak onu yazarız'''

    kamera=cv2.VideoCapture(0)

    '''sonsuz bir döngü yparak kameradan alınan her bir kareyi okumus oluyoruz
    ve boylelikle okdugumuz bilgileri ekranda göstermiş oluyoruz'''

    while True:
        '''kameradan okdudumuguz değer olarak 2 değişken bulunmakta
        ret bize çalısıp çalışmaıdıgı hakkında bool bir ceri verirken
        kare ise kameradan okunan her bir kareyi vermekte'''
        ret,kare=kamera.read()

        '''burada ise kameradan okdugumuz her bir kareyi while döngüsü ile 
        gösteriyoruz'''
        cv2.imshow('Gıruntu',kare)

        '''burası onemlidir biraz kameradan aldıgımız fps ile alakalı diyebilriz
        waitkey bize 25milisaniye boyunca bekletiyor ve diyotuz ki ord() fonk ile
        eğer 25mili saniye içerisinde q tusuna basılmış ise döngüden çık diyoruz
        waitkey içerisinde ki değişkeni değiştirirsek bizim adlıgımız fps azalacak veya
        cogalacaktır ne kadar 0 a yakın olursa o kadar hızlı bir fps alıyoruz
        yani bir nevi mili saniye cinsinden bekletiyoruz =) kamerayı'''
        if cv2.waitKey(25)&0xFF==ord('q'):
            'break ile while döngüsünden cık diyoruz'
            break

if __name__ == '__main__':
    main()