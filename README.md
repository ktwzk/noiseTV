# noiseTV

Random TV-noise generator with some interesting variables.

Based on [http://py.processing.org](Processing.py).

###Config-file format
Configuration file must have 4 lines for 4 variables:  
* BPM, float. Can be 0 (actually, means 3600),  
* Length of squares' side, int (px),  
* Color palette: ```b/w``` for black and white, ```rainbow``` for all colors; ```wheel``` for mouse-wheel control of Hue; ```mouse``` for Hue & Saturation control, based on mouseX and mouseY; or ```%x %y``` (int,int) for color in HSB: color will be: ```Rand(0,x)/255, Rand(0,y)/255, Rand(255)/255```,
* Cursor type: ```cross```, ```arrow```or ```no```.
