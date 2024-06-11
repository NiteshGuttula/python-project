pip install opencv-python
import cv2

# Load the cascade
cascade_classifier = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

# Start capturing video
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Couldn't open webcam.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame is empty
    if not ret:
        print("Error: Couldn't capture frame.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect license plates
    detections = cascade_classifier.detectMultiScale(gray, scaleFactor=1.3)

    # Draw rectangles around detected plates
    for (x, y, w, h) in detections:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('pythonlife', frame)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
