import fitz # PyMuPDF kütüphanesi, PDF dosyalarını okumak ve içerik çıkarmak için kullanılır
from sentence_transformers import SentenceTransformer, util # Metin gömme ve benzerlik hesaplama için gereken kütüphane

class PDFSimilarity:
    def __init__(self,model_name='all-MiniLM-L6-v2'):# Sınıf başlatıldığında çalışacak olan constructor metot
        print("Loading Model...")
        self.model = SentenceTransformer(model_name)
        print("Model Loaded.")

    def extract_text(self,pdf_path):# Bu metot PDF dosyasındaki tüm metni çıkartır.
        try:
            doc = fitz.open(pdf_path)
            return "\n".join([page.get_text() for page in doc])# Her sayfadan metni alıyor ve birleştiriyor.
        except Exception as e:
            print(f"Error reading: {pdf_path}- {e}")
            return ""

    def compare(self,pdf1_path, pdf2_path):# İki PDF dosyasını karşılaştırarak benzerlik skorunu döner
        text1 = self.extract_text(pdf1_path)# İlk PDF'den metni çıkarır.
        text2 = self.extract_text(pdf2_path)# İkinci PDF'den metni çıkarır.

        if not text1 or not text2:
            return 0.0# Her iki PDF'de metin yoksa benzerlik oranı sıfır döner.

        embeddings1 = self.model.encode(text1, convert_to_tensor=True)# İlk metni vektöre dönüştür
        embeddings2 = self.model.encode(text2, convert_to_tensor=True)# İkinci metni vektöre dönüştür

        similarity = util.pytorch_cos_sim(embeddings1, embeddings2).item()# Kosinüs benzerliği ile iki metin arasındaki benzerliği hesaplar.
        return similarity