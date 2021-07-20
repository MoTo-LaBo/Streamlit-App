import json
import time
import sys
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image
import os
from array import array
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
import streamlit as st

# st.write("ENDPOINT", st.secrets["ENDPOINT"])
# st.write("KEY", st.secrets["KEY"])


# st.write("Has environment variables been set:",
#          os.environ["ENDPOINT"] == st.secrets["ENDPOINT"],
#          os.environ["KEY"] == st.secrets["KEY"]
#          )
# with open('secret.json') as f:
#     secret = json.load(f)
# KEY = secret['KEY']
# ENDPOINT = secret['ENDPOINT']
# secret.json は githubにあげることはできないので

computervision_client = ComputerVisionClient(st.secrets["ENDPOINT"], CognitiveServicesCredentials(st.secrets["KEY"]))


def get_tags(filepath):
    local_image = open(filepath, "rb")
    # Call API with local image
    tags_result = computervision_client.tag_image_in_stream(local_image)
    tags = tags_result.tags
    tags_name = []
    for tag in tags:
        tags_name.append(tag.name)

    return tags_name


def detect_objects(filepath):
    local_image = open(filepath, "rb")
    # Call API with URL
    detect_objects_results = computervision_client.detect_objects_in_stream(local_image)
    objects = detect_objects_results.objects
    return objects


st.title('物体検出アプリ')

uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'png'])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_path = f'static/img/{uploaded_file.name}'
    img.save(img_path)
    objects = detect_objects(img_path)

    # 描画
    draw = ImageDraw.Draw(img)
    for object in objects:
        x = object.rectangle.x
        y = object.rectangle.y
        w = object.rectangle.w
        h = object.rectangle.h
        caption = object.object_property

        font = ImageFont.truetype('static/Helvetica 400.ttf', size=40)
        text_w, text_h = draw.textsize(caption, font=font)

        draw.rectangle([(x, y), (x+w, y+h)], fill=None, outline='green', width=4)
        draw.rectangle([(x, y), (x+text_w, y+text_h)], fill='green')
        draw.text((x, y), caption, fill='white', font=font)

    st.image(img)

    tags_name = get_tags(img_path)
    tags_name = ', '.join(tags_name)
    st.markdown('**認識されたコンテンツタグ**')
    st.markdown(f'>{tags_name}')
