import cv2

def capture(camera = 0,frameName = "Image",filename = "Image.png"):

    cap = cv2.VideoCapture(camera)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    ret, frame = cap.read() 
    
    if ret:
        image_filename = filename
        cv2.imwrite(image_filename, frame)
        print(f"Image saved as {image_filename}")

        # Optional: Display the captured image for 5 seconds
        cv2.imshow(frameName, frame)
        cv2.waitKey(5000) # Wait for 5000 milliseconds (5 seconds)
        cv2.destroyAllWindows()
    else:
        print("Error: Failed to capture frame.")

    # 4. Release the camera resource
    cap.release()

capture()