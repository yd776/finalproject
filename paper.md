
# III Research problem

# IV Methodology

  ## 4.1 Dataset description

The dataset we've created consists of 18,000 individual frames extracted from 17 videos. This dataset is categorized into two distinct subsets: "Glitched" and "Not Glitched." The "Glitched" subset encompasses various types of noise and glitches, including:

Laplacian Transformation: This method, derived from the Laplace distribution, was applied to induce irregularities resembling sudden and intense changes in pixel values.

Salt and Pepper Noise: By introducing random, sporadic white and black pixels, akin to salt and pepper sprinkled on an image, we mimicked the presence of impulsive noise in digital media.

Noisy Transformation: Through the injection of Gaussian noise, we replicated the subtle distortions often observed in images, enhancing the dataset's diversity and robustness.

Hazy Transformation: Utilizing haze simulation techniques, we replicated atmospheric interference, resulting in a blurred and obscured appearance, akin to images captured in adverse weather conditions.

By integrating these transformations, our dataset reflects a spectrum of anomalies encountered in real-world scenarios, facilitating comprehensive analysis and evaluation in image processing tasks.
  
  ### 4.2 Dataset Generation
To form our dataset, we procured 10 video files in the .mp4 format. These videos were first converted into individual frames. Subsequently, a random selection process was employed, where 20% of these frames were subjected to various types of noise and glitches using laplacian functions and Python libraries. This step aimed to introduce variability and challenge into the dataset. Ultimately, our dataset consists of two distinct classes: glitched and non-glitched, each comprising 9000 individual images.

  ## 4.3 Proposed System

  Video Acquisition and Storage: The system collects user videos via a Flask web interface and stores them locally.

Frame Extraction and Storage: The received video undergoes frame extraction, and individual frames are saved locally for analysis.

Dataset Expansion: To diversify the training dataset, 20% of frames are randomly selected and augmented with glitches and noises using vector calculations.

Frame Classification: Each frame, original or augmented, is classified using a Convolutional Neural Network (CNN) to determine if it's glitched or not.

Result Presentation: The system displays the classification results to users, indicating glitched frames and offering a qualitative assessment of video quality.

Quantification of Glitchiness: As an enhancement, the system aims to quantify glitch severity, providing users with a numeric measure of video degradation for informed decision-making
  ## 4.5 Preprocessing

# v Results and discussions
The deep learning model acheived impressive results in classifying real time video showcasing its robustness and efficiency in accurately classifying video frames for glitches and noise.Upon training the modelwith the curated datset it obtained an overall accuracy of 99.7% indicating its high precission in classifying noise in video files. The precisio recall and f1 score for is xyz.Furthermore the model showcased wxceptional performance across all type of video formats demonstrating its adaptability and robustness in real-world scenarios. The integration of advanced data augmention techniques during the traing pocess contributed significantly to the models great performance.




