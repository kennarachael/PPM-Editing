from itertools import batched

class PPMimage:
    
    def __init__(self, infile, outfile):
        self.input_file_name = infile
        self.output_file_name = outfile
        self.image = self.setup(infile)
        self.attributes = self.find_attributes(self.image) #tuple
    

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
        count = 0
        pix_count = 0
        for val in file:
            row = []
            pixel = []
            pixel += val
            #after 3, void pixel list after adding it to row

            #below checks if the row is complete based on rows amount given (attribute)
            if count == self.attributes[2]:
                count = 0
                list.append[row]
                row = []
            count +=1






    def negate_red(self,file):
        pass

    def flip_horizontal(self, file):
        pass

    def grey_scale(self, file):
        pass

    def flatten_red(self,file):
        pass



        