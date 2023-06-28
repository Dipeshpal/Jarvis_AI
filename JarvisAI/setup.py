import setuptools
from setuptools import find_namespace_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="JarvisAI",
    version="4.9",
    author="Dipesh",
    author_email="dipeshpal17@gmail.com",
    description="JarvisAI is python library to build your own AI virtual assistant with natural language processing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dipeshpal/Jarvis_AI",
    include_package_data=True,
    packages=find_namespace_packages(include=['JarvisAI.*', 'JarvisAI']),
    install_requires=['numpy', 'gtts', 'playsound', 'pyscreenshot', "opencv-python",
                      'SpeechRecognition', 'pyjokes', 'wikipedia', 'scipy', 'lazyme',
                      "requests", "pyttsx3", "spacy==3.5.0", 'pywhatkit', 'speedtest-cli',
                      'pytube', 'pycountry', 'playsound', 'pyaudio', 'mediapipe==0.8.11',
                      'pycaw', 'openai-whisper', 'shutup', 'sounddevice', 'html2text==2020.1.16',
                      'wikipedia==1.4.0', 'Markdown==3.4.1', 'markdown2==2.4.8',
                      'lxml==4.9.2', 'googlesearch-python==1.2.3', 'selenium', 'selenium-pro',
                      'element-manager'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        'Official Website': 'https://jarvisai.in',
        'Documentation': 'https://github.com/Dipeshpal/Jarvis_AI',
        'Donate': 'https://www.buymeacoffee.com/dipeshpal',
        'Say Thanks!': 'https://youtube.com/techportofficial',
        'Source': 'https://github.com/Dipeshpal/Jarvis_AI',
        'Contact': 'https://www.dipeshpal.in/social',
    },
)
