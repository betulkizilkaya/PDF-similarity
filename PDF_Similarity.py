import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer, util

class PDFSimilarity:
    def __init__(self,model_name='all-MiniLM-L6-v2'):
        print("Loading Model...")
        self.model = SentenceTransformer(model_name)
        print("Model Loaded.")

    def extract_text(self,pdf_path):
        try:
            doc = fitz.open(pdf_path)
            return "\n".join([page.get_text() for page in doc])
        except Exception as e:
            print(f"Error reading: {pdf_path}- {e}")
            return ""

    def compare(self,pdf1_path, pdf2_path):
        text1 = self.extract_text(pdf1_path)
        text2 = self.extract_text(pdf2_path)

        if not text1 or not text2:
            return 0.0

        embeddings1 = self.model.encode(text1, convert_to_tensor=True)
        embeddings2 = self.model.encode(text2, convert_to_tensor=True)

        similarity = util.pytorch_cos_sim(embeddings1, embeddings2).item()
        return similarity