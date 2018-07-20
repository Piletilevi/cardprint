import sys
import os
import csv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def printCard(card):
    bg_fn = os.path.join(datadir, card['taustafail'])
    face_fn = os.path.join(datadir, card['pildifail'])
    out_fn = os.path.join(datadir, card['kood']+'.png')
    print(bg_fn, face_fn, out_fn)
    bg_img = Image.open(bg_fn)
    face_img = Image.open(face_fn)
    face_offset = (100, 700)
    bg_img.paste(face_img, face_offset)
    draw = ImageDraw.Draw(bg_img)
    font = ImageFont.truetype("arial.ttf", 50)
    font2 = ImageFont.truetype("courbd.ttf", 22)
    draw.text((150, 550), card['eesnimi'], (0, 0, 0), font=font)
    draw.text((200, 600), card['perenimi'], (0, 0, 0), font=font)
    draw.text((150, 650), card['lisainfo'], (0, 0, 0), font=font2)
    bg_img.save(out_fn)


datadir = os.path.dirname(sys.argv[1])

with open(sys.argv[1], newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    firstrow = True
    labels = 'foo'
    for row in csvreader:
        if firstrow:
            labels = list(map(str.strip, row))
            firstrow = False
        else:
            values = list(map(str.strip, row))
            card = dict(zip(labels, values))
            printCard(card)
