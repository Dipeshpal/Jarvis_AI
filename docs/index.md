
# AdonisAI  
  
Official Website: [Click Here](https://adonis-ai.herokuapp.com) 

Official Instagram Page: [Click Here](https://www.instagram.com/_jarvisai_)
  
![enter image description here](https://source.unsplash.com/1600x900/?robots)  
  
1. What is AdonisAI?  
2. Prerequisite  
3. Getting Started- How to use it?  
4. What it can do (Features it supports)  
5. Future / Request Features  
6. What's new?   
7. Contribute  
8. Contact me  
9. Donate  
10. Thank me on-  
  
  
## 1. What is AdonisAI?  
  
AdonisAI is as advance version of [JarvisAI](https://pypi.org/project/JarvisAI/). AdonisAI is a Python Module which is able to perform task like Chatbot, Assistant etc. It provides base functionality for any assistant application. This library is built using Tensorflow, Pytorch, Transformers and other opensource libraries and frameworks. Well, you can contribute on this project to make it more powerful.  
  
This project is crated only for those who is having interest in building Virtual Assistant. Generally it took lots of time to write code from scratch to build Virtual Assistant. So, I have build an Library called "Adonis", which gives you easy functionality to build your own Virtual Assistant.  
  
**AdonisAI is more powerful and light weight version of https://pypi.org/project/JarvisAI/**  
  
## 2.  Prerequisite  
  
- Get your Free API key from https://adonis-ai.herokuapp.com  
  
- To use it only Python (> 3.6) is required.  
  
- To contribute in project: Python is the only prerequisite for basic scripting, Machine Learning and Deep Learning knowledge will help this model to do task like AI-ML. Read How to contribute section of this page.  
  
## 3.  Getting Started- How to use it?  
  
- Install the latest version-  
  
    `pip install AdonisAI`  
  
  It will install all the required package automatically.  
  
  - You need only this piece of code-  
      ```  
     # create your own function       # RULES (Optional)-  
     # It must contain parameter 'feature_command' (What ever input you provide when AI ask for input will be passed to this function) 
     # Return is optional
      # If you want to provide return value it should only return text (str)       
	
    def pprint(feature_command="custom feature (What ever input you provide when AI ask for input will be passed to this function)"):    
          # write your code here to do something with the command    
          # perform some tasks   
          # return is optional    
          return feature_command + ' Executed'    
       
      obj = AdonisEngine(bot_name='alexa',    
                         input_mechanism=InputOutput.speech_to_text_deepspeech_streaming,    
                         output_mechanism=[InputOutput.text_output, InputOutput.text_to_speech],    
                         backend_tts_api='pyttsx3',    
                         wake_word_detection_status=True,    
                         wake_word_detection_mechanism=InputOutput.speech_to_text_deepspeech_streaming,    
                         shutdown_command='shutdown',  
                         secret_key='your_secret_key')   
                           
      # Check existing list of commands, Existing command you can not use while registering your function  
     print(obj.check_registered_command())     
     
      # Register your function (Optional)  
     obj.register_feature(feature_obj=pprint, feature_command='custom feature')     
     
      # Start AI in background. It will always run forever until you don't stop it manually.  
     obj.engine_start() 
     ```  
  **Whats now?**  
  
  It will start your AI, it will ask you to give input and accordingly it will produce output.  
      You can configure `input_mechanism` and `output_mechanism` parameter for voice input/output or text input/output.  
  
     ### Parameters-  
- 
  ![enter image description here](https://i.imgur.com/rliCjBE.png)  
    
    
# 4.  What it can do (Features it supports)-  
  
1. Currently, it supports only english language  
2. Supports voice and text input/output.  
3. Supports AI based voice input and by using google api voice input.  
  
  
 ### 4.1. Supported Commands-  
 ![enter image description here](https://i.postimg.cc/9M66tfwP/raycast-untitled-9.png)   

 ### 4.3. Supported Input/Output Methods (Which option do I need to choose?)-  
   
 ![enter image description here](https://i.ibb.co/sCDWW7K/raycast-untitled-5.png)  
  
# 5. Future/Request Features-  
  
**WIP**  
  
**You tell me**  
  
# 6. What new-  
  
1. AdonisAI==1.0: Initial Release.  
  
2. AdonisAI==1.1: Added news and weather features. Added AdonisAI.InputOutput.wake_word_detection_mechanism.  
  
3. AdonisAI==1.2: Added new input mechanism (AdonisAI.InputOutput.speech_to_text_deepspeech_streaming) fast and free. And new features (jokes, about).  
  
4. AdonisAI==1.3: Added New feature (send whatsapp, open website, play on youtube, send email).  
  
5. AdonisAI==1.4: Added new feature (AI Based Chatbot Added, from now you need Secret key for AdonisAI, it's used for security purpose. Get your free key from https://adonis-ai.herokuapp.com).  
  
6. AdonisAI==1.5: Major Bug Fix from version 1.4. *[DO NOT USE AdonisAI==1.4]*  
  
7. AdonisAI==1.6: New features added (screenshot, photo click, youtube video download, play games, covid updates, internet speed check)

8. AdonisAI==1.7: Bug Fixes from version 1.6. *[DO NOT USE AdonisAI==1.6]*
  
# 7. Contribute-  
  
Instructions Coming Soon  
  
# 8. Contact me-  
  
- [Instagram](https://www.instagram.com/dipesh_pal17)

- [YouTube](https://www.youtube.com/dipeshpal17)
  
  
# 9. Donate-  
  
[Donate and Contribute to run me this project, and buy a domain](https://www.buymeacoffee.com/dipeshpal)
  
**_Feel free to use my code, don't forget to mention credit. All the contributors will get credits in this repo._**  
  
**_Mention below line for credits-_**   
  
Credits-  
  
- https://jarvis-ai-api.herokuapp.com/  
  
- https://github.com/Dipeshpal/Jarvis_AI/  
  
- https://www.youtube.com/dipeshpal17  
  
- https://www.instagram.com/dipesh_pal17/  
  
  
# 10. Thank me on-  
  
- Follow me on Instagram: https://www.instagram.com/dipesh_pal17/  
  
- Subscribe me on YouTube: https://www.youtube.com/dipeshpal17
