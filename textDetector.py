#imports
import easyocr
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
from textToIPA import convert_to_ipa

#setting up camera
wCam, hCam = 960,540
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

#initialize key to prevent reference error
key = 0

#initializes font and boolean to track when video is paused
ipa_font = ImageFont.truetype("arial.ttf", 30)
takePic = False

while True:

    #if spacebar is pressed, paused/resume video
    if key == 32:
        if not takePic:
            #if paused, detect word and display IPA translations
            takePic = True
            reader = easyocr.Reader(['en'], gpu=False)
            img2char = reader.readtext(img)
            words = []
            for item in img2char:
                top_left = tuple((round(item[0][0][0]), round(item[0][0][1])))
                bottom_right = tuple((round(item[0][2][0]), round(item[0][2][1])))
                text = item[1]
                img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
                img_pil = Image.fromarray(img)
                draw = ImageDraw.Draw(img_pil)
                draw.text((top_left[0], top_left[1] - 40),  f"{text} | {convert_to_ipa(text)}", font = ipa_font, fill = (0, 0, 0))
                img = np.array(img_pil)
                cv2.imshow("Transciber", img)
        else:
            #resume video if already paused
            takePic = False
    #exit is escape key is pressed
    elif key == 27:
        break

    if not takePic:
        #show video if not paused
        success, img = cap.read()

        cv2.imshow("Transciber", img)
        
    key = cv2.waitKey(1)


cap.release()