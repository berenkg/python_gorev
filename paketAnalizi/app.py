from scapy.all import *

def genelIstatistik(packets):
    toplamUDP =len(packets[UDP])
    toplamTCP =len(packets[TCP])
    toplam =len(packets)
    print("")
    print("[*]Toplam Paket sayısı", str(toplam))
    print("[*]Toplam TCP Paket sayısı", str(toplamTCP))
    print("[*]Toplam UDP Paket sayısı", str(toplamUDP))
    print("")

def menu(packets):
    print("1. TCP Paketlerinin özetlerini listelemek için 1")
    print("2. UDP Paketlerinin özetlerini listelemek için 2")
    print("3. ICMP Paketlerinin özetlerini listelemek için 3")
    print("4. Çık")
    print("") 

    cevap = input("Lütfen seçiminizi yapınız. (örn: 1)\r\n")
    if(cevap == "1"):
        paketNumarasi = 0
        for i in packets[TCP]:
            paketNumarasi =+ 1
            pCevap = input("[*] Ayrıntılı bilgi ister misiniz?(e/h/q)")

            if(pCevap == "q"):
                break
            print("-------------------------------------")
            print("-------------------------------------")
            print("Özet Bilgiler[",str(paketNumarasi),"]:\r\n-------------------")
            print("Kaynak IP:", i[IP].src)
            print("Kaynak Port:", i[TCP].sport)
            print("Hedef IP:", i[IP].dst)
            print("Hedef Port:", i[TCP].dport)
            print("Protokol:", i[IP].proto)
            print("Tip:", i.type)


            if(pCevap != "h"):
                print("-------------------\r\n")
                print("IP\r\n", i[IP].show())
                print("TCP\r\n", i[TCP].show())
                try:
                    print("Raw\r\n", i[Raw].show())
                except:
                    continue
                print("-------------------------------------")
                print("-------------------------------------")
                devam = input("")

    if(cevap == "2"):
        paketNumarasi = 0
        for i in packets[UDP]:
            paketNumarasi =+ 1
            pCevap = input("[*] Ayrıntılı bilgi ister misiniz?(e/h/q)")

            if(pCevap == "q"):
                break

            print("-------------------------------------")
            print("-------------------------------------")
            print("Özet Bilgiler[",str(paketNumarasi),"]:\r\n-------------------")
            print("Kaynak IP:", i[IP].src)
            print("Kaynak Port:", i[UDP].sport)
            print("Hedef IP:", i[IP].dst)
            print("Hedef Port:", i[UDP].dport)
            print("Protokol:", i[IP].proto)
            print("Tip:", i.type)

            

            if(pCevap != "h"):
                print("-------------------\r\n")
                print("IP\r\n", i[IP].show())
                print("UDP\r\n", i[UDP].show())
                try:
                    print("Raw\r\n", i[Raw].show())
                except:
                    continue
                print("-------------------------------------")
                print("-------------------------------------")
                devam = input("")

    if(cevap == "3"):
        paketNumarasi = 0
        for i in packets[ICMP]:
            paketNumarasi =+ 1
            pCevap = input("[*] Ayrıntılı bilgi ister misiniz?(e/h/q)")

            if(pCevap == "q"):
                break

            print("-------------------------------------")
            print("-------------------------------------")
            print("Özet Bilgiler[",str(paketNumarasi),"]:\r\n-------------------")
            print("Kaynak IP:", i[IP].src)
            print("Hedef IP:", i[IP].dst)
            print("Protokol:", i[IP].proto)
            print("Tip:", i.type)

            

            if(pCevap != "h"):
                print("-------------------\r\n")
                print("IP\r\n", i[IP].show())
                print("UDP\r\n", i[ICMP].show())
                try:
                    print("Raw\r\n", i[Raw].show())
                except:
                    continue
                print("-------------------------------------")
                print("-------------------------------------")
                devam = input("")

    if(cevap == "4"):
        exit()

print("[*] Bu uygulamada belirtilen pcap dosyalarından aşağıdaki analizler yapıalcaktır. Analiz işlemleri için ilk önce paket dosyasının tam yolunu belirtiniz daha sonrasında seçim yapınız.")

paketAdi = input("[*] Paket adını belirtiniz:\r\n")

#Paket dosyasından okuma
packets = rdpcap(paketAdi)

while(1):
    genelIstatistik(packets)
    menu(packets)