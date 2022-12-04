from flask import Flask, render_template,request
from datetime import datetime
start = None
end = None
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/uploaded',methods=['GET','POST'])
def uploaded():
    if request.method == 'POST':
        f = request.files['file']
        
        f.filename="whatsapp.txt"
        f.save(f.filename)
        from analysis2 import p,neg,neu,dataInsights
        l = []
        l.append(p)
        l.append(neu)  
        # print(l)
        context = {'analysis': dataInsights()}
        return render_template('Analysis.html',text=l,context=context)
    # return render_template('Analysis.html',{'sent':l})
    # return render_template('Analysis.html')

@app.route('/range',methods=['GET','POST'])
def range():  
    if request.method == 'POST':
        start = request.form['start-date']
        print(start)
        end= request.form['end-date']
        print(end)
    return render_template('range.html')
        
    

if __name__=="__main__":
    app.run(debug=True)
