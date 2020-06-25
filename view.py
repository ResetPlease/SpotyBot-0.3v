from flask import render_template, request, make_response, redirect, json
#from flask_mysqldb import MySQL
from __init__ import app
import time
import threading
from spotibot import SpotifyC


base = "http://1e2ae66ec27c.ngrok.io/"
narmal = "http://localhost:5000/"
global_data_id = 0
login = "Andrey"
password = "Qwerty112233"

data_G = [] 
#{"id":global_data_id,"login":'asd', "password":"asd",
#            'first_t':"asd", "second_t":"asd", "limit":"asd", "link":"asd", "status":"200"},
#            {"id":global_data_id+1,"login":"123", "password":"123",
#            'first_t':"123", "second_t":"123", "limit":"123", "link":"123", "status":"300"}

def listen(id,log_sp="arnold2020@gmail.com", pass_sp="Qwerty112233", link_sp="https://open.spotify.com/album/1fQL5ZynvGJmJAybF0SwvT?si=m80eYaZoSve67eTFHdaQOA"):
    try:
        chrome = SpotifyC(proxy = [True,"185.174.101.253:4045"])
        chrome.driver.get(link_sp)
        chrome.LogIn(login_sp = log_sp, password_sp = pass_sp)
        chrome.driver.implicitly_wait(15)
        elem = chrome.driver.find_element_by_class_name("_11f5fc88e3dec7bfec55f7f49d581d78-scss")
        forward = chrome.driver.find_element_by_xpath("//button[@data-testid='control-button-skip-forward']")
        chrome.driver.execute_script("arguments[0].click();", elem)
        val=0
        while val!=10:
            slp = random.randint(40,60)
            #print(slp,"\n")
            time.sleep(slp)
            chrome.driver.execute_script("arguments[0].click();", forward)
            val+=1
        chrome.driver.close()
        for i in data_G:
            if i["id"] == id:
                i['status'] ="300" #status 300 is ok
        return "ok"
    except:
        for i in data_G:
            if i["id"] == id:
                i['status'] ="500" #status 500 is error
        return "error"

@app.route('/signin',methods=['post', 'get'])
def admin_login():
    if request.method == "POST":
        log_in = request.form['username']
        passw = request.form['password']
        if(log_in == login and passw==password):
            res = make_response('./')
            res.set_cookie('auth',"aPgGfGHJL6uwR0BudTwmj5kY",60*60*24)
            return res
        else:
            return "Err:login_pass_error"
    return render_template("adminlogin.html")

@app.route('/addbot', methods=['post'])
def AddBot():
    if request.method == "POST":
        try:
            global global_data_id
            data_G.append({"id":global_data_id,"login":request.form['login'], "password":request.form['password'],
            'first_t':request.form['first_t'], "second_t":request.form['second_t'], "limit":request.form['listen'], "link":request.form['link'], "status":"200"})
            x = threading.Thread(target=listen, args=(global_data_id,request.form['login'],request.form['password'],request.form['link'],))
            x.start()
            #print(data_G)
            global_data_id+=1
            return "ok"    
        except:
            return "soso"
    return "ass"
    

@app.route('/', methods=['post', 'get'])
def profiles():
    try:
        if(request.cookies['auth']=='aPgGfGHJL6uwR0BudTwmj5kY'):
            return render_template("adminpanel.html", data = data_G)
    except:
        return render_template("redirect.html", redirect="./signin")

@app.route('/setup', methods=['post', 'get'])
def SetupPage():
    try:
        if(request.cookies['auth']=='aPgGfGHJL6uwR0BudTwmj5kY'):
            return render_template("setup.html", data = data_G)
    except:
        return render_template("redirect.html", redirect="./signin")

@app.route('/addSetUp', methods=['post'])
def addSetUp():
    return "ok"