# noiseTV
#### Random TV-noise generator with some interesting variables.
Based on [http://py.processing.org](Processing.py).

###Config-file format
Configuration file must have 5 lines for 5 variables:  
* BPM, float. Can be 0 (actually, means 3600)
* Length of squares' side in px, int
* Color palette: 
  * ```b/w``` for black and white
  * ```rainbow``` for all colors
  * ```wheel-hue``` for mouse-wheel control of Hue
  * ```wheel-saturation``` for mouse-wheel control of Saturation
  * ```keyboard``` for H&S control by the keyboard arrows: Hue: right/left, Saturation: up/down
  * ```mouse``` for Hue & Saturation control, based on mouseX and mouseY
  * ```%x %y``` (int,int) for color in HSB, so color will be: ```Rand(0,x)/255, Rand(0,y)/255, Rand(255)/255```
* Cursor type: ```arrow```, ```cross``` or ```no```
* ```3D``` or ```2D```. In 2D-mode, you can see noise like when you see it on TV. On 3D-mode there is a room with strange noisy walls

####2D mode, rainbow
![2D](http://kotwizkiy.ru/img/2D.png)
####Red 3D room
![3D](http://kotwizkiy.ru/img/3D.png)


###TODO:
* Add Tap-BPM
* Make 3D-room interesting and beautiful
* http://py.processing.org/reference/imageMode.html, http://py.processing.org/reference/image.html
