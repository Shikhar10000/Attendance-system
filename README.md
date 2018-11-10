Facenet: Real-time face recognition using deep learning Tensorflow 
This specific implementation is the code used to deploy on Floydhub 

app.py uses flask for api deployemnt.

This is completly based on deep learning nueral network and implented using Tensorflow framework. 
# Installation Python Libraries:

tensorflow (1.4.0)

scipy (0.17.0)

scikit-learn (0.19.1)

Opencv (2.4.9.1)

pyrebase

flask

# Implementation
## For firebase connection refer Pyrebase documentation
https://github.com/thisbejim/Pyrebase

1. Run the download_attendance.py to download the necessary files.
2. Under packages in facenet.py file line 374 and point it to the model folder.
3. Then use any of the webcam / image/ video to run the program.

for deployment refer the deployment documentation on floyd hub.
https://docs.floydhub.com/guides/serving/
