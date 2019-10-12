
"""
# Problem Set 5
# Name: Deniz Sert
# Collaborators: Chris Noga, Miles Kaming-Thanassi
# Time: 6 hrs
# Late Days Used: 1
"""    

from PIL import Image

binary_string_1 = 111 # TODO: fill in binary representation of 7
binary_string_2 = 100000 # TODO: fill in binary representation of 32
binary_string_3 = 11101 # TODO: fill in binary representation of 29

def make_matrix(color):
    """
    Generates a transformation matrix for the specified color.
    Inputs:
        color: string with exactly one of the following values:
               'red', 'blue', 'green', or 'none'
    Returns:
        matrix: a transformation matrix corresponding to
                deficiency in that color
    """
    # You do not need to understand exactly how this function works.
    if color == 'red':
        c = [[.567, .433, 0],[.558, .442, 0],[0, .242, .758]]
    elif color == 'green':
        c = [[0.625,0.375, 0],[ 0.7,0.3, 0],[0, 0.142,0.858]]
    elif color == 'blue':
        c = [[.95, 0.05, 0],[0, 0.433, 0.567],[0, 0.475, .525]]
    elif color == 'none':
        c = [[1, 0., 0],[0, 1, 0.],[0, 0., 1]]
    return c


def multiply_matrices(m1,m2):
    """
    Multiplies the input matrices.
    Inputs:
        m1,m2: the input matrices
    Returns:
        result: matrix product of m1 and m2
        in a list of floats
    """

    product = numpy.matmul(m1,m2)
    if type(product) == numpy.int64:
        return float(product)
    else:
        result = list(product)
        return result


def image_to_pixels(image_file):
    """
    Takes an image_file (must be inputted as a string
    with proper file attachment ex: .jpg, .png)
    and converts to a list of tuples representing pixels.
    Each pixel is a tuple containing (R,G,B) values.

    Returns the list of tuples.

    Inputs:
        image_file: string representing an image file, such as 'lenna.jpg'
        returns: list of pixel values in form (R,G,B) such as
                 [(0,0,0),(255,255,255),(38,29,58)...]
    """
    pixels = []
    im = Image.open(image_file)
    pix = im.load()
    width, height = im.size

    #iterates through Image (R,G,B)s and creates a list
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x,y]
            pixels.append(cpixel)
    return list(pixels)


def pixels_to_image(pixels, size, mode):
    """
    Creates an Image object from a inputted set of RGB tuples.

    Inputs:
        pixels: a list of pixels such as the output of
                convert_image_to_pixels.
        size: a tuple of (width,height) representing
              the dimensions of the desired image. Assume
              that size is a valid input such that
              size[0] * size[1] == len(pixels).
        mode: 'RGB' or 'L' to indicate an RGB image or a 
              BW image, respectively
    returns:
        img: Image object made from list of pixels
    """
    #creates a new blank image
    im = Image.new(mode, size)
    #collects data from pixel list and places it into blank image
    im.putdata(pixels)
    return im


def filter(pixels, color):
    """
    pixels: a list of pixels in RGB form, such as 
            [(0,0,0),(255,255,255),(38,29,58)...]
    color: 'red', 'blue', 'green', or 'none', must be a string representing 
           the color
    deficiency that is being simulated.
    returns: list of pixels in same format as earlier functions,
    transformed by matrix multiplication
    """
    updated_pixel_list = []
    for p in pixels:
        new_p = tuple(map(int, multiply_matrices(make_matrix(color), pixel)))
        updated_pixel_list.append(new_pixels)
    return new_p_list

#STUDY THIS
def get_end_bits(num_bits, pixel_value):
    """
    Extracts the last num_bits bits of a given pixel. 

    For example:
        num_bits = 5
        pixel_value = 214

        214 in binary is 11010110. 
        The last 5 bits of 11010110 are 10110.
                              ^^^^^
        The integer representation of 10110 is 22, so we return 22.

    Inputs:
        num_bits: the number of bits to extract
        pixel_value: the integer value of a pixel, between 0 and 255

    Returns:
        The last num_bits bits of pixel_value, as an integer.
    """
    binary = bin(pixel_value)
    #iterates through pixel values from the end
    new_bin = binary[-(num_bits):]
    num = int(new_bin, 2)
    return num

def decimal_to_binary(n):
    if (n>1):
        convert_to_binary(n//2)
    print(int(n%2))

def binary_to_decimal(n):
    return bin(n).replace("0b", "")

def set_end_bits(num_bits, pixel_value, new_bits):
# '''
#     #Sets the last num_bits bits of a given pixel to a specified value.
#
#     For example:
#         num_bits = 5
#         pixel_value = 214
#         new_bits = 16
#
#         214 in binary is 11010110.
#         16 in binary is 10000.
#         We therefore want to set the last 5 bits of 11010110 to 10000.
#         This yields 11010000.
#         The integer representation of 11010000 is 208, so we return 208.
#
#     Inputs:
#         num_bits: the number of bits to set
#         pixel_value: the integer value of a pixel, between 0 and 255
#         new_bits: the new bits to set
#
#     Returns:
#         The new pixel value when the last num_bits of pixel_value
#         are set to new_bits, as an integer.
#
# '''

    return pixel_value - ged_end_bits(num_bits, pixel_value) + new_bits

# #from Internet
# def change_contrast(filename, img, level):
#     '''
#
#
#     '''
#     img = Image.open(filename)
#     img.load()
#
#     factor = (259 * (level+255)) / (255 * (259-level))
#     for x in range(img.size[0]):
#         for y in range(img.size[1]):
#             color = img.getpixel((x, y))
#             for c in color:
#                 new_color = tuple(int(factor * (c-128) + 128)
#             img.putpixel((x, y), new_color)
#
#     return img


def show_image(filename):
    """
    Extracts the single LSB (for a BW image) or the 2 LSBs (for a 
    color image) for each pixel in the input image. Hint: you can
    use a function to determine the mode of the input image (BW or
    RGB) and then use this mode to determine how to process the image.
    Inputs:
        filename: string, input BW or RGB file to be processed
    Returns:
        result: an Image object containing the hidden image
    """
    # use mode of the given image to determine if you need 1/2 LSBs
    
    #initializes the image
    img_mode = Image.open(filename).mode()
    img_size = Image.size(filename)
    pixel_list = []
    #creates pixel list from image
    image_pixels = image_to_pixels(filename)
    #if color image
    if img_mode == 'RGB':
        for pixels in image_pixels:
            #uses end bits to manipulate and show an image
            a = filename.get_end_bits(pixels, 2)
            pixel_list.append(a)
        b = pixels_to_image(pixel_list, image_size, 'RGB')
    #if Black and White image
    else:
        for pixels in image_pixels:
            a = filename.get_end_bits(pixels, 1)
            pixel_list.append(a)
        y = pixels_to_image(pixel_list, img_size, 'L')
    return y




    # else:
    #     img_m = image_to_pixels(filename)
    #     new_con_img = filename.get_end_bits(img_m, 1)


def hide_image(hidden_image_filename, showing_image_filename):
    """
    Create a new image with an image file hidden_image_filename 
    inside the LSBs of another image file showing_image_filename.
    The new image will look like showing_image_filename, but
    running show_image on the new image will reveal 
    hidden_image_filename. 

    Set the last 2 LSBs (for a color image) for each pixel in 
    the original_image_filename to a scaled representation of 
    the respective pixel in hidden_image_filename.

    Inputs:
        hidden_image_filename: string, input RGB file to be 
            hidden in a new image
        showing_image_filename: string, input RGB file new 
            image should look like. has same dimensions as 
            hidden_image_filename.
    Returns:
        combined_image_filename: string, output RGB file 
            looks like hidden_image_filename and has 
            showing_image_filename encoded in LSBs
    """
    #initialize Images



    #each image has the same dimensions
    image_size = Image.size(hidden_image_filename)

    
    #initializes Image
    hidden_image = Image.open(hidden_image_filename)
    showing_image = Image.open(showing_image_filename)
    #finds mode of image (black&white or color)
    img_mode = Image.open(hidden_image_filename).mode()
    #converts Image to Pixels
    hidden_pixels = image_to_pixels(hidden_image)
    shown_pixels = image_to_pixels(showing_image)
    new_pixels_list = []
    #iterates through the length of the pixels of 1 of the images (both are same size)
    for i in range(len(hidden_pixels)):
        #scales image to a LSB btwn 1-3
        pixel_tuple = (hidden_pixels[i][0]//64, hidden_pixels[i][1]//64, hidden_pixels[i][2]//64)
        #adds tuple to new list
        for j in range(0,3):
            new_pixels_list.append(set_end_bits(8, shown_pixels[i](j), pixel_tuple(j)))
    #converts new list into an image
    new_img = image_to_pixels(new_pixels_list)
    new_img.save("secret.bmp")
    return "secret.bmp"








    #scale image by divding each number by 64
    #make a new tuple representing 1 pixel
    #add tuple to list


    #shown image. set_n_bits(new tuple, 8 bit, RGB)
    #add new numbers to last numbers of shown image list
    #make a new image out of pixel list




    # showing_image[width][height][i].set_end_bits(8, i, hidden_image[width][height][i].get_end_bits(8, [i]))
    # Image.save("secret.bmp")





def main():
    pass

    # Uncomment the following lines to test part 1

    # im = Image.open('image_15.png')
    # width, height = im.size
    # pixels = image_to_pixels('image_15.png')
    #
    # non_filtered_pixels = filter(pixels,'none')
    # im = pixels_to_image(non_filtered_pixels, (width, height), 'RGB')
    # im.show()
    #
    # red_filtered_pixels = filter(pixels,'red')
    # im2 = pixels_to_image(red_filtered_pixels,(width,height), 'RGB')
    # im2.show()

    # No tests for part 2. Write your own code to find the secret images!


if __name__ == '__main__':
    main()
?>

