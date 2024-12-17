import cv2
import torch
import os


class ObjectDetection:

    def __init__(self,image_path): 

        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  
        self.image_path = f'{image_path}'  
        self.image = cv2.imread(self.image_path)

    
    
    
    def object_detection(self):
        """
        The function `object_detection` reads an image, performs object detection using a model, filters
        the detections based on confidence level, and returns the filtered detections.
        :return: The `object_detection` method returns the filtered detections where the confidence level
        is greater than 0.4 from the input image using the specified model.
        """
        image = cv2.imread(self.image_path)
        results = self.model(image)
        detections = results.pandas().xyxy[0]

        filtered_detections = detections[detections['confidence'] > 0.4]
        return filtered_detections

    def visualize_objects(self,filtered_detections):
        """
        This function visualizes objects detected in an image by drawing rectangles around them and
        displaying labels with confidence scores.
        
        :param filtered_detections: The `visualize_objects` function takes in a DataFrame
        `filtered_detections` containing information about detected objects. Each row in the DataFrame
        represents a detected object with columns for 'xmin', 'ymin', 'xmax', 'ymax', 'name', and
        'confidence'
        """

        for index, row in filtered_detections.iterrows():
            xmin, ymin, xmax, ymax = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
            label = row['name']
            confidence = row['confidence']

            cv2.rectangle(self.image, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
            cv2.putText(self.image, f'{label} {confidence:.2f}', (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # Display the image with detections
        # cv2.imshow('detected',self.image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
