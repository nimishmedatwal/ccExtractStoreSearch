### ccExtractStoreSearch
ccExtractStoreSearch is a website on which video(s) can be uploaded, processed and then searched using the subtitles in that video as keywords.


### **Features**
- Upload a video file
- Extract subtitles from that video 
- Upload the Video file to AWS S3 and the .srt (captions) file to DynamoDB
- Searching for a particular word or phrase returns the time segment within which the video (or videos) has those phrases being mentioned.

### Programming Languages & Technologies

- This website is created using python with structure of **Django REST Framework**
- **AWS S3** is used for storing the video file
- **AWS DynamoDB** is used for storing .srt file
- **Boto38* is used for integration of AWS in python

## Installation and Usage
- For cloning this Repository : git clone https://github.com/nimishmedatwal/ccExtractStoreSearch.git
- Refer to this website for installing ccextractor https://ccextractor.org/public/general/downloads/
- run: *pip install -r requirements.txt* in your shell.
- Run this django project by : *python manage.py runserver*

##Demo Link
- See the Demo Video here : https://drive.google.com/file/d/1IXzZ-u4rA6klFNK089YdEp1Tyx4HnzsT/view?usp=sharing
