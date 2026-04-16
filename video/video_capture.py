import cv2

def start_camera():
   
   #open webcam
   
    cam=cv2.VideoCapture(0)



    # check if the webcam is opened correctly
    if not cam.isOpened():
      print("Cannot open camera")
      exit()
   

   #Display the video feed
    while True:
        ret, frame = cam.read()
       

       #If no frame is captured, break the loop
        if not ret:
           break

        
           #convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)





        #Display the frames
        cv2.imshow('Webcam', gray)

        #Exit the webcam feed when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
           
            break



    #Release the webcam and close all windows
    cam.release()
    cv2.destroyAllWindows()



        
        
        
       
