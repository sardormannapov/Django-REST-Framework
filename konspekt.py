    #drf views without serializers
#Response - bu serializator-ni vazifasi yaniy lug'atni JSON formatga o'tqizish
#models-da qanaqadir o'zgartirish kiritsak har doim migrations qivolishimiz kerak
#models-da biz cat deb ketamiz chunki database-da автоматический cat_id qivoradi
#serializers-da cat_id deb ketamiz
#is_valid - bu валидация yaniy postman-da error qaytarsa odam chunadigon tilda error qilib qaytaradi
#request.data - bu biz bervoradigon parametr hisoblanadi


    #CRUD - Create, Read, Update, Delete
#Bizda get, post, put, patch, delete запрос bor
#get запрос requests qabul qimidi chunki bizga просто ma'lumotlarimizni database-dan olib kevotti
#post запрос requests qabul qiladi va bizga umumiy bitta ma'lumot qaytadi lug'atdan JSON-ga o'girilgan holda
#put запрос requests, *arguments va **kwarguments qabul qiladi
 #put запрос bitta ma'lumotni yangilidi, yaniy biz bergan ma'lumotni yangilidi
 #id orqali yangilidi
 #put запрос-да id bu **kwarguments, biz yangilamoqchi bo'lgan ma'lumotimiz bu requests
 #instance - bu database
 #if not pk bilan try, except alohida:
  #if not pk - bu agar id yozmasak bizga shuni resulti qaytadi
  #try, except bu agar mavjud bo'lmagan id yozsak
#patch запрос put запрос faqqat patch запрос-да biz qisman o'zgartirsak bo'ladi
 #partial=True bu частично o'zgartirishyaniy qisman o'zgartirish
#delete запрос requests qabul qimidi, *arguments va **kwarguments qabul qladi


  

