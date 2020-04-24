# Giriş

Projede hedef gösterilen bir sayfaya önceden hazırlanmış olan wordlistler ile fuzzing işlemi yapılmaktadır. Kendi makinam üzerinde basit bir sayfa inşa ederek deneeleri o sayfa üzerinden göstereceğim. İlk olarak sayfanın php kodları ile başlayalım.

```php
<?php
if(isset($_POST["gonder"]))
{
	echo "istek basarili(post)";
}
if(isset($_GET["gonder"]))
{
	echo "istek basarili(get)";
}
?>
<html>
	<body>
		<form action="" method="post">
			<input type="text" name="isim" ></br>
			<input type="text" name="soyisim">
			<input name="gonder" type="submit" value="gönder">
		</form>

		 <form action="" method="get">
                        <input type="text" name="isim" ></br>
                        <input type="text" name="soyisim">
                        <input name="gonder" type="submit" value="gönder">
                </form>


	</body>
</html>

```
Anlaşıldığı üzere 2 adet form bulunmaktadır. Bunun gibi durumlarda proje sayfadaki form sayısını tespit edip kullanıcıya hangi formu seçmek istediğini soracaktır.

## Analiz

Projeyi başlattığımızda bizden hedef sitenin adresini ve wordlist dosyasını istemektedir.


<img src="https://raw.githubusercontent.com/berenkg/python_gorev/master/fuzz/img/foto1.PNG" style="width:100%;">

Görüldüğü üzere sayfada birden fazla HTML FORM buunmaktadır. BUndan dolayı proje bize bir seçim yapmamızı söyleyecektir. İlk olara tespit edilen formları görelim. Burada form elemanını seçmemiz gerekecektir. 1. Formu seçelim.

<img src="https://raw.githubusercontent.com/berenkg/python_gorev/master/fuzz/img/foto2.PNG" style="width:100%;">

Proje bize özet bilgiler gösterdikten sonra ayrıntılı bilgiler ister misiniz? diye bir soru sordu bunu evet şeklinde cevapladığımızda çıktının wiresharktaki ile ayı olduğunu görebiliriz.

<img src="https://raw.githubusercontent.com/berenkg/python_gorev/master/fuzz/img/foto3.PNG" style="width:100%;">

`CSRF Tespit edilmiş olabilir` ifadesi form elemanlarının bir value'su varsa o değerlerde bir değişiklik yapılmadığından ekrana basılmıştır. Bu sayfada bir CSRF Token yoktur ancak buton'un bir value değeri vardır. Şİmdi dönen cevabı görüntüleyelim. 

<img src="https://raw.githubusercontent.com/berenkg/python_gorev/master/fuzz/img/foto4.PNG" style="width:100%;">

Burada wordlist dosyasıdaki kelimeler kadar stek gömderlmiştir ve suncuudan dönen cevaplar ekrana basılmıştır. Dikkat edereniz dönen html kodları içerisinde `istek başarılı` ifadesibi görebilirsiniz. Bu POST yada GET isteiğinin başarılı bir şekilde yapıldığını göstermektedir.