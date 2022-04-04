
  
# JarvisAI    
 ***Last Updated: 05 Apr, 2022***   
 
# NOTE

This is the final update (05 Apr, 2022) on this libray. You can still use this library. We have introduce new library [AdonisAI](https://pypi.org/project/AdonisAI)

AdonisAI is as advance version of JarvisAI which is lightweight but more powerful. AdonisAI is a Python Module which is able to perform task like Chatbot, Assistant etc. It provides base functionality for any assistant application. This library is built using Tensorflow, Pytorch, Transformers and other opensource libraries and frameworks. Well, you can contribute on this project to make it more powerful.
    
1. What is Jarvis AI?    
 2. Prerequisite    
 3. Getting Started- How to use it?    
 4. How to contribute?    
 5. Future?    

## Check Out Lightweight (More Powerful) Version  of JarvisAI-

AdonisAI: https://pypi.org/project/AdonisAI

     
## 1. What is Jarvis AI-
Jarvis AI is a Python Module which is able to perform task like Chatbot, Assistant etc. It provides base functionality for any assistant application. This JarvisAI is built using Tensorflow, Pytorch, Transformers and other opensource libraries and frameworks. Well, you can contribute on this project to make it more powerful.    
    
This project is crated only for those who is having interest in building Virtual Assistant. Generally it took lots of time to write code from scratch to build Virtual Assistant. So, I have build an Library called "JarvisAI", which gives you easy functionality to build your own Virtual Assistant.    
    
**Check more details here:** https://github.com/Dipeshpal/Jarvis_AI    
    
**Check official website here:** https://jarvis-ai-api.herokuapp.com/    
    
**API Documentations:** https://jarvis-ai-api.herokuapp.com/api_docs/    
    
## 2. Prerequisite-    
 * To use it only Python (> 3.6) is required.    
* To contribute in project: Python is the only prerequisite for basic scripting, Machine Learning and Deep Learning knowledge will help this model to do task like AI-ML. Read How to contribute section of this page.    
    
## 3. Getting Started (How to use it)-    
  ### Install the latest version-    
 `pip install JarvisAI`    
    
 It will install all the required package automatically.    
     
 *If anything not install then you can install requirements manually.*     
 `pip install -r requirements.txt`    
 The [requirementx.txt](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/requirements.txt) can be found [here](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/requirements.txt).    
     
 https://pypi.org/project/JarvisAI/    
     
    
### Usage and Features-    
 After installing the library you can import the module-    
    
Example-    
    
1. Basic Usages: https://github.com/Dipeshpal/Jarvis-Assisant/blob/master/scripts/main.py    
    
2. Advance Usages (Wake up using Hand Gesture): https://github.com/Dipeshpal/Jarvis-Assisant/blob/master/scripts/main_advance_usages.py    
       
``` 
import JarvisAI 

obj = JarvisAI.JarvisAssistant(sync=True, token='5ec64be7ff718ac25917c198f3d7a4', disable_msg=False, load_chatbot_model=True, high_accuracy_chatbot_model=False,    
chatbot_large=False)  # or JarvisAI.JarvisAssistant(sync=False) 

response = obj.mic_input_ai() # or mic_input() can be also used print(response) ```    
```

**Check this script for more examples-** https://github.com/Dipeshpal/Jarvis-Assisant/blob/master/scripts/main.py    
    
#### Available Methods-    
 The functionality is cleared by methods name.  You can check the code for example. These are the names of available functions you can use after creating JarvisAI's object-    
    
``` 
import JarvisAI 

obj = JarvisAI.JarvisAssistant(sync=True, token='5ec64be7ff718ac25917c198f3d7a4', disable_msg=False, load_chatbot_model=True, high_accuracy_chatbot_model=False,    
chatbot_large=False) # or JarvisAI.JarvisAssistant(sync=False) response = 

obj.mic_input_ai()  # mic_input() can be also used ```    
```

 **Available Parameters-**    
 1. sync (bool): It is used to sync your JarvisAI setting with server. We don't use this information for any purpose, it's just for better user experience. If you enable this you need to add your token also. You can get your token from JarvisAI's official website.     
 2. Token (str): It is the token which you can obtain from the JarvisAI's official website. This features help to sync your setting each time run the assistant.    
 3. disable_msg (bool): It enables/disable the JarvisAI's initialization message.    
 4. load_chatbot_model (bool): If you want to use our AI based ChatBot model then you need to enable this. Without enabling this you can't use 'chatbot_base' or 'chatbot_large' functions. Disable this if you don't want to use JarvisAI's chatbot feature.    
 5. high_accuracy_chatbot_model (bool): All the AI's models will use some amount of bandwidth while downloading the models from Transformers Hub. Higher accuracy model will give you high accuracy, and size of these model is also high which required lot's or memory (RAM) while loading for the inference. If you have low memory system or less internet data then set this option to False. If it is false, it will load small model, which is around 1GB - 2GB and it has pretty much good accuracy.    
 6. chatbot_large (bool): If it is True it means, In case chatbot can't answer, or it recognizes the intent of your query is different from normal conversation then it will use Wikipedia/Internet to resolve your query, and it will analyze (summarize) extracted data from internet before response. You can use 'chatbot_large' with 'high_accuracy_chatbot_model=False' for better experience and lower RAM (internet data). Well, 'chatbot_large=False' only answer you queries based on it's AI model knowledge base, it doesn't use Wikipedia/Internet.       
 7. backend_tts_api (str): Male Voice Added (if your system support pyttsx3 module and your system have multiple voices inbuilt)
	
    You can try different voices. This is one time setup. You can reset your voice by deleting 'configs/JarvisAI-Voice.txt' file in your working directory. This file will be created during first run of the program only if you are using pyttsx3.
 
    *Usages-*

    ```
    import JarvisAI
    # backend_tts_api='pyttsx3' for different voices options
     # backend_tts_api='gtts' for female voice by google text to speech library
    obj = JarvisAI.JarvisAssistant(sync=True, token='5ec64be7ff718ac25917c198f3d7a4', disable_msg=False,
                               load_chatbot_model=False, high_accuracy_chatbot_model=False,
                               chatbot_large=False, backend_tts_api='pyttsx3')
     ```
    
     What is 'configs/JarvisAI-Voice.txt' file contains?
    - Voice information in plain text (do not modify this file manually)
    
**_Note:_** _First of all setup initial settings of the project by calling setup function._    
 
 ``` res = obj.setup() ```    
 
 1. res = obj.mic_input(lang='en')    
2. res = obj.mic_input_ai(record_seconds=5, debug=False)    
3. res = obj.website_opener("facebook")    
4. res = obj.send_mail(sender_email=None, sender_password=None, receiver_email=None, msg="Hello")    
5. res = obj.launch_app("edge")    
6. res = obj.weather(city='Mumbai')    
7. res = obj.news()    
8. res = obj.tell_me(topic='tell me about Taj Mahal')    
9. res = obj.tell_me_time()    
10. res = obj.tell_me_date()    
11. res = obj.shutdown()    
12. res = obj.text2speech(text='Hello, how are you?', lang='en')    
13. res = obj.datasetcreate(dataset_path='datasets', class_name='Demo',    
                      haarcascade_path='haarcascade/haarcascade_frontalface_default.xml',    
                      eyecascade_path='haarcascade/haarcascade_eye.xml', eye_detect=False,    
                      save_face_only=True, no_of_samples=100,    
                      width=128, height=128, color_mode=False)    
14. res = obj.face_recognition_train(data_dir='datasets', batch_size=32, img_height=128, img_width=128, epochs=10,    
                               model_path='model', pretrained=None, base_model_trainable=False)    
15. res = obj.predict_faces(class_name=None, img_height=128, img_width=128,    
                      haarcascade_path='haarcascade/haarcascade_frontalface_default.xml',    
                      eyecascade_path='haarcascade/haarcascade_eye.xml', model_path='model',    
                      color_mode=False)    
16. res = obj.setup()    
17. res = obj.show_me_my_images()    
18. res= obj.show_google_photos()    
19. res = obj.tell_me_joke(language='en', category='neutral')    
20. res = obj.hot_word_detect(lang='en')    
21. status, response = obj.get_user_data(token="436c57eab581dbb2253cfa77c41574f6")  # get your token from https://jarvis-ai-api.herokuapp.com/    
22. obj.set_user_data()    
23. obj.jarvisai_configure_hand_detector(camera=0, detectionCon=0.7, maxHands=2, cam_display=True, cam_height=480,    
                                         cam_width=888)    
       
24. obj.jarvisai_detect_hands(self, message="")    
25. obj.chatbot_base(input_text='how are you')   # You must set obj=JarvisAI.JarvisAssistant(load_chatbot_model=True)  
26. obj.chatbot_large(input_text='how are you')  # You must set obj=JarvisAI.JarvisAssistant(load_chatbot_model=True)  
27. obj.create_new_list('add milk in my shopping list')
28.	obj.delete_particular_list('delete my shopping list')
29. obj.show_me_my_list()
30. obj.show_me_some_tech_news()  # It will show tech news in your browser
31. obj.show_me_some_tech_videos() # It will show tech videos in your browser
32.	obj = JarvisAI.JarvisAssistant(sync=True, token='5ec64be7ff718ac25917c198f3d7a4', disable_msg=False,
                               load_chatbot_model=False, high_accuracy_chatbot_model=False,
                               chatbot_large=False, backend_tts_api='pyttsx3') # you must set backend_tts_api='pyttsx3' for different voices options (Read 'What's new' of '20 Dec, 2021' update section of this page for more details.)
     	
    ------

## 4. How to contribute?    
    
1. Clone this [reop](https://github.com/Dipeshpal/Jarvis_AI)    
 2. Create virtual environment in python.    
 3. Install requirements from [requirements.txt](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/requirements.txt).    
    `pip install requirements.txt` 4. Now run, [__ init__.py](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/__init__.py)    
   `python __init__.py` and understand the working.    
    
   ***Guidelines to add your own scripts / modules-***    
 Lets understand the projects structure first-    
    
  
 ![enter image description here](https://i.ibb.co/kX1DM1j/Screenshot-2021-10-17-220210.png) 
  
- **JarvisAI:** Root folder containing all the files    

- **features:** All the features supported by JarvisAI. This 'features' folder contains the different modules, you can create your own modules. Example of modules- "[weather](https://github.com/Dipeshpal/Jarvis_AI/tree/master/JarvisAI/JarvisAI/features/weather)", "[setup](https://github.com/Dipeshpal/Jarvis_AI/tree/master/JarvisAI/JarvisAI/features/setup)". These are the two folders inside '[features](https://github.com/Dipeshpal/Jarvis_AI/tree/master/JarvisAI/JarvisAI/features)' directory.    

- **[__ init__.py](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/__init__.py):** You can code here and add call your functions from here. User will be able to directly access functions listed in this file.   
   
  
 4.2. **You can create your own modules in this 'features' directory. Call you function in __init__ file.**    
 
 4.3. **Let's create a module and you can learn by example-**    

 - **4.3.1. We will create a module which will tell us a date and time.**    

 - **4.3.2. Create a folder (module) name- 'date_time' in features directory.**    

 - **4.3.3. Create a python script name- 'date_time.py' in 'date_time' folder.**    

 - **4.3.4. Write this kind of script (you can modify according to your own script).**  ***Read comments in script below to understand format***-     
	    
	 `'features/date_time/date_time.py' file-` ***Make sure to add docs / comments. Also return value if necessary.***    
	  ```    
	 import datetime      
	      def date():      
	          """      
	          Just return date as string  :return: date if success, False if fail      
	          """      
	          try:      
	              date = datetime.datetime.now().strftime("%b %d %Y")      
	          except Exception as e:      
	              print(e)      
	              date = False      
	         return date      
	            
	            
	      def time():      
	          """      
	         Just return date as string  :return: time if success, False if fail      
	         """    
	 try:              time = datetime.datetime.now().strftime("%H:%M")      
	          except Exception as e:      
	              print(e)      
	              time = False      
	          return time    
	  ```  
	  *** you can run and test your script by calling from main-***  
	    
	  

	     if __name__ == '__main__': 
	    	 response = date() 
	    	 print(response) 
	    	 response = time() 
	    	 print(response)   

	  
  - **4.3.4. Integrate your module to Jarvis AI-**    

	- Open `JarvisAI\JarvisAI\__init__.py`    

	- Format of this py file-    

	       # import custom features 
	       try: 
		       import features.date_time.date_time
		   except: 
			   from JarvisAI.features.date_time import date_time  # integrate your features    
	       
	       class JarvisAssistant:
		       def __init__(self):      
		           pass   
		            
		       def tell_me_date(self):
			       return date_time.date()      
	                           
	           def tell_me_time(self):
		           return date_time.time()    
	       
	       # test your features from main    
	       if __name__ == '__main__':         
	           obj = JarvisAssistant()           
			    res = obj.tell_me_time()      
	            print(res)    
		        res = obj.tell_me_date()  
		        print(res)  


4.4. That's it, if you applied all the things as per as guidelines then now just run __ init__.py it should works fine.    
    
4.5. Push the repo, we will test it. If found working and good then it will be added to next PyPi version.    
    
Next time you can import your created function from JarvisAI    
Example: `import JarvisAI.tell_me_date`    
   
## 5. Future?    
 Lots of possibilities, GUI, Integrate with GPT-3, support for android, IOT, Home Automation, APIs, as pip package etc.    
    
### Todo list-    
 5.1. More API features    
    
5.2. You tell me    
    
    
## FAQs for Contributors-
 1. What I can install?    
Ans: You can install any library you want in your module, make sure it is opensource and compatible with win/linux/mac.    
    
2. Code format?    
Ans: Read the example above. And make sure your code is compatible with win/linux/mac.    
    
3. What should I not change?    
Ans: Existing code.    
    
4. Credits-    
Ans: You will definitely get credit for your contribution.    
    
5. Note-    
Ans: Once you created your module, test it with different environment (windows / linux). Make sure the quality of code because your features will get added to the JarvisAI and publish as PyPi project.    
    
6. Help / Contact?    
Ans. Contact me on any of my social media or Email.    
    
### **Let's make it big.**    
   
**What's new?-**    

 1. **05 Apr, 2022-**

	This is the final update on this libray. You can still use this library. We have introduce new library [AdonisAI](https://pypi.org/project/AdonisAI)
	
	AdonisAI is as advance version of JarvisAI which is lightweight but more powerful. AdonisAI is a Python Module which is able to perform task like Chatbot, Assistant etc. It provides base functionality for any assistant application. This library is built using Tensorflow, Pytorch, Transformers and other opensource libraries and frameworks. Well, you can contribute on this project to make it more powerful.
	
	In this last update we mostly update the documentation.

 2. **20 Dec, 2021-**

	Male Voice Added (if your system support pyttsx3 module and your system have multiple voices inbuilt)
	
    You can try different voices. This is one time setup. You can reset your voice by deleting 'configs/JarvisAI-Voice.txt' file in your working directory. This file will be created during first run of the program only if you are using pyttsx3.
 
    *Usages-*

    ```
    import JarvisAI
    # backend_tts_api='pyttsx3' for different voices options
     # backend_tts_api='gtts' for female voice by google text to speech library
    obj = JarvisAI.JarvisAssistant(sync=True, token='5ec64be7ff718ac25917c198f3d7a4', disable_msg=False,
                               load_chatbot_model=False, high_accuracy_chatbot_model=False,
                               chatbot_large=False, backend_tts_api='pyttsx3')
     ```
    
     What is 'configs/JarvisAI-Voice.txt' file contains?
    - Voice information in plain text (do not modify this file manually)

    
 3. **22 Nov, 2021-**
	
    * Now you can add and delete items in list.
	
        Example: you can say- "add milk in my shopping list".
		
        It will create list name with "Shopping", and you can delete or show this list with following options-
        It uses deep learning models to identify list name and list items, so there might be some inaccuracy in results. 
	
            obj.create_new_list('add milk in my shopping list')
            obj.delete_particular_list('delete my shopping list')
            obj.show_me_my_list()
	
    * Show tech news and Videos-
          ```
          obj.show_me_some_tech_news()  # It will show tech news in your browser
		
         obj.show_me_some_tech_videos() # It will show tech videos in your browser
        ```
	 
 4. **24 Oct, 2021-**
	
    New features added, features number 27, 28 and 29.
 
 5. **17 Oct, 2021-**  
        - Bug Fixes
        - Docs Update

 6. **19 Sep, 2021-**  
     
       Chatbot features added. Two new methods added (25, 26 check 'Usage and Features').   
       It used Transformers based AI models to response users general queries.   
	     
       Below answers depends on the type of chatbot you choose and type of accuracy you have choosen.  
     
   - Example (chatbot_small) [Directly answered from chatbot model's knowledge base]-  
        
         user >> How are you?
	 	AI >> I am good, how are you?  

 - Example (chatbot_large) [Fetched data from internet and answered it after analyzing the gathered data]-  

		user >> Who is president of India?  
		AI >> Ram Nath Kovind  

 - Example (chatbot_large) [Fetched some of the URL from Internet]-

	     user >> who is the captain of team India? 
	     AI >> URL1, URL2, URL3  

 7. **Before 19 Sep, 2021-**  
     
   Features 1-25 added. Check 'Usage and Features'  
  
  
  
***Feel free to use my code, don't forget to mention credit.    
All the contributors will get credits in this repo.***
