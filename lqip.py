from PIL import Image, ImageFilter
import base64
import pyperclip

def image_lqip(image_path,output_image_path,length=16,width=8,radius=2):
    """
    Generate a Low-Quality Image Placeholder (LQIP) and save it to a file, then return the base64 encoded string.

    Parameters:
    - image_path: Path to the original image file.
    - output_image_path: Path to save the LQIP file.
    - length: Length of the adjusted image, default is 16.
    - width: Width of the adjusted image, default is 8.
    - radius: Radius of Gaussian blur, default is 2.

    Return:
    - Base64 encoded string.
    """
    im = Image.open(image_path)
    im = im.resize((length,width))
    im = im.convert('RGB')
    im2 = im.filter(ImageFilter.GaussianBlur(radius)) # Gaussian blur
    im2.save(output_image_path) # save image

    # Convert to base64 encoding
    with open(output_image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        base64_string = encoded_string.decode('utf-8')

    return base64_string

# Example
image_path = "/workspaces/blog/assets/img/posts/2024-09-10-analyzing-pey-postings-part-2/00-thumbnail.png"
output_image_path = "test_blur.jpg"
base64_image = image_lqip(image_path, output_image_path)

# pyperclip.copy('data:image/jpg;base64,'+ base64_image) # Copy the result into the clipboard.
print(base64_image)