## FINAL YEAR PROJECT 
### VIDEO QUALITY ANALYSIS USING AI

### INTRODUCTION :movie_camera:

The number of people watching content for entertainment has grown tremendously in the past decade with the increase in use of streaming services like 
Netfilx , Disney plus, Amazon Prime Video.Several objective video quality assessment (VQA) algorithms exist, whose performance is typically evaluated using the results 
of a subjective study performed by the video quality experts group (VQEG) in 2000.


There is a great need for a free, publicly available subjective study of video quality that embodies state-of-the-art in video processing 
technology and that is effective in challenging and benchmarking objective VQA algorithms.

With the increase in computation technology in the past decade and the advancement of AI ad ML technologies.Our objective is to create an ML model that will be able to 
analyse the quality of each frame in a video file.

### PREVIOUS TECHNIQUES :information_desk_person:

### CHALLENGES FACED :anguished:

The main challenge faced was the creation of a dataset containing all different types of glitches as there are less number of publically available datasets containg 
different types of glitches and noise.

The dataset we have created contains more than 18000 images divided into 2 classes glitched and not glitched.

The glitched frames have the following type of noises:

* LAPLACIAN
* SALT AND PEPPER
* NOISY
* HAZY

### OBJECTIVE OF THE PROJECT :grey_question :grey_question:

The main objective of the project was to create an ML model based on CNN (Convolutional Neural Network).
We created our ML model based on our dataset created 
to be able to analyse video files frame by frame and can test the quality based on the output provided by the classification model.

### INNOVATION AND IDEA OF THE PROJECT 💡:

The original idea was part on a research project given by LGSI (LG soft India), which wanted students to explore ways to create a deep learning model that will be able to predict the qualaity of video data coming form streaming services.

The major issue faced was the unavailabilty of a large enough dataset to train a model on.To solve this problem we had to create our own datset by applying different types of glitches and noises on different videos to form a large enough dataset conating 18000 frames for training our CNN model.

We used many vecor operations to add different types of glitches and noises to the vector format of the images using the numpy libraries, The process involved transormations,dot products ,scaler multiplications etc.

### SCOPE AND APPLICATION

### ARCHITECTURE

### PROPOSED MODULES AND ALGORITHM DESCRIPTION


The proposed method follows the following steps:


* Procuring the video from the user using a flask webpage stored in the local drive using selection feature.
* Converting the received video into individual frames and storing them locally in a frames directory.
* Taking 20% of the frames to be formated and modified by using different vector calculations to add glitches and noises to be added in the training datset , so that our overall dataset increases with reusing.
* The frames are then classified one by one suing a CNN model into two classes either glitched or not glitched.
* The final result is then shown to the user on the screen along with the frame that has been identified as glitched.
* The planned final project is planned be able to give a numeric quantity as well on the amount of glitchiness.



### INSTALLATION 

* Download the ML model mentioned above in the github repository above
* Create a local folder on your VS code and add the followinf files
** APP.PY
** INDEX.HTML


* Run app.py on your vs local and open the local 3000 local host on your browser.
* Upload the video that you want to get result of
* Update the result to the user in index.html
  


### UML DIAGRAM :
![](https://github.com/yd776/finalproject/blob/869c4f0ebe570a9b13d1232d28e7babf5005e82a/Screenshot%202024-02-14%20122058.png) 



### Languages used 👩‍💻
* Python
* Flask 
* HTML <>

### Libraries used 📚

* Flask: A web framework for building web applications.
* os: Provides a way to interact with the operating system, such as working with files and directories.
* cv2 (OpenCV): A computer vision library for image processing and computer vision tasks.
* glob: Used for file path pattern matching.
*shutil: Provides utility functions for file operations.
* random: For generating random numbers or making random selections.
* numpy: A library for numerical computations and array manipulation.
* skimage: Part of the scikit-image library, used for image processing.
* PIL (Pillow): Python Imaging Library, used for working with images.
* ImageGlitcher (from glitch_this): A library for creating glitch art from images.



### Team Members 🧑
1. Yashas Dewan
2. Mihir Singh Malik
3. Dr.G.Vdivu (Guide)





