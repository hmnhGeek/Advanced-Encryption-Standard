import imagefinder as imgf
import argparse as ap
import os, shutil

parser = ap.ArgumentParser()
parser.add_argument('--move', action = 'store_true', help = 'Pass if you want to move images.')
parser.add_argument('folder', type = str, help = 'Pass a folder.')
parser.add_argument('destination', type = str, help = 'Pass a destination folder.', nargs = '?')
args = parser.parse_args()

if not args.move:
    images = imgf.findallimages(args.folder)

    if args.folder[-1] != '/':
        args.folder+='/'
        
    for image in images:
        print "Removing Image: "+image
        os.remove(args.folder+image)

    print "done"

else:
    images = imgf.findallimages(args.folder)

    if args.folder[-1] != '/':
        args.folder+='/'

    if args.destination[-1] != '/':
        args.destination+='/'

    if not os.path.exists(args.destination):
        os.makedirs(args.destination)
        
    for image in images:
            
        print "Moving Image: "+image
        shutil.move(args.folder+image, args.destination+image)

    print "done"
