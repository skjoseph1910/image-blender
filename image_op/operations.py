class operation:

    def blend(self, image, logo, x=None, y=None, alpha=None):
        '''
        Use logo and blend it on the image at location (x, y)
        image: the original image
        logo: the logo to blend on to the image
        x: topleft coordinate x
        y: topleft coordinate y
        alpha: blend ratio to the logo

        returns the image blended with logo at loction (x, y)
        '''
		#code
        ### add your code here
        ### Please do not change the structure

        blended_image = image

        for i in range(0, 225):
            for j in range(0, 225):
                if  0 <= x+i < 1960 and 0 <= y+j < 1960:
                    blended_image[x+i][y+j] = (alpha *image[x+i][y+j]) + ((1 - alpha) * logo[i][j])


        return blended_image 

 
