# Alag file: cli.py — User se interaction

from generator import generate_qr, auto_detect_logo
import os

def main():
    """User-friendly CLI for QR Code Generator."""
    
    print("=" * 50)
    print("📱 QR CODE GENERATOR (Advanced)")
    print("=" * 50)
    
    # Step 1: URL lo
    url = input("\n🔗 Enter URL/Link: ").strip()
    if not url:
        print("❌ URL cannot be empty!")
        return
    
    # Step 2: Logo ka option do
    print("\n🖼️  LOGO OPTIONS:")
    print("1. Auto-detect (URL ke hisaab se)")
    print("2. Custom logo file path")
    print("3. No logo (Simple QR Code)")
    
    logo_choice = input("Choose (1/2/3): ").strip()
    
    logo_path = None
    
    if logo_choice == "1":
        # Auto-detect
        logo_path = auto_detect_logo(url)
        if logo_path:
            print(f"🔍 Detected: {logo_path}")
        else:
            print("⚠️  No logo found for this URL. Generating without logo.")
    
    elif logo_choice == "2":
        # Custom path
        logo_path = input("📁 Enter logo file path: ").strip()
        if not os.path.exists(logo_path):
            print(f"❌ File not found: {logo_path}")
            logo_path = None
    
    # Step 3: Colors (Optional — Default rakho ya poochho)
    print("\n🎨 COLOR OPTIONS:")
    custom_color = input("Custom fill color? (press Enter for black): ").strip()
    fill_color = custom_color if custom_color else "black"
    
    # Step 4: File name
    print("\n💾 SAVE OPTIONS:")
    default_name = "qr_code.png"
    file_name = input(f"Enter file name (press Enter for '{default_name}'): ").strip()
    
    if not file_name:
        file_name = default_name
    
    # Ensure .png extension
    if not file_name.endswith(".png"):
        file_name += ".png"
    
    # Step 5: Generate!
    print("\n⏳ Generating QR Code...")
    generate_qr(
        url=url,
        logo_path=logo_path,
        fill_color=fill_color,
        save_as=file_name
    )
    
    print(f"\n🎉 Done! Open '{file_name}' to see your QR Code.")

if __name__ == "__main__":
    main()