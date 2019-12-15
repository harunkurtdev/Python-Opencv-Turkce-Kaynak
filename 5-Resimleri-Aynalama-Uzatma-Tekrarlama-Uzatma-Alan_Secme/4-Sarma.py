import cv2

'okdugumuz rsmi atadık'
image=cv2.imread('image.jpg')
'burada copymakeBorder ile işlemeler yapıyoruz 4 derstir' \
'asıl amac bu fonksiyonun bir şeyi kopyalayarak copyladagı resim üzerinde' \
'değişiklikler yapabilmemizi sağlamaktadır' \
'borderType bize hangi işlem yapacaksak onu söyler' \
'top yukarıdan boşluk bırakır left soldan bottom aşağıdan ' \
'diye value ise bize bıraktıgımız boslukları doldurmamaıza yarar sağlar ' \
've böylelikle resmimizi işlemiş oluruz...'

constant=cv2.copyMakeBorder(image,#hangi resim işlenecekse
                            100,100,100,100,#padding diyebilirz buna =)
                            cv2.BORDER_CONSTANT,#borderType ını belirlemiş o
                            #oluyoruz Constat ise sarmlama tarzı bir kelime bbirleiştir
                            #mede diye geçmektedir
                            value=[255,0,255])#burası cok önemlidir value ile biz bir değer
                            #vererek bunun etrafındaki rengi belirliyoruz sarmlama için gerekli
                            #olan

'imshow ile işlenmiş resmi gösteriyoruz'
cv2.imshow('Constat',constant)

'imshow ile orjinal resmi gösteriyoruz'
cv2.imshow('Orjinal',image)

cv2.waitKey(0)
cv2.destroyAllWindows()