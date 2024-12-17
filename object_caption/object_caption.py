
from transformers import BlipProcessor, BlipForConditionalGeneration,AutoModelForCausalLM, AutoTokenizer, pipeline
from PIL import Image
from huggingface_hub import InferenceClient



class objectCaption:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        self.MODEL ="microsoft/Phi-3-mini-128k-instruct"
        self.client = InferenceClient(token='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',timeout=300)



    def generate_basic_caption(self,image):
        """
        The function `generate_basic_caption` processes an image using a model to generate a caption and
        then decodes the output to remove special tokens before returning the caption.
        
        :param image: The `image` parameter in the `generate_basic_caption` method is the input image for
        which you want to generate a caption.
        :return: The `generate_basic_caption` method returns a basic caption generated by the model for
        the input image.
        """
        inputs = self.processor(image, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        return self.processor.decode(outputs[0], skip_special_tokens=True)


    def enhance_caption_with_objects(self, image,detected_objects, context=None):
        """
        The function `enhance_caption_with_objects` takes an image, detected objects, and optional context
        to generate a detailed description of the scene by combining the basic caption with object
        descriptions and context for enhanced interpretation.
        
    
        :param detected_objects: The `detected_objects` parameter seems to be a DataFrame containing
        information about objects detected in the image. 
        :param context: The `context` parameter in the `enhance_caption_with_objects` function is used to
        provide additional information or background that might influence the interpretation of the scene 
        :return: The function `enhance_caption_with_objects` returns the response generated by the text
        """

        image_caption = self.generate_basic_caption(image)
        print('Caption before enhancemenet', image_caption)
        object_descriptions = ", ".join(obj["name"] for _,obj in detected_objects.iterrows())
        
        prompt = f""""
        The image caption is: '{image_caption}'. 
        The detected objects are: {object_descriptions}. 
        Please provide a detailed description of the scene, explaining the relationships between the objects, their positions
        consider how the context of {context} might influence the interpretation of the scene.
        
        """
        try:
            response = self.client.text_generation(model=self.MODEL, prompt=prompt, max_new_tokens=100)
            print('Caption after enhancment',response)
        except Exception as e:
            print(f"Error during text generation: {e}")

        return response    

   
        




