import pyautogui
import time
from fpdf import FPDF
from PIL import Image

# --- SETTINGS ---
total_pages = 50            # Number of pages you want to convert
delay_between_pages = 3     # Seconds to wait before flipping
pdf_output = "ceh_book.pdf"

# --- INIT ---
pdf = FPDF()

print("⏳ Starting in 5 seconds...")
time.sleep(5)

for i in range(total_pages):
    print(f"📸 Capturing page {i+1}/{total_pages}")
    
    # Take screenshot
    screenshot = pyautogui.screenshot()
    img_path = f"page_{i+1}.png"
    screenshot.save(img_path)

    # Add to PDF
    pdf.add_page()
    pdf.image(img_path, 0, 0, 210, 297)  # A4 size in mm

    # Flip to next page
    pyautogui.press('right')
    time.sleep(delay_between_pages)

# Save PDF
pdf.output(pdf_output)
print(f"✅ PDF saved as: {pdf_output}")
