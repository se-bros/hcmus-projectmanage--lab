import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import os


def extract_text(file_path: str) -> str:
    """
    Trích xuất văn bản từ file ảnh (PNG/JPEG) hoặc PDF.
    Với PDF: render từng trang thành ảnh rồi chạy OCR.
    """
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return _ocr_pdf(file_path)
    else:
        return _ocr_image(file_path)


def _ocr_image(file_path: str) -> str:
    """Chạy Tesseract OCR trên file ảnh, ưu tiên tiếng Việt."""
    try:
        img = Image.open(file_path)
        # lang='vie' là gói tiếng Việt của Tesseract
        text = pytesseract.image_to_string(img, lang="vie")
        return text.strip()
    except Exception as e:
        return f"[Lỗi OCR ảnh]: {str(e)}"


def _ocr_pdf(file_path: str) -> str:
    """Render PDF thành ảnh rồi chạy OCR từng trang."""
    try:
        doc = fitz.open(file_path)
        all_text = []
        for page_num, page in enumerate(doc, start=1):
            # Render trang thành ảnh độ phân giải cao (2x)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            img_path = f"/tmp/page_{page_num}.png"
            pix.save(img_path)

            img = Image.open(img_path)
            text = pytesseract.image_to_string(img, lang="vie")
            all_text.append(f"--- Trang {page_num} ---\n{text.strip()}")
            os.remove(img_path)

        doc.close()
        return "\n\n".join(all_text)
    except Exception as e:
        return f"[Lỗi OCR PDF]: {str(e)}"
