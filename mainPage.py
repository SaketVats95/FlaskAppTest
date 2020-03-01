from flask import Flask

app = Flask(__name__)

@app.route('/',defaults={'fileName': 'file1'})
@app.route('/<fileName>')
def index(fileName):
    #if True:
    fileName=fileName+'.txt' 
    return ''.join(readData(fileName))
    return "Hello, World!"

def readData(fileName,startLine=0,endLine=0):
    lines=[]
    with open('./data/'+fileName,encoding='utf8') as f:
        lines=f.read()
    print(lines) 
    if(startLine!=0 and endLine!=0):
        return lines[startLine:endLine]
    return lines

if __name__ == "__main__":
    readData('file1.txt')
    app.run(debug=True)


