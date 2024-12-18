from PyPDF2 import PdfReader

# Load the PDF file
pdf_path = "./raw-data/2025FourteenYearPlan_Final.pdf"
reader = PdfReader(pdf_path)

# Extract text from each page
text = ""
for page in reader.pages:
    text += page.extract_text()

# Save or process the extracted text
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Text extraction complete!")