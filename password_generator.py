import argparse
import string
import random
import qrcode

class PasswordGenerator:
    def __init__(self, length) -> None:
        self.length = length
     
        
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
    

    # Additional Option
    # Create QR Code
    # -qr qrcode as png
    # git repository
    # commit progress
    

def main():
    parser = argparse.ArgumentParser(description="Password Generator")
    parser.add_argument("-l", "--length", type=int, default=12)
    parser.add_argument("-u", "--uppercase", action="store_true")
    parser.add_argument("-n", "--numbers", action="store_true")
    parser.add_argument("-s", "--special", action="store_true")
    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.uppercase, args.numbers, args.special)
        print("Your generated password is:", password)
    except ValueError as e:     
        print("Error:", e)

if __name__ == "__main__":
    main()
