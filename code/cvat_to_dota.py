import os
import xml.etree.ElementTree as ET
import math
import numpy as np

# Function to rotate a point around a center
def rotatePoint(xc, yc, xp, yp, theta):
    xoff = xp - xc
    yoff = yp - yc
    cosTheta = math.cos(math.radians(theta))
    sinTheta = math.sin(math.radians(theta))
    pResx = cosTheta * xoff - sinTheta * yoff
    pResy = sinTheta * xoff + cosTheta * yoff
    return int(xc + pResx), int(yc + pResy)

# Function to convert XML to TXT
def totxt(xml_path, out_path, cls_list):
    files = os.listdir(xml_path)
    for file_name in files:
        tree = ET.parse(os.path.join(xml_path, file_name))
        root = tree.getroot()
        
        count = 0
        images = root.findall('image')
        for image in images:
            count += 1
            # name = image.get('name').split('.')[0]
            name = image.get('name').rsplit('.', 1)[0]  # Метод rsplit('.', 1) разбивает строку на две части, начиная справа, по первому вхождению точки '.'
            output = os.path.join(out_path, f"{name}.txt")

            with open(output, 'w') as f:
                boxes = image.findall('box')
                img_width = float(image.get('width'))
                img_height = float(image.get('height'))
                for box in boxes:
                    cls = box.get('label')  # Получение значения label из каждого <box>
                    xtl = float(box.get('xtl'))
                    ytl = float(box.get('ytl'))
                    xbr = float(box.get('xbr'))
                    ybr = float(box.get('ybr'))
                    rotation = float(box.get('rotation', 0))

                    cx = (xtl + xbr) / 2
                    cy = (ytl + ybr) / 2
                    w = xbr - xtl
                    h = ybr - ytl

                    x0, y0 = rotatePoint(cx, cy, cx - w / 2, cy - h / 2, -rotation)
                    x1, y1 = rotatePoint(cx, cy, cx + w / 2, cy - h / 2, -rotation)
                    x2, y2 = rotatePoint(cx, cy, cx + w / 2, cy + h / 2, -rotation)
                    x3, y3 = rotatePoint(cx, cy, cx - w / 2, cy + h / 2, -rotation)

                    # Normalize the corner points
                    # x0, y0, x1, y1, x2, y2, x3, y3 = map(lambda x: x / img_width if x in [x0, x1, x2, x3] else x / img_height, [x0, y0, x1, y1, x2, y2, x3, y3])
                    x0, y0, x1, y1, x2, y2, x3, y3 = map(lambda x: round(x / img_width, 6) if x in [x0, x1, x2, x3] else round(x / img_height, 6), [x0, y0, x1, y1, x2, y2, x3, y3])

                    cls_index = cls_list.index(cls) if cls in cls_list else -1
                    f.write(f"{cls_index} {x0} {y0} {x1} {y1} {x2} {y2} {x3} {y3}\n")
                    # f.write(f"{cls} {x0} {y0} {x1} {y1} {x2} {y2} {x3} {y3}\n")

        print(f"✅ Done with {count} files [images]")

# Main function or entry point
if __name__ == "__main__":
    xml_path = './IN'   # "path/to/xml/files"
    out_path = './labels/' # "path/to/save/txt/files"
    cls_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "основное", "дополнительное", "номер", "режим"]  # class labels
    os.makedirs(out_path, exist_ok=True)
    totxt(xml_path, out_path, cls_list)
