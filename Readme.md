### File Converter Script
This Python script converts files into various formats:

- Images (any common format like JPG, PNG, BMP) to PNG, JPG, or WEBP
- DOCX files to PDF
The script relies on the following dependencies:

- LibreOffice for DOCX to PDF conversion
- Pillow (PIL) for image format conversions
##Requirements
1. Python 3.x
2. LibreOffice (for DOCX to PDF conversion)
3. Pillow library for image handling
##Installation
#Step 1: Install LibreOffice
If LibreOffice is not already installed, you can install it with the following command:

```# For Debian/Ubuntu-based systems
sudo apt update
sudo apt install libreoffice```
#Step 2: Install Python Libraries
Install Pillow via pip:

```pip install pillow```

##Usage
#Running the Script
Place the script and the files you want to convert in the same directory, or specify the full paths. The script accepts file paths and performs conversions based on the specified format.

#Example Usage
1. Convert Image Files

To convert an image to another format, specify the input file and the desired output format (PNG, JPG, or WEBP):


# Convert an image to PNG
```python3 ./multi-converter.py -png "image.jpg"```

2. Convert DOCX to PDF

To convert a DOCX file to PDF, specify the DOCX file as the input. The script will generate a PDF in the specified output directory.

```python3 ./multi-converter.py -pdf "a.docx"```


##Troubleshooting
LibreOffice conversion issues: If DOCX to PDF conversion fails, make sure LibreOffice is installed correctly and accessible from the command line.
Permission issues: Ensure you have permission to read the input files and write to the output directory.
##License
This project is open-source and licensed under the MIT License.