import os
import json
import requests
import urllib.request

files = []
for dirname, _, filenames in os.walk('/home/pimang62/AI-Challenge-for-Biodiversity/YOLOv8/data/beekeeping/Training/02.라벨링데이터'):
    for filename in filenames:
        files.append(os.path.join(dirname, filename))

training_path = '/home/pimang62/AI-Challenge-for-Biodiversity/YOLOv8/data/beekeeping/Training'
validation_path = '/home/pimang62/AI-Challenge-for-Biodiversity/YOLOv8/data/beekeeping/Validation'

# ['/home....json', ...]
for file in files:
    with open(file) as f:
        jsonfile = json.load(f)
        
        image_url = jsonfile["IMAGE"]["IMAGE_URL"]
        image_name = jsonfile["IMAGE"]["IMAGE_FILE_NAME"]
        
        # 이미지 요청 및 저장 : '/home/pimang62/AI-Challenge-for-Biodiversity/YOLOv8/data/beekeeping/Training/images/~.jpg'
        urllib.request.urlretrieve(image_url, os.path.join(training_path, 'images', image_name))

        image_width = jsonfile["IMAGE"]["WIDTH"]
        image_height = jsonfile["IMAGE"]["HEIGHT"]

        with open(os.path.join(training_path, 'labels', image_name.split('.')[0]+'.txt'), 'w') as text:
            for each in jsonfile["ANNOTATION_INFO"]:
                """
                    XTL : 왼쪽 상단 X
                    YTL : 왼쪽 상단 Y
                    XBR : 오른쪽 하단 X
                    YBR : 오른쪽 하단 Y
                """
                diseases = str(each["DISEASES"])  # '1'

                half_x = (each["XBR"]-each["XTL"])/2
                half_y = (each["YBR"]-each["YTL"])/2

                x = str((each["XTL"]+half_x) / image_width)
                y = str((each["YTL"]+half_y) / image_height) 
                w = str((half_x*2) / image_width)  # half*2 : 원상태
                h = str((half_y*2) / image_height) 

                context = ' '.join([diseases, x, y, w, h])
                text.write(context+'\n')
            text.close()
        f.close()

print("Training files Done")

files = []
for dirname, _, filenames in os.walk('/home/pimang62/AI-Challenge-for-Biodiversity/YOLOv8/data/beekeeping/Validation/02.라벨링데이터'):
    for filename in filenames:
        files.append(os.path.join(dirname, filename))
        
for file in files:
    with open(file, 'r', encoding='ISO-8859-1') as f:
        try:
            jsonfile = json.load(f)
            
            image_url = jsonfile["IMAGE"]["IMAGE_URL"]
            image_name = jsonfile["IMAGE"]["IMAGE_FILE_NAME"]

            # 이미지 요청 및 저장 : '/home/pimang62/AI-Challenge-for-Biodiversity/YOLOv8/data/beekeeping/Validation/images/~.jpg'
            urllib.request.urlretrieve(image_url, os.path.join(validation_path, 'images', image_name))

            image_width = jsonfile["IMAGE"]["WIDTH"]
            image_height = jsonfile["IMAGE"]["HEIGHT"]

            with open(os.path.join(validation_path, 'labels', image_name.split('.')[0]+'.txt'), 'w') as text:
                for each in jsonfile["ANNOTATION_INFO"]:
                    """
                        XTL : 왼쪽 상단 X
                        YTL : 왼쪽 상단 Y
                        XBR : 오른쪽 하단 X
                        YBR : 오른쪽 하단 Y
                    """
                    diseases = str(each["DISEASES"])  # '1'

                    half_x = (each["XBR"]-each["XTL"])/2
                    half_y = (each["YBR"]-each["YTL"])/2

                    x = str((each["XTL"]+half_x) / image_width)
                    y = str((each["YTL"]+half_y) / image_height) 
                    w = str((half_x*2) / image_width)  # half*2 : 원상태
                    h = str((half_y*2) / image_height) 

                    context = ' '.join([diseases, x, y, w, h])
                    text.write(context+'\n')
                text.close()
            f.close()
        except json.JSONDecodeError:
            print(f"JSONDecodeError: {file} is not a valid JSON file or is empty.")
            continue  # 다음 파일로 넘어감
            
print("Validation files Done")