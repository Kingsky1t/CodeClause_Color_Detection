import cv2
import pandas as pd

img_path = r'colorpic.jpg'
img = cv2.imread(img_path)

# global variables
clicked = False
r = g = b = x_pos = y_pos = 0

# importing csv
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
csv = pd.read_csv('colors.csv', names=index, header=None)


def get_color_name(R, G, B):
     minimum = 10000
     for i in range(len(csv)):
          d = abs(R-int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B-int(csv.loc[i, "B"]))
          if d <= minimum:
               minimum = d
               cname = csv.loc[i, "color_name"]
     return cname


# function to get the X and y coordinates of a mouse double click
def draw_function(event, x, y, flags, param):
     if event == cv2.EVENT_LBUTTONDBLCLK:
          global b, g, r, x_pos, y_pos, clicked
          clicked = True
          x_pos = x
          y_pos = y
          b, g, r = img[y, x]
          b = int(b)
          g = int(g)
          r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:

     cv2.imshow("image", img)
     if clicked:
          
          # creates a rectangle to show the color
          cv2.rectangle(img, (10,10), (int(img.shape[1]),int(img.shape[0]*0.2)), (b, g, r), -1)

          # text inside the rectangle
          text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
          
          # print the text on the rectangle
          cv2.putText(img, text, (40, 40), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
          
          # if background color is light
          if r+g+b >= 600:
               cv2.putText(img, text, (40, 40), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

          clicked = False

     # break the loop if user clicks esc key
     if cv2.waitKey(20) & 0xFF == 27:
          break
