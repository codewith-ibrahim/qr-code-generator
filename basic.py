# import qrcode as qr #using alias as qr
import qrcode
from PIL import Image
from PIL import ImageDraw

# basic version
# img = qrcode.make("https://www.linkedin.com/in/codewithibrahim")
# img.save("linkedin_qr.png")

#using user base input 
# user_link = input("Enter Your Link Here: ")
# generate_qr = qr.make(user_link)
# generate_qr.save("qr_code.png")


#Advanced Version using logo 
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("https://www.linkedin.com/in/codewithibrahim")
qr.make(fit=True)

img = qr.make_image(
    fill_color="black",
    back_color="white"
).convert("RGBA")

logo = Image.open("github_logo.png").convert("RGBA")
qr_width, qr_height = img.size
logo_size = qr_width // 5

logo = logo.resize(
    (logo_size, logo_size),
    Image.Resampling.LANCZOS
)

circle_size = logo_size + 5

circle = Image.new("RGBA", (circle_size, circle_size), (255, 255, 255, 0))
draw = ImageDraw.Draw(circle)
draw.ellipse(
    (0, 0, circle_size, circle_size),
    fill=(255, 255, 255, 255)
)

circle_x = (qr_width - circle_size) // 2
circle_y = (qr_height - circle_size) // 2
img.paste(circle, (circle_x, circle_y), circle)
logo_x = (qr_width - logo_size) // 2
logo_y = (qr_height - logo_size) // 2
img.paste(logo, (logo_x, logo_y), logo)

# Save image
img.save("advanced_qr.png")

print("GitHub QR Code generated successfully!")




