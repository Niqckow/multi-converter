import sys
import os
from PIL import Image
import subprocess

def imagetopng(filepath, extension):
    try:
        imgopen = Image.open(filepath)
        resultimage = imgopen.convert("RGBA")
        resultimage.save(filepath.partition('.')[0] + extension)
    except Exception as e:
        print(f"An error occurred: {e}")

def dc2pdf(input_path, output_dir=None):
    try:
        input_path = os.path.abspath(input_path)

        if not os.path.isfile(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")

        if output_dir is None:
            output_dir = os.path.dirname(input_path)
        else:
            output_dir = os.path.abspath(output_dir)


        command = [
            "libreoffice", "--headless", "--convert-to", "pdf", input_path,
            "--outdir", output_dir
        ]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode != 0:
            print("LibreOffice Error:", result.stderr)
            raise Exception("LibreOffice conversion failed.")
        output_file_path = os.path.join(output_dir, os.path.basename(input_path).replace('.docx', '.pdf'))
        print(f"Expected output file path: {output_file_path}")
        print(f"Conversion successful! PDF saved to: {output_dir}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while converting DOCX to PDF: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

img_format_list = ["-png", "-jpg", "-jpeg", "-webp"]
file_format_list = ["-pdf", "-docx", "-txt"]

def main():
    if len(sys.argv) != 3:
        print("Usage: script.py -[format] <file>")
        print("Formats: \n\t-pdf, -png, -jpg, -jpeg, -webp")
        sys.exit(1)
    

    format_arg = None
    file_arg = None


    for arg in sys.argv[1:]:
        if arg in img_format_list or arg in file_format_list:
            if format_arg is None:
                format_arg = arg
            else:
                print("Error: The format must be provided only once.")
                sys.exit(1)
        elif os.path.isfile(arg):
            if file_arg is None:
                file_arg = arg
            else:
                print("Error: Only one file must be provided.")
                sys.exit(1)
            
        else:
            print(f"Error: File '{arg}' cannot be found.")
            sys.exit(1)


    if format_arg is None or file_arg is None:
        print("Error: You need to provide a valid format and an existing file")
        sys.exit(1)
    if (format_arg in img_format_list):
        imagetopng(file_arg, '.' + format_arg.partition('-')[2])
    if (format_arg == "-pdf"):
        dc2pdf(file_arg, './tmp')

    print(f"Format : {format_arg}")
    print(f"File : {file_arg}")

if __name__ == "__main__":
    main()