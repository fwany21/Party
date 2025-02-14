import streamlit as st
import os
from PIL import Image

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

# Photo slideshow
photo_dir = 'photos'
if os.path.exists(photo_dir):
    photos = [f for f in os.listdir(photo_dir) if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif'))]
    if photos:
        st.write("## 📸 사진 슬라이드쇼")
        for photo in photos:
            image = Image.open(os.path.join(photo_dir, photo))
            width, height = image.size
            if width > height:
                st.image(image, use_container_width=True)
            else:
                st.image(image, width=300)
    else:
        st.write("사진이 없습니다.")
else:
    st.write("사진 디렉토리가 존재하지 않습니다.")