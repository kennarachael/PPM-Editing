
class PPMimage:
    
    def __init__(self, file, outfile):
        
        self.output_file_name = outfile
        self.image = self.setup(file)
        self.attributes = [] #list
    

    def out(self,file):
        
        print(self.attributes[0] + "\n" + self.attributes[1] + " " + self.attributes[2] + "\n" + self.attributes[3]+ "\n")
        for row in file:
            for pixel in row:
                for val in pixel:
                    print(val + " ")
            print("\n") 




    def setup(self,file):
        #read file and turn into list
        #infile = open(file, "r")
        #nimage = infile.read()
        image = file.split() #image = nimage.split()
        
        self.attributes = self.find_attributes(image)

        nimage = image[3:]
        nimage = self.format(nimage)

        return nimage
        

    def find_attributes(self,file):
        magic_num = file[0] 
        columns = file[1]
        rows = file[2]
        max_colour = file[3]
        
        return [magic_num, columns, rows, max_colour]
    

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

            #below checks if the row is complete based on columns amount given (attribute)
            if len(row) == self.attributes[1]:
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
#print(c.image)
#print(c.attributes)

print(c.setup("P3\
    4 4\
    255\
    0  0  0   100 0  0       0  0  0    255   0 255\
    0  0  0    0 255 175     0  0  0     0    0  0\
    0  0  0    0  0  0       0 15 175    0    0  0\
    255 0 255  0  0  0       0  0  0    255  255 255"))
