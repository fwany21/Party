import streamlit as st
import os
from PIL import Image, ExifTags, UnidentifiedImageError

# Title of the invitation
st.set_page_config(page_title="나연이의 생일 파티 초대", layout="centered")
st.title("🎉 나연이의 8번째 생일 파티에 초대합니다! 🎉")

# Custom CSS to handle mobile viewport height issues
st.markdown("""
    <style>
    .main {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .block-container {
        flex: 1;
    }
    </style>
    """, unsafe_allow_html=True)

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
        st.error(f"Error correcting image orientation: {e}")

    return image

# Photo slideshow
photo_dir = 'photos'
if os.path.exists(photo_dir):
    photos = [f for f in os.listdir(photo_dir) if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif'))]
    if photos:
        for photo in photos:
            try:
                image = Image.open(os.path.join(photo_dir, photo))
                image = correct_image_orientation(image)
                st.image(image)
            except UnidentifiedImageError:
                st.error(f"이미지를 로드하는 동안 오류가 발생했습니다: {photo}. Error: Unidentified image file.")
            except Exception as e:
                st.error(f"이미지를 로드하는 동안 오류가 발생했습니다: {photo}. Error: {e}")
    else:
        st.info("사진이 없습니다.")
else:
    st.warning("사진 디렉토리가 존재하지 않습니다.")

# st.markdown('#')
