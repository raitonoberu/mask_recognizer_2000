import cv2
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.lang import Builder
from kivy.uix.image import Image

import recognition


class KivyCamera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, _):
        ret, img = self.capture.read()
        if ret:
            # update image
            buf1, status = recognition.update(img)
            # convert it to texture
            buf = buf1.tostring()
            image_texture = Texture.create(
                size=(img.shape[1], img.shape[0]), colorfmt="bgr"
            )
            image_texture.blit_buffer(buf, colorfmt="bgr", bufferfmt="ubyte")
            # display image from the texture
            self.texture = image_texture
            app.show_status(status)


class CamApp(App):
    source = 0

    def build(self):
        self.title = "Mask Recognizer 2000"
        with open("data/gui.kv", "r", encoding="UTF-8") as f:
            gui = f.read()
        self.screen = Builder.load_string(gui)
        return self.screen

    def show_status(self, status):
        if status is None:  # no face
            text = "Лицо не видно"
            color = [0.41, 0.42, 0.74, 1]
        elif status:  # mask is weared
            text = "Маска надета!"
            color = [0.04, 0.6, 0.19, 1]
        elif not status:  # mask is not weared
            text = "Наденьте маску!"
            color = [1, 0, 0, 1]

        self.screen.ids["status"].text = text
        self.screen.ids["status"].color = color

    def change_capture(self, _):
        if self.source == 0:
            self.source = 1
        else:
            self.source = 0
        self.capture.release()
        self.capture = cv2.VideoCapture(self.source)
        self.camera.capture = self.capture

    def on_start(self):
        self.capture = cv2.VideoCapture(self.source)
        self.camera = KivyCamera(capture=self.capture, fps=30)
        self.screen.ids["boxlayout"].add_widget(self.camera)
        self.screen.ids["change"].bind(on_release=self.change_capture)

    def on_stop(self):
        self.capture.release()


if __name__ == "__main__":
    app = CamApp()
    app.run()
