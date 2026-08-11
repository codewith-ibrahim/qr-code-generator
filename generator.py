import qrcode
from PIL import Image, ImageDraw
import os
import requests
from io import BytesIO
from urllib.parse import urlparse

# Socho: User ne github.com dia to GitHub logo, linkedin.com dia to LinkedIn logo
# Kaise? URL mein domain name check karo!
# ab mein auto detection ky liye function bana raha hon

#auto detect logo
def auto_detect_logo(url):
    """Url ky accordign auto logo return karega"""

    # step1 yeh url ko lowercase mein karega

    url_lower = url.lower()

    # step2 Domain name check

    #maine aik dictionary banai hai if esle or match-case sy ho skta tha lekin baad mein ager mjhe or logos add krne hoe tw chain bht baari hojaegi 
    logos = {
        "github.com" : "logos/github_logo.png",
        "linkedin.com" : "logos/linkedin_logo.png",
        "youtube.com" : "logos/youtube_logo.png",
        "instagram.com" : "logos/instagram_logo.png",
        "facebook.com" : "logos/facebook_logo.png",
        "twitter.com" : "logos/twitter_logo.png",
        "x.com" : "logos/x_logo.png"
    }

    #step3 
    for domain, logo_path in logos.items():
        if domain in url_lower:
            return logo_path

    #ager koi domain match nahi hota tw none return hojaega.
    return None        



# Agar user ka domain match nahi hua to?
# Website ka FAVICON download karke logo banao!
# Har website ka favicon hota hai: https://website.com/favicon.ico

#favicon download
def download_favicon(url):
    """ yeh website sy favicon download karega ager available hoa tw"""

    try:
        domain = urlparse(url).netloc

        favicon_url = f"https://{domain}/favicon.ico"
        # Alternative: Google's favicon service
        # favicon_url = f"https://www.google.com/s2/favicons?domain={domain}"

        response = requests.get(favicon_url, timeout=5)

        if response.status_code == 200:
            favicon = Image.open(BytesIO(response.content))
            return favicon.convert("RGBA")
    except Exception:
        pass

    return None        



def generate_qr(url, logo_path=None, fill_color="black", 
                back_color="white", save_as="qr_code.png"):
    """
    QR Code generate karo with logo.
    
    Parameters:
    url = QR Code mein encode hone wala link
    logo_path = Logo image ka path (None = auto-detect)
    fill_color = QR Code ka color
    back_color = Background color
    save_as = File name to save
    """
    
    # Step 1: Logo decide karo (Auto ya Manual)
    if logo_path is None:
        # Auto-detect try karo
        logo_path = auto_detect_logo(url)
    
    # Step 2: QR Code object create
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    # Step 3: Data add karo
    qr.add_data(url)
    qr.make(fit=True)
    
    # Step 4: QR Image banao
    img = qr.make_image(
        fill_color=fill_color,
        back_color=back_color
    ).convert("RGBA")
    
    # Step 5: Agar logo hai to center mein lagao
    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        
        # QR aur logo ke dimensions
        qr_width, qr_height = img.size
        logo_size = qr_width // 5
        
        # Logo resize
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # White circle behind logo
        circle_size = logo_size + 10
        circle = Image.new("RGBA", (circle_size, circle_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, circle_size, circle_size), fill=(255, 255, 255, 255))
        
        # Center positions
        circle_x = (qr_width - circle_size) // 2
        circle_y = (qr_height - circle_size) // 2
        logo_x = (qr_width - logo_size) // 2
        logo_y = (qr_height - logo_size) // 2
        
        # Paste circle + logo
        img.paste(circle, (circle_x, circle_y), circle)
        img.paste(logo, (logo_x, logo_y), logo)
        
        print(f"✅ Logo added: {logo_path}")
    
    elif logo_path:
        # Favicon download try karo
        print("🔍 Auto-detecting logo...")
        favicon = download_favicon(url)
        if favicon:
            # Same process as above with favicon
            qr_width, qr_height = img.size
            logo_size = qr_width // 5
            favicon = favicon.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
            
            circle_size = logo_size + 10
            circle = Image.new("RGBA", (circle_size, circle_size), (0, 0, 0, 0))
            draw = ImageDraw.Draw(circle)
            draw.ellipse((0, 0, circle_size, circle_size), fill=(255, 255, 255, 255))
            
            circle_x = (qr_width - circle_size) // 2
            circle_y = (qr_height - circle_size) // 2
            logo_x = (qr_width - logo_size) // 2
            logo_y = (qr_height - logo_size) // 2
            
            img.paste(circle, (circle_x, circle_y), circle)
            img.paste(favicon, (logo_x, logo_y), favicon)
            print("✅ Favicon added as logo!")
    
    # Step 6: Save karo
    img.save(save_as)
    print(f"✅ QR Code saved as: {save_as}")
    
    return save_as