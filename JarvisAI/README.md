# JarvisAI

***Last Upadted: 01 September, 2020***

 1. What is Jarvis Ai?
 2. Prerequisite
 3. Getting Started- How to use it?
 4. How to contribute?
 5. Future?
 
## 1. What is Jarvis AI-
Jarvis AI is a Python Module which is able to perform task like Chatbot, Assistant etc. Currently it is in development stage. Currently only support CLI method, no UI yet. Well, you can contribute on this project to make it more powerful.

Check more details here- https://github.com/Dipeshpal/Jarvis_AI

## 2. Prerequisite-
To use it only Python (> 3.6) is required.
To contribute in project: Python is the only prerequisite for basic scripting, Machine Learning and Deep Learning knowledge will help this model to do task like AI-ML.

## 3. Getting Started (How to use it)-
 
 ### Jus run this on terminal-
 `pip install JarvisAI`
 https://pypi.org/project/JarvisAI/
 This will install the latest version available.
 
### Usage and Features-
**The input you can enter to perform different task-**

1. **Setup Jarvis Ai-**
	Setup basic details about user which [Jarvis](https://github.com/Dipeshpal/Jarvis_AI) will use to provide results to user.
	- *Example:* Setup / Set up / Let's Setup etc.

2. **Ask weather-**
		We are using NLP here to understand human inputs. So there may be lots of possibilities to say one command.
	 - *Example:* What is the weather? / What is temerature? What is temperature in `your city`? etc.

3. **Ask time and date-**
	- *Example:* tell me time, tell me date/
		 
	**Working on new features like chatbot, notes, reminder, perform task, show photos from PC etc**


## 4. How to contribute?

1. Clone this [reop](https://github.com/Dipeshpal/Jarvis_AI)
 2. Create virtual environment in python.
 3. Install requirements from [requirements.txt](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/requirements.txt).
	 `pip install requirements.txt`
4. Now run, [__init__.py](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/__init__.py)
	`python __init__.py`
	(Currently only support input as text, working on input from mic. Mic is in beta stage, sometimes not works)
-  So, once you run the [__init__.py](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/__init__.py) it will ask you to enter text.  
- It will produce output as text and audio accordingly.
- You no need to run script again and again, it will keep asking you to enter next queries. If you want to stop, just close the script.


 - You can clone the repo and understand how this works.
 - You can add your own features / scripts. Follow this guideline while writing scripts-

	***Guidelines to add your own scripts / modules-***
	Lets understand the projects structure first-

	```
	JarvisAI:.
	├───configs
	├───features
	│   ├───setup
	│   │   └───...
	│   └───weather
	│       └───...
	└───...
	```
	4.1. **All these above things are folders. Lets understand-**
	
	
	 - **JarvisAI:** 	Root folder containing all the files
	 - **configs:** It contain .py files, just a configuration files. Which may need by any script. We will talk about it later.
	 - **features:** All the features supported by JarvisAI. This 'features' folder contains the different modules, you can create your own modules. Example of modules- "weather", "setup". These are the two folders inside 'features' directory.
	 - **action.py:** Perform action according to input. It call exact module / function according to user input. If user input matches in `jarvis_features_config.py` file then it call respected function.
	 - **jarvis.py:** Main file to get input from user, call action file and perform action accordingly then show output to user.
	
	4.2. **You can create your own modules in this 'features' directory.**
	
	4.3. **Let's create a module and you can learn by example-**
	
	- **4.3.1. We will create a module which will tell us a date and time.**
	
	- **4.3.2. Create a folder (module) name- 'date_time' in features directory.**
	
	- **4.3.3. Create a python script name- 'jarvis_date_time'**
	
	- **4.3.4. Write this kind of script (you can modify according to your own script).** ***Read comments in script below to understand format***- 

		```
		# import statements  
		import datetime  
		  
		  
		# do not remove inp=None the function format should be same, name can be change  
		# inp is the input from the user (query ask by user)  
		# you can use this inp inside the function. LOL, because you may need user input  
		# Function should return something because this is the output we want to show user  
		
		def tell_me_date(inp=None):  
		    # inp (do something if you want to do with inp)  
		  date = datetime.datetime.now().strftime("%b %d %Y")  
		  
		    # the return format should be string or integer only
		  return date  
		  
		  
		def tell_me_time(inp=None):  
		    time = datetime.datetime.now().strftime("%H:%M")  
		    return time  
		  
		  
		# you can run and test your script by calling from main  
		if __name__ == '__main__':  
		    response = tell_me_date()  
		    print(response)  
		    response = tell_me_time()  
		    print(response)


	- **4.3.4. Integrate your module to Jarvis AI-**
		- Remember? We have configs folder.
		   We have 'JarvisAI\configs\jarvis_features_config.py' this python file. It contains data releated to run modules.
		 - Format of this Json file-
			```
			jarvis_features_config = [  
				{  
				  "regex": "weather|temperature|wind|clouds|rainy",  
				  "import": "JarvisAI.features.weather.weather",  
				  "function_name": "weather_app"  
				},  
				{  
				  "regex": "setup|set up",  
				  "import": "JarvisAI.features.setup.user_setup",  
				  "function_name": "setup_mode"  
				},
			]

		- At the end of this file add your own dictionary (modules data)-
			```
			jarvis_features_config = [
				{...
				},
				{  
				  "regex": "tell me date|date|today is what day",  
				  "import": "JarvisAI.features.date_time.jarvis_date_time",  
				  "function_name": "tell_me_date"  
				},  
				{  
				  "regex": "time",  
				  "import": "JarvisAI.features.date_time.jarvis_date_time",  
				  "function_name": "tell_me_time"  
				}
			]	
		
		- **regex:** you can put all the possible match pattern which user can aks. Multilple patterns can be seperated by `|` operator. Check existing regex pattern in dictionary before adding your regex. In this case `tell me date|date|today is what day`
		- **import:** you need to put your module's path. In this case- `JarvisAI.features.date_time.jarvis_date_time`
		- **function_name:** your function name according to your script file. In this case `tell_me_date` and `tell_me_time`
		- Now, if you added any library in the project (Example- Pandas) then make sure to add it in `requirements.txt`. And also add to `setup.py`  `install_requires=['pandas']` .
		- Now one last thing, change mode='pro' to mode='dev' in [jarvis.py](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/jarvis.py) and [_ _init__.py](https://github.com/Dipeshpal/Jarvis_AI/blob/master/JarvisAI/JarvisAI/__init__.py). This is because you may need to run this in local machine. Otherwise you will get an error. Make sure to change it back to 'pro' before pushing.
		- Now run `__init__.py` to check it on local.
		
4.4. **That's it, if you applied all the things as per as guidelines then now just run jarvis.py it should works fine.**

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