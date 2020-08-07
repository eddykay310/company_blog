import os
from PIL import Image
from flaskimport url_for,current_app

def add_profile_picture(image,username):

    filename = pic_upload.filename
    extension_type = filename.split('.')[-1]
    storage_name = str(username)+'.'+extension_type
    filepath = os.path.join(current_app.root_path,'static/pofile_images',storage_name)
    
    output_size = (200,200)
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)