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

We used many vecor operations to add different types of glitches and noises to the vector format of the images using the numpy libraries, The process involved transormations,



### Language used 👩‍💻
* Python
* Flask

### Libraries used 📚



### Team Members 🧑
1. Yashas Dewan
2. Mihir Singh Malik
3. Dr.G.Vdivu (Guide)




