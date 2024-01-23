import json

# 위에서 제공한 JSON 데이터
json_data = # file path

with open(json_data, 'r') as f:
    data = json.load(f)


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_json_to_yolo(data):
    image_info = data['IMAGE']
    annotation_info = data['ANNOTATION_INFO']

    img_file_name = image_info['IMAGE_FILE_NAME'].partition('.')[0]
    w = int(image_info['WIDTH'])
    h = int(image_info['HEIGHT'])

    yolo_data = ''
    for i, an in enumerate(annotation_info):
        xtl = an['XTL']
        ytl = an['YTL']
        xbr = an['XBR']
        ybr = an['YBR']

        b = (float(xtl), float(xbr), float(ytl), float(ybr))
        bb = convert((w, h), b)

        # Construct yolo format data
        yolo_data += "0 " + " ".join([str(a) for a in bb]) + '\n'

    # Make .txt file
    with open(f'{img_file_name}.txt', 'w') as f:
        f.write(yolo_data)


convert_json_to_yolo(data)