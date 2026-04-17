import cv2
import mediapipe as mp



def start_camera():
    
    # open webcam
    cam = cv2.VideoCapture(0)

    # check if the webcam is opened correctly
    if not cam.isOpened():
        print("Cannot open camera")
        exit()


    ret, frame = cam.read()
   
    if not ret:
        print("Failed to read from camera")
        exit()



     # Loads the pose module from mediapipe
    mp_pose = mp.solutions.pose

    #Creates the pose detection model
    pose = mp_pose.Pose()

    # Creates the drawing utility from mediapipe
    mp_drawing = mp.solutions.drawing_utils



    # start video loop
    while True:
        ret, frame = cam.read()

        if not ret:
            break


    # Convert the image to RGB format for mediapipe since OpenCV uses BGR format by default
        rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)    



    # Process the image and detect the pose
        result = pose.process(rgb)


        
            

    # Draw the pose landmarks on the original frame
        if result.pose_landmarks:
            mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)



    # 
       
        # show the frames
        cv2.imshow('Webcam', frame)
        

      

        # exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # cleanup
    cam.release()
    cv2.destroyAllWindows()