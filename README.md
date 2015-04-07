# noiseTV

Random TV-noise generator with some interesting variables.

Based on [http://py.processing.org](Processing.py).

###Config-file format
Configuration file must have 4 lines for 4 variables:  
* BPM, float. Can be 0 (actually, means 3600).
* Length of squares' side in px, int.
* Color palette: 
  * ```b/w``` for black and white
  * ```rainbow``` for all colors 
  * ```wheel-hue``` for mouse-wheel control of Hue
  * ```wheel-saturation``` for mouse-wheel control of Saturation
  * ```keyboard``` for H&S control by the keyboard arrows: Hue: right/left, Saturation: up/down
  * ```mouse``` for Hue & Saturation control, based on mouseX and mouseY
  * ```%x %y``` (int,int) for color in HSB, so color will be: ```Rand(0,x)/255, Rand(0,y)/255, Rand(255)/255```
* Cursor type:  ```arrow```, ```cross``` or ```no```.
