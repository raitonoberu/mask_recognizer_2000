import cv2
import tkinter as tk
from PIL import Image, ImageTk

import recognition


class RecognitionApp(object):
    def __init__(self, flip=None, callback=None, source=0):
        self.flip = flip
        self.callback = callback
        self.source = source

        # set up gui
        self.window = tk.Tk()
        self.window.resizable(False, False)
        self.window.wm_title("Mask Recognizer 2000")
        self.window.config(background="#FFFFFF")

        self.image_frame = tk.Frame(self.window)
        self.image_frame.grid(row=0)

        self.image_label = tk.Label(self.image_frame)
        self.image_label.grid(row=0)

        self.bottom_frame = tk.Frame(self.window)
        self.bottom_frame.grid(row=1)

        self.status_label = tk.Label(self.bottom_frame)
        self.status_label.grid(row=0, column=1)
        self.status_label.config(font=("Arial", 44))

        self.flip_button = tk.Button(self.bottom_frame, text="🔄")
        self.flip_button.grid(row=0, column=0)
        self.flip_button.bind('<Button-1>', self.flip_camera)

        self.camera_button = tk.Button(self.bottom_frame, text="📷")
        self.camera_button.grid(row=0, column=2)
        self.camera_button.bind('<Button-1>', self.change_camera)

        # set up opencv
        self.capture = cv2.VideoCapture(self.source)
        self.window.protocol("WM_DELETE_WINDOW", self.on_stop)

    def update(self):
        ret, img = self.capture.read()
        if ret:
            # update image
            buffer, status = recognition.update(img)
            if self.flip is not None:
                buffer = cv2.flip(buffer, self.flip)
            # convert it to texture
            buffer = cv2.cvtColor(buffer, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(buffer)
            imgtk = ImageTk.PhotoImage(image=img)
            self.image_label.imgtk = imgtk
            self.image_label.configure(image=imgtk)

            # callbacks
            self.show_status(status)
            if self.callback:
                self.callback(status)

            self.image_label.after(10, self.update)

    def show_status(self, status):
        if status:  # mask is weared
            text = "Маска надета!"
            color = "#00FF00"
        else:
            if status is None:  # no face
                text = "Лицо не видно"
                color = "#000000"
            else:  # mask is not weared
                text = "Наденьте маску!"
                color = "#FF0000"

        self.status_label['text'] = text
        self.status_label.config(fg=color)

    def flip_camera(self, _):
        # None / -1 / 0 / 1
        if self.flip is None:
            self.flip = -1
        elif self.flip == -1:
            self.flip = 0
        elif self.flip == 0:
            self.flip = 1
        else:
            self.flip = None

    def change_camera(self, _):
        if self.source == 0:
            self.source = 1
        else:
            self.source = 0
        self.capture.release()
        self.capture = cv2.VideoCapture(self.source)

    def run(self):
        self.update()
        self.window.mainloop()

    def on_stop(self):
        self.capture.release()
        cv2.destroyAllWindows()
        self.window.destroy()


if __name__ == '__main__':
    RecognitionApp().run()