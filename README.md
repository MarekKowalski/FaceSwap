# FaceSwap #
FaceSwap is an app that I have originally created as an exercise for my students in "Mathematics in Multimedia" on the Warsaw University of Technology.
The app is written in Python and uses face alignment, Gauss Newton optimization and image blending to swap the face of a person seen by the camera with a face of a person in a provided image.

You will find a short presentation the program's capabilities in the video below (click to go to YouTube):
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/yZRuSsyxvos/0.jpg)](http://www.youtube.com/watch?v=yZRuSsyxvos)

## How to use it ##
To start the program you will have to run a file named zad2.py (Polish for exercise 2), which will require:
  * Python 2.7 (I recommend Anaconda)
  * OpenCV (I used 2.4.13)
  * Numpy
  * dlib
  * pygame
  * PyOpenGL

You can download all of the libraries above either from PIP or from Christoph Gohlke's excellent website: http://www.lfd.uci.edu/~gohlke/pythonlibs/

You will also have to download the face alignment model from here: http://sourceforge.net/projects/dclib/files/dlib/v18.10/shape_predictor_68_face_landmarks.dat.bz2 and unpack it to the main project directory.

## Licensing ##
The code is licensed under the MIT license, some of the data in the project is downloaded from 3rd party websites:
  * brad pitt.jpg - https://en.wikipedia.org/wiki/Brad_Pitt#/media/File:Brad_Pitt_Fury_2014.jpg
  * einstein.jpg - https://www.viewfoo.com/uploads/images/702_1433440837_albert-einstein.jpg
  * jolie.jpg - http://cdni.condenast.co.uk/720x1080/a_c/Angelina-Jolie_glamour_2mar14_rex_b_720x1080.jpg
  * hand.png - http://pngimg.com/upload/hands_PNG905.png
  * eye.png - http://cache4.asset-cache.net/xd/521276062.jpg?v=1&c=IWSAsset&k=2&d=62CA815BFB1CE4807BD8B4D34504661CD6D7111452E48A17257DA6DB0BD6EA6DE35742C781328F67
  * candide 3D face model source - http://www.icg.isy.liu.se/candide/
  
## Contact ##
If need help or you found the app useful, do not hesitate to let me know. 

Marek Kowalski <m.kowalski@ire.pw.edu.pl>, homepage: http://home.elka.pw.edu.pl/~mkowals6/
  
  
