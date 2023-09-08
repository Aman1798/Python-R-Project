# Create a convertor tool, converting pdf files to .html using python

'''import subprocess


def convert_pdf_to_html(pdf_path, output_path):
    try:
        subprocess.run(["pdf2htmlEX", "--zoom", "1.3", pdf_path, output_path])
        print(f"Conversion successful. HTML file saved at {output_path}")
    except FileNotFoundError:
        print("pdf2htmlEX command-line tool not found. Please make sure it is installed.")
    except Exception as e:
        print(f"An error occurred during conversion: {str(e)}")


# Example usage
pdf_file = "path/to/input.pdf"
html_file = "path/to/output.html"

final = convert_pdf_to_html(pdf_file, html_file)

print(final)'''


import subprocess


def convert_pdf_to_html(pdf_path, output_path):
    try:
        subprocess.run(["pdf2htmlEX", "--zoom", "1.3", pdf_path, output_path])
        print(f"Conversion successful. HTML file saved at {output_path}")
    except FileNotFoundError:
        print("pdf2htmlEX command-line tool not found. Please make sure it is installed.")
    except Exception as e:
        print(f"An error occurred during conversion: {str(e)}")
    else:
        return True


# Example usage
pdf_file = "path/to/input.pdf"
html_file = "path/to/output.html"

conversion_successful = convert_pdf_to_html(pdf_file, html_file)

if conversion_successful:
    print("Conversion completed.")