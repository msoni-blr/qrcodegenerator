import qrcode
from datetime import datetime


# Input : Data to be encoded in the QR code
def generate_qr_code(data, filename):

    # Create a QRCode object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 to 40)
        # Error correction level (L, M, Q, H)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Size of each box (pixel) in the QR code
        border=4,  # Thickness of the border around the QR code
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)  # Ensures the entire QR code space is utilized

    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    img.save(filename)


def get_datetime():
    # Get the current local date and time as a datetime object
    current_datetime = datetime.now()
    # Convert the datetime object to a Unix timestamp (float representing seconds since the epoch)
    unix_timestamp = current_datetime.timestamp()
    # To get an integer Unix timestamp
    return int(unix_timestamp)
