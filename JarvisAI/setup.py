import setuptools
from setuptools import find_namespace_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="JarvisAI",
    version="0.1.8",
    author="Dipesh",
    author_email="dipeshpal17@gmail.com",
    description="JarvisAI is AI python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dipeshpal/Jarvis_AI",
    include_package_data=True,
    packages=find_namespace_packages(include=['JarvisAI.*', 'JarvisAI']),
    install_requires=['gtts', 'playsound', 'SpeechRecognition',
                      'pipwin', 'lxml',
                      'beautifulsoup4', 'wikipedia', 'pipwin'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
