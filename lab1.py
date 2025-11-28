import cv2

img_path = 'IMG_20180813_185949.jpg'
vid_path = '(1993) DBZ - Broly LSSJ.mp4'

# TASK 2

img = cv2.imread(filename=img_path,flags=cv2.IMREAD_COLOR)
cv2.namedWindow('abas color', cv2.WINDOW_NORMAL)
cv2.resizeWindow("abas color", 2520, 1890)
cv2.imshow('abas color', img)
cv2.waitKey(0)
cv2.destroyWindow('abas color')

img = cv2.imread(filename=img_path,flags=cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('abas grey', cv2.WINDOW_GUI_EXPANDED)
cv2.resizeWindow("abas grey", 2520, 1890)
cv2.imshow('abas grey', img)
cv2.waitKey(0)
cv2.destroyWindow('abas grey')

img = cv2.imread(filename=img_path,flags=cv2.IMREAD_REDUCED_COLOR_8)
img = cv2.resize(img, None, fx=8, fy=8)
cv2.namedWindow('abas reduced', cv2.WINDOW_NORMAL)
cv2.resizeWindow("abas reduced", 2520, 1890)
cv2.imshow('abas reduced', img)
cv2.waitKey(0)
cv2.destroyWindow('abas reduced')

# TASK 3-4

broly = cv2.VideoCapture(vid_path)
ok, img = broly.read()
w = int(broly.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(broly.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = float(broly.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
vwz = cv2.VideoWriter("broly.mp4", fourcc, fps, (w,h))
broly.set(cv2.CAP_PROP_POS_FRAMES, 65934)
frame = 65934
while ok:
    ok, img = broly.read()
    if frame == 66174: break
    cv2.imshow('broly', img)
    vwz.write(img)
    if cv2.waitKey(1) & 0xFF == ord("q"): break
    frame+=1
broly.release()
cv2.destroyWindow('broly')

# TASK 5

png = cv2.imread(filename=img_path,flags=cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(png, cv2.COLOR_BGR2HSV)
cv2.namedWindow('abas BGR', cv2.WINDOW_NORMAL)
cv2.namedWindow('abas HSV', cv2.WINDOW_NORMAL)
cv2.imshow('abas BGR', png)
cv2.imshow('abas HSV', hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

# TASK 6-7

vid = cv2.VideoCapture(0)
ok, img = vid.read()
w = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
vw = cv2.VideoWriter("output.mp4", fourcc, 10, (w,h))
while True:
    ok, img = vid.read()
    height = img.shape[0]; width = img.shape[1]
    hc = height // 2; wc = width // 2
    b,g,r = map(int, img[hc,wc])
    blue = abs(r - 0) + abs(g - 0) + abs(b - 255)
    green = abs(r - 0) + abs(g - 255) + abs(b - 0)
    red = abs(r - 255) + abs(g - 0) + abs(b - 0)
    if red <= green and red <= blue: color = (0,0,255)
    if red <= green and red <= blue: color = (0, 0, 255)
    if red <= green and red <= blue: color = (0, 0, 255)
    #img = cv2.bitwise_not(img)
    cv2.rectangle(img, (wc - 25 // 2, hc - 50), (wc + 25 // 2, hc + 50), color, 4)
    cv2.rectangle(img, (wc - 50, hc - 25 // 2), (wc + 50, hc + 25 // 2), color, 4)
    cv2.imshow('img', img)
    vw.write(img)
    if cv2.waitKey(1) & 0xFF == ord("q"): break
vid.release()
cv2.destroyAllWindows()

# TASK 8

def pick_color(p):
    dR = math.dist(p,[0,1,0]); dG = math.dist(p,[0,0,1]); dB = math.dist(p,[1,0,0])
    if dR >= dG and dR >= dB: return (255,0,0)
    elif dG >= dR and dG >= dB: return (0,255,0)
    else: return (0,0,255)
vid = cv2.VideoCapture(0)
ok, img = vid.read()
w = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
while True:
    ok, img = vid.read()
    height = img.shape[0]; width = img.shape[1]
    hc = height // 2; wc = width // 2
    fillColor = pick_color(img[hc,wc])
    cv2.rectangle(img, (wc - 25 // 2, hc - 50), (wc + 25 // 2, hc + 50), fillColor, cv2.FILLED)
    cv2.rectangle(img, (wc - 25 // 2, hc - 50), (wc + 25 // 2, hc + 50), (0,0,255), 4)
    cv2.rectangle(img, (wc - 50, hc - 25 // 2), (wc + 50, hc + 25 // 2), fillColor, cv2.FILLED)
    cv2.rectangle(img, (wc - 50, hc - 25 // 2), (wc + 50, hc + 25 // 2), (0,0,255), 4)
    cv2.rectangle(img, (wc - 25 // 2 + 3, hc - 25 // 2 - 2), (wc + 25 // 2 - 3, hc + 25 // 2 + 2), fillColor, cv2.FILLED)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord("q"): break
vid.release()
cv2.destroyAllWindows()

# TASK 9

cap = cv2.VideoCapture(r"http://[REDACTED]:8080/video")
while cap.isOpened():
    ok, img = cap.read()
    cv2.imshow('cam', cv2.resize(img, (640,480)))
    if cv2.waitKey(1) & 0xFF == ord("q"): break
cap.release()
