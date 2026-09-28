import cv2 as cv

# Initialize video capture from the default camera (index 0)
cap = cv.VideoCapture(0)
while True: 
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to rgb color space
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
   

    # Display the original and rgb frames
    cv.imshow('Original Frame', frame)
    cv.imshow('RGB Frame', rgb_frame)

    # Break the loop on 'q' key press
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


