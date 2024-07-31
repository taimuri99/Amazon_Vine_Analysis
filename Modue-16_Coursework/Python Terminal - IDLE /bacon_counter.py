#pip install MRJob
from mrjob.job import MRJob

#Create a class called Bacon_count, which inherits, or takes properties, from the MRJob class. We create this class to be called to run the full MapReduce job withMRJob:
class Bacon_count(MRJob):

#Next, create a mapper()function that will take (self, _, line) as parameters. The mapper() function will assign the input to key-value pairs:
#The second parameter (here using an underscore (_), explained next) allows methods to be mapped together. Since we are not chaining anything together, we use the Python convention of an underscore to indicate that we won’t use this parameter. The line parameter will be the line of text taken from the raw input file
    
    
    
    #The function will loop through each word in the line of text, as described below: 
        #Call the split() method on each line to break the text into a list of words.
        #Each word will convert to lowercase.
        #If the words match the search word "bacon," a key-value pair will show as yield "bacon", 1.
        #When you call a function with yield it returns what is called a generator object. A generator is an iterator like a list, however unlike a list the contents are not stored in memory, useful for large files. When yield is called the function is suspended and returns a value. A generator won't return another value until next() is called, which is something that mrJobs calls a number of times till it is done. So, for a yield, each time the word "bacon" appears, mrJobs returns “bacon”, 1. If "bacon" appears three times, then an output of “bacon”, 1 would be produced three times.
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "bacon":
                yield "bacon", 1


    #There's a shuffle step that occurs after the mapper. There is no code written for this step, and it occurs because the class inherits from the mrjob library. This shuffle step organizes the key-value pairs so that there's only one key for each unique key, and combines the values into a list.
    #The reducer function might not look like it's doing as much as the mapper function, but it's just as important. The reducer function takes three parameters: self, key, and values:
    #The self parameter is used in Python to represent the instance of the class.
    #The key parameter represents the key of the key-value pair created in the mapper function. In this example, the key is "bacon."
    #The values parameter is a list of values created in the mapper function. We want to sum all of these values. Recall that from the mapper function the yield was used to produce multiple outputs. With the reducer we'll produce the key and sum of all the values assigned with it:
    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == "__main__":
   Bacon_count.run()


   #in terminal python bacon_counter.py input.txt