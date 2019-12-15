import cv2
'Burada 2 resimlerimizi ojkuyoruz' \
'okudugumuz resimleri on ve arka diye değikenlere atadık burada asıl amac ' \
'telefondan okuuuuunan on ve arka resimleri tek bir resim haline getirmek'
on=cv2.imread('on.jpg')
arka=cv2.imread('arka.jpg')

'burada resimlerimizin shape lerini gösteriyoruz'
print('On resim shape : ',on.shape
      ,'\n','ARka resim shape ', arka.shape)

'gördülüğü gibi asagıda resimleriöiz aynı boyda ve aynı renk kanalına ' \
'sahipler'

'''
On resim shape :  (197, 256, 3) 
Arka resim shape  (197, 256, 3)
'''

'burada resimleri üst üste birleştirerek yani birbirine ekleyerek ' \
'resmimizi tek bir resim haline getirmiş oluyoruz '
newimage=cv2.add(on,arka)

'burada birbirine ekleme işlemi yaptık'

' aşağıda ise resimlerimizi gösteriyoruz'
cv2.imshow('On resim',on)
cv2.imshow('Arka Resim',arka)
cv2.imshow('Birlesitirlmis resim',newimage)

cv2.waitKey(0)
cv2.destroyAllWindows()