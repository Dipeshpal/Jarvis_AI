import setuptools
from setuptools import find_namespace_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="JarvisAI",
    version="3.2",
    author="Dipesh",
    author_email="dipeshpal17@gmail.com",
    description="JarvisAI is AI python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dipeshpal/Jarvis_AI",
    include_package_data=True,
    packages=find_namespace_packages(include=['JarvisAI.*', 'JarvisAI']),
    install_requires=['numpy', 'gtts==2.2.1', 'playsound==1.2.2',
                      'SpeechRecognition==3.8.1', 'pipwin==0.5.0', 'lxml==4.6.1', 'pyjokes',
                      'beautifulsoup4==4.9.3', 'wikipedia==1.4.0', 'auto_face_recognition', 'transformers==4.3.2',
                      'lazyme==0.0.23', 'librosa==0.8.0', "torch==1.7.1", "requests", "opencv-contrib-python==4.5.2.52",
                      "opencv-python==4.5.2.52", "cvzone==1.1.1"],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
