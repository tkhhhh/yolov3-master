import cv2
from detect import *

def video_cut():
    video1_path = "video/1.mp4"
    video2_path = "video/1out.mp4"
    image1_path = "samples"
    image2_path = "outputs"
    key = 0
    cap = cv2.VideoCapture(video1_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    frame_rate = int(cap.get(5))
    width = int(cap.get(3))
    height = int(cap.get(4))
    size = (width,height)
    ret, image = cap.read()
    while ret:
        cv2.imwrite(image1_path + "/" + str(key) + ".jpg",image)
        ret, image = cap.read()
        key += 1
    dete()
    out = cv2.VideoWriter(video2_path, fourcc, frame_rate, size, 1)
    #fgbg = cv2.createBackgroundSubtractorMOG2()
    for i in range(key):
        filename = image2_path + "/" + str(i) + ".jpg"
        img = cv2.imread(filename)
        #img = fgbg.apply(img)
        out.write(img)
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_cut()
