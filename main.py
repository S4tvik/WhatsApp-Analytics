from flask import Flask, render_template,request

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
        
if __name__=="__main__":
    app.run(debug=True)
