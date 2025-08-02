import utils


def generate_qr_code():
    while True:
        data = input("Enter the text for QR code: ")
        if len(data) < 1:
            print("Invalid input!")
            continue
        filename = input(
            "(Optional) Enter the file name for QR code, or hit enter: ")
        if not filename:
            filename = f"qrcode_img_{utils.get_datetime()}.png"
        try:
            utils.generate_qr_code(data, filename)
            print(f"Successfully generated the QR code at {filename}")
            break
        except Exception as e:
            print(f"Exception occurred while generating QR code: {e}")
            break


generate_qr_code()
