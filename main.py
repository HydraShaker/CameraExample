import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.camera import Camera


kv = ''' 
Screen:
    Camera:
        id: cam
        resolution: (640, 400)
        play: True
'''


class CameraApp(App):
    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    CameraApp().run()
