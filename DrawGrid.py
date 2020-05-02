from Vec2d import Vec2d
from PIL import Image, ImageDraw, ImageFont
import numpy as np
winsize=(Vec2d(210,210))
img=Image.new("RGB",(winsize.x,winsize.y),(255,255,255))
img1=ImageDraw.Draw(img)
font = ImageFont.truetype('/usr/share/fonts/truetype/open-sans/OpenSans-ExtraBold.ttf')
inset=Vec2d(10,10)
def DrawGrid(canvas,min,max):
    step=(max.x-min.x)/10
    for x in np.arange(min.x,max.x,step-1):
        vertical=((x,min.y),(x,max.y-min.x))
        canvas.line(vertical,fill=128)
    for y in np.arange(min.y,max.y,step-1):
        horizontal=((min.x,y),(max.x-min.x,y))
        canvas.line(horizontal,fill=128)
DrawGrid(img1,inset,winsize-inset)
img.show()
