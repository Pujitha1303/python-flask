from flask import Flask,render_template ,jsonify

app=Flask(__name__)

JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru,India',
        'salary':'Rs 10,10000'
    },

      {
        'id':2,
        'title':'Data Scientist',
        'location':'Delhi,India',
        'salary':'Rs 20,10000'
    },
      {
        'id':3,
        'title':'Frontend Developer',
        'location':'Khammam,India',
        'salary':'Rs 30,10000'
    },
      {
        'id':4,
        'title':'Backend',
        'location':'USA',
    }

]
@app.route("/")
def index():
    return render_template('home.html', jobs=JOBS , title='boat-page')

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__=="__main__":
    app.run(port=8001,debug=True)

# print(__name__)
