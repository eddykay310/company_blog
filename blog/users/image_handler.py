import os
from PIL import Image
from flask import url_for,current_app

# handling user profile images
def add_profile_picture(image,username):

    filename = image.filename
    extension_type = filename.split('.')[-1]
    storage_filename = str(username)+'.'+extension_type
    filepath = os.path.join(current_app.root_path,'static\profile_images',storage_filename)
    
    output_size = (300,300)
    pic = Image.open(image)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename