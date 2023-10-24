Submit the document "exit-ticket-10-24-23.md" on GitHub with your answers.

1. What is your favorite color? Tell us in English, and write the color's 3 number BGR code. You can use the Color Trackbar to find it, or look it up online.

2. Suppose we have two colors, `color_1` and `color_2` which are defined by the hue, saturation, values `(hue_1, sat_1, val_1)` and `(hue_2, sat_2, val_2)` respectively. Suppose that `hue_1 = hue_2`, `sat_1 = sat_2`, and `val_1 < val_2`(hue and saturation are the same but one value is lower). How would `color_1` and `color_2` differ visually?

# Challenge question!
3. We can *invert* a color by subtracting its respective $(B, G, R)$ values from 255. For example, the inverse of green $(0, 255, 0)$ is purple $(255, 0, 255)$. The inverse of gray $(127, 127, 127)$ is also gray $(128, 128, 128)$. $In the following code block, complete the function `invert_color` which takes in a tuple representing a BGR color, and returns a tuple representing its inverse.
```python
from typing import Tuple
green = (0, 255, 0)
purple = (255, 0, 255)

# Returns the inverse of a BGR color
def invert(bgr: Tuple) -> Tuple:
	# Erase pass and write you code here!
	pass
```