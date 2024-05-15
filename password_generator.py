import argparse
import string
import random

import qrcode
from qrcode.main import QRCode


class PasswordGenerator:


    def __init__(self, length, use_uppercase, use_numbers, use_special, use_qrcode) -> None:
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_numbers = use_numbers
        self.use_special = use_special
        self.use_qrcode = use_qrcode
     
        
    def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
        chars = string.ascii_lowercase
        if use_uppercase:
            chars += string.ascii_uppercase 
        if use_numbers:
            chars += string.digits          
        if use_special:
            chars += string.punctuation  
       
        if length < 12:
            raise ValueError("The specified length is less than the default length (12).")
        password = ''.join(random.sample(chars, length))
        return password
    

    def generate_qrcode(data="http://www.lincolnloop.com", *args, **kwargs):
        qr = QRCode(*args, **kwargs)
        qr.add_data(data)

        im = qr.make_image()
        im.show()
    

    # Additional Option
    # Create QR Code
    # -qr qrcode as png
    # git repository      +
    # commit progress     +
    

def main():
    parser = argparse.ArgumentParser(description="Password Generator")
    parser.add_argument("-l", "--length", type=int, default=12)
    parser.add_argument("-u", "--uppercase", action="store_true")
    parser.add_argument("-n", "--numbers", action="store_true")
    parser.add_argument("-s", "--special", action="store_true")
    parser.add_argument("-qr", "--qrcode", action="store_true")
    args = parser.parse_args()

    try:
        password = PasswordGenerator.generate_password(args.length, args.uppercase, args.numbers, args.special)
        print("Your generated password is:", password)
        qr_code = PasswordGenerator.generate_qrcode()
    except ValueError as e:     
        print("Error:", e)

if __name__ == "__main__":
    main()
