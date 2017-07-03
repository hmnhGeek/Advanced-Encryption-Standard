#!/usr/bin/env python
import argparse as ap
import imageencrypt as icr
from getpass import getpass
import imagefinder

p = ap.ArgumentParser()
p.add_argument('-c', action = 'store_true', help = 'To encrypt!!')
p.add_argument('-d', action = 'store_true', help = 'To decrypt!!')
p.add_argument('--findall', action = 'store_true', help = 'To operate on all images in a folder.!!')
p.add_argument('--keeporg', action = 'store_true', help = 'Pass this to keep original files.')
p.add_argument('address', type = str, help = 'Pass image address.')

args = p.parse_args()

password = getpass()


if args.findall:
    if args.c and not args.d:
        images = imagefinder.findallimages(args.address)

        if args.address[-1] != '/':
            args.address += '/'

        for image in images:
            try:
                icr.encrypt(password, args.address+image, args.keeporg)
                print args.address+image
            except:
                print "Unable to encrypt: File name smaller than key for: "+args.address+image
                continue
    else:
        dats = imagefinder.findallbinaries(args.address)

        if args.address[-1] != '/':
            args.address += '/'

        for dat in dats:
            try:
                icr.decrypt(password, args.address+dat)
                print args.address+dat
            except RuntimeError:
                print "Unable to decrypt: Different password has been set for the file: "+args.address+dat
                continue
    
else:

    if args.c and not args.d:
        icr.encrypt(password, args.address, args.keeporg)
    else:
        icr.decrypt(password, args.address)
