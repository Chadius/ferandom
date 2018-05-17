# Requirements
## Python 3.6
This application was developed in Python 3.6

## Virtual Environment
python3 -m virtualenv --system-site-packages .

## kivy
https://kivy.org/docs/guide/basic.html

### Mac
You can follow the guide to install the kivy app.

If you don't want to follow the kivy app, you can do this instead:

https://gist.github.com/garyjohnson/53c1eef4adaf57c247a4

#!/bin/bash
brew install sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer
pip3 install --upgrade Cython==0.25.2
# USE_OSX_FRAMEWORKS=0 pip3 install kivy # currently doesn't work due to incompatibility with SDL_mixer: https://github.com/kivy/kivy/pull/5459
USE_OSX_FRAMEWORKS=0 pip3 install http://github.com/kivy/kivy/archive/master.zip

Also install pygame
pip install pygame