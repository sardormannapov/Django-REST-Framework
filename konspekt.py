#APIView - bu rest_framework-dan olinadi, lekin views-da ishlatiladigan va CRUD qilish uchun paketlarimizni eng kattasidan biri bu APIView bo'ladi
#Response - bu bizga qaytiyotgan ma'lumot(narsa) postmanni console-da chiqotgan ma'lumotimiz

# class Meta:
#     model = Person
#     fields = "__all__" - mana shu ko'd ham get qiloladi, ham create qiloladi, ham update qiloladi, ham delete qiloladi

#APIView - bu eng главный ota class
#generics bor
 #CreateAPIView - bu POST запрос uchun
 #ListAPIView - bu GET запрос uchun (ma'lumotlarni ovolish uchun)
 #RetriveAPIView - bu GET запрос, lekin hamma ma'lumotlarni olib kemidi, faqqat bitta конкретный ma'lumotni olib keladi
 #DestroyAPIView - bu DELETE запрос uchun
 #UpdateAPIView - bu PUT va PATCH запрослар uchun
 #ListCreateAPIView - bu GET запрос bilan POST запрос birlashtirilgan
 #RetriveUpdateAPIView - bu GET запрос(конкретный запрос) bilan PUT va PATCH запрослар birlashtirilingan
 #RetriveDestroyAPIView - bu GET запрос(конкретный запрос) bilan DELETE запрос birlashtirilingan
 #RetriveUpdateDestroyAPIView - bu GET запрос(конкретный запрос), PUT va PATCH запрослар va DELETE запрос, uchtasi birlashtirilingan

 #queryset - bizda models bilan ishlidi

#ORM - bu model
#Meta - bu специальный конструктор, har doim Meta deb yoziladi
#generics-lar to'g'ridan to'g'ri models bilan ishlidi, shuning uchun cat deb yoziladi postman-da
#viewsets har doim router-lar bilan ishlidi
#router - bu masalan biz urls yozamizku, shu urls-larni qismlarga bo'lib router-larga bog'lab qo'ysak bo'ladi
 #bizda 2-xil routerlar mavjud:
  #1)Simple router
  #2)Default router
  #Simple router bilan Default routerni farqi nima
  #Simple router-da biz "api/v1/" url-ni o'zini chaqiromimiz
  #Default router-da biz "api/v1/" url-ni chaqirolamiz, agar biz "api/v1/" urls-ni bersak bizga указать qilib beradi полный urls-ni ko'rsatib

#mixins - bu ModelViewSet-ni ichida get, post, put, patch, delete, retrive get запросларни bajarotti
#get_queryset qilganimizda urls-da router-ni register qivotganimizda "basename" bo'lishi shart(kerak)
 #get_queryset - bu bizga ma'lumotlarni olib keladi lekin biz bergan limitgacha, masalan [:3] bizga birinchi uchta ma'lumotlarni olib kelsin degani
 #get_queryset har doim basename bilan ishlidi, basename-siz ishlayomidi

#action-lar bor
 #action - bu masalan bitta url-ni ichida qo'shimcha yana bitta url yasasak bo'ladi

