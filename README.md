# computer_vision_algorithm2
Putting every pixel into color group to make it easir to work with! You will have only dozens of pixel values to work with!!


Intstructions

you need to have picture before executing python file.

To start the program.
Simply execute the python file with Python interpreter.

From the windows command line.
py -3 putting_pixels_into_color_groups.py


What putting_pixels_into_color_groups.py does.

open the pixture and get pixels from it.

read list of colors.txt to get color groups names and RGB values.

Then, it compares all the pixels from the image with every one of color group RGB values and
determine which color group matches the pixel closest.

Once it finds the closest match, it replaces the pixel RGB values with the closest match RGB values.

There are about 30 - 40 color groups. So you will have only 30 to 40 pixels values to work with! instead of 100s of pixel values!



----------------------   WARNING   -----------------------

there is a bug in getting the closest values of color group.
I will fix this when I get a chance.

I am suspecting the code below is the culprit. I did not really check what this code does. I just found it from the internet and just used it without actually investigating what this code does.

    key_min = min(difference_dict.keys(), key=(lambda k: difference_dict[k]))  
