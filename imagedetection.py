import pixellib
from pixellib.instance import instance_segmentation
import cv2
import os
from gtts import gTTS
def img():

    segment_image = instance_segmentation()
    #Loading the mask rcnn
    segment_image.load_model('mask_rcnn_coco.h5')
    #Load the image
    img = "road.jpg"
    segment_image.segmentImage("road.jpg", show_bboxes = True, output_image_name = "output.jpg")
    #crime.jpg
    if img == "crime.jpg":
        fh = open ("crime.txt", "r")
        myText = fh.read ().replace ("\n", " ")
        # Language we want to use
        language = 'en'
        output = gTTS (text=myText, lang=language, slow=False)
        output.save ("output.mp3")
        fh.close ()
        # Play the converted file
        os.system ("start output.mp3")
    #City.jpg
    if img == "horse.jpg":
        fh = open ("horse.txt", "r")
        myText = fh.read ().replace ("\n", " ")
        # Language we want to use
        language = 'en'
        output = gTTS (text=myText, lang=language, slow=False)
        output.save ("output.mp3")
        fh.close ()
        # Play the converted file
        os.system ("start output.mp3")
    if img == "road.jpg":
        fh = open ("road.txt", "r")
        myText = fh.read ().replace ("\n", " ")
        # Language we want to use
        language = 'en'
        output = gTTS (text=myText, lang=language, slow=False)
        output.save ("output.mp3")
        fh.close ()
        # Play the converted file
        os.system ("start output.mp3")
    else :
        print("the given picture is not valid or not in this directory")
    #read image
    img = cv2.imread("output.jpg")
    img = cv2.resize(img,(600,600))
    # Show the Output
    cv2.imshow("Output",img)
    cv2.waitKey(0)





