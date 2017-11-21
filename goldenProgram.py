
import csv

from collections import defaultdict

def posts(fileName):

        if (fileName = "project-portion.csv"):          ## checks to see if the file is real.
        
            count = 60                                    ##starts excel at 60 for me
            
            infile = csv.reader(open(fileName,"r"))             ## takes in my file to read
            
            fileOut = open("wp_posts4.csv","w")               ## file to be sent out
            
            string = "0000-00-00 00:00:00"                   ## sets dateTime to default
            
            for tuple1 in infile:
                
                num = 0
                myLine = ""                     
                num = 0
                tuple1[num] = tuple1[num].replace(",","")               ## replaces unwanted characters from projectPortion
                
                myLine = tuple1[num].lower()

                ## print(infile)
                
                for charactr in myLine:                         ## takes out unwanted characters
                    
                    myLine = myLine.replace(" ","-")
                    myLine = myLine.replace("?","")
                    myLine = myLine.replace("!","")
                    myLine = myLine.replace("@","")
                    myLine = myLine.replace("#","")
                    ## print(myLine)
                    myLine = myLine.replace("$","")
                    myLine = myLine.replace("%","")
                    myLine = myLine.replace("^","")
                    myLine = myLine.replace("&","")
                    ## print(myLine)
                    myLine = myLine.replace("*","")
                    myLine = myLine.replace("~","")
                    myLine = myLine.replace("<","")
                    myLine = myLine.replace(">","")
                    myLine = myLine.replace(";","")
                    myLine = myLine.replace("|","")
                    myLine = myLine.replace(",","")
                    myLine = myLine.replace(",","")

                    ##ste = str(count)
                    
                fileOut.write(str(count) + ','+str(1) + ',' + "'" + string + "'"+"," + "'" + string + "'" + "," + "''" + ",")
                
                fileOut.write("'" + tuple1[num] + "'" + ',' + "''" + ',' + "'publish'" + "," + "'open'" + "," + "'closed'" + ',')
                
                fileOut.write("''" + ',' + "'" + myLine + "'" + "," + "''" + "," + "''" + "," + string + "'" + "," + "'" + string + "'" + "," )
                 
                fileOut.write("''" + "," + str(num) + ',' + "'https://storm.cs.uni.edu/~renbergm/?post_type=listing&#038;p=" + str(count) + "'" + "," + str(num) + ',' + "'listing'" + ',' + "''" + ',' + str(num) + ',') fileOut.write('\n')
                 
                fileOut.write(str(count + 1) + ',' + str(1) + ',' + "'" + string + "'" + "," + "'" + string + "'" + "," + "''" + "," )
                
                fileOut.write("'"+tuple1[num] + "'" + ',' + "''"+',' + "'inherit'"+","+"'open'" + "," + "'closed'"+",")
                
                fileOut.write("''"+','+"'"+str(count)+'-revision-v1'+"'"+","+"''"+","+"''"+","+string+"'"+","+"'"+string+"'"+",")
                
                fileOut.write("''"+","+str(count)+','+"'https://storm.cs.uni.edu/~renbergm/"+str(count)+'-revision-v1/'+"'"+","+str(num)+','+"'revision'"+','+"''"+','+str(num)+',') fileOut.write('\n')

                count = count + 1

            else:
                return '0'

            

def wp_geo(fileName):

        count=60
        
        inFile = csv.reader(open(fileName,'r'))
        
        fileOut = open('wp_geo.csv','w')
        
        num1 = 22
        num2 = 23
        
        for tuple1 in inFile:
            
            fileOut.write(str(count) + ',' + tuple1[num1] + ',' + tuple1[num2]) fileOut.write('\n')
            
            count = count + 1

        

def wp_term_rel(fileName):
    
        myDict = function("project-portion.csv")
        
        inFile = csv.reader(open(fileName,"r"))
        
        fileOut = open("wp_term_rel3.csv","w")
        
        num1 = 14
        count = 61
        
        for tuple1 in inFile:
            
            if tuple1[num1] in myDict:
                
                fileOut.write(str(count) + "," + str(myDict[tuple1[num1]]) + "," + str(0))
                
                fileOut.write("\n")
                
                count = count + 1

            

def wp_term_tax(fileName):
    
    inFile = csv.reader(open(fileName,"r"))
    
    out = open("wp_term_tax.csv","w")
    
    myDict = function("project-portion.csv")
    
    nextDict = {}

    ## reverse the key and value of the dictionary
    ## while 
    
    for key in myDict:
        if myDict[key] not in newDict:
            nextDict[myDict[key]] = key

    myDict1 = counter("project-portion.csv")
    count = 6

    var = str(count)
    
    for row in inFile:
        
        out.write( var + ',' + var + ',' + "'listing_category'" + ',' + "''" + ',' + str(0) + str( myDict1[newDict[count]] ) )
        out.write("\n")
        count = count + 1
        
        if count == 10700:
            break



        
def wp_postmeta(fileName):

    
        count1 = 281
        
        inFile = csv.reader(open(fileName,"r"))
        fileOut=open("wp_postmeta.csv","w")

        return1 = fileOut.write("\n")
        
        for sett in inFile:
            
            fout.write(str(count1) + ',' + str(57) + ',' + ',' + "'phone'" + ',' + "'" + sett[5] + "'" + ',')
            return1
            
            fout.write(str(count1+1) + ',' + str(57) + ',' + ',' + "'address'" + ',' + "'" + sett[1] + sett[2] + sett[3] + sett[4] + "'" + ',')
            return1
            
            fout.write(str(count1+2) + ',' + str(57) + ',' + ',' + "'website'" + ',' + "'" + sett[35] + "'" + ',')
            return1
            
            fout.write(str(count1+3) + ',' + str(57) + ',' + ',' + "'featured'" + ',' + str(0) + ',')
            return1
            
            fout.write(str(count1+4) + ',' + str(57) + ',' + ',' + "'featured-home'" + ',' + str(0) + ',')
            return1
            
            fout.write(str(count1+5) + ',' + str(57) + ',' + ',' + "'featured-cat'" + ',' + str(0) + ',')
            return1
            
            count1+=6

        

def function(f):
    
    inputFile = csv.reader( open(f,'r'))
    
    myDict = {}
    
    myList = list
    
    fourT = 14
    
    for line in inputFile:               ## use uniq to categories
        
        if line[fourT] not in myList:
            
            myList.append(line[fourT])
            
    myList.sort() 

    ## going through categories
    
    for index in range( 0, len(myList)):
        
        if myList[index] not in myDict:
            
            myDict[myList[index]] = index + 6
            
    return myDict





def counter(fileName):
    
        inFile = csv.reader(open(fileName,"r"))
        
        myDict = {}
        
        f = 14
        ## create dict to caculate number of time a categories got a new business
        for tuple1 in inFile:
            
            if tuple1[f] not in myDict:
                
                myDict[tuple1[f]] =  1

                ## ????

            else:
            myDict[row[f]] += 1
    return myDict






