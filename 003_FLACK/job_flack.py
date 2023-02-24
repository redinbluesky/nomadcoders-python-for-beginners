from flask import Flask, render_template, request, redirect, send_file
from extractors.wwr import extract_wwr_job
from file import save_to_file

app = Flask(__name__)

db = {}
@app.route("/")
def home():
    return render_template("home.html",name='nico')

@app.route("/search")
def hello():
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = extract_wwr_job(keyword)
        db[keyword] = jobs
    return render_template("search.html",keyword=keyword,jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword,db[keyword])
    return send_file(f"{keyword}.csv",as_attachment=True)

app.run("127.0.0.1")