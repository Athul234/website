from flask import Flask, render_template, jsonify

app = Flask(__name__)


jobs=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'bengaluru',
    'salary':'1000000'
  },
  {
    'id':2,
    'title':'Data sumn',
    'location':'bengaluru',
    'salary':'1003000'
  },
  {
    'id':3,
    'title':'some Analyst',
    'location':'bengaluru',
    'salary':'2100000'
  }
]

@app.route("/")
def hello_world():
    return render_template("home.html",
                           job=jobs,comp_name='haha')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug ='True')