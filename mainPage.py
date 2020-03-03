from flask import Flask,request
import codecs

app = Flask(__name__)

#http://10.1.1.1:5000/file1?startLineNumber=10&endLineNumber=20
@app.route('/',defaults={'fileName': 'file1'})
@app.route('/<fileName>')
def index(fileName):
    #if True:
    startLine,endLine = 0 , 0  
    try:
        startLine = int(request.args.get('startLineNumber'))
        endLine = int(request.args.get('endLineNumber'))
    except Exception as e:
        print('start and end not provided by user')
    fileName=fileName+'.txt' 
    return "<pre>"+'\n'.join(readData(fileName,startLine,endLine+1))+"</pre>"
    

def readData(fileName,startLine=0,endLine=0):
    lines=[]
    with open('./data/'+fileName,encoding='utf8',errors='ignore') as f:
        lines=f.read().split('\n')
    print(lines) 
    if(startLine!=0 and endLine!=0):
        if(startLine<0 or endLine>len(lines)):
            return "Provided start Line number or end Line Number is not present in {0}".format(fileName)
        return lines[startLine:endLine]
    return lines

def readData_HavingDiffLanguage(fileName,startLine=0,endLine=0):
    lines=[]
    with codecs.open('./data/'+fileName,'r',encoding='cp720',error='ignore') as f:
        for line in f:
            lines.append(line)
    print(lines) 
    if(startLine!=0 and endLine!=0):
        if(startLine<0 or endLine>len(lines)):
            return "Provided start Line number or end Line Number is not present in {0}".format(fileName)
        return lines[startLine:endLine]
    return lines
if __name__ == "__main__":
    app.run(debug=True)





