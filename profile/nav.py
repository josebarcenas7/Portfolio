import os

def get_names():
    names = []
    files = os.listdir("template/")
    files.remove('base.html')
    print "-------", files
    #move index to the front of the list, so it's always in the first position
    #of the nav bar
    index1 = files.index("index.html")
    files.insert(0,files.pop(index1))
    #move contact to the end of the list, so it's always in the last position
    #of the nav bar
    index2 = files.index("contact.html")
    files.insert(len(files), files.pop(index2))

    print "-------", files

    for n in files:
        #remove .html from every file to clean up the text
        n = n[:-5]
        #capitalize the first letter to further clean up the text
        n = n.capitalize()
        #add the formated string to the names array
        names.append(n)
    #we know that index is at the front, however we want to rename it to "Home"
    names[0]="Home"
    #combine lists to make one that will be easier to use in Jinja
    newfile=zip(files,names)
    print newfile
    return newfile;
