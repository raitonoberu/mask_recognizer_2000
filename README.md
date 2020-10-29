# Mask Recognizer 2000 😷
An app that checks whether you are wearing a mask or not. Made with OpenCV and Kivy. This is a competitive work for [РДШ "Меридиан"](https://vk.com/public177923488).

<p align="center">
    <img src="example.jpg?raw=true" width="300"/>
</p>


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
...if only it were that simple. **I promise you**, something won't install properly (if only because the damn Kivy still doesn't normally support Python 3.8+). Google each individual error yourself.

## Packaging
```bash
$ pip install pyinstaller
$ pyinstaller app.spec
```
A 200 MB+ .exe file will be generated in *dist* folder. It doesn't contain a *data* folder, so use them together. I do not know how to reduce the size, so make a Pull Request if you know.
