# Digital Image Processing 
Assignment #0

Due: Tue 01/28/20 11:59 PM

1. Image Blending:

Do not use any in-built functions from opencv and numpy. In general, you can use function from math library. <br/>
Functions allowed for this part are: np.array(), np.matrix(), np.zeros(), np.ones(), cv2.imread(), cv2.namedWindow(), cv2.waitKey()

(2 pts.) Write code to blend a logo on to an image. The input to your program is: (i) image, (ii) logo, (iii) location x-coordinate, (iv) location y-coordinate, and (v) blending ratio (alpha).

  - Starter coder available in directory image_op/
  - image_op/operations.py: Edit the function blend
    - Write code to to blend a logo on to an image
    - Write code to handle invalid location. If the logo extends beyond the bounds of the image, ignore the part of logo that is outside the bounds of the image
    - Please do not change the code structure
  - Usage:
   
        - python dip_hw0.py -i <image-name> -l <logo> -x <x> -y <y> -a <alpha>
        - Example: python dip_hw0.py -i lenna.jpg -l uh.png -x 0 -y 0 -a 0.5
  - Please make sure the code runs when you run the above command from prompt/terminal
  - All the output images and files are saved to "output/" folder
  - The TA will not be able to graded if the code does not pass the CircleCI test

Two images are provided for testing: lenna.jpg and uh.png
  
PS. Please do not change: dip_hw0.py, requirements.txt, and .circleci directory 


1. Operation      - 2 Pts

    Total          - 2 Pts.

-----------------------

<sub><sup>
License: Property of Quantitative Imaging Laboratory (QIL), Department of Computer Science, University of Houston. This software is property of the QIL, and should not be distributed, reproduced, or shared online, without the permission of the author This software is intended to be used by students of the digital image processing course offered at University of Houston. The contents are not to be reproduced and shared with anyone with out the permission of the author. The contents are not to be posted on any online public hosting websites without the permission of the author. The software is cloned and is available to the students for the duration of the course. At the end of the semester, the Github organization is reset and hence all the existing repositories are reset/deleted, to accommodate the next batch of students.
</sub></sup>
