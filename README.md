# 📚 PDF Anlamsal Benzerlik Projesi

Bu proje, akademik PDF dosyaları arasında **anlamsal benzerlik (semantic similarity)** skoru hesaplamak amacıyla Python diliyle geliştirilmiştir.

---

## 🎯 Projenin Amacı

Bu projenin temel amacı; farklı konularda yazılmış akademik PDF makaleleri arasında içerik bazlı **anlamsal benzerlik** oranlarını hesaplayarak, benzer içeriklerin belirlenmesini sağlamaktır. Özellikle bilgi kümelerini gruplayarak sınıflandırma, arama motoru geliştirme ve içerik analizi gibi alanlarda kullanılabilecek temel bir altyapı sunar.

---

## 🌟 Özellikler

- ✅ PDF dosyalarından metin çıkarımı
- 🧠 BERT tabanlı dil modeliyle metin vektörleştirme
- 📊 Cosine similarity kullanarak içerik benzerliği hesaplama
- 🗃️ SQLite veritabanına sonuçların kayıt edilmesi
- 📂 PDF silo yapısı ile organize veri kullanımı
- 🖥️ Komut satırı üzerinden kolay kullanım

---

## 🛠️ Kullanılan Teknolojiler

- 🐍 Python 3
- 🤗 Hugging Face üzerinden `all-MiniLM-L6-v2` dil modeli
- 🧰 Kütüphaneler:
  - `sentence-transformers`
  - `PyMuPDF` (`fitz`)
  - `sqlite3`

---

## 📁 Proje Yapısı

```
PDF-similarity/
├── main.py             # Veritabanını oluşturur, PDF’leri veritabanına ekler, benzerlik sürecini başlatır
├── PDF_Similarity.py   # PDF içeriklerini işler, metinleri karşılaştırır
├── Similarity_scores.py# Benzerlik skorlarını hesaplar ve veritabanına yazar
├── PDF/                # PDF dosyalarının bulunduğu klasör
└── pdf_silo.db         # SQLite veritabanı
```

---

## 🚀 Nasıl Çalıştırılır?

1. `PDF/` klasörüne PDF dosyalarınızı yerleştirin.

2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install sentence-transformers pymupdf
   ```

3. Ana dosyayı çalıştırın:
   ```bash
   python main.py
   ```

---

## 🧠 Çıktılar

- PDF dosyaları arasındaki benzerlik oranları terminalde görüntülenir.
- Tüm sonuçlar `pdf_silo.db` veritabanında `similarity_scores` tablosunda saklanır.

---


## 📄 Lisans

MIT Lisansı © 2025 [Betül Kızılkaya](https://github.com/betulkizilkaya)  
Lisans detayları için: [LICENSE](LICENSE)




