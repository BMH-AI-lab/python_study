import os

print("현재 작업 디렉토리: ", os.getcwd())

folder_name = "sample_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"{folder_name} 폴더를 생성했습니다.")
else:
    print(f"{folder_name} 폴더가 이미 존재합니다.")

print("현재 디렉터리 내 파일 폴더 목록: ")
print(os.listdir())