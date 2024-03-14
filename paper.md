#  Abstract

Video streaming is a common service utilized in todays times, ranging from popular platforms such as Netflix, Disney, and Amazon Prime to live video calls facilitated by WhatsApp and FaceTime. Given the growing computational capabilities and the imperative of delivering optimal end-user experiences, there arises a necessity to develop methods for testing and analyzing the video quality of streaming content. In our research, we propose a method for analyzing the same as well as a substantial publicly available dataset comprising thousands of distorted frames. We employ a Convolutional Neural Network (CNN) to train a model for discerning whether a frame in a video input is glitched or not, addressing the imperative of ensuring seamless video playback and enhanced user satisfaction.

Keywords- Classification,Neural Network ,Video quality

# INTRO

Introduction:

The integration of Deep Learning (DL) methodologies has catalyzed a significant paradigm shift in modern society, augmenting cognitive capabilities beyond traditional data analysis frameworks. With applications ranging from face detection to object classification, DL technologies have permeated various aspects of daily life, profoundly influencing how individuals interact with data. This technological evolution extends beyond conventional boundaries, with DL's impact increasingly felt in domains where its utilization transcends conventional data processing paradigms. In this context, our research focuses on the burgeoning realm of entertainment content consumption, exemplified by the widespread adoption of video streaming services.

Over the past decade, the landscape of entertainment consumption has undergone a transformative metamorphosis, fueled by the proliferation of video services such as YouTube, Netflix, and Hotstar. Concurrently, the democratization of data accessibility has empowered individuals from diverse backgrounds to engage with these services as a primary source of entertainment. This shift underscores a fundamental change in how society interacts with media, marked by an unprecedented fusion of technology and entertainment.

Moreover, the pervasive integration of Artificial Intelligence (AI) technologies across various sectors, including home automation and healthcare, signals a broader technological revolution. The emergence of smart home systems and AI-driven healthcare solutions epitomizes this paradigmatic shift, highlighting the transformative potential of AI in enhancing daily living experiences. Additionally, continuous advancements in media devices, boasting unparalleled computational capabilities, herald a new era of innovation and possibility in the realm of entertainment technology.

However, amidst this technological progress, significant challenges and limitations persist. The creation of comprehensive datasets containing diverse glitches and noise types remains a formidable challenge, compounded by the scarcity of publicly available datasets in this domain. Our research addresses this challenge by meticulously curating a dataset comprising over 18,000 images, categorized into glitched and non-glitched classes. Furthermore, existing Video Quality Assessment (VQA) algorithms suffer from limited understanding, real-time processing constraints, and a lack of large, freely available datasets for training and evaluation purposes. These limitations underscore the critical need for robust methodologies and tools for video quality analysis, which our research endeavors to address.

Driven by these converging trends, our research endeavors to explore and enhance the landscape of video services by leveraging cutting-edge DL methodologies. Through the creation of open-source datasets encompassing various glitches and the development of Convolutional Neural Network (CNN)-based DL models, our objective is to comprehensively analyze video quality and contribute to the ongoing evolution of entertainment technology. By elucidating the need for video quality analysis and synthesizing our findings across diverse service platforms, we aim to propel the field towards new frontiers of exploration and innovation.

# II Literature survey

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

  ### 4.3 Classification

  
  
  
  ## 4.4 Total creation
  ## 4.5 Preprocessing

# v Results and discussions
The deep learning model acheived impressive results in classifying real time video showcasing its robustness and efficiency in accurately classifying video frames for glitches and noise.Upon training the modelwith the curated datset it obtained an overall accuracy of 99.7% indicating its high precission in classifying noise in video files. The precisio recall and f1 score for is xyz.Furthermore the model showcased wxceptional performance across all type of video formats demonstrating its adaptability and robustness in real-world scenarios. The integration of advanced data augmention techniques during the traing pocess contributed significantly to the models great performance.

In conclusion, the implementation of AI-driven video quality analysis demonstrates promising prospects for revolutionizing the assessment and enhancement of video content across diverse platforms.Through the utilization of advanced deep learning methodologies, our research has showcased the model's remarkable accuracy, precision, and recall rates in discerning intricate nuances within video frames. The meticulous curation of a diverse dataset, encompassing various glitches and noise types, has played a pivotal role in bolstering the model's robustness and applicability to real-world scenarios. Moreover, the superiority of deep learning techniques over traditional algorithms highlights the transformative potential of AI in tackling complex image classification tasks, including video quality analysis.

### Future Work
In considering future endeavors, expanding the scope of our model to accommodate real-time video streaming presents an intriguing avenue for enhancing video quality analysis. While our current framework adeptly processes uploaded video files, extending its capabilities to seamlessly handle live streaming poses a significant yet promising challenge. By integrating real-time processing capabilities and adaptive algorithms, we can empower our model to dynamically analyze streaming content, enabling timely detection and mitigation of quality degradation issues as they occur. Furthermore it can be directly preinstalled into hardware like tv's and smartphones to beforehand predict the quality of video and providing the user with an notification regarding the cause and the solution to make it better hence increasing the overall user experience.


# VI REFERENCES




# links for internal refernce

https://www.researchgate.net/publication/344621593_Video_Quality_Enhancement_Using_Deep_Learning-Based_Prediction_Models_for_Quantized_DCT_Coefficients_in_MPEG_I-frames


https://pdf.sciencedirectassets.com/280203/1-s2.0-S1877050918X00088/1-s2.0-S1877050918309335/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLWVhc3QtMSJHMEUCIAqmKv6rAl2bTOkSUjc2bpYES3401y49QSx%2F8CiSpqSuAiEA3XQaXrrsyKRVK0P4%2FwBekrM3BmolMzSXCHFunxx2ocIqswUIJxAFGgwwNTkwMDM1NDY4NjUiDFpxbxAAecjl20b4GSqQBTZnupY%2Ba59UbPuXGxpInjPhNpmfTDZ51dZFJ6Ptzs8rBikeQhJOOYgDCK31g0K7gxMFYJzVy6tYTFP6TIBGmDUvbVwH1UDFjAH2%2B%2FrdTZ%2By0N5redQ1PghcufE6NS3%2BTkh8iSEDIQje1h36K%2B%2FYZT5bo14rJhitEefu%2BkbL125xZ2GHw9viyFvy%2F0GThKk4cnPrkyW0XZtU9DdRlZpWWK27t6Iyl4g0L8p8pvsPqHW%2FsvnAh0wyYotiUDtdI%2BJAAdPsk3Cmkf63G17iuYTbiENVGLVgxz3Fg0n9hNaX3lWVhBfJ03enByuDdO0QT5FVGIgTRDPJ9vHnCh3vYZHiHMLbpw%2BbegXr2UYxwZUQwz8s0IxD6hAivRYyzKleMuh6LEzJ3z9rKILuXoG5loLbNyg3q0um6P5v6Ww5cWUApuHK4IpreppXBnY9oDmCWIHJ7rYJ9P29NTiZqr6eJqN5kR6Y8lOAtK%2FRcTtpG%2BVqxDulRpKHPI9uSU2CdvB%2BI5X3gRuWY5bjZE62jvcFrX3yF%2FWdl7OKdjs0sxVUJzLK%2F%2F8R3vz14ILLtZ7EKMUrozpLOiXIigLxluUDKN6P0ytycWXKS9xH%2BPrScAZzrkfyvZp%2BCuL0eNw1PQuqwU%2FjLE%2FLS2xo4NqTIs9a%2BAuzuK0QQnmfqcmcNpduM0%2Fc93QepIbvrr6%2Bip25r%2Bpl10Njt%2FNbRf6cthREfxs%2FI7UGslyuxdhB7AuIrHFcQMXfRShsfHwUHVe%2BvQ%2BkONcb%2FjlVGh7AivgGCWH5IOPtPLJDJ0XItfLjcgxaBxdmWQPnVVf1lmcUrGGKtInmOnch6zXCvSFKXsuJk5Zm11JwFwnUrLK6WEhVHrzWfkaL1QLBUhzQiA86MObYha8GOrEBVPGafUw%2BHUeRKw8dvw53tqOU2m3OPL32gSD5aSNMdaACagXYj71Pe65JVach4jc0pzNLzXRSXDNbz7SsfwQK%2FidWl5LMQckC4o9XG%2FdlRiap65cSdvnJz6CpCBIVqVhzsXI33lcVA%2Fj4auKewZ8bjp%2FuwEjvNmANXKWujdaCLTGus7B6xUPqBd%2FlVBXnVAYmkQ%2F3f0xceB3pMAhoYGtN7JjU3MZ9dF3V6Fcrq3blg6pF&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240301T071852Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYR5UR7OW2%2F20240301%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=7e34c572f61d4d5414a8ac55cfaa6486fa940f4580a3ae7fefcd484e8d306bfe&hash=8c7e64ef80b297591adb1a21c87d6a069c1ea365971e97f31ea9d2cb49814802&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1877050918309335&tid=spdf-03b35993-35a2-425e-8856-392deb426452&sid=181e1eb6542e2641c44a7f10fda8c8c84adbgxrqb&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=130c5a510b5755535702&rr=85d7601ebd937eaa&cc=in


https://www.sciencedirect.com/science/article/pii/S1877050918309335


