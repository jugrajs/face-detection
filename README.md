# Face Detection

This Python script utilizes the OpenCV library to perform real-time face detection on a live video feed. It employs the Haar Cascade classifier to locate faces within the video stream and draw bounding boxes around them.

## Getting Started

1. Clone this repository to your local machine:
```
git clone https://github.com/yourusername/face-detection.git
```
2. Navigate to the project directory:
```
cd face-detection

```

3. **The Haar Cascade XML file for frontal face detection (`haarcascade_frontalface_default.xml`) is already included in the repository.**

4. Make sure you have OpenCV installed by using the `requirements.txt` file:
```
pip install -r requirements.txt

```

5. Run the script:

```
python3 face_detection.py

```

6. The script will open the default camera (usually the webcam) and display the live video feed with faces detected and bounding boxes drawn around them.

7. Press the 'Esc' key to exit the application.

## Dependencies

- Python
- OpenCV

## Usage

- `face_detection.py`: The main script that captures the live video feed and performs real-time face detection using the Haar Cascade classifier.

## Notes

- You can adjust the `sf` (scale factor) and `nb` (number of neighbors) parameters in the `localize_face` function to fine-tune the face detection sensitivity.



   
