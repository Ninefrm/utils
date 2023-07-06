from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
from config import (
    FONT_PATH, 
    OUTPUT_IMAGE
)

class CompareImage:
    def __init__(self):
        self.font_path = FONT_PATH
        self.font = ''
        self.before_image = ''
        self.after_image = ''
    
    def load_images(self, BEFORE_PATH, AFTER_PATH):
        # Load both images and convert them to RGB
        self.before_image = Image.open(BEFORE_PATH).convert('RGB')
        self.after_image = Image.open(AFTER_PATH).convert('RGB')
        return True
    
    def check_dimensions(self):
        # Check for image dimensions, make them equal if they are not
        if self.before_image.size != self.after_image.size:
            width = max(self.before_image.size[0], self.after_image.size[0])
            height = max(self.before_image.size[1], self.after_image.size[1])

            # Correct this line here
            self.before_image = self.before_image.resize((width, height))
            self.after_image = self.after_image.resize((width, height))
        return True
    
    def load_font(self):
        # Load font. The first parameter is the font file (you may need to provide full path) 
        # and the second parameter is the size of the font.
        self.font = ImageFont.truetype(self.font_path, 50)
        return True

    def get_unique_filename(self, base_filename):
        base, ext = os.path.splitext(base_filename)
        i = 1
        while os.path.exists(base_filename):
            base_filename = f"{base}_{i}{ext}"
            i += 1
        return base_filename

    def draw_image(self):
        # Prepare draw and add text on the bottom left for the before_image
        draw = ImageDraw.Draw(self.before_image)
        draw.text((10, self.before_image.size[1] - 60), 'BEFORE', (255, 255, 255), font=self.font)
        # Prepare draw and add text on the bottom left for the after_image
        draw = ImageDraw.Draw(self.after_image)
        draw.text((self.after_image.size[0] - 200, self.after_image.size[1] - 60), 'AFTER', (255, 255, 255), font=self.font)
        # Convert images to numpy arrays
        before_image_np = np.array(self.before_image)
        after_image_np = np.array(self.after_image)
        # Concatenate images along the width
        combined = np.concatenate((before_image_np, after_image_np), axis=1)
        # Convert back to Image and save
        output_image = self.get_unique_filename(OUTPUT_IMAGE)
        Image.fromarray(combined).save(output_image)
        return True
    
    def start(self, BEFORE_PATH, AFTER_PATH):
        self.load_images(BEFORE_PATH, AFTER_PATH)
        self.check_dimensions()
        self.load_font()
        self.draw_image()
        return True
