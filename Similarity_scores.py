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
    conn.commit()
    conn.close()

def compute_all():
    conn=sqlite3.connect('pdf_silo.db')
    cursor=conn.cursor()

    cursor.execute("SELECT file_path FROM pdf_files")
    rows=cursor.fetchall()
    conn.close()

    pdf_paths=[row[0] for row in rows]
    sim_model=PDFSimilarity()

    conn=sqlite3.connect('pdf_silo.db')
    cursor=conn.cursor()

    for i in range(len(pdf_paths)):
        for j in range(i+1,len(pdf_paths)):
            path1=pdf_paths[i]
            path2=pdf_paths[j]
            score=sim_model.compare(path1,path2)

            pdf1_name = os.path.basename(path1)
            pdf2_name = os.path.basename(path2)

            print(f"{os.path.basename(path1)} vs {os.path.basename(path2)}: {round(score,4)}")

            cursor.execute('''
                           INSERT INTO similarity_scores (pdf1_name, pdf2_name, sim_score)
                           VALUES (?, ?, ?)''',(pdf1_name,pdf2_name, score))
    conn.commit()
    conn.close()
    print("\n All similarity scores were calculated and written to the database.")



