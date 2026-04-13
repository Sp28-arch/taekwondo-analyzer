import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame.")
        break

 
    cv2.imshow("Taekwondo Analysis - Camera Feed", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()