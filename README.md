# 📱 QR Code Generator

> A Python-based QR Code Generator with custom logos, automatic logo detection, website favicon support, custom colors, CLI, and a Streamlit web interface.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-green)](https://python-pillow.org/)
[![QR Code](https://img.shields.io/badge/QR%20Code-Generator-black)](https://pypi.org/project/qrcode/)
[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-red?style=for-the-badge&logo=streamlit)](https://cwi-qr-code-generator.streamlit.app/)

A simple yet advanced QR Code Generator built with **Python**.

The project started as a basic QR generator and gradually evolved into a feature-rich application with logo detection, favicon support, custom logos, CLI interaction, and a Streamlit web interface.

---

## ✨ Features

### 🌐 Streamlit Web App

- Generate QR codes directly from your browser
- Enter any URL or text
- Download generated QR codes as PNG
- Choose custom QR colors
- Select different logo options
- Clean and simple user interface

### 🖼️ Logo Support

The generator supports multiple ways of adding logos:

- 🔍 Automatic Logo Detection
- 📁 Custom Logo Upload
- 🚫 No Logo
- 🌐 Website Favicon Detection

### 🔍 Automatic Logo Detection

The application can detect logos based on the URL domain.

Currently supported domains include:

- GitHub
- LinkedIn
- YouTube
- Instagram
- Facebook
- Twitter
- X

If a predefined logo is not found, the application can attempt to retrieve the website's favicon.

### 🎨 Custom QR Colors

Users can choose a custom QR code color instead of using the default black.

### 💻 CLI Version

The project also includes a command-line interface where users can:

- Enter a URL
- Select logo options
- Add a custom logo
- Choose QR color
- Set a custom output filename

### 🧪 Basic Version

A simple version of the QR generator is also included to demonstrate how QR codes can be generated using Python and the `qrcode` library.

---

## 🛠️ Technologies Used

- **Python**
- **qrcode**
- **Pillow (PIL)**
- **Requests**
- **Streamlit**

---

## 📂 Project Structure

```text
qr-code-generator/
│
├── app.py                    # Streamlit web application
├── generator.py              # Core QR generation logic
├── cli.py                    # Command-line interface
├── basic.py                  # Basic QR generation example
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
├── .gitignore
│
└── logos/
    ├── github_logo.png
    ├── linkedin_logo.png
    ├── youtube_logo.png
    ├── instagram_logo.png
    ├── facebook_logo.png
    ├── twitter_logo.png
    └── x_logo.png
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/codewith-ibrahim/qr-code-generator.git
```

### 2. Navigate to the Project

```bash
cd qr-code-generator
```

### 3. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Streamlit App

Start the web application with:

```bash
streamlit run app.py
```

Streamlit will open the application in your browser.

---

## 💻 Run the CLI Version

To use the command-line version:

```bash
python cli.py
```

You will be asked for:

1. URL / Link
2. Logo option
3. Custom logo path (if selected)
4. QR color
5. Output filename

Example:

```text
==================================================
📱 QR CODE GENERATOR (Advanced)
==================================================

🔗 Enter URL/Link: https://github.com/

🖼️ LOGO OPTIONS:
1. Auto-detect
2. Custom logo file path
3. No logo

Choose (1/2/3): 1

🎨 COLOR OPTIONS:
Custom fill color? (press Enter for black):

💾 SAVE OPTIONS:
Enter file name (press Enter for 'qr_code.png'):

⏳ Generating QR Code...

🎉 Done! Open 'qr_code.png' to see your QR Code.
```

---

## 🧠 How It Works

The QR generator follows this workflow:

```text
User enters URL
       ↓
Detect website/domain
       ↓
Check predefined logos
       ↓
Logo found?
   ↙          ↘
 Yes           No
  ↓             ↓
Use logo    Try favicon
  ↓             ↓
  └──────┬──────┘
         ↓
Generate QR Code
         ↓
Add logo to center
         ↓
Save / Download PNG
```

---

## 🔍 Logo Detection

The project uses a dictionary to map supported domains to their corresponding logo files.

Example:

```python
logos = {
    "github.com": "logos/github_logo.png",
    "linkedin.com": "logos/linkedin_logo.png",
    "youtube.com": "logos/youtube_logo.png",
    "instagram.com": "logos/instagram_logo.png",
    "facebook.com": "logos/facebook_logo.png",
    "twitter.com": "logos/twitter_logo.png",
    "x.com": "logos/x_logo.png"
}
```

This makes it easier to add new websites without creating a long chain of `if/elif` statements.

---

## 🌐 Favicon Support

If a website is not included in the predefined logo list, the application can attempt to retrieve its favicon.

For example:

```text
https://example.com/favicon.ico
```

The downloaded favicon can then be used as the QR code logo.

---

## 📦 Dependencies

The project uses the following Python packages:

```text
streamlit
qrcode[pil]
Pillow
requests
```

### qrcode

Used to generate QR codes.

### Pillow

Used for image processing, resizing logos, creating backgrounds, and combining images.

### Requests

Used to retrieve website favicons.

### Streamlit

Used to create the web interface.

---

## 🎯 Future Improvements

- [ ] Support more website logos
- [ ] Better favicon detection
- [ ] QR code size customization
- [ ] Background color customization
- [ ] Rounded QR code styles
- [ ] Multiple output formats
- [ ] SVG QR code support
- [ ] Logo size control
- [ ] Logo position control
- [ ] QR code preview before download
- [ ] Custom background images
- [ ] Improved error handling
- [ ] Mobile-friendly UI

---

## 📸 Screenshots

![QR Code Generator](deploy_screenshot/deploy-screenshot.png)

---

## 📚 Learning Purpose

This project was created as part of my **Python learning journey**.

It helped me practice:

- Python functions
- Modules and imports
- Dictionaries
- Conditional logic
- File handling
- Exception handling
- Image processing
- Working with external libraries
- HTTP requests
- URL parsing
- Command-line interfaces
- Streamlit
- Project structure
- Dependency management
- Git & GitHub

The project started with a simple QR code generator and was gradually expanded into a more complete application.

---

## 👨‍💻 Author

**Shaikh Muhammad Ibrahim**

Frontend Developer | Aspiring AI Engineer

- GitHub: [@codewith-ibrahim](https://github.com/codewith-ibrahim)
- LinkedIn: [codewithibrahim](https://www.linkedin.com/in/codewithibrahim)
- Portfolio: [Portfolio Website](https://shaikh-muhammad-ibrahim-portfolio.vercel.app/)

---

## ⭐ Support

If you find this project useful or interesting, consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is available for learning and personal use.