import os
from PIL import Image

def replace_images_with_logo(logo_path="logo.png", target_dir="."):
    # 로고 이미지 로드
    logo = Image.open(logo_path)

    for filename in os.listdir(target_dir):
        filepath = os.path.join(target_dir, filename)

        if not os.path.isfile(filepath):
            continue  # 디렉토리 무시

        name, ext = os.path.splitext(filename)
        ext = ext.lower()

        try:
            if ext == ".png" and filename != os.path.basename(logo_path):
                # PNG 파일 교체
                logo.save(filepath, format="PNG")
                print(f"✅ Replaced {filename} with logo.png")

            elif ext == ".ico":
                # ICO 파일 교체 (16x16 확실히 변환 후 저장)
                logo_resized = logo.resize((16, 16), Image.LANCZOS)
                logo_resized.save(filepath, format="ICO")
                print(f"✅ Replaced {filename} with logo.png as ICO (16x16)")
        except Exception as e:
            print(f"⚠️ {filename} 변환 실패: {e}")

if __name__ == "__main__":
    replace_images_with_logo("logo.png", ".")
