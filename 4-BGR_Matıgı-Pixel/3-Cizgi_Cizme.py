import cv2
'burada biz image.jpg değerini değişkene atamıs oluyoruz'
image=cv2.imread('image.jpg')

'cizgiyi cizebilmek için bir for döngüsüne ihtiyacımız vardır ' \
've range fonksiyonu ile 0 dan 99 a kadar say dedik'
for i in range(100):
    'aşağıda iki türlü siyah çizgi çizebilmek için method vardır' \
    'birincisi 0 girerek tüm değerlerimizin sıfır oldugunu söylüyoruz' \
    'bu şekilde yapmak sizin cizgide ki rengi ayarşamaya yaramaz'
    image[50,i]=0
    'aşağıda ki tanımalama şeklinde ise bgr kodlarımızın hepsini sıfır olarak' \
    'atayarak cizgimizi siyah olarak ayarlamasını istiyoruz ve böylelikle hasas ' \
    'vizgi renklerini aarlama yapabiliyoruz...'
    image[55,i]=[0,0,0]
    'gelin burada kırımızı renkli çizgi çizelim tam olarak  60. pixel e'
    image[60,i]=[0,0,255]
    '255 dememin sebebi burada bizim en maksimum değerini almasını sağlıyoruz ve böylelikle ' \
    'rengimiz kırmızı olarak karsımıza cıkıyor'

'burada ise resmimizi göösteriyoruz'
cv2.imshow('Cizgili Resim',image)

cv2.waitKey(0)
cv2.destroyAllWindows()