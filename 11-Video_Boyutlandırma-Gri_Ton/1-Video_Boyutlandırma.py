import cv2
import  numpy as np

'''Program ilk defa çalışıtıgında gerekli olan dosyaya girmesini belirttik'''

if __name__ == '__main__':
    main()

'bu fonksiyonun acıklaması bir aşağıda acıklanmakta neden kurdugumuza dair' \
'kare ile kameradan gelen kare bilgisini alıyorız yuzde ile de biz yüzdelik büyüme oranını' \
'hesaplatııtrmakta kullanıyoruz'
def pixel_ayarla(kare,yuzde=75):
    'asağıda int tipinde bşr veri geri dönüşü yapsın'\
    'diyoruz kare.shape1 diyeerke kareden aldıgın genislik bilgisini yüzdekilk olarka hesapla'
    genislik=int(kare.shape[1]*(yuzde/100))
    yukseklik=int(kare.shape[0]*(yuzde/100))
    'burada 2 değişkeni tek bir değişkene indirgiyoruz'
    boyut=(genislik,yukseklik)
    'burada ise ressize ile tekrar boyutu ayarlamaya çalışıyoruz'
    'interpolation ile cv3.ınter_area ile tekrar dan kare mizi ayarlamamızı sağlıyoruz'
    return cv2.resize(kare,boyut,interpolation=cv2.INTER_AREA)


'bu fonk ana fonksiyonumuz buradan belirtilen yere doğru gideceğiz'
def main():
    'burada kameradan gelen veriyi okumak istediğimiz için 0 verdik'
    kamera = cv2.VideoCapture(0)

    'Burada kameranın boyunu setlemek için bir takım setler yapıyoruz ' \
    '3 bize boyu' \
    '4 ise bize genisligi set etmemizi sağlıyor' \
    'sonra ki parametreler ise pixel sayısıdır ne kadar büyük ' \
    'veya küüçük olacagı ayarlıyor' \
    'ancak cok orantısız bir şekilde büyütme veya küçültme işlemi yapmakta'
    #kamera.set(3,300)
    #kamera.set(4,300)

    'kamerada gelen bilgiyi sürekli bir biçim de okmamız gerektiği için while ı kullandık'
    while(True):
        'burada bize ret kamera aktif veya değil bilgisi gönderiyor ' \
        'kare ise kameradan alınan p.xellerin bilgisiini göndermekte '
        ret,kare=kamera.read()

        'biz burada aslında orantısız bir biçimde büyümesini sağlayan kamera.set methodunu kendimiz farklı bir yöntem ile ' \
        'yaptık burada bir fonksiyona kare bilgisini ve yüzdelik bilgisini göndermiş olduk böylelikle bize ' \
        'kare den aldıgı pixelleri büyülterek verdi '
        kare2=pixel_ayarla(kare)

        'resimlerimizi gösterdik'
        cv2.imshow('Kare',kare)
        cv2.imshow('Kare Two',kare2)

        'burada waitkey ile 25 ms de bir kontol ederek q butonuna basılıp basılmadıgını kontrol ediyoruz'
        'eğer ki basılmıs ise break ile döngüden cık diyoruz'
        if cv2.waitKey(25)&0xFF==ord('q'):
            break

    'kamera relase ile kameradan bilgi almayı bırak diyoruz'
    kamera.release()
    cv2.destroyAllWindows()


