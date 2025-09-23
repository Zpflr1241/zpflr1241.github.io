import os
from PIL import Image

# 대상 디렉토리 설정 ('.'은 현재 디렉토리)
target_dir = r'C:\zpflr1241.github.io\assets\img\favicons'
logo_filename = 'logo.png'

# logo.png 이미지 열기
logo_path = os.path.join(target_dir, logo_filename)
logo_image = Image.open(logo_path)

# 디렉토리 내 모든 파일 반복
for filename in os.listdir(target_dir):
    if (filename.endswith('.ico') or filename.endswith('.png')) and filename != logo_filename:
        file_path = os.path.join(target_dir, filename)
        # logo.png 이미지를 그대로 저장 (덮어쓰기)
        logo_image.save(file_path)

print("모든 PNG 파일을 logo.png 이미지로 덮어썼습니다.")
