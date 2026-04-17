import cv2

def start_camera():
    
    # open webcam
    cam = cv2.VideoCapture(0)

    # check if the webcam is opened correctly
    if not cam.isOpened():
        print("Cannot open camera")
        exit()

    # get first frame (previous frame)
    ret, prev_frame = cam.read()
    if not ret:
        print("Failed to read from camera")
        exit()


    # start video loop
    while True:
        ret, frame = cam.read()

        if not ret:
            break


       
        # show the frames
        cv2.imshow('Webcam', frame)
        

      

        # exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # cleanup
    cam.release()
    cv2.destroyAllWindows()