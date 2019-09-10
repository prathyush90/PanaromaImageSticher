import cv2 as cv
import os
import imutils
import numpy as np

input_path = os.path.join(os.getcwd(),'inputimages/')
out_path    = os.path.join(os.getcwd(), 'output.png');
list = os.listdir(input_path)

list_withfull_filename = [input_path+x for x in list]
list_withfull_filename = sorted(list_withfull_filename)
images = []
for image in list_withfull_filename:
    frame = cv.imread(image)
    images.append(frame)

stitcher = cv.createStitcher()
(status, stitched) = stitcher.stitch(images)

if status == 0:
    # stitched = cv.copyMakeBorder(stitched, 10, 10, 10, 10,
    #                               cv.BORDER_CONSTANT, (0, 0, 0))
    #
    # gray = cv.cvtColor(stitched, cv.COLOR_BGR2GRAY)
    # thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY)[1]
    #
    #
    # cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL,
    #                        cv.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    # c = max(cnts, key=cv.contourArea)
    #
    # # allocate memory for the mask which will contain the
    # # rectangular bounding box of the stitched image region
    # mask = np.zeros(thresh.shape, dtype="uint8")
    # (x, y, w, h) = cv.boundingRect(c)
    # cv.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
    #
    # # create two copies of the mask: one to serve as our actual
    # # minimum rectangular region and another to serve as a counter
    # # for how many pixels need to be removed to form the minimum
    # # rectangular region
    # minRect = mask.copy()
    # sub = mask.copy()
    #
    # # keep looping until there are no non-zero pixels left in the
    # # subtracted image
    # while cv.countNonZero(sub) > 0:
    #     # erode the minimum rectangular mask and then subtract
    #     # the thresholded image from the minimum rectangular mask
    #     # so we can count if there are any non-zero pixels left
    #     minRect = cv.erode(minRect, None)
    #     sub = cv.subtract(minRect, thresh)
    #
    # # find contours in the minimum rectangular mask and then
    # # extract the bounding box (x, y)-coordinates
    # cnts = cv.findContours(minRect.copy(), cv.RETR_EXTERNAL,
    #                        cv.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    # c = max(cnts, key=cv.contourArea)
    # (x, y, w, h) = cv.boundingRect(c)
    #
    # # use the bounding box coordinates to extract the our final
    # # stitched image
    # stitched = stitched[y:y + h, x:x + w]
    cv.imwrite(out_path, stitched)

    # display the output stitched image to our screen
    cv.imshow("Stitched", stitched)
    cv.waitKey(0)
else:
	print("error")