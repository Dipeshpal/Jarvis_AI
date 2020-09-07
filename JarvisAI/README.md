# JarvisAI

***Last Upadted: 02 September, 2020***

 1. What is Jarvis Ai?
 2. Prerequisite
 3. Getting Started- How to use it?
 4. How to contribute?
 5. Future?
 
## 1. What is Jarvis AI-
Jarvis AI is a Python Module which is able to perform task like Chatbot, Assistant etc. It provides base functionality for any assistant application. Well, you can contribute on this project to make it more powerful.

Check more details here- https://github.com/Dipeshpal/Jarvis_AI

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
```
import JarvisAI
obj = JarvisAI.JarvisAssistant()
response = obj.mic_input()
print(response)
```


#### Commands and features-

The functionality is cleared by methods name.  You can check the code for example.

1. mic_input
2. text2speech
3. shutdown
4. website_opener
5. send_mail
6. tell_me_date
7. tell_me_time
8. launch_any_app
9. weather
10. news 
11. tell_me


## 4. How to contribute?

 1. Clone this [reop](https://github.com/Dipeshpal/Jarvis_AI)
 2. Create virtual environment in python.
 3. Install requirements from [requirements.txt](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/requirements.txt).
	 `pip install requirements.txt`
4. Now run, [__ init__.py](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/__init__.py)
	`python __init__.py` and understand the working.

	***Guidelines to add your own scripts / modules-***
	Lets understand the projects structure first-

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

Lots of possibilities, GUI, Integrate with GPT-3, support for android, IOT, Home Automation, APIs, as pip package etc.


## FAQs for Contributers-
1. What I can install?
Ans: You can install any library you want in your module, make sure it is opensource and compatible with win/linux/mac.

2. Code format?
Ans: Read the example above. And make sure your code is compatible with win/linux/mac.

3. What should I not change?
Ans: Existing code.

4.  Credits-
Ans: You will definetly get credit for your contribution.

5. Note-
Ans: Once you created your module, test it with different environment (windows / linux). Make sure the quality of code because your features will get added to the JarvisAI and publish as PyPi project.

6. Help / Contact?
Ans. Contact me on any of my social media or Email.

### **Let's make it big.**

***Feel free to use my code, don't forget to metion credit.
All the contributers will get credits in this repo.***