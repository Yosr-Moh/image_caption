README for Image Captioning and Object Detection System

Overview

This project combines image captioning with object detection to generate detailed descriptions of images. By detecting objects in an image and using contextual information, the system creates enhanced captions that explain the relationships and context of the detected elements.

The project integrates advanced models like YOLOv5 for object detection and Salesforce’s BLIP for image captioning, along with fine-tuned text generation using a transformer model.

Features
	1.	Object Detection
	•	Detects objects in an image using YOLOv5.
	•	Filters objects based on confidence thresholds.
	•	Visualizes detected objects by drawing bounding boxes and displaying labels.
	2.	Image Captioning
	•	Generates a basic caption for the image using the BLIP model.
	•	Enhances the caption with contextual descriptions using detected objects and additional context.
	3.	User Context Integration
	•	Allows users to provide context for image descriptions to generate more meaningful captions.
	4.	Object Visualization
	•	Draws bounding boxes on the image and labels detected objects with their names and confidence levels.

Code Structure

1. Object Detection

The ObjectDetection class handles object detection tasks:
	•	Model Loading: Uses YOLOv5 from PyTorch Hub.
	•	Object Detection: Detects objects in an image and filters detections with confidence > 0.4.
	•	Visualization: Draws bounding boxes and labels on the image to visualize detections.

Key Methods:
	•	object_detection(): Detects and filters objects.
	•	visualize_objects(filtered_detections): Visualizes the detections on the image.

2. Image Captioning

The objectCaption class is responsible for generating captions:
	•	Basic Captioning: Uses the BLIP model to generate a generic caption for the image.
	•	Enhanced Captioning: Combines basic captions with object descriptions and user-provided context for detailed scene interpretation.

Key Methods:
	•	generate_basic_caption(image): Generates a basic caption.
	•	enhance_caption_with_objects(image, detected_objects, context): Enhances the caption by integrating object information and context using a language model.

3. Main Execution Flow

The script iterates through a list of images:
	•	Detects objects in each image and visualizes them.
	•	Prompts the user to input a context for the image.
	•	Generates an enhanced caption for the image using object detection and contextual data.

Installation

Prerequisites
	1.	Python 3.8 or above
	2.	Required libraries:
	•	transformers
	•	torch
	•	Pillow
	•	opencv-python
	•	ultralytics
	•	huggingface_hub

Installation Steps
	1.	Clone the repository:

git clone https://github.com/your-repo/image-captioning-object-detection.git


	2.	Install the dependencies:

pip install -r requirements.txt


	3.	Download the pretrained models used in the code:
	•	YOLOv5: Loaded dynamically from PyTorch Hub.
	•	BLIP: Downloaded via transformers.
	•	Text Generation Model: Use the Hugging Face microsoft/Phi-3-mini-128k-instruct.

How to Run
	1.	Place the images to be processed in the ./test images/ directory.
	2.	Run the main script:

python main.py


	3.	For each image:
	•	The detected objects will be visualized in a window.
	•	Enter a context to guide the caption generation.
	4.	Captions will be printed to the console and stored in a list.

Overall Flow of the Code
	1.	Initialization:
	•	Instantiate the ObjectDetection and objectCaption classes.
	•	Specify the list of images to process.
	2.	Object Detection:
	•	Detect objects in the image using YOLOv5.
	•	Filter detections by confidence > 0.4.
	•	Visualize detections by drawing bounding boxes and labels.
	3.	Caption Generation:
	•	Generate a basic caption for the image using BLIP.
	•	Enhance the caption by:
	•	Incorporating detected objects.
	•	Considering user-provided context.
	4.	Output:
	•	Display the enhanced captions.
	•	Optionally save or use captions for further tasks.


Workflow:
	1.	Object Detection:
	•	Detected objects: ["dog", "ball", "grass"].
	2.	Basic Caption:
	•	“A dog is outdoors.”
	3.	User Context:
	•	“Summer park.”
	4.	Enhanced Caption:
	•	“The image shows a dog sitting on the grass with a ball nearby in a summer park. The dog appears to be relaxed, and the ball suggests playtime activities.”

Future Improvements
	1.	Add support for batch processing of images.
	2.	Save captions and visualized images to files.
	3.	Enhance context interpretation using semantic analysis.



**Sample of the output** 

image 1:
context: Summer
Caption before enhancemenet a bench in a park with a tree in the background
Caption after enhancment 
    Output:
        The image depicts a serene park scene during the summer season. The bench, a common fixture in such parks, is positioned in a way that suggests it is a popular spot for visitors

image 2:
contect: night 
Caption before enhancemenet a busy street in the city at night
Caption after enhancment:
Output:
        The scene depicted in the image is a bustling urban street during the summer night. The image captures the vibrant energy of city life, with various objects and individuals interacting in a dynamic environment.

image 3:
contect: cute 
Caption before enhancemenet a cat sitting on a couch next to a laptop
Caption after enhancment 
    Output:
        The image depicts a domestic scene during the summer season, where a cat is comfortably seated on a couch, possibly enjoying the warmth of the room.