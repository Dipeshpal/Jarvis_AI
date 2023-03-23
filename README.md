[![Header](https://i.postimg.cc/mDCdt9Jn/Mixing-Panel-Photocentric-EDM-Youtube-Channel-Art-1.png "Header")](http://jarvis-ai-api.herokuapp.com/)    
    
    
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)    
    
# Hello, folks! <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px">    
 This project is created only for those who are interested in building a Virtual Assistant. Generally, it took lots of time to write code from scratch to build a Virtual Assistant. So, I have built a Library called "JarvisAI", which gives you easy functionality to build your own Virtual Assistant.    
# Content-    
    
1. What is JarvisAI?    
2. Prerequisite    
3. Architecture  
4. Getting Started- How to use it?    
5. What it can do (Features it supports)    
6. Future / Request Features    
7. Contribute    
8. Contact me    
9. Donate    
10. Thank me on-    
  
## YouTube Tutorial-  
  
Click on the image below to watch the tutorial on YouTube-  
  
**Tutorial 1-**  
  
[![JarvisAI Tutorial 1](https://img.youtube.com/vi/p2hdqB11S-8/0.jpg)](https://www.youtube.com/watch?v=p2hdqB11S-8)  
  
**Tutorial 2-**  
  
[![JarvisAI Tutorial 2](https://img.youtube.com/vi/6p8bhNGtVbA/0.jpg)](https://www.youtube.com/watch?v=6p8bhNGtVbA)  
  
  
    
## **1. What is Jarvis AI?**    
 Jarvis AI is a Python Module that is able to perform tasks like Chatbot, Assistant, etc. It provides base functionality for any assistant application. This JarvisAI is built using Tensorflow, Pytorch, Transformers, and other open-source libraries and frameworks. Well, you can contribute to this project to make it more powerful.    
  
* Official Website:  [Click Here](https://jarvisai.in)    
    
* Official Instagram Page:  [Click Here](https://www.instagram.com/_jarvisai_)    
    
    
## 2. Prerequisite    
 - Get your Free API key from  [https://jarvisai.in](https://jarvisai.in)    
        
- To use it only Python (> 3.6) is required.    
        
- To contribute to the project: Python is the only prerequisite for basic scripting, Machine Learning, and Deep Learning knowledge will help this model to do tasks like AI-ML. Read the How to Contribute section of this page.  
  
## 3. Architecture  
  
The JarvisAI’s architecture is divided into two parts.  
  
1. User End- It is basically responsible for getting input from the user and after preprocessing input it sends input to JarvisAI’s server. And once the server sends its response back, it produces output on the user screen/system.  
2. Server Side- The server is responsible to handle various kinds of AI-ML, and NLP tasks. It mainly identifies user intent by analyzing user input and interacting with other external APIs and handling user input.  
  
   ![JarvisAI’s Architecture](https://cdn-images-1.medium.com/max/800/1*_PK8b96tBgRHlmZecli-nA.jpeg)  
  
  
## 4. Getting Started- How to use it?    
    
#### NOTE: Old version is depreciated use latest version of JarvisAI

 ### 4.1. Installation-  
  
* Install the latest version-    
  
	```bash  
	pip install JarvisAI  
	```   

#### Optional Steps (Common Installation Issues)-  
  
* [Optional Step] If Pyaudio is not working or not installed you might need to install it separately-  
     
   In the case of Mac OSX do the following:  
     
	```  
	brew install portaudio  
	pip install pyaudio  
	```  
 
 In the case of Windows or Linux do the following:  
     
   - Download pyaudio from: lfd.uci.edu/~gohlke/pythonlibs/#pyaudio  
     
   - ```pip install PyAudio-0.2.11-cp310-cp310-win_amd64.whl```  
  
* [Optional Step] If pycountry is not working or not installed then Install "python3-pycountry" Package on Ubuntu/Linux-  
		 
	```  
	sudo apt-get update -y  
	sudo apt-get install -y python3-pycountry
	```  
 

* [Optional Step] You might need to Install [Microsoft Visual C++ Redistributable for Visual Studio 2022](https://visualstudio.microsoft.com/downloads/#microsoft-visual-c-redistributable-for-visual-studio-2022)  
  
### 4.2. Code You Need-  
   
   You need only this piece of code-
	
	
	def custom_function(*args, **kwargs):
        command = kwargs.get('query')
        entities = kwargs.get('entities')
        print(entities)
        # write your code here to do something with the command
        # perform some tasks # return is optional
        return command + ' Executed'


    jarvis = JarvisAI.Jarvis(input_mechanism='voice', output_mechanism='both',
                    google_speech_api_key=None, backend_tts_api='pyttsx3',
                    use_whisper_asr=False, display_logs=False,
                    api_key='527557f2-0b67-4500-8ca0-03766ade589a')
    # add_action("general", custom_function)  # OPTIONAL
    jarvis.start()
	
  
   
 ### 4.3. **What's now?**    
    
 It will start your AI, it will ask you to give input and accordingly it will produce output.      
   You can configure  `input_mechanism` and  `output_mechanism` parameter for voice input/output or text input/output.    
    
   ### 4.4. Let's understand the Parameters-    
     
  ```bash :param input_method: (object) method to get input from user <allowed values: [InputsMethods.text_input, InputsMethods.voice_input_google_api, InputsMethods.voice_input_deepspeech_streaming]> :param output_method: (object) method to give output to user <allowed values: [OutputMethods.text_output, OutputMethods.voice_output] :param backend_tts_api: (str) [Default 'pyttsx3'] backend tts api to use <allowed values: ['pyttsx3', 'gtts']> :param api_key: (str) [Default ''] api key to use JarvisAI get it from http://jarvis-ai-api.herokuapp.com :param detect_wake_word: (bool) [Default True] detect wake word or not <allowed values: [True, False]> :param wake_word_detection_method: (object) [Default None] method to detect wake word <allowed values: [InputsMethods.voice_input_google_api, InputsMethods.voice_input_deepspeech_streaming] :param bot_name: (str) [Default 'Jarvis'] name of the bot :param display_intent: (bool) [Default True] display intent or not <allowed values: [True, False]> :param google_speech_recognition_input_lang: (str) [Default 'en'] language of the input Check supported languages here: https://cloud.google.com/speech-to-text/docs/languages :param google_speech_recognition_key: (str) [Default None] api key to use Google Speech API :param google_speech_recognition_duration_listening: (int) [Default 5] duration of the listening    
 READ MORE: Google Speech API (Pricing and Key) at: https://cloud.google.com/speech-to-text  
```   
## 5. What it can do (Features it supports)-    
    
1. Currently, it supports only english language    
2. Supports voice and text input/output.    
3. Supports AI based voice input (using whisper asr) and by using google api voice input.    
4. All intellectual task is process in JarvisAI server so there is no load on your system.    
5. Lightweight and able to understand natural language (commands)    
6. Ability to add your own custom functions.    
    
### 5.1. Supported Commands-    

These are below supported intent that AI can handle, you can ask in natural language.

**Example- "What is the time now", "make me laugh", "click a photo", etc.**

**Note: Some features / command might not work. WIP. Tell me bugs.**

 1. asking time 
 2. asking date 
 3. greet and hello hi kind of things goodbye
 4. tell me joke
 5. tell me about 
 6. i am bored 
 7. volume control 
 8. tell me news
 9. click photo 
 10. places near me 
 11. play on youtube 
 12. play games 
 13. what can you do 
 14. send email 
 15. download youtube video 
 16. asking weather 
 17. take screenshot 
 18. open website 
 19. send whatsapp message 
 20. covid cases 
 21. check internet speed
 22. others  / Unknown Intent  (IN PROGRESS)

  
### 5.2. Supported Input/Output Methods (Which option do I need to choose?)-    

You can set below parameter while creating object of JarvisAI-

    jarvis = JarvisAI.Jarvis(input_mechanism='voice', output_mechanism='both',  
                    google_speech_api_key=None, backend_tts_api='pyttsx3',  
                    use_whisper_asr=False, display_logs=False,  
                    api_key='527557f2-0b67-4500-8ca0-03766ade589a')
    
1. **For text input-**'    
    
		input_mechanism='text'
       
2. **For voice input-**    
   
		input_mechanism='voice'
    
3. **For text output-**    
    
	    output_mechanism='text'
    
4. **For voice output-**    

	    output_mechanism='text'

5. **For voice and text output-**    

	    output_mechanism='both'
       
## 6. Future/Request Features-    
 **WIP**    
 **You tell me**    
    
 ## 7. Contribute-    
 **Instructions Coming Soon**    
 ## 8. Contact me-    
 - [Instagram](https://www.instagram.com/dipesh_pal17)    
        
- [YouTube](https://www.youtube.com/dipeshpal17)    
        
    
    
## 9. Donate-    
 [Donate and Contribute to run me this project, and buy a domain](https://www.buymeacoffee.com/dipeshpal)    
    
**_Feel free to use my code, don't forget to mention credit. All the contributors will get credits in this repo._**    
 **_Mention below line for credits-_**    
 ***Credits-***    
 - [https://jarvis-ai-api.herokuapp.com](https://jarvis-ai-api.herokuapp.com/)    
        
- [https://github.com/Dipeshpal/Jarvis_AI](https://github.com/Dipeshpal/Jarvis_AI)    
        
- [https://www.youtube.com/dipeshpal17](https://www.youtube.com/dipeshpal17)    
        
- [https://www.instagram.com/dipesh_pal17](https://www.instagram.com/dipesh_pal17/)    
        
    
## 10. Thank me on-    
 - Follow me on Instagram:  [https://www.instagram.com/dipesh_pal17](https://www.instagram.com/dipesh_pal17/)    
        
- Subscribe me on YouTube:  [https://www.youtube.com/dipeshpal17](https://www.youtube.com/dipeshpal17)    
    
## License    
 [MIT](https://choosealicense.com/licenses/mit/)
