# JarvisAI

***Last Updated: 31 May, 2021***

 1. What is Jarvis AI?
 2. Prerequisites
 3. Getting Started- How to use it?
 4. How to contribute?
 5. Future?
 
## 1. What is Jarvis AI-
Jarvis AI is a Python Module which is able to perform task like Chatbot, Assistant etc. It provides base functionality for any assistant application. This JarvisAI is built using Tensorflow, Pytorch, Transformers and other open source libraries and frameworks. Well, you can contribute on this project to make it more powerful.

This project is created only for those who is having interest in building Virtual Assistant. Generally, it takes a lot of time to write code from scratch to build Virtual Assistants. So, I have build an Library called "JarvisAI", which gives you easy functionality to build your own Virtual Assistant.

**Check more details here:** https://github.com/Dipeshpal/Jarvis_AI

**Check official website here:** https://jarvis-ai-api.herokuapp.com/

**API Documentation:** https://jarvis-ai-api.herokuapp.com/api_docs/

## 2. Prerequisites-

* To use this project only Python Version > 3.6 is required.
* To contribute in project: Python is the only prerequisite for basic scripting, Machine Learning and Deep Learning knowledge will help this model to do task like AI-ML. Read How to contribute section of this page.

## 3. Getting Started (How to use it)-
 
 ### Install the latest version-
 `pip install JarvisAI`

 It will install all the required package automatically.
 
 *If anything not install then you can install requirements manually.* 
 
 `pip install -r requirements.txt`
 
 The `requirements.txt` can be found [here](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/requirements.txt).
 
 https://pypi.org/project/JarvisAI/
 

### Usage and Features-

After installing the library you can import the module-

Example-

1. Basic Usage: 
   
   https://github.com/Dipeshpal/Jarvis-Assisant/blob/master/scripts/main.py

2. Advance Usage (Wake up using Hand Gestures): 
   
   https://github.com/Dipeshpal/Jarvis-Assisant/blob/master/scripts/main_advance_usages.py
	
```
import JarvisAI
obj = JarvisAI.JarvisAssistant(sync=True, token='5ec64be7ff718ac25917c198f3d7a4')  
response = obj.mic_input_ai() 
print(response)
```
OR
```
import JarvisAI
obj = JarvisAI.JarvisAssistant(sync=False) 
response = mic_input() 
print(response)
```

**Check this script for more examples-**
https://github.com/Dipeshpal/Jarvis-Assisant/blob/master/scripts/main.py

#### Available Methods-

The functionality is cleared by method names. For example, you can check the code. These are the names of available methods you can use after creating JarvisAI's object-

```
import JarvisAI
obj = JarvisAI.JarvisAssistant(sync=True, token='5ec64be7ff718ac25917c198f3d7a4') 
response = obj.mic_input_ai()
```
OR
```
import JarvisAI
obj = JarvisAI.JarvisAssistant(sync=False) 
response = mic_input() 
```

**_Note:_** _First of all setup initial settings of the project by calling setup function._

```
res = obj.setup()
```

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
23. obj.get_user_data()
24. obj.jarvisai_configure_hand_detector(camera=0, detectionCon=0.7, maxHands=2, cam_display=True, cam_height=480,
                                         cam_width=888)
	
25. jarvisai_detect_hands(self, message="")

## 4. How to contribute?

 1. Clone this [repository](https://github.com/Dipeshpal/Jarvis_AI)
 2. Create virtual environment in python.
 3. Install requirements from [requirements.txt](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/requirements.txt) using
	 `pip install requirements.txt`
4. Now, run [__ init__.py](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/__init__.py)
	using `python __init__.py` and try to understand the working.

	***Guidelines to add to your own scripts / modules-***
	Lets understand the project structure first-

	```
	JarvisAI:.
	├───configs
	├───features
	│   ├─── date_time
	│   │   └───...
	│   └───weather
	│       └───...
	└───...
	```
	4.1. **All these above things are folders. Lets understand-**
	
	 - **JarvisAI:** 	Root folder containing all the files
	
	 - **features:** All the features supported by JarvisAI. This 'features' folder contains the different modules, you can create your own modules. Example of modules- "[weather](https://github.com/Dipeshpal/Jarvis_AI/tree/master/JarvisAI/JarvisAI/features/weather)", "[setup](https://github.com/Dipeshpal/Jarvis_AI/tree/master/JarvisAI/JarvisAI/features/setup)". These are the two folders inside '[features](https://github.com/Dipeshpal/Jarvis_AI/tree/master/JarvisAI/JarvisAI/features)' directory.
	
	 - **[__ init__.py](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/__init__.py):** You need to run this file to test it during the production.
	
	4.2. **You can create your own modules in this 'features' directory.**
	
	4.3. **Let's create a module and you can learn by example-**
	
	- **4.3.1. We will create a module which will tell us a date and time.**
	
	- **4.3.2. Create a folder (module) name- 'date_time' in features directory.**
	
	- **4.3.3. Create a python script name- 'date_time.py' in 'date_time' folder.**
	
	- **4.3.4. Write this kind of script (you can modify according to your own script).**  ***Read comments in script below to understand format***- 

		`'features/date_time/date_time.py' file-`
		***Make sure to add docs / comments. Also return value if necessary.***
		
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
			try:  
		        time = datetime.datetime.now().strftime("%H:%M")  
		    except Exception as e:  
		        print(e)  
		        time = False  
			 return time


		# you can run and test your script by calling from main
		if __name__ == '__main__':
		    response = date()
		    print(response)
		    response = time()
		    print(response)

	- **4.3.4. Integrate your module to Jarvis AI-**
		- Open `JarvisAI\JarvisAI\__init__.py`
	
		 - Format of this py file-
			```
			# import custom features
			try:
				import features.date_time.date_time
			except:
				from .features.date_time import date_time
			
			# integrate your features
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

There are lots of possibilities like GUI, Integrate with GPT-3, support for android, IOT, Home Automation, APIs, as pip package etc.

### Todo list-

5.1. More API features

5.2. You can tell me


## FAQs for Contributors-
1. What can I install?

   Ans: You can install any library you want in your module, make sure it is opensource and compatible with win/linux/mac.

2. What is the code format?

   Ans: Read the example above. And make sure your code is compatible with win/linux/mac.

3. What should I not change?

   Ans: Existing code.

4. Would I get credits?
  
   Ans: You will definitely get credit for your contribution.

5. **Important Note**-

   Once you created your module, test it with different environment (windows / linux). Make sure the quality of code because your features will get added to the JarvisAI and publish as PyPi project.

6. Help / Contact?

   Ans. Contact me on any of my social media or Email.

### **Let's make it big.**

***Feel free to use my code, don't forget to mention credit.
All the contributors will get credits in this repository.***
