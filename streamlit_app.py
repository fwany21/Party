import streamlit as st
import os
from PIL import Image, ExifTags

# Title of the invitation
st.title("🎉 나연이의 8번째 생일 파티에 초대합니다! 🎉")

# Invitation message
st.write("""
👋안녕하세요

우리 나연이 8번째 생일을 함께 축하해주세요~~🎀

📆 **언제**: 2월 15일 토요일 6시

🚩 **장소**: 무키무키 수원하늘채점
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

# Photo slideshow
photo_dir = 'photos'
if os.path.exists(photo_dir):
    photos = [f for f in os.listdir(photo_dir) if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif'))]
    if photos:
        st.write("## 📸 사진 슬라이드쇼")
        for photo in photos:
            image = Image.open(os.path.join(photo_dir, photo))
            image = correct_image_orientation(image)
            width, height = image.size
            if width > height:
                st.image(image, use_column_width=True)
            else:
                st.image(image, width=300)
    else:
        st.write("사진이 없습니다.")
else:
    st.write("사진 디렉토리가 존재하지 않습니다.")