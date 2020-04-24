# Giriş

Projede Wireshark aracılığı ile bazı paketler yakalanmıştır ve daha sonrasında analizi yaılması için scapy modülünden yararlanılmıştır. Yakalanan paketler `/paketler` klasörü altına eklenmiştir. rojeyi çalıştırmak için `python3` ve `python3-scapy` modülüne sahip olmanız gerekmektedir.  

## Analiz

İLk olarak aşağıdaki fotoğrafta wireshark üzerinde yakalanan paketler gösterilmiştir. BU paketlerden örnek olarak 1. ICMP paketini seçelim ve kıyaslamamızı bunun üzerine yapalım.

<img src="/img/foto2.PNG" style="width:100%;">

Projeyi başlatalım ilk karşılama ekranında bize bazı istatitikler verecektir. Biz burada ICMP seçeneği ile daevam edeceğiz.

<img src="/img/foto3.PNG" style="width:100%;">

Proje bize özet bilgiler gösterdikten sonra ayrıntılı bilgiler ister misiniz? diye bir soru sordu bunu evet şeklinde cevapladığımızda çıktının wiresharktaki ile ayı olduğunu görebiliriz.

<img src="/img/foto4.PNG" style="width:100%;">


