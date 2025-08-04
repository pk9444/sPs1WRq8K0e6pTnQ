# MonReader

## CONTEXT

The client, focused in AI and Computer Vision has developed a mobile app "MonReader" that provides a document digitalization experience for the blind, for researchers, and for general users who want an automated solution for bulk-scanning documents.  

MonReader detects page flips from low-resolution camera preview and takes a high-resolution picture of the document, recognizing its corners and crops it accordingly, and it dewarps the cropped document to obtain a bird's eye view, sharpens the contrast between the text and the background and finally recognizes the text with formatting kept intact, being further corrected by MonReader's ML powered redactor.

## DATA DESCRIPTION

The Client collected page flipping video from smart phones and labelled them as "flipping" and "not flipping".

The client then clipped the videos as short videos and labelled them as flipping or not flipping. The extracted frames are then saved to disk in a sequential order with the following naming structure: VideoID_FrameNumber.

## PROJECT GOALS
- Predict if the page is being flipped using a single image.
- Predict if a given sequence of images contains an action of flipping.

### SUCCESS METRIC 
 - Evaluate model performance based on F1 score -> the greater it is, the better the model.

## METHODOLOGY

<img width="1471" height="488" alt="Apziva_P4_Methodology" src="https://github.com/user-attachments/assets/d17e81fd-13aa-45f0-9c9b-f7f23a3f49f1" />

## THE NEURAL NETWORK (CNN) PROCESS

<img width="319" height="540" alt="Apziva_P4_CNN" src="https://github.com/user-attachments/assets/34ec6b92-81cf-4604-84d1-9d315b2b1d70" />

## PERFORMANCE EVALUATION

<img width="1188" height="764" alt="Apziva_P4_Train_Val_Loss" src="https://github.com/user-attachments/assets/e764bf2a-8f35-4c28-9d36-5a6c00c3983e" />


## REAL-TIME DEPLOYMENT ARCHITECTURE

<img width="635" height="460" alt="Apziva_p4_dep_arch" src="https://github.com/user-attachments/assets/7340c7a4-8f9f-465e-a5b8-8d67f0009890" />


