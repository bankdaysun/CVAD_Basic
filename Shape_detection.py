import cv2
import numpy as np
image_path = "path"
def detect_rectangle(image_path):
    frame = cv2.imread(image_path)
    if frame is None:
        print(f"error: {image_path}")
        return

    gray = cv2.cvtColor(_, cv2.COLOR_BGR2GRAY)##########
    blurred = cv2.GaussianBlur(gray, (_, _), 0)#######
    edges = cv2.Canny(blurred, _, _)#########
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > _:  #########
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)

            if len(approx) == _:##########
                cv2.drawContours(_, [approx], 0, (_, _, _), 4)######
                cv2.putText(frame, "Rectangle", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imshow("Rectangle Detection", _)########
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect_rectangle(image_path)

print("Finish")