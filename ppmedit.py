
class PPMimage:
    
    def __init__(self, infile, outfile):
        
        self.output_file_name = outfile
        self.image = self.setup(infile)
        self.attributes = self.find_attributes(infile) #list


    def out(self,file):
        o = open(self.output_file_name, "w+")
        o.write(str(self.attributes[0]) + "\n" + "\t" + str(self.attributes[1]) + " " + str(self.attributes[2]) + "\n" + "\t" + str(self.attributes[3]) + "\n")

        for row in file:
            for pixel in row:
                o.write("\t")
                for val in pixel:
                    o.write(str(val) + " ")
            o.write("\n") 

        o.read()
        return o

    def open(self,file):
        infile = open(file, "r")
        nimage = infile.read()
        image = nimage.split()
        return image

    def setup(self,file):
        #read file and turn into list
        image = self.open(file)
        #print(image)
        self.attributes = self.find_attributes(file)
        nimage = image[4:] 
        nimage = self.format(nimage)

        return nimage
        

    def find_attributes(self,file):
        pix = self.open(file)
        self.magic_num = pix[0]
        self.columns = pix[1]
        self.rows = pix[2]
        self.max_colour = pix[3]
        
        return [self.magic_num, self.columns, self.rows, self.max_colour]
    

    def copy(self,file):
        dub = file
        return dub
    

    def format(self,file):
        #formats the file in a way that makes transformations easier (3d list)
        list = []
        row = []
        pixel = []

        for val in file:
            
            pixel.append(val)
            #after 3, void pixel list after adding it to row
            if len(pixel) == 3:
                row.append(pixel)
                pixel = []

            #below checks if the row is complete based on columns amount given (attribute)
            if len(row) == int(self.attributes[1]):
                list.append(row)
                row = []
        
        return list



    def negate_red(self):
        negimage = self.copy(self.image)
        #make a copy of self.image first and only makes changes to the copy
        for row in negimage:
            for pixel in row:
                red = int(pixel[0])
                neg_red = 255 - red
                pixel[0] = neg_red
                
        self.out(negimage)

    def flip_horizontal(self):
        flipimage = self.copy(self.image)
        for row in flipimage:
            row = (row.reverse())
        self.out(flipimage)

    def grey_scale(self):
        grey = self.copy(self.image)

        
        for row in grey:
            for pixel in row:
                total = 0
                count = 0
                for val in pixel:
                    total +=int(val)
                    count +=1
                    if count ==3:
                        num = total // 3
                        pixel[0] = num
                        pixel[1] = num
                        pixel[2] = num

                        count = 0
                        total = 0
                    
                
                

        self.out(grey)
    
    def flatten_red(self):
        flat = self.copy(self.image)

        for row in flat:
            for pixel in row:
                pixel[0] = 0
        
        self.out(flat)



c = PPMimage("tinypix.ppm","outpix.ppm")
