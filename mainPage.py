from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    #if True: 
    return ''.join(readData('file1.txt'))
    return "Hello, World!"

def readData(fileName,startLine=0,endLine=0):
    lines=[]
    with open('./data/'+fileName,'r') as f:
        lines=f.read().split('\n')
    #print(lines) 
    if(startLine!=0 and endLine!=0):
        return lines[startLine:endLine]
    return lines

if __name__ == "__main__":
    readData('file1.txt')
    app.run(debug=True)


