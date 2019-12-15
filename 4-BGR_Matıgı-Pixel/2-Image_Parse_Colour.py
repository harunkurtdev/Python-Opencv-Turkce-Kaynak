import  cv2
import numpy as np
'burada biz image.jpg bilgisini okyarak image atadık'
image=cv2.imread('image.jpg')

new_image=cv2.merge(cv2.split(image))

'burada ise bir önce ki derste olan konunun sadece kıslatılmış halini' \
'sadece görmekteyiz splitten gelen parametleri direk olarak merge e ' \
'atamış olduk'

new_image[:,:,0]=255

'burası cok önemlidir butada biz resmimizin parclama işlemlerini yapmaktayız ' \
've bu parcalama işlemine göre resmimizin rengini belirlemekteyiz' \
'asıl amac resmimizin renginin temasını ileri boyutlar da değistirebiliriz ' \
'demek oluyor bunu bgr kısmından birimci bölgeyi sıfır yaparak red yapabiliriz' \

'--- new_image[:,:,0:2]=255 --- yaparakta resmimizi sarı renge bürümüş olduk'

#burada ise biz resmimizi göstermekteyiz tam olarak
cv2.imshow('Mavi ekran',new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
