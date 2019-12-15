import cv2
import numpy as np

'''author: @harunlakoda'''

#burada biz resim okuma işlemi yapıyoruz okudugumuz resmmi değişkene
# attıyooruz ve değişkeni çağırma işlemleri yapacağız

#cv2 kütüphanesinden okdugumuz resmi image atama yaptık
image=cv2.imread('image.jpg')

'''burada bizim resmimiz matris sekilinde oldugu için bize bizim 1 pixelimiz
bize 3 adet renk olarak döner buna bgr deriz 

b=blue
    g=green
        r=red 
        
olarrak görülmektedir...

Biz bunları yani BGR değerlerini değiştirerek bir pixel in rengini 
değiştirebilmekteytiz bunları ilerleyen dönemler de yapacagız
  
  aşağıda print in biizim resmimizi ekrana yazdırmasını istoyoruz
  büyük olasılıkla bize mattris bir değer dönecektir =D...

'''
print(image)

''' 
   blue gren red
        .
        .
        .
  [[ 55 184 241] => 100. pixelimiz
  [ 36 186 240]  => 101. pixelimiz
  [ 32 183 240]
  ...
  [  6 109 218]
  [  5  98 213]
  [  1 100 204]]] =>sonuncu pixelimiz
  
  yukarıda ki array de yani dizide resimden aldıgımız int değerleri 
  görmekteyiz
  
  burada dikkaat edilmesi asıl gerekn şey bizim bgr renk değerlerimiz 
  en fazla 2**8 olabilmektedir yani 0 dan 255 e kadar olabilmektedir
  
  b      g       r
  0      0       0 => gri
  255    255     255 =>beyaz olmaktadır
  
  ve renk skalasında bu 1 pixelin rengini değiştibiliriz bunu
  BGR kodlarımızı değiştirerek görmekteyiz... 
  '''

'''gelen değerin tipini nasıl bulabiliriz '''

print(type(image))

'''bir önceki derslerimizde bahsetmiştik bunu olarak <class 'numpy.ndarray'> 
gelmektedir diye
'''

''' elimiz de ki resmin pixel sayısını nasıl bulabilriz ?'''

print(image.size)# 151353 adet pixel bulunmakta imiş resmimizde

''' resmimizin nasıl data-tipini bulabiliriz onu görelim birde =D'''

print(image.dtype)#uint8 olarak dönmekte ve buna göre bütün
'matematiksel hesaplamlarımızı yapmaktayız'

'Yükseklik genişlik hakkında bize bilgi vermektedir' \
'bunu parcalama işlemleri ile resmimizin belli bir kısmını nasıl ' \
'alacagımıza dair bir kac proje yapacagız' \
'yani kısca pixelllerimizin belli bir kısmını allacagız'

print(image.shape)
'''Gelen bilgimiz çok ilignç =)'''
'''(251, 201, 3)'''
''' gelen bilhimize ilginc demein sebebi (251, 201, 3) böyle bir cıktı 
 alıyoruz 
    251 =>heigth
        201=>witdh
            3=> color channel
            
    ilk data yükseklik 2. data genişlik 3. data ise renklermizin kanalı
    renklerimizin kanalı bize 1 resimde ki renk değerlerini göstermektedir  
 
 '''

'''Sadece bir pixelimizn o bgr kodlarını ayırarak biz hangi değer
oldugunu görebilme sansımız da bulunmakta '''

print(image.item(0,#burrada 0. sutunda ki pixellerden
                 0,# 0. ki satırda ki pixelin
                 1))# bgr demiştik burada 1 yazıyorquz bize green değerini
                    # dönsün diye 0 yazarsak blue döner 2 yazarsak red döner

'burada ise resmimizi göster diyoruz'
cv2.imshow('İmage',image)

cv2.waitKey(0)
cv2.destroyAllWindows()