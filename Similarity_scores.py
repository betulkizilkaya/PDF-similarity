import sqlite3
import os
from PDF_Similarity import PDFSimilarity

def create_similarity_scores():
    conn = sqlite3.connect('pdf_silo.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS similarity_scores (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   pdf1_name TEXT,
                   pdf2_name TEXT,
                   sim_score REAL)
                   ''')
    conn.commit()# Değişiklikleri kaydet
    conn.close()# Bağlantıyı kapat

def compute_all():# Tüm PDF dosyaları arasındaki benzerlikleri hesaplar ve veritabanına kaydeder
    conn=sqlite3.connect('pdf_silo.db')
    cursor=conn.cursor() # Veritabanı ile Python arasında SQL komutlarını gönderip sonuç alınmasını sağlayan nesne oluşturur.

    cursor.execute("SELECT file_path FROM pdf_files")
    rows=cursor.fetchall()# Sonuçları liste olarak al
    conn.close()

    pdf_paths=[row[0] for row in rows]# Veritabanından gelen dosya yollarını listeye dönüştür
    sim_model=PDFSimilarity()

    conn=sqlite3.connect('pdf_silo.db')
    cursor=conn.cursor()

    for i in range(len(pdf_paths)):# Tüm PDF dosyaları arasında çiftler oluştur
        for j in range(i+1,len(pdf_paths)): # Aynı çiftleri tekrar etmemek için j, i+1'den başlar
            path1=pdf_paths[i]
            path2=pdf_paths[j]
            score=sim_model.compare(path1,path2)# PDFSimilarity sınıfını kullanarak benzerlik skorunu hesaplanır.

            pdf1_name = os.path.basename(path1)# Yalnızca dosya adını al
            pdf2_name = os.path.basename(path2)

            print(f"{os.path.basename(path1)} vs {os.path.basename(path2)}: {round(score,4)}")

            cursor.execute('''
                           INSERT INTO similarity_scores (pdf1_name, pdf2_name, sim_score)
                           VALUES (?, ?, ?)''',(pdf1_name,pdf2_name, score))
    conn.commit()
    conn.close()
    print("\n All similarity scores were calculated and written to the database.")



