from bs4 import BeautifulSoup
import requests

hedefUrl = input("[*] Hedef internet adresini beliritiniz.\r\n")
istek = requests.get(hedefUrl)
wordlistPath = input("[*] HTML Formlarına basılacak olan dosya yolunu belirtiniz.\r\n")
wordlistFile = open(wordlistPath)
wordlist = wordlistFile.read()
wordlist = wordlist.split("\n")


sayfa = BeautifulSoup(istek.content, "lxml")
htmlFormlar = sayfa.find_all("form")
htmlFormSayisi = len(htmlFormlar)
if(htmlFormSayisi > 1):
    while(1):
        cevap = input("[*] Hedef sayfada birden fazla FORM elemanı bulundu. Formları görüntülemek için g tuşuna basınız. Seçim yapmak için form numarasını giriniz. Çıkmak için q tuşuuna basınız.")
        if(cevap == "q"):
            exit()

        if(cevap == "g"):
            sayac = 0
            for i in htmlFormlar:
                sayac += 1
                print("----------")
                print("Form",str(sayac))
                print(i)
                print("----------")
                devam = input("Devam etmek için bir tuşa dokununuz...")
        
        else:
            sonuc = int(cevap) - 1
            print("Seçilen FORM:\r\n")
            print("Form elemanları seçiliyor...")
            inputElemanlar = htmlFormlar[sonuc].find_all("input")
            csrf = 0
            query = ""
            for x in inputElemanlar:
                if(x.get('value') != "None"):
                    csrf = 1
                query = query + "&" + str(x.get("name")) + "=" + str(x.get("value"))
            print("Form elemanları yakalandı.")
            if(csrf == 1):
                print("CSRF Tespit edilmiş olabilir. Bazı form elemanlarının default değerleri tespit edildi. Bu elemanlarda herhangi bir değişiklik yapılmayacaktır.")

            action = str((htmlFormlar[sonuc].get("action")))
            method = str((htmlFormlar[sonuc].get("method")))
            if(action=="" or action=="#"):
                action = hedefUrl
            print("İstek Yapılacak adres:", action)
            print("İstek türü: ", method)
            

            if(method == "get"):
                for word in wordlist:
                    hedefUrl = action + "?" + query.replace("None",word)[1:]
                    hedefIstek = requests.get(hedefUrl)
                    print("[*] Hedef İstek:",hedefUrl)
                    print("[*] İstek Başarılı Bir Şekilde Gönderildi.")
                    cevap = input("Dönen cevabı görmek ister misiniz?(e/h)")
                    if(cevap == "e"):
                        print(hedefIstek.content)

            if(method=="post"):
                for word in wordlist:
                    payload = {}
                    for x in inputElemanlar:
                        if(x.get('value') != "None"):
                            payload[str(x.get("name"))] = str(x.get("value"))
                        else:
                            payload[str(x.get("name"))] = word

                    hedefIstek = requests.post(action, data = payload)
                    print("[*] Hedef İstek:",action)
                    print("[*] İstek Başarılı Bir Şekilde Gönderildi.")
                    cevap = input("Dönen cevabı görmek ister misiniz?(e/h)")
                    if(cevap == "e"):
                        print(hedefIstek.content)

if(htmlFormSayisi == 1):
    print("[*] HTML FORM yakalandı!")
    print("")
    print("")
    print(htmlFormlar[0])
    devam = input("Devam etmek için bir tuşa dokununuz...")
    print("Form elemanları seçiliyor...")
    inputElemanlar = htmlFormlar[0].find_all("input")
    csrf = 0
    query = ""
    for x in inputElemanlar:
        if(x.get('value') != "None"):
            csrf = 1
        query = query + "&" + str(x.get("name")) + "=" + str(x.get("value"))
    print("Form elemanları yakalandı.")
    if(csrf == 1):
        print("CSRF Tespit edilmiş olabilir. Bazı form elemanlarının default değerleri tespit edildi. Bu elemanlarda herhangi bir değişiklik yapılmayacaktır.")

    action = str((htmlFormlar[0].get("action")))
    method = str((htmlFormlar[0].get("method")))
    print("İstek Yapılacak adres:", action)
    print("İstek türü: ", method)
    if(action=="" or action=="#"):
        action = hedefUrl
    if(method == "get"):
        for word in wordlist:

            hedefUrl = action + "?" + query.replace("None",word)[1:]
            hedefIstek = requests.get(hedefUrl)
            print("[*] Hedef İstek:",hedefUrl)
            print("[*] İstek Başarılı Bir Şekilde Gönderildi.")
            cevap = input("Dönen cevabı görmek ister misiniz?(e/h)")
            if(cevap == "e"):
                print(hedefIstek.content)

    for word in wordlist:

        if(method=="post"):
            payload = {}
            for x in inputElemanlar:
                if(x.get('value') != "None"):
                    payload[str(x.get("name"))] = str(x.get("value"))

            for x in payload:
                if(payload[x] == "None"):
                    payload[x] = word
            

            hedefIstek = requests.post(action, data = payload)
            print("[*] Hedef İstek:",action)
            print("[*] İstek Başarılı Bir Şekilde Gönderildi.")
            print("Payload:", payload)
            cevap = input("Dönen cevabı görmek ister misiniz?(e/h)")
            if(cevap == "e"):
                print(hedefIstek.content)


