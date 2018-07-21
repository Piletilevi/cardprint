import sys
import os
import csv
import datetime
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pyqrcode


def printCard(card):
    bg_fn = os.path.join(confdir, card['taustafail'])
    face_fn = os.path.join(facesdir, card['pildifail'])
    out_fn = os.path.join(outdir, card['kood']+'.png')

    bg_img = Image.open(bg_fn)
    face_img = Image.open(face_fn)

    face_offset = (100, 700)
    qr_offset = (400, 700)
    bg_img.paste(face_img, face_offset)
    draw = ImageDraw.Draw(bg_img)
    font = ImageFont.truetype("arial.ttf", 50)
    font2 = ImageFont.truetype("courbd.ttf", 22)
    draw.text((150, 550), card['eesnimi'], (0, 0, 0), font=font)
    draw.text((200, 600), card['perenimi'], (0, 0, 0), font=font)
    draw.text((150, 650), card['lisainfo'], (0, 0, 0), font=font2)

    qrcode = pyqrcode.create(
        card['kood'],
        error='H',
        version=1,
        mode='numeric'
        )
    qrcode.png(
        tmp_code_fn,
        scale=6,
        module_color=[0, 0, 0, 128],
        background=[0xff, 0xff, 0xcc]
        )
    qr_img = Image.open(tmp_code_fn)
    bg_img.paste(qr_img, qr_offset)
    bg_img.save(out_fn)


# Setup
datafile_fn = sys.argv[1]
datafile_bn = os.path.basename(datafile_fn)
exedir = os.path.dirname(sys.argv[0])
now = datetime.datetime.now()
outdir = os.path.join(
    exedir, 'out',
    datetime.datetime.now().isoformat()
    .replace('T', '_').replace('-', '').replace(':', '')
    .split('.')[0]
)
if not os.path.exists(outdir):
    os.mkdir(outdir)
confdir = os.path.join(exedir, 'configuration')
facesdir = os.path.join(exedir, 'faces')
tmp_code_fn = os.path.join(exedir, 'code.png')


# Main
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

# Cleanup
os.rename(datafile_fn, os.path.join(outdir, datafile_bn))
os.remove(tmp_code_fn)
