# Mask Recognizer 2000 😷
An app that checks whether you are wearing a mask or not. Made with OpenCV and Tkinter. This is a competitive work for [РДШ "Меридиан"](https://vk.com/public177923488).

<!--  ADD LATER
<p align="center">
    <img src="example.jpg?raw=true" width="300"/>
</p>
-->

## How does it work?
The script tries to find the nose and mouth on your face. If he couldn't find them, you wear a mask. Pretty simple, huh?

## Installation
Python 3.7+
```bash
$ git clone https://github.com/raitonoberu/mask_recognizer_2000
$ cd mask_recognizer_2000
$ pip install -r requirements.txt
$ python app.py
```

## Packaging
```bash
$ pip install pyinstaller
$ pyinstaller app.spec
```
A ~60 MB .exe file will be generated in *dist* folder. It doesn't contain a *data* folder, so use them together.
