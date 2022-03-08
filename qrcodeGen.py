# Author: Nana Parker
# Date: 8th March, 2022
# Title: QR Code Generator

import qrcode
import argparse
import os

parser = argparse.ArgumentParser(description = "Generate QR Codes.")
parser.add_argument("text", help="Information to be converted to a QR Code")
args = parser.parse_args()

extension = os.path.splitext(str(args.text))

if (str(extension[len(extension) - 1]) == ".txt"):
    with open(args.text) as f:
        data = f.read()
    qr = qrcode.make(data)
else:
    qr = qrcode.make(args.text)

qr.save(str(extension[0])+"_QRCode.png")