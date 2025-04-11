from itertools import batched

class PPMimage:
    
    def __init__(self, infile, outfile):
        self.output_file_name = outfile
        self.image_copy = self.copy(infile)

        self.image = self.setup(infile)
        self.attributes = () #tuple
    

    def copy(self,file):
        open(file)
        asdf = file.read()
        image = asdf.split(" ")


    def setup(self,file):
        #read file and turn into list
        open(file)
        asdf = file.read()
        image = asdf.split(" ")
        self.attributes = self.find_attributes(image)

        image = image[3:]
        image = self.format(image[4:])

        return image
        

    def find_attributes(self,file):
        magic_num, columns, rows, max_colour = file[0], file[1], file[2], file[3]

        return magic_num,columns,rows,max_colour
    
    def format(self,file):
        list = []
        
        for val in file:
            row = []
            pixel = []
            pixel += val
            #after 3, void pixel list after adding it to row
            if len(pixel) == 3:
                row.append(pixel)
                pixel = []

            #below checks if the row is complete based on rows amount given (attribute)
            if len(row) == self.attributes[2]:
                list.append[row]
                row = []
        
        return list



    def negate_red(self,file):

        #make a copy of self.image first and only makes changes to the copy
        for row in self.image:
            for pixel in row:
                red = pixel[0]
                neg_red = reversed(red)
                red = neg_red
        return self.image

    def flip_horizontal(self, file):
        pass

    def grey_scale(self, file):
        pass

    def flatten_red(self,file):
        pass



c = PPMimage("tinypix.ppm","out.ppm")
c.format()