# Question 1
Which of the following lines correctly converts `img`, a BGR image, into `gray`, a grayscale image?
a) `gray = cv2.Color(img, cv2.COLOR_BGR2GRAY)`
b) `gray = cv2.cvtColor(img, cv2.BGR2GRAY)`
c) `gray = cvtColor(img, cv2.COLOR_BGR2GRAY)`
d) `gray = cv2.cvtColor(img, cv2COLOR_BGR2GRAYSCALE)`
# Question 2
Recall the `bitwise_and` (&) operator. Given the following two binary numbers `a` and `b`, what would be the result of `a & b`?
`a = 0001 0101`
`b = 1111 1100`
`a & b = ...`
# Question 3
You have been hired by Volta Electric Cars to work on their new autonomous vehicle systems. They want to design a system that can identify if a traffic light is red, yellow, or green, in order to instruct the engine to stop or go. In 2-4 sentences, describe how you would design a function `read_traffic_light(img)` which takes in a picture containing a traffic light and returns one of "green", "yellow", or "red". Your answer should be an English description of how you would process the image to decide which color to output, but you may include snippets of code if you'd like.