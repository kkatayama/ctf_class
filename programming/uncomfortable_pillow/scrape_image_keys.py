# coding: utf-8
# %load scrape_image_keys.py
# %load scrape_image_keys.py
from hashlib import sha256
from pwn import *
from PIL import Image

def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)

signatures = []

### Interesting, only 25 characters available??? ###
while len(signatures) < 25:
    r = remote('52.15.140.126', 6968)
    m =''
    while r.can_recv(timeout=0.5):
        m += r.recv()
    print m[:100]
    with open('temp.png', 'wb') as f:
        f.write(m.split('\n')[0].decode('hex'))

    for i in range(4):
        crop('temp.png', ((i)*30, 0, (i+1)*30, 27), 'temp_'+str(i)+'.png')
        with open('temp_'+str(i)+'.png', 'rb') as f:
            tmp = f.read()
        tmp_sig = sha256(tmp).hexdigest()
        if tmp_sig not in signatures:
            with open('key_'+str(len(signatures))+'.png', 'wb') as f:
                f.write(tmp)
            signatures.append(tmp_sig)
r.close()
    
