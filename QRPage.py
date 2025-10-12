import qrcode
from PIL import Image
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# ===== CONFIG =====
template_path = "template.png"  # Your "Order me!" image
output_dir = "qr_framed"
os.makedirs(output_dir, exist_ok=True)

compid = 99
total_qrs = 10  # Total QR codes to make
pdf_output_path = f"Comp{compid}_QRCodes.pdf"

# ===== STEP 1: Generate framed QR images =====
qr_images = []
template = Image.open(template_path).convert("RGB")

# Coordinates for black box in template (x1, y1, x2, y2)
# Adjust these if the black box changes
qr_box_coords = (120, 80, 380, 350)  # left, top, right, bottom

for i in range(total_qrs):
    qrurl = f'https://mark5.wilerhub.com/pro/public/menu2?id={compid}&table={i+1}'

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(qrurl)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Resize QR to fit inside template black box
    box_width = qr_box_coords[2] - qr_box_coords[0]
    box_height = qr_box_coords[3] - qr_box_coords[1]
    qr_resized = qr_img.resize((box_width, box_height), Image.LANCZOS)

    # Paste QR into template
    framed = template.copy()
    framed.paste(qr_resized, qr_box_coords)

    # Save framed QR image
    save_path = os.path.join(output_dir, f'Comp{compid}QR{i+1}.jpg')
    framed.save(save_path, "JPEG")
    qr_images.append(save_path)

print(f"Generated and framed {len(qr_images)} QR codes.")

# ===== STEP 2: Create PDF with 6 per A4 page =====
c = canvas.Canvas(pdf_output_path, pagesize=A4)
page_width, page_height = A4
cols, rows = 2, 3
img_width, img_height = 200, 250  # Size in PDF (adjust to fit nicely)
margin_x, margin_y = 50, 50
spacing_x = (page_width - 2*margin_x - cols*img_width) / (cols - 1)
spacing_y = (page_height - 2*margin_y - rows*img_height) / (rows - 1)

x_pos = margin_x
y_pos = page_height - margin_y - img_height
count = 0

for idx, img_path in enumerate(qr_images):
    c.drawImage(img_path, x_pos, y_pos, img_width, img_height)

    # Move to next column
    count += 1
    if count % cols == 0:
        x_pos = margin_x
        y_pos -= img_height + spacing_y
    else:
        x_pos += img_width + spacing_x

    # New page after 6 images
    if count % (cols * rows) == 0 and idx != len(qr_images) - 1:
        c.showPage()
        x_pos = margin_x
        y_pos = page_height - margin_y - img_height

c.save()
print(f"PDF saved: {pdf_output_path}")
