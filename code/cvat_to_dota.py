import os
import xml.etree.ElementTree as ET
import math

# Function to rotate a point around a center
def rotatePoint(xc, yc, xp, yp, theta):
    xoff = xp - xc
    yoff = yp - yc
    cosTheta = math.cos(math.radians(theta))
    sinTheta = math.sin(math.radians(theta))
    pResx = cosTheta * xoff - sinTheta * yoff
    pResy = sinTheta * xoff + cosTheta * yoff
    return str(int(xc + pResx)), str(int(yc + pResy))

# Function to convert XML to TXT
def totxt(xml_path, out_path, cls_list):
    files = os.listdir(xml_path)
    for file_name in files:
        tree = ET.parse(os.path.join(xml_path, file_name))
        root = tree.getroot()
        
        images = root.findall('image')
        for image in images:
            name = image.get('name').split('.')[0]
            output = os.path.join(out_path, f"{name}.txt")

            with open(output, 'w') as f:
                boxes = image.findall('box')
                for box in boxes:
                    cls = box.get('label')  # Получение значения label из каждого <box>
                    label = box.get('label')
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

                    cls_index = cls_list.index(cls) if cls in cls_list else -1

                    f.write(f"{cls_index} {x0} {y0} {x1} {y1} {x2} {y2} {x3} {y3}\n")

        print(f"Wrote to: {output}")

# Main function or entry point
if __name__ == "__main__":
    xml_path = './IN'   # "path/to/xml/files"
    out_path = './lables/' # "path/to/save/txt/files"
    cls_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "основное", "дополнительное", "номер", "режим"]  # class labels
    os.makedirs(out_path, exist_ok=True)
    totxt(xml_path, out_path, cls_list)
