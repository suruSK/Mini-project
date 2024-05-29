import cv2
import
numpy as np
import
serial

# Load YOLOv3 pre-trained model yolo = cv2.dnn.readNet

("D:\Deep Learning\OpenCV\yolov3.weights",
"D:\Deep Learning\OpenCV\yolov3.cfg.txt")

# Read class names from file with open("D:\Deep Learning\OpenCV\coco.names.txt", "r") as f: classes f.read().splitlines()

#Configure webcam

input cap = cv2.VideoCapture(0)

# Initialize serial connection to Arduino board ser serial. Serial('COM7', 9600)

whil

e

True

:

#Capture frame from webcam ret, frame = cap.read()

#Perform obje Ptection on the captured frame blob cv2.dnn.blob.comImage(frame, 1/255, (320,320), (0,0,0), swapRB-True, crop=False) output_layers yolo.setInput(blob) yolo.getUnconnectedOutLayersNames() detections yolo. forward (output_layers)

#Initialize person present flag

person_present = False

#Iterate over detected

objects for detection in

detections: for object in

detection: object[5:] scores = class_id =

np.argmax(scores)

confidence scores [class_id]

if confidence > 0.5 and

classes[class_id] == "person"

: #Label the frame as "person"

cv2.putText(frame, "Person", (50,50),

CV2. FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

person_present = True

#Send signal to Arduino board based on person present

flag

If person_present:

on ser.write(b'1') # send '1' to turn lights

else:

ser.write(b'e') # send 'e' to turn lights off

# Display the processed frame cv2.imshow("Webcam Feed", frame)

# Exit on 'q' key press if cv2.waitKey(1) & 0xFF == ord('q'):

break

# Release resources

cap.release()

cv2.destroyAllWindows()

ser.close()