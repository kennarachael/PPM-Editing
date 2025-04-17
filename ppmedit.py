class PPMimage:
    
    def __init__(self, file, outfile):
        self.infile = open(file, "r")
        self.output_file_name = outfile
        self.image_copy = self.infile

        self.image = self.setup(self.infile)
        self.attributes = () #tuple
    
    """
    def copy(self,file):
        open(file)
        asdf = file.read()
        image = asdf.split(" ")
    """
    def out(self,file):
        pass





    def setup(self,file):
        #read file and turn into list
        
        nimage = file.read()
        image = nimage.split("\n"," ")
        index = 0
        for val in image:
            image[index] = val.strip("\t")
            index +=1
        
        self.attributes = self.find_attributes(image)

        nimage = nimage[3:]
        nimage = self.format(nimage)

        return image
        

    def find_attributes(self,file):
        magic_num, columns, rows, max_colour = file[0], file[1], file[2], file[3]

        return magic_num,columns,rows,max_colour
    

    def copy(self,file):
        dub = file
        return dub
    

    def format(self,file):
        #formats the file in a way that makes transformations easier (3d list)
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



    def negate_red(self):
        nimage = self.copy(self.image)
        #make a copy of self.image first and only makes changes to the copy
        for row in nimage:
            for pixel in row:
                red = pixel[0]
                neg_red = reversed(red)
                red = neg_red
        return nimage

    def flip_horizontal(self):
        flipimage = self.copy(self.image)
        for row in flipimage:
            row.replace(row.reverse())
        return flipimage

    def grey_scale(self, file):
        grey = self.copy(self.image)

        
        for row in grey:
            for pixel in row:
                total = 0
                count = 0
                for val in pixel:
                    total +=val
                    count +=1
                    if count ==3:
                        num = total /3
                        pixel = [num,num,num]
                total = 0
                count = 0

        return grey
    

    def flatten_red(self,file):
        flat = self.copy(self.image)

        for row in flat:
            for pixel in row:
                pixel[0] = 0
        
        return flat



c = PPMimage("tinypix.ppm","out.ppm")
print(c.image)
print(c.attributes)