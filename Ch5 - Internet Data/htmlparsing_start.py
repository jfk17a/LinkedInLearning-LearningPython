# 
# Example file for parsing and processing HTML
# LinkedIn Learning Python course by Joe Marini
#

from html.parser import HTMLParser

paragraphs = 0

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encoutered a comment:", data)
        pos = self.getpos()
        print("At line:", pos[0]," position",pos[1])

    def handle_starttag(self, tag, attrs):
        print("Encoutered a start tag:", tag)
        pos = self.getpos()
        print("At line:", pos[0]," position",pos[1])
        
        global paragraphs
        if tag == "p":
            paragraphs += 1

        if len(attrs) > 0:
            print("Attriputes:")
            for a in attrs:
                print("\t",a[0],"=",a[1])

    def handle_data(self, data):
        if data.isspace():
            return
        print("Encoutered text data:", data)
        pos = self.getpos()
        print("At line:", pos[0]," position",pos[1])

def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read() # read the entire file
        parser.feed(contents)    
    
    print("Paragraph tags:", str(paragraphs))

if __name__ == "__main__":
    main()
  