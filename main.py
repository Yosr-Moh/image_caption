from object_detection.object_detction import ObjectDetection
from object_caption.object_caption import objectCaption

if __name__=="__main__":
# This Python code snippet is creating a list called `captions` and a list of image filenames called
# `images`. It then iterates over each image filename in the `images` list. For each image, it prompts
# the user to enter a context for describing the image.
    captions = []
    images = ['1.jpg','2.jpg','3.jpg']
    for i in images:
        context = input("Enter the context you want the image to be descriped by: ")
        objDetection = ObjectDetection(f'./test images/{i}')
        detected_objects = objDetection.object_detection()
        objDetection.visualize_objects(detected_objects)
        ObjCaption = objectCaption()
        captions.append(ObjCaption.enhance_caption_with_objects(objDetection.image,detected_objects,context='Summer'))
    print(captions)


