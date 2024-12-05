# 1-masala
# ijobiyson = 0
# sonlar = int(input("Ijobiy son kiriting:"))
#
# while ijobiyson != sonlar:
#     print("Bu ijobiy son emas")
#     sonlar = int(input("Ijobiy son kiriting:"))
# print("Bu ijobiy son.")
# 2-masala
# i = 2
# while i <= 100:
#     print(i)
#     i += 2
# 3-masala
# import random
# maxfiyson = random.randint(1,11)
# while True:
#     son = int(input("Maxfiy sonni toping:"))
#     if maxfiyson != son:
#         print("Yo'q siz topolmadingiz!")
#     else:
#         print("Qoyil siz topdingiz!")
#         break
# 4-masala
# while True:
#     matn = str(input("Matn kiriting:"))
#     if matn != "stop":
#         print(matn)
#     else:
#         break
# 5-masala
# while True:
#     son1 = int(input("Birinchi sonni kiriting:"))
#     son2 = int(input("ikkinchi sonni kiriting:"))
#     son3 = int(input("Uchinchi sonni kiriting:"))
#     yigindi = son1 + son2 + son3
#     if yigindi != 0:
#         print("Yig'indi:",yigindi)
#     else:
#         break
#     ques = int(input("Davom etamizmi?:"))
#     if ques == 1:
#         continue
#     else:
#         break
# 6-masala
# while True  :
#     son = int(input("Son kiriting:"))
#     yigindi = sum(range(1, son))
#     print(yigindi)
# 7-masala
# i = 1
# while i < 20:
#     print(i)
#     i += 2
# 8-masala
# parol = "parol"
# inparol = str(input("Parolni kiriting:"))
# while parol != inparol:
#     print("Bu parol mos emas!")
#     inparol = str(input("Parolni kiriting:"))
# print("Parol to\'g\'ri!")
# 9-masala
# n = int(input("Son kiriting:"))
# i =1
# while i <= n:
#     print(i)
#     i +=1
# 10-masala
# while True:
#     son1 = int(input("Birinchi sonni kiriting:"))
#     son2 = int(input("ikkinchi sonni kiriting:"))
#     son3 = int(input("Uchinchi sonni kiriting:"))
#     yigindi = son1 + son2 + son3
#     if son1 < 0:
#         print("Kechirasiz bu son manfiy ", son1)
#         break
#     elif son2 < 0:
#         print("Kechirasiz bu son manfiy ", son2)
#         break
#     elif son3 < 0:
#         print("Kechirasiz bu son manfiy ", son3)
#         break
#     elif yigindi != 0:
#         print("Yig'indi:",yigindi)
#     else:
#         break
#     ques = int(input("Davom etamizmi?:"))
#     if ques == 1:
#         continue
#     else:
#         break
# 11-masala
# while True:
#     son1 = int(input("Birinchi sonni kiriting:"))
#     son2 = int(input("ikkinchi sonni kiriting:"))
#     son3 = int(input("Uchinchi sonni kiriting:"))
#     yigindi = son1 + son2 + son3
#     if son1 > 0:
#         print("Kechirasiz bu son musbat", son1)
#         break
#     elif son2 > 0:
#         print("Kechirasiz bu son musbat", son2)
#         break
#     elif son3 > 0:
#         print("Kechirasiz bu son musbat", son3)
#         break
#     print(son1, son2, son3)
#     ques = int(input("Davom etamizmi?:"))
#     if ques == 1:
#         continue
#     else:
#         break
# 12-masala
# while True:
#     ism = str(input("Ismizni kiriting:"))
#     if ism != "stop":
#         print(ism)
#     else:
#         print("Stopped!")
#         break
# 13-masala
# i = 0
# while i < 100:
#     i += 1
#     print(i**2)
# 14-masala
# import math
# while True:
#     son = int(input("Biror son yozing:"))
#     if son > 0:
#         print(son,"ning faktoriali",math.factorial(son))
#     else:
#         print("Bu manfiy son")
#         break
# 15-masala Fibonacci
# while True:
#     n = int(input("Biror son yozing:"))
#     son1 = int(0)
#     son2 = 1
#     knraqam = son1
#     count = 1
#     while count <= n:
#         print(knraqam)
#         count += 1
#         son1, son2 = son2, knraqam
#         knraqam = son1 + son2
#     print()
# 16-masala
# while True:
#     ism = str(input("Ismingizni kiriting:"))
#     if ism != "exit":
#         print("Salom",ism)
#     else:
#         break
#17-masala
# i = 1
# while i <= 100:
#     if i%3==0 :
#         print(i)
#     i += 1
#18-masala
# while True:
#     yosh = int(input("Yoshingizni kiriting:"))
#     if yosh >= 18:
#         print("Voyaga yetgansiz!")
#     elif yosh <= 18 and yosh > 0:
#         print("Siz hali kichkinasiz")
#     else:
#         print("Siz hali tugilmagansiz")
#         break
#19-masala
# while True:
#     son = int(input("Son kiriting:"))
#     if son != 0:
#         kv = son**2
#         print(kv)
#     else:
#         break
#20-masala
# while True:
#     son1 = int(input("Birinchi sonni kiriting:"))
#     son2 = int(input("ikkinchi sonni kiriting:"))
#     son3 = int(input("Uchinchi sonni kiriting:"))
#     yigindi = son1 + son2 + son3
#     if yigindi != 0 and son1%2==1 and son2%2==1 and son3%2==1:
#         print("Yig'indi:",yigindi)
#     else:
#         print("Sonlar orasida jufti bor")
#         break
#     ques = int(input("Davom etamizmi?:"))
#     if ques == 1:
#         continue
#     else:
#         break
#21-masala
# def count_vowels(text):
#     vowels = "aeıioöuüAEIİOÖUÜ"
#     count = 0
#     index = 0
#
#     while index < len(text):
#         if text[index] in vowels:
#             count += 1
#         else:
#             pass  # Bu kısmı geçiyoruz, ek işlem yok
#         index += 1
#     return count
# # Kullanıcıdan metin alıp ünlü sayısını bulma
# text = input("Bir metin girin: ")
# vowel_count = count_vowels(text)
# print("Metindeki ünlü harf sayısı:", vowel_count)
#22-masala
# while True:
#     son1 = int(input("Birinchi sonni kiriting:"))
#     son2 = int(input("ikkinchi sonni kiriting:"))
#     kopaytma = son1 * son2
#     if kopaytma != 0 and son1!=0 and son2==0 or son1==0 and son2!=0:
#         print("Ko'paytma:",kopaytma)
#     else:
#         break
#     ques = int(input("Davom etamizmi?:"))
#     if ques == 1:
#         continue
#     else:
#         break
#23-masala
# while True:
#         son = int(input("Biror son kiriting:"))
#         if son !=0 and son%10==0:
#             print(son//10)
#             son += 1
#         else:
#             break
#24-masala
# while True:
#     son = int(input("Qaysidir sonni kiriting:"))
#     if son**2 <=1000:
#         print(son**2)
#         son =+1
#     else:
#         print("Bu sonning kvadrati 1000dan katta!")
#25-masala
# while True:
#     son1 = int(input("Birinchi sonni kiriting:"))
#     son2 = int(input("ikkinchi sonni kiriting:"))
#     son3 = int(input("Uchinchi sonni kiriting:"))
#     if son1>son2 and son1>son3:
#         print(son1)
#     elif son2>son1 and son2>son3:
#         print(son2)
#     else:
#         print(son3)
#     ques = int(input("Davom etamizmi?:"))
#     if ques != 0:
#         continue
#     else:
#         break
#26-masala
# while True:
#     son1 = int(input("Birinchi son:"))
#     son2 = int(input("Ikkinchi son:"))
#     if son1 != 0 and son2 != 0:
#         print(son1+son2)
#         print(son1-son2)
#         print(son1*son2)
#         print(son1/son2)
#     else:
#         break
# 27masala
# while True:
#     ism = str(input("Matn kiriting:"))
#     if ism != "stop":
#         for i in ism:
#             print(i)
#     else:
#         break
# 28masala
# while True:
#     ism = str(input("Matn kiriting:"))
#     if ism != "exit":
#       print(ism[::-1])
#     else:
#         break
# 29masala
# import math
# while True:
#     son = int(input("Biror son yozing:"))
#     if son > 0:
#         print(son,"ning faktoriali",math.factorial(son))
#     else:
#         print("Bu manfiy son")
#         break
# 30masala
# while True:
#     son = int(input("Biror son kiriting:"))
#     if son%2==0:
#         print(son**2)
#     elif son == -1:
#         break
#     else:
#         print("Bu son toq!")
#         continue
# 31masala
# for i in range(11):
#     print(i)
#32-masala
# son = int(input("Enter a number: "))
# for i in range(son, 0, -1):
#     print(i)
# #33-masala
# for i in range(0, 21, 2):
#     print(i)
# #34-masala
# son = int(input("Enter a number: "))
# if son % 2 == 0:
#     for i in range(son, 500,2):
#         print(i+1)
# elif son % 2 == 1:
#     for i in range(son, 500,2):
#         print(i)
# #35-masala
# p = "Python"
# for i in p:
#     print(i)
# #36-masala
# for i in range(11):
#     print(i**2)
# #37-masala
# p = "salom dunyo"
# for i in p:
#     print(p)
# #38-masala
# sum = 0
# for i in range(101):
#     sum +=i
#     print(sum)
# #39-masala
# matn = str(input("Matn kiriting:"))
# for i in matn:
#     print(i)
# #40-masala
#....
# #41-masala
# import  random
# for i in range(10):
#     print(random.randint(0,999))
# #42-masala
# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))
# son3 = int(input("3-sonni kiriting: "))
# son4 = int(input("4-sonni kiriting: "))
# son5 = int(input("5-sonni kiriting: "))
# son6 = int(input("6-sonni kiriting: "))
# son7 = int(input("7-sonni kiriting: "))
# son8 = int(input("8-sonni kiriting: "))
# son9 = int(input("9-sonni kiriting: "))
# son10 = int(input("10-sonni kiriting: "))
# print("Musbat sonlar: ")
# if son1 >= 0:
#     print(son1)
# elif son2 >= 0:
#     print(son1)
# elif son3 >= 0:
#     print(son1)
# elif son4 >= 0:
#     print(son1)
# elif son5 >= 0:
#     print(son1)
# elif son6 >= 0:
#     print(son1)
# elif son7 >= 0:
#     print(son1)
# elif son8 >= 0:
#     print(son1)
# elif son9 >= 0:
#     print(son1)
# elif son10 >= 0:
#     print(son1)
# else:
#     print("Blar hammasi manfiy o'xshidi!")
# 43masala
# matn = str(input("Enter a text: "))
# unli = "aeuio"
# hisob = 0
# for i in matn:
#         if i in unli:
#             hisob +=1
# print("Matnda",hisob,"ta unli bor")
# 44masala
# import math
# son = 0
# for son in range(1,11):
#     print(math.factorial(son))
#     son += 1
# 45masala
# son = 0
# for son in range(1,21):
#     print(son**3)
#     son += 1
# 46masala
# matn = str(input("Enter a text: "))
# print(matn.strip())
# #47masala
# print(matn.lower())
# #48masala
# print(matn.find("Python"))
# #49masala
# print(len(matn))
# #50masala
# print(matn.capitalize())
# #51masala
# print(matn.title())
# #52masala
# print(matn.rjust(10))
# #53masala
# print(matn.replace("a","o"))
# #54masala
# print(matn.startswith("Hello"))
# #55masala
# print(matn.endswith("!"))
# #56masala
# print(matn.isdigit())
# #57masala
# print(matn.split(""))
# #58masala
# print(matn.swapcase())
# #59masala
# print(matn.isalpha())
# #60masala
# print(matn.zfill(10))
# 61masala
# son = 0
# if son >0:
#     print("Musbat")
# elif son ==0:
#     print("0 ga teng")
# else:
#     print("Manfiy")
# 62masala
# soz = "Python"
# unli = "euiao"
# undosh = "qwrtypsdfghjklzxcvbnm"
# cout_unli = 0
# cout_undosh = 0
# for i in soz:
#     if i in unli:
#         cout_unli += 1
#     if i in undosh:
#         cout_undosh += 1
# print(cout_unli)
# print(cout_undosh)
# 63masala
# print(sum(range(1,21)))
# 64masala
# x = "malayalam"
# w = ""
# for i in x:
#     w = i + w
#
# if x == w:
#     print("Yes")
# else:
#     print("No")
# while b<=n:
#     if b%2==0:
#        print(b)
#     b+=1
# 65masala
# a_son = int(input("Enter a son number: "))
# b_son = int(input("Enter a son number: "))
# c_son = int(input("Enter a son number: "))
# d_son = int(input("Enter a son number: "))
# e_son = int(input("Enter a son number: "))
#
# if a_son%2 ==0:
#     print(a_son)
# elif b_son%2 ==0:
#     print(b_son)
# elif c_son%2 ==0:
#     print(c_son)
# elif d_son%2 ==0:
#     print(d_son)
# elif e_son%2 ==0:
#     print(e_son)
# else:
#     print("Juft son yo'q")
#     print(a_son,b_son,c_son,d_son,e_son)
# 66masala
# soz = str(input("Enter a words: "))
# print(soz[::-1])
# 67masala
# soz = str(input("Enter a words: "))
# print(soz.count(" "))
# 68masala
# num = int(input("Enter a number: "))
# bir = 1
# faktorial = 1
# while bir <= num:
#   faktorial *= bir
#   bir += 1
# print(faktorial)
# 69masala
# a_son = int(input("Enter a son number: "))
# b_son = int(input("Enter a son number: "))
# c_son = int(input("Enter a son number: "))
# if a_son%2!=0 and b_son%2!=0 and c_son%2!=0:
#     print((a_son+b_son+c_son)/3)
# 70masala
# for i in range(1,11):
#     print(i**2)
# 71masala
# matn = [input("Enter a matn: ")]
# print(matn.sort())
# 72masala
# parol = input("Enter a parol: ")
# if len(parol) > 8:
#     print("Parolizni uzunligi:",len(parol))
# else:
#     print("Parol juda qisqa!")
# 73masala
# a_son = int(input("Enter a son number: "))
# b_son = int(input("Enter a son number: "))
# c_son = int(input("Enter a son number: "))
# if a_son > b_son and a_son > c_son:
#     print(a_son," son Eng katta!")
# elif b_son > a_son and b_son > c_son:
#     print(b_son," son Eng katta!")
# elif c_son > a_son and c_son > b_son:
#     print(c_son," son Eng katta!")
# if a_son < b_son and a_son < c_son:
#     print(a_son," son Eng kichik!")
# elif b_son < a_son and b_son < c_son:
#     print(b_son," son Eng kichik!")
# elif c_son < a_son and c_son < b_son:
#     print(c_son," son Eng kichik!")
# 74masala
# matn = "Salom Python"
# for i in matn:
#     if i in matn.upper():
#         print(i)
#     else:
#        continue
# 75masala
# while True:
#     parol = input("Enter a parol: ")
#     if parol != "python":
#         continue
#     else:
#         print("Parol tog'ri!")
#         break
# 76masala
# matn = input("Enter a matn: ")
# if matn[0]==matn[-1]:
#     print("Birinchi va oxirgi harflari bir xil")
# else:
#     print("Birinchi va oxirgi harflari bir xil emas!")
# 77masala
# import re
# matn = "salom123"
# numbers = re.findall(r'\d+', matn)
# print(sum(numbers))
# 78masala
# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))
# son3 = int(input("3-sonni kiriting: "))
# son4 = int(input("4-sonni kiriting: "))
# son5 = int(input("5-sonni kiriting: "))
# son6 = int(input("6-sonni kiriting: "))
# son7 = int(input("7-sonni kiriting: "))
# son8 = int(input("8-sonni kiriting: "))
# son9 = int(input("9-sonni kiriting: "))
# son10 = int(input("10-sonni kiriting: "))
# print("Musbat sonlar: ")
# if son1 >= 0:
#     print(son1)
# elif son2 >= 0:
#     print(son1)
# elif son3 >= 0:
#     print(son1)
# elif son4 >= 0:
#     print(son1)
# elif son5 >= 0:
#     print(son1)
# elif son6 >= 0:
#     print(son1)
# elif son7 >= 0:
#     print(son1)
# elif son8 >= 0:
#     print(son1)
# elif son9 >= 0:
#     print(son1)
# elif son10 >= 0:
#     print(son1)
# else:
#     print("Blar hammasi manfiy o'xshidi!")
# 79masala
# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))
# son3 = int(input("3-sonni kiriting: "))
# if son1%5==0:
#     print(son1)
# elif son2%5==0:
#     print(son2)
# elif son3%5==0:
#     print(son3)
# else:
#     print("Hammasi manfiy!")
# 80masala
# import random
# son = int(input("Enter a son: "))
# if son != random.randint(1,100) and son > random.randint(1,100):
#     print("Katta")
# elif son != random.randint(1,100) and son < random.randint(1,100):
#     print("Kichik")
# else:
#     print("Qoyil topdingiz!")
#81masala
# sonlar = []
# while True:
#     add = int(input("Son kiriting:"))
#     if add != 0:
#         sonlar.append(add)
#     else:
#         print(sonlar)
#82masala
# royxat =[7,5,8,1,2,4,9]
# royxat.sort()
# print(royxat[6])
# print(royxat[0])
#83masala
# royxat =[7,5,8,1,2,4,9]
# print(sum(royxat))
#84masala
# royxat =[7,5,8,1,2,4,9]
# print(sum(royxat)//len(royxat))
#85masala
# my_list = [1,2,1,8,5,2]
# new_set = set(my_list)
# print(new_set)
#86masala
# royxat =[7,5,8,1,2,4,9]
# royxat.sort()
# print(royxat)
#87masala
# royxat =[7,5,8,1,2,4,9]
# print(royxat)
# rm = int(input("Qaysi indeksni o'chirmoqchisiz?"))
# royxat.pop(rm)
# print(royxat)
#88masala
# royxat =[7,5,8,1,2,4,9]
# indx = int(input("Qaysi indeksdaki kerak?"))
# print(royxat[indx])
#89masala
# words = ["salom", "good", "bye", "welcome"]
# words.sort()
# print(words)
#90masala
# words = ["salom", "good", "bye", "welcome"]
# indx = str(input("Ro'yxatdaki so'zni kiriting:"))
# if words.count(indx) != 0:
#     print(indx, "-ro'yxatda bor!")
# else:
#     print(indx, "ro'yxatda yo'q!")
#91masala
# bir_list=["bir","ikki","uch"]
# iki_list=["to'rt","besh","olti"]
# bir_list.extend(iki_list)
# print(bir_list)
#92masala
# list=["bir","ikki","uch"]
# list.reverse()
# print(list)
#93masala
# listin=["bir","ikki","uch"]
# print(listin)
# indeks = int(input("Qaysi indeksdagi qiymatni ikkilantirmoqchisiz?"))
# add= listin[indeks]
# listin.append(add)
# print(listin)
#94masala
# royxat=[-7,5,-8,1,-2,4,9]
# for son in royxat:
#     if son > 0:
#         print(son)
#95masala
# bir_list=["besh","ikki","olti"]
# iki_list=["ikki","besh","uch"]
# for item in bir_list:
#     if item in iki_list:
#         new_list = [item]
#         print(new_list)
#96masala
# royxat=[-7,5,-8,1,-2,4,9]
# print("Musbat sonlar")
# for son in royxat:
#     if son > 0:
#         print(son)
# print("Manfiy sonlar")
# for son in royxat:
#     if son < 0:
#         print(son)
#97masala
# royxat=[-7,5,-8,1,-2,4,9]
# print(royxat)
# indx = int(input("Enter a number: "))
# print(royxat.index(indx))
#98masala
# royxat = [2, 5, -8, 9, 2, 5, 9]
# if royxat.count(0) >= 2:
#     royxat.remove(0)
#     print(royxat)
# elif royxat.count(1) >= 2:
#     royxat.remove(1)
#     print(royxat)
# elif royxat.count(2) >= 2:
#     royxat.remove(2)
#     print(royxat)
# elif royxat.count(3) >= 2:
#     royxat.remove(3)
#     print(royxat)
# elif royxat.count(4) >= 2:
#     royxat.remove(4)
#     print(royxat)
# elif royxat.count(5) >= 2:
#     royxat.remove(5)
#     print(royxat)
# elif royxat.count(6) >= 2:
#     royxat.remove(6)
#     print(royxat)
# else:
#     print(royxat)
#99masala
# royhat = [5, 6, 10, 4, 7, 1, 19]
# toq = royhat[1::2]
# print(toq)
# 100masala
# royhat = [5, 6, 10, 4, 7, 1, 19]
# juft = royhat[0::2]
# print(juft)
# 101masala
# royhat = [5, 6, 10, 4, 7, 1, 19]
# engkatta = royhat.index(max(royhat))
# engkichik = royhat.index(min(royhat))
# print(engkatta, engkichik)
# 102masala
# royhat = [5, 6, 10, 4, 7, 1, 19]
# print(royhat[-3 :])
# 103masala
# royhat = [5, 6, 10, 4, 7, 1, 19]
# print(royhat)
# rm = int(input("Qaysi indeksdakini o'chirjaksann?:"))
# royhat.pop(rm)
# print(royhat)
# 104masala
#...
#105masala
# royhat = [5, 6, 10, 4, 7, 1, 19]
# royhat.reverse()
# royhat.insert(0, royhat[-1])
# print(royhat)
# 106masala
# royxat = [input("Enter a list: ")]
# royxat.reverse()
# 107masala
# royxat = ["Salom","Nagap"]
# royxat.sort()
# print(royxat)
# 108masala
# royhat = [5, 6, 10, 4, 7, 1, 19]
# for i in royhat:
#     new_list = [i**2]
#     print(new_list)
# 109masala
# royxat = [5, 6, 10, 4, 7, 1, 19]
# royxat.sort(reverse=True)
# print(royxat)
# 110masala
# royxat = [5,[5.1,5.2], 6, 10,[10.5,10.8], 4, 7, 1, 19]
# print(royxat[1])
# 111masala
# son = 4
# if son%2==0 :
#     print("Juft")
# else:
#     print("Toq")
# 112masala
# son =0
# if son >0:
#     print("Musbat")
# elif son ==0:
#     print("0 ga teng")
# else:
#     print("Manfiy")
# 113masala
# n = int(input("Enter a number: "))
# b = 1
# while b<=n:
#     print(b)
#     b+=1
# 114masala
# n = int(input("Enter a number: "))
# b = 1
# while b<=n:
#     if b%2==0:
#        print(b)
#     b+=1
# 115masala
# list = [0,2,5,7]
# print(sum(list))
# 116masala
# soz = "Python"
# unli = "euiao"
# cout = 0
# for i in soz:
#     if i in unli:
#         cout += 1
# print(cout)
# 117masala
# soz = "Python"[::-1]
# print(soz)
# 118masala
# royxat =[7,5,8,1,2,4,9]
# royxat.sort()
# print(royxat[7])
# 119masala
# n = int(input("Enter a number: "))
# b = 1
# for i in range(1,n+1):
#     print(b**2)
#     b+=1
# 120masala
# royxat =[7,5,8,1,2,4,9][::-1]
# print(royxat)
# 121masala
# word = "kamoladdin"
# print(word)
# hafr = str(input("Qaysi harf: "))
# new = str(input("Yangi harf: "))
# print(word.replace(hafr,new))
# 123masala
# matn = "Salom dunyo!"
# print(matn.count(" "))
# 124masala
# royxat =[7,5,8,1,2,4,9]
# print(royxat)
# for i in royxat:
#     if i%2==1:
#         royxat.remove(i)
# print(royxat)
# 125masala
# matn = "Salom dunyo!"
# print(matn.upper())
# 126masala
# n = int(input("Enter a number: "))
# b=1
# for i in range(1,n+1):
#     b=b*i
#     print(b)
# 127masala
# royxat =[7,5,8,1,2,4,9]
# print(royxat)
# son = int(input("Qaysi elem:"))
# for i in royxat:
#     item=royxat.index(son)
#     kop = int(input("Qanchaga:"))
#     print(kop*item)
# 128masala
# matn = ["Salom","dunyo"]
# matn.reverse()
# print(matn)
# 130masala
# royxat =[7,5,8,1,2,4,9]
# royxat.sort()
# print(royxat)
#131masala
# list=[1,3,2,3,4,5,5]
# unikal_list= set(list)
# print(unikal_list)
#132masala
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# kesishma = set1 & set2
# print(kesishma)
#133,134masala
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# kesishma = set1 - set2
# print(kesishma)
#135masala
# matn = "lorem ipsum avagadro pedro ipsum strike"
# n = set(matn.split())
# print(n)
#136masala
# set={1,2,3,4,5}
# bir = {1}
# print(set.isdisjoint(bir))
#137masala
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# all = set1 ^ set2
# print(all)
#138masala
# set = {""}
# set.add(2)
# print(set)
#139masala
# list=[1,3,2,3,4,5,5]
# unikal_list= set(list)
# print(unikal_list)
# 140masala
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# all = set1 ^ set2
# print(all)
# 141masala
# set1={4,2,5,1,3}
# newlist = [set1]
# newlist.sort()
# print(newlist)
# 142masala
# set={4,2,5,1,3}
# set.clear()
# print(set)
# 143masala
# set1 = {"Ali", "Vali", "Olimboy"}
# set2 = {"Hasan", "Husan", "Olim"}
# if set1.isdisjoint(set2):
#     print("Umumiy ishtirokchilar yo'q.")
# else:
#     print("Umumiy ishtirokchilar bor!")
# 144masala
# set={4,2,5,1,3}
# print(max(set))
# print(min(set))
# 145masala
# set={4,2,5,1,3}
# t_item = set.pop()
# print(set)
# print(t_item)
# print(set)
#146masala
# ...
# 160masala
# 161masala
# my_tuple=(1,2,3,4,5)
# print(my_tuple.index(5))
# 162masala
# my_tuple=(1,2,2,4,5,5)
# print(my_tuple.count(2))
# 163masala
# tuple_1=(1,2,3)
# tuple_2=(3,5,7)
# all_tuple=tuple_1+tuple_2
# print(all_tuple)
# 164masala
# my_tuple=(1,2,2,4,5,5)
# print(max(my_tuple))
# print(min(my_tuple))
# 165masala
# my_tuple=(1,2,2,4,5,5)
# print(len(my_tuple))
# 166masala
# my_tuple=(1,2,2,4,5,5)
# tuple_list =list(my_tuple)
# print(tuple_list.reverse())
# 167masala
# my_tuple=(1,(2.1,2.2,2.3),(3.1,3.2,3.3),5)
# print(my_tuple[1][2])
# 168masala
# my_tuple=(1,3,2,4,7,5)
# tuple_list =list(my_tuple)
# tuple_list.sort()
# my_tuple =tuple(tuple_list)
# print(type(my_tuple))
# 169masala
# my_tuple=(1,3,2,4,7,5)
# if 2 in my_tuple:
#     print("This number in tuple!")
# else:
#     print("This number not in tuple!")
# 170masala
# my_tuple=(1,3,2,4,7,5)
# print(sum(my_tuple))
# 171masala
# my_tuple=("Kamoladdin","Jumanazarov")
# tuple_str =str(my_tuple)
# print(tuple_str.upper())
# 172masala
# my_tuple=(1,3,2,4,7,5)
# for i in my_tuple:
#     if i % 2 == 0:
#         print(i)
# 173masala
# tuple_name = ("Kamoladdin","Sayilxon","Hamidbek")
# tuple_surename = ("Jumanazarov","Yoldashev","Ismoilov")
# fish = tuple(zip(tuple_name, tuple_surename))
# print(fish)
# 174masala
# //
# //
# //
# 175masala
# my_tuple=(1,"mrx",True)
# print(type(my_tuple[0]))
# print(type(my_tuple[1]))
# print(type(my_tuple[2]))
# 176masala
# my_dict= {"name1":"Kamoladdin","name22":"Sardor","name333":"Jasurbek"}
# print(len(my_dict.keys()))
# print(len(my_dict.values()))
# 177masala
# my_dict= {"name1":"Kamoladdin","name22":"Sardor","name333":"Jasurbek"}
# print(max(my_dict.values()))
# 178masala
# my_dict={"one":1,"two":2,"three":3}
# print(sum(my_dict.values()))
# 179masala
# my_dict={"one":1,"two":2,"three":3}
# keys= str(my_dict.keys())
# print(keys.upper())
# 180masala
# my_dict={"one":1,"two":1,"three":2}
# values= set(my_dict.values())
# print(values)
# 181masala
# def OddEven(num):
#     if num % 2 == 0:
#         print(f"{num}-Even")
#     else:
#         print(f"{num}-Odd")
# OddEven(4)
# 182masla
# def Som(*numbers):
#     return sum(numbers)
# print(Som(1,2,5,7))
# 183masala
# def palindrome(word):
#     return word[::-1] == word
# print(palindrome("kiyik"))
# 184masala
# def Word_list(*list):
#     print(f"Eng katta:{max(list)}")
#     print(f"Eng kichik:{min(list)}")
# Word_list("bir","ikki","yetti")
# 185masala
#none
# 186masala
# def user_info(**info):
#     for key, value in info.items():
#         print(f"{key}: {value}")
# ism = str(input("Enter your name:"))
# yow = int(input("Enter your age:"))
# cry = str(input("Enter your country:"))
# user_info(name=ism,age=yow,country=cry)
# 187masala
# none
# 188masala
# import math
# def Factorial(son):
#     if son > 0:
#         print(f"{math.factorial(son)}")
# Factorial(5)
# 189masala
# def Print_vowels(text):
#     undosh = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
#     unli = "aeuioAEUIO"
#     final = [each for each in text if each in unli]
#     print(final)
# Print_vowels(text = input("Enter a text:"))
# 190masala
# import math
# def ekub(a,b):
#     while b:
#         a, b = b, a % b
#     return a
# print(ekub(9,12))
# 191masala
# def masala11(numbers):
#     once = set()
#     twice = set()
#     for i in numbers:
#         if i in once:
#             twice.add(i)
#         else:
#             once.add(i)
#     return twice
# lst=[1,2,2,5,5]
# print(masala11(lst))
# 192masala
# def word_cout(word):
#     print(word)
# word_cout("salom")
# 193masala
# ...
# 194masala
# def kvadrat(*list):
#     for i in list:
#         print(i ** 2)
# kvadrat(1, 2, 4, 5)
# 195masala
# ...
import math


# 196masala
# a = int(input("Natural son: "))
#
# if a % 2 == 0:
#     if a % 4 ==0:
#        print("Bu son juft va 4ga bo'linadi.")
#     else:
#          print("Bu son 4ga bolinmaydi.")
# else:
#     print("Bu son toq")
# 197masala
# a = int(input("Natural son: "))
#
# if a % 2 == 1:
#     if a % 5 ==0:
#        print("Bu son toq va 5ga bo'linadi.")
#     else:
#        print("Bu son 5ga bo'linmaydi.")
# else:
#     print("Bu son juft ")
# 198masala
# a = int(input("Natural son: "))
#
# if a % 2 == 1:
#     if a % 7 ==0:
#        print("Bu son toq va 7ga bo'linadi.")
#     else:
#        print("Bu son 7ga bo'linmaydi.")
# else:
#     print("Bu son juft")
# 199masala
# a = int(input("Natural son: "))
#
# if a % 2 == 0:
#     if a % 10 ==0:
#        print("Bu son juft va 10ga bo'linadi.")
#     else:
#         print("Bu son 10ga bo'linmaydi.")
# else:
#     print("Bu son toq.")
# 200masala
# a = int(input("Quti eni: "))
# b = int(input("Quti bo'yi: "))
# m = int(input("Eshik m: "))
# n = int(input("Eshik n: "))
#
# if a <= m and b <= n:
#     print("Quti eshikdan o'ta oladi.")
# else:
#     print("Quti teshikdan o'ta olmaydi")
# 201masala
# a = int(input("Son : "))
# if a>0 :
#     print("Bu son musbat.")
# elif a==0:
#     print("Bu son 0")
# else:
#     print("Bu son manfiy.")
# 202masala
# a = int(input("Brusni eni : "))
# d = int(input("G'o'lani eni : "))
# if d >= a:
#     print("G'o'la brussni kesa oladi.")
# else:
#     print("G'o'la brussni kesa olmaydi.")
# 203masala
# s = int(input("Zal tomoni: "))
# r = int(input("Sahna radiusi: "))
#
# if 4*2<10:
#     print("Sahna sig'adi va ",((10)-(4*2))/4, "metr joy qoladi."  )
# elif 4*2==10:
#     print( "Sahna sig'adi lekin joy qolmaydi")
# else:
#     print("Sahna Zalga sig'maydi")
# 204masala
# if 4*2<10:
#     print("Sahna sig'adi va ",((10)-(4*2))/4, "sm joy qoladi."  )
# elif 4*2==10:
#     print( "Sahna sig'adi lekin joy qolmaydi")
# else:
#     print("Sahna Zalga sig'maydi")
# 205masala
# print("Eslatib o'tamiz vagonda faqat 10ta o'rin mavjud.")
# n = int(input("Vagon raqami: "))
# if n == 1:
#     print("Sizni joyingiz vagonning 1-bo'lmasini pastgi qismda ")
# elif n == 2:
#     print("Sizni joyingiz vagonning 1-bo'lmasini yuqori qismda ")
# elif n == 3:
#     print("Sizni joyingiz vagonning 2-bo'lmasini pastgi qismda ")
# elif n == 4:
#     print("Sizni joyingiz vagonning 2-bo'lmasini yuqori qismda ")
# elif n == 5:
#     print("Sizni joyingiz vagonning 3-bo'lmasini pastgi qismda ")
# elif n == 6:
#     print("Sizni joyingiz vagonning 3-bo'lmasini yuqori qismda ")
# elif n == 7:
#     print("Sizni joyingiz vagonning 4-bo'lmasini pastgi qismda ")
# elif n == 8:
#     print("Sizni joyingiz vagonning 4-bo'lmasini yuqori qismda ")
# elif n == 9:
#     print("Sizni joyingiz vagonning 1-yon bo'lmasini pastgi qismda ")
# elif n == 10:
#     print("Sizni joyingiz vagonning 1-yon bo'lmasini yuqori qismda ")
# else:
#     print("Joy raqami bu vagonga tegishli emas.")
# 206masala
# pul = int(input("Qancha pulingiz bor: "))
# print("500 so'mlik = 1")
# print("100 so'mlik = 2")
# print("10 so'mlik = 3")
# print("2 so'mlik = 4")
# valyuta = int(input("Qanday tangaga almashmoqchisiz:"))
#
# if valyuta == 1:
#     print(pul // 500, "ta 500 so'mlik tanga olasiz")
# elif valyuta == 2:
#     print(pul//100,"ta 100 so'mlik tanga olasiz")
# elif valyuta == 3:
#     print(pul//10,"ta 10 so'mlik tanga olasiz")
# elif valyuta == 4:
#     print(pul//2, "ta 2 so'mlik tanga olasiz")
# else:
#     print("Uzur bunday pul birligi yoq.")
# 207masala
# a = int(input("Kub tomoni : "))
# b = int(input("Konusning boyi:"))
# c = int(input("Konusning radiusi:"))
# kub_hajm = a**3
# konus_hajm = 3.14*(c*2)*b

# m = int(input("Suv hajmi : "))
# kub_hajm = 125
# konus_hajm = 150
# if  m <= kub_hajm and m <= konus_hajm:
#     print(" Suv kubga va konusga mos keladi.")
# elif m <= kub_hajm and m > konus_hajm:
#     print("Suv kubga mos keladi lekin konusga mos kelmaydi.")
# elif m > kub_hajm and m <= konus_hajm:
#     print("Suv konusga mos keladi lekin kubga mos kelmaydi.")
# else:
#     print("Suv ikkisiga ham mos kelmaydi.")


# kubnihajmi = 100
# konusnihajmi = 20
# suvnihajmi = 15
#
# if kubnihajmi >= suvnihajmi:
#     print("Suv kubga togri keladi")
# elif konusnihajmi >= suvnihajmi:
#     print("Suv konusga togri keladi")
# 208masala
# a = int(input("Kub tomoni : "))
# b = int(input("Konusning boyi:"))
# c = int(input("Konusning radiusi:"))
# m = int(input("Suv hajmi : "))
# kub_hajm = a**3
# konus_hajm = (1/3)*3.14*(c*2)*b
#
# if  m <= kub_hajm and m <= konus_hajm:
#     print("Kubga va Konusga suv to'ldirish mumkin.")
# elif m <= kub_hajm and m > konus_hajm:
#     print("Kubga suv to'ldirish mumkin lekin Konusga suv to'lmaydi.")
# elif m > kub_hajm and m <= konus_hajm:
#     print("Konusga suv to'ldirish mumkin lekin Kubga suv to'lmaydi.")
# else:
#     print("Suv ikkisida ham to'lmaydi")
# 209masala
# a = int(input("A tomoni: "))
# b = int(input("B tomoni: "))
# c = int(input("C tomoni: "))
#
# if a >0 and b >0 and c > 0:
#     print("Bular uchburchak bola oladi.")
# else:
#     print("Bular uchburchak bola olmaydi.")
#
# if c == a+b:
#     print("Bu to'g'ri burchakli uchburchak.")
# else:
#     print("Bu to'g'ri burchakli uchburchak emas.")
# 210masala
#  x soni berilgan bu raqam [a;b] oraliqqa tegishli yoki yo'qligini aniqlash kerak

# x = int(input("Biror raqam kiriting: "))
# a = int(input("a nuqtani kiriting: "))
# b = int(input("b nuqtani kiriting: "))
#
# if x >= a and x <= b:
#     print("Shu oraliqqa tegishli son !")
# else:
#     print("Bu oraliqqa tegishli son emas !")
# 211masala
# x = int(input("X soni: "))
# y = int(input("Y soni: "))
# z = 1/(x*y)
# print(z)
# 212masala
# yil = int(input("Yil: "))
# asr = yil//100+1
# if yil%4==0:
#     print("Bu yil pog'ona yili va", asr, "asr")
# else:
#     print("Bu yil pog'ona yili emas va", asr, "asr")
# 213masala
# import math
# s = 144
# a = math.sqrt(s)
# k = 2
# r =6
#
# if a>=r*2+k:
#     print("Boladi")
# else:
#     print("Bolmaydi")
 
# 944LINE