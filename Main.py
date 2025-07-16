import os
import sqlite3
from Similarity_scores import create_similarity_scores, compute_all


def create_db():
    conn=sqlite3.connect('pdf_silo.db')
    cursor=conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS pdf_files (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   folder_name TEXT,
                   file_name TEXT,
                   file_path TEXT)
                     ''')
    conn.commit()
    conn.close()

def insert_files(pdf_root_folder):
    conn = sqlite3.connect('pdf_silo.db')
    cursor = conn.cursor()

    for root,dirs,files in os.walk(pdf_root_folder):
        for file in files:
            if file.endswith('.pdf'):
                folder_name = os.path.basename(root) #Bulunan PDF’in bulunduğu klasörün adını alır
                file_path= os.path.join(root, file) #PDF’in tam yolunu alır
                cursor.execute('''
                               INSERT INTO pdf_files (folder_name, file_name,file_path) 
                               VALUES (?, ?, ?)''',
                               (folder_name, file,file_path))
    conn.commit()
    conn.close()
    print("📁 PDF files have been added to the database.")



if __name__ == "__main__":
    pdf_files = (r'C:\Users\betul\OneDrive\Belgeler\GitHub\PDF-similarity\PDF')

    create_db()
    insert_files(pdf_files)
    create_similarity_scores()
    compute_all()



