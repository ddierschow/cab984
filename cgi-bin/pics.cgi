#!/usr/local/bin/python

import sys
sys.path.append("../bin")

if __name__ == '__main__':
    import basics
    import images
    basics.StartPage(images.PicturesMain, 'editor')