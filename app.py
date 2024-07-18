from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("login1.html")
#rounting "/login"-login page
#database:username/password
database={"ram":"ram@123","raj":"raj@123","ravi":"ravi@123"}
@app.route("/form_login",methods=["POST","GET"])
def form_login():
    if request.method=="POST":
        name1=request.form['username']#chandra
        password1=request.form["password"]
        if name1 not in database:
            return render_template("login1.html",info="Invalid User")
        else:
            if database[name1]!=password1:
                return render_template("login1.html",info="Invalid password")
            else:
                return render_template("home1.html",name=name1)
    return render_template("login1.html")
#main program
if __name__=="__main__":
    app.run(debug=True)        
