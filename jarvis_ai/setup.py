import setuptools
from setuptools import find_namespace_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jarvis-ai",
    version="0.0.02",
    author="Dipesh",
    author_email="dipeshpal17@gmail.com",
    description="Jarvis-AI is AI python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dipeshpal/Jarvis_AI",
    include_package_data=True,
    packages=find_namespace_packages(include=['jarvis_ai.*', 'jarvis_ai']),
    install_requires=['numpy', 'gtts', 'playsound', 'SpeechRecognition',
                      'spacy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
