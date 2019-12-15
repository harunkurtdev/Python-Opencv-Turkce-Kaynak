import cv2
import numpy as np
'Resmimizi arrap tipinde image e atıyoruz'
image=cv2.imread('image.jpg')
'replitace bize orjianl resimde ki kenarda ki pixelleri uzatmamızı sağlar'
replitace=cv2.copyMakeBorder(image,#resmimizi yazıoyurz
                             100,100,100,100,#bunlar ise resmimizi sağdan soldan yukarıdan felan
                             #uzunluk bırakmamızı sağlıyor
                             borderType=cv2.BORDER_REPLICATE)#borderType denilen yer bizim için çok önemlidir
                            #burada resmimize nasıl bir işlem yapcaksak onu belirtiyoruz

cv2.imshow('Uzatma',replitace)#resmimizi gösteriyoruz
cv2.imshow('Orjianl resim',image)#burada ise orjinal resmi gösteriyoruz

'burada resmimizin boytları hakkında bilgi alıyoruz'
print(replitace.shape)

'burada ise resmimizin pixel sayılarını öğreniyoruz'
print(replitace.size)

cv2.waitKey(0)
cv2.destroyAllWindows()