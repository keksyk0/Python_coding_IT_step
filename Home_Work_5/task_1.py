import cv2
from PIL import Image

image_path = 'ezgif.com-gif-maker-3.jpg'
left_eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_lefteye_2splits.xml")
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
left_eye = left_eye_cascade.detectMultiScale(gray)
person = Image.open(image_path)

monocle = Image.open('pngegg (1).png')
person = person.convert("RGBA")
monocle = monocle.convert("RGBA")
for (x,y,w,h) in left_eye:
    monocle = monocle.resize((int(w * 2), int(h * 2)))
    offset_x = int(x - w * 0.3)
    offset_y = int(y - h * 0.1)
    person.paste(monocle, (offset_x, offset_y), monocle)

person.save("person_with_monocle.png")
person_with_monocle = cv2.imread("person_with_monocle.png")
cv2.imshow("Person_with_monocle", person_with_monocle)
cv2.waitKey()
