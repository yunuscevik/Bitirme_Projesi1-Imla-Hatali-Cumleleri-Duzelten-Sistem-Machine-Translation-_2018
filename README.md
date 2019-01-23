# Bitirme_Projesi1-Imla-Hatal-Cumleleri-Duzelten-Sistem-Machine-Translation-_2018

Projenin amacı imla hatalı cümleleri düzelten bir sistem kurmaktır. Günlük hayatta birçok kelime kısaltılarak ve imla kurallarından saptırılarak kullanılır. Bu duruma mesajlaşma dilinde "merhaba" yerine "mrhb" veya "selam" yerine "slm" kullanılması gibi veya bilgisayarda on parmak yazı yazılırken yanlış bir harfe basmak örnek olarak verilebilir. Bu durum resmi yazılarda imla bozukluğundan dolayı anlam bozukluğuna ve anlam karmaşasına yol açar.
İmla Hatalı Cümleleri Düzelten Sistem ise bu tür problemleri Türkçe imla kurallarına bağlı olarak tekrar düzenler ve bu şekilde oluşabilecek sorunların giderilmesine yardım eder. 2015 yılına ait makale, dergi, gazete gibi düzgün anlatıma sahip kaynaklardan Python’ da crawler yardımı ile bilgiler çekilerek doğru imla kurallı bir dataset oluşturulmuştur. Oluşturulan dataset (Doğru imla kurallı) de bulunan kelimelerin veya cümlelerin yapısının bozulması ile yeni bir dataset (Bozuk imla kurallı) oluşturulmuştur. Makine öğrenmesi ile imla kurallarına uymayan kelime veya cümlelerin orijinal halleri ile sistem eğitilmiştir.
One-hot encode yapısı kullanılarak karakter tabanlı vektörler oluşturulmuştur. Hazırlanan datasetlerin eğitimi için Google Colab kullanılmıştır. İmla Hatalı Cümleleri Düzelten sistem bir web sitesi aracılığı ile kullanıcıya sunulmuştur. Projenin derin öğrenme bölümü Python programlama dili ile yazılmıştır. Python dili ile yazabilmek için Anaconda’ nın Spyder ve Jupyter Notebook programları kullanılmıştır. Makine öğrenmesi bölümü, Theano veya Tensorflow’u backend olarak kullanan Keras kütüphanesi ile yapılmıştır.


### Dizinlerin Açıklamaları
* Yardımcı dosyalar klasörü, içerisinde yer alan Python dosyaları ile Düzgün metinlerle oluşturulan “.txt” uzantılı dosyayı belirli kurallar çerçevesinde bozmaya ve satır satır ayırmaya yarayan dosyalardır. Ayrıca “Sitelerden Çekilen Paragraflar” klasörü içerisinde bazı sitelerden elde edilmiş makale,dergi gibi doğru imla kurallı kaynaklardan alınmış paragraflar mevcuttur.

* Program klasörü içerisinde yer alan “train.ipynb” ve “predict.ipynb” ile datasetleri eğitmeye ve daha sonra eğitilen modelin predict edilmesine olanak sağlar. Bozuk imla kurallı dataset içerisindeki verilerin eğitilmiş model ile düzeltme işleminin gerçekleştirilir. Sonuçlar program çalıştıktan sonra ekran çıktısı olarak sunulmaktadır. Bu dosyaları çalıştırmak için "Google Colab" veya "Anaconda Jupyter Notebook" kullanılmalıdır.

* Kaydedilmiş Modeller klasöründe datasetlerin belirli örnekleri ile denemelerin sonuçlarında oluşan modeller mevcuttur.

* "Datasets" klasörü içerisinde “Doğru imla kurallı dataset” ve “Yanlış imla kurallı dataset” bulunmaktadır.
