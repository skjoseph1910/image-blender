"""dip_hw0.py: Starter file to run howework 0"""

__author__      = "Pranav Mantini"
# revised by Zhenggang Li
__email__ = "pmantini@uh.edu"
__version__ = "1.0.0"

import cv2
import sys
from datetime import datetime
from image_op import operations


def display_image(window_name, image):
    """A function to display image"""
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)


def main():
    """ The main funtion that parses input arguments, calls the approrpiate
     method and writes the output image"""

    #Parse input arguments
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-i", "--image", dest="image",
                        help="specify the name of the image", metavar="IMAGE")
    parser.add_argument("-l", "--logo", dest="logo",
                        help="use the name of the UH LOGO image", metavar="UH_IMAGE")

    parser.add_argument("-x", "--topleft_x", dest="topleft_x",
                        help="specify location of x", metavar="X")
    parser.add_argument("-y", "--topleft_y", dest="topleft_y",
                        help="specify location of y", metavar="Y")

    parser.add_argument("-a", "--alpha", dest="alpha",
                        help="specify blend ratio to LOGO image", metavar="ALPHA")

    
    args = parser.parse_args()
	
    #Load image
    if args.image is None:
        print("Please specify the name of image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        image_name = args.image.split(".")[0]
        input_image = cv2.imread(args.image, 0)

    if args.logo is None:
        print('Please use UH LOGO image')
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        logo = cv2.imread(args.logo, 0)

    # Check if the logo is the smaller one
    
    r1, c1 = input_image.shape
    r2, c2 = logo.shape
    
    if r1 < r2 or c1 < c2:
        print('The image should be larger than UH LOGO')
        sys.exit(2)

    # Check the location to blend
    if args.topleft_x is None:
        print("Location X not specified using default (0)")
        print("use the -h option to see usage information")
        x = 0
    else:
        x = int(args.topleft_x)

    if args.topleft_y is None:
        print("Location Y not specified using default (0)")
        print("use the -h option to see usage information")
        y = 0
    else:
        y = int(args.topleft_y)

    # Check the alpha is between 0 to 1
    if args.alpha is None:
        print('ALPHA not specified using default (0)')
        alpha = 0
    else:
        if 0 <= float(args.alpha) <= 1:
            alpha = float(args.alpha)
        else:
            print('The weight should within range 0 to 1')
            sys.exit(2)


    operation_obj = operations.operation()
    operation_image = operation_obj.blend(input_image, logo, x=x, y=y, alpha=alpha)

    # display_image('operation_image', operation_image)

    #Write output file
    outputDir = 'output/'

    output_image_name = outputDir+image_name+datetime.now().strftime("%m%d-%H%M%S%f")+".jpg"
    cv2.imwrite(output_image_name, operation_image)



if __name__ == "__main__":
    main()







