import utils

FILE_EXTENSION = ".png"
FILE_PREFIX = "qrcode_img_"


def generate_qr_code():
    while True:
        data = input("Enter the text for QR code: ")
        if len(data) < 1:
            print("Invalid input!")
            continue
        filename = input(
            "(Optional) Enter the file name with .png extension for QR code, or hit enter for default: ")

        if not filename:
            filename = f"{utils.get_datetime()}{FILE_EXTENSION}"
        elif not filename.endswith(FILE_EXTENSION):
            filename = f"{filename}{FILE_EXTENSION}"

        filename = f"{FILE_PREFIX}{filename}"
        try:
            utils.generate_qr_code(data, filename)
            print(f"Successfully generated the QR code at {filename}")
            break
        except Exception as e:
            print(f"Exception occurred while generating QR code: {e}")
            break


generate_qr_code()
