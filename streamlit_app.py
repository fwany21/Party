import streamlit as st
import os
from PIL import Image, ExifTags
import base64
from io import BytesIO

# Title of the invitation
st.title("🎉 나연이의 8번째 생일 파티에 초대합니다! 🎉")

# Invitation message
st.write("""
👋안녕하세요

우리 나연이 8번째 생일을 함께 축하해주세요~~🎀

📆 **언제**: 2월 15일 토요일 6시

🚩 **장소**: [무키무키 수원하늘채점](https://naver.me/xprAEmgI)
(주차공간이 협소하다고 합니다)

함께 와서 맛있는 거 먹고 즐겁게 놀아보아요~🤩
""")

# Function to correct image orientation
def correct_image_orientation(image):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break

        exif = image._getexif()

        if exif is not None:
            orientation = exif.get(orientation)

            if orientation == 3:
                image = image.rotate(180, expand=True)
            elif orientation == 6:
                image = image.rotate(270, expand=True)
            elif orientation == 8:
                image = image.rotate(90, expand=True)
    except Exception as e:
        pass

    return image

# Function to convert image to base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Photo slideshow
photo_dir = 'photos'
if os.path.exists(photo_dir):
    photos = [f for f in os.listdir(photo_dir) if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif'))]
    if photos:
        st.write("## 📸 사진 슬라이드쇼")
        for photo in photos:
            try:
                image = Image.open(os.path.join(photo_dir, photo))
                image = correct_image_orientation(image)
                width, height = image.size
                if width > height:
                    st.image(image, use_column_width=True)
                else:
                    img_base64 = image_to_base64(image)
                    st.markdown(
                        f"<div style='display: flex; justify-content: center;'><img src='data:image/png;base64,{img_base64}' width='300'/></div>",
                        unsafe_allow_html=True
                    )
            except Exception as e:
                st.write(f"이미지를 로드하는 동안 오류가 발생했습니다: {photo}")
    else:
        st.write("사진이 없습니다.")
else:
    st.write("사진 디렉토리가 존재하지 않습니다.")