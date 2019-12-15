import cv2
'Burada resmimizi okuyoruz ve okunan resmi değişkene atıyoruz'
image=cv2.imread('image.jpg')

'burada copyMakeBorder fonksiyonunu kullanrak tekrar etme methodunu ele alacagız' \
' '
wrap=cv2.copyMakeBorder(image#işlenecek resim
                        ,100,100,100,100,#yükseklik en boy
                        borderType=cv2.BORDER_WRAP)#burada bordertype methodumuzu seçeriz

cv2.imshow('Orjinal Resim',image)#orjinal rsmi gösteriyoruz
cv2.imshow('Tekrarlanmış Resim',wrap)#işlenmiş ressmi gösteriyorurz

cv2.waitKey(0)
cv2.destroyAllWindows()