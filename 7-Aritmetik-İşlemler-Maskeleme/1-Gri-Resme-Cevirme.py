import cv2
'Burada biz resmimizi zar değikenine atadık'
zar=cv2.imread('zar.jpg')

'cvtColor bize resimlerimizin tamamen renginin değiştirilmesine' \
'yardımcı olur resmimizi tanıttıktan sonra cv2 lib inden' \
'bize git COLOR_BGR2GRAY çağır ve resmimizi işle' \
've bu işlenen resmi gidip biz değişkene atarak yeni resmimizde değişiklikler' \
'yapabiliyoruz'

griresim=cv2.cvtColor(zar#işlenecek resim
                      ,cv2.COLOR_BGR2GRAY)#işletme yaptıgımız renk kodu
'resimleri gösteriyoruz' \
'not : Burada imread fonksiyonun da direk olarak ' \
'ikinci değişkene 0 vererek resmimizi değiştirebiliyor olucaktık'

cv2.imshow('Arkaplan plan resim',zar)
cv2.imshow('Gri Resim',griresim)

cv2.waitKey(0)
cv2.destroyAllWindows()