

from PIL import Image
import re

import os

global im
im = Image.open("./child on bars Copy.jpg")
original_pixel = im.getdata()
image_size = im.size


def putIntoColorGroup(image_pixel):

    file = open("list of colors.txt")

    lines = file.readlines()

    #dictionary for storing color group name and rgb values. this is needed after finding the image pixel's closest color group
    color_group_dict = {}



    # initializing dictionary for storing total difference value for every matching pixel with particular color group.
    difference_dict = {}

    for line in lines: 
        if 'rgb(' in line:

            pattern_color_Number = "[0-9]{1,3}"
            match_color_Number = re.findall(pattern_color_Number, line[line.find("rgb(") + 4:])

            color_group_red, color_group_green, color_group_blue = match_color_Number

            color_group_red = int(color_group_red)
            color_group_green = int(color_group_green)
            color_group_blue = int(color_group_blue)
            
            image_red, image_green, image_blue = image_pixel
            
            red_difference = abs(image_red - color_group_red)
            green_difference = abs(image_green - color_group_green)
            blue_difference = abs(image_blue - color_group_blue)
            

            total_difference = red_difference + green_difference + blue_difference

            pattern_color_name = "[a-z]+[^rgb\(]"
            match_color_name = re.search(pattern_color_name, line).group(0)

            #populating all color group name and values
            color_group_dict[match_color_name] = [color_group_red, color_group_green, color_group_blue]

            difference_dict[match_color_name] = total_difference

    # key_min has the color group name that has the closest match for the image pixel
    key_min = min(difference_dict.keys(), key=(lambda k: difference_dict[k]))  

    return color_group_dict[key_min]
    file.close()    


debug = False


#image_size[0] is image width
for x in range(image_size[0]):

   for y in range(image_size[1]):

        # converting for the getdata(). y is the row that you want to get data for
        new_x = y * image_size[0] + x 

        # is this how you get return tuple/list values from function?
        red, green, blue = putIntoColorGroup(original_pixel[new_x])

        
        im.putpixel((x, y),(red,green,blue))
        
        if debug == True:
           break
        
   if debug == True:
       break














