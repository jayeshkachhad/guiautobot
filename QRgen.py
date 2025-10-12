import qrcode
from PIL import Image
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Folder to store temp QR JPGs
output_dir = "qr_codes"
os.makedirs(output_dir, exist_ok=True)

compid = 99
total_qrs = 10

# Step 1: Generate QR codes and store as JPG
qr_images = []
for i in range(total_qrs):
    qrurl = f'https://mark5.wilerhub.com/pro/public/menu2?id={compid}&table={i+1}'
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(qrurl)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    save_path = os.path.join(output_dir, f'Comp{compid}QR{i+1}.jpg')
    img.convert("RGB").save(save_path, "JPEG")
    qr_images.append(save_path)

print(f"Generated {len(qr_images)} QR codes.")

# Step 2: Create PDF with 6 per page
pdf_path = f"Comp{compid}_QRCodes.pdf"
c = canvas.Canvas(pdf_path, pagesize=A4)

page_width, page_height = A4
cols, rows = 2, 3  # 2 columns, 3 rows
qr_size = 200       # QR image size in points
margin_x, margin_y = 50, 50
spacing_x = (page_width - 2*margin_x - cols*qr_size) / (cols - 1)
spacing_y = (page_height - 2*margin_y - rows*qr_size) / (rows - 1)

x_pos = margin_x
y_pos = page_height - margin_y - qr_size
count = 0

for idx, img_path in enumerate(qr_images):
    c.drawImage(img_path, x_pos, y_pos, qr_size, qr_size)

    # Move to next column
    count += 1
    if count % cols == 0:
        x_pos = margin_x
        y_pos -= qr_size + spacing_y
    else:
        x_pos += qr_size + spacing_x

    # New page after 6 QRs
    if count % (cols * rows) == 0 and idx != len(qr_images) - 1:
        c.showPage()
        x_pos = margin_x
        y_pos = page_height - margin_y - qr_size

# Save final PDF
c.save()
print(f"PDF saved: {pdf_path}")
