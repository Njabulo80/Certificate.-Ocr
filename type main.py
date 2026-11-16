import pytesseract
from PIL import Image

def extract_certificate_data(image_path):
    try:
        img = Image.open(image_path)
        gray_img = img.convert('L')
        extracted_text = pytesseract.image_to_string(gray_img)
        return extracted_text
    except Exception as e:
        return f"An error occurred: {e}"

image_path = 'path_to_your_certificate.jpg'
text_result = extract_certificate_data(image_path)

print("--- Extracted Text ---")
print(text_result)
