from flask import Flask,render_template,request
import requests
from urllib.request import urlretrieve
import random
import json
from pprint import PrettyPrinter
from firebase import firebase

firebase = firebase.FirebaseApplication('https://movies-app-7a60e-default-rtdb.firebaseio.com/', None)




app=Flask(__name__)

@app.route('/' , methods=['GET', 'POST'])

def home():
    try:
        if request.method=="POST" :
            text1 = request.form["search1"]
            
            my_key="b21437b2"
            
            url = 'http://www.omdbapi.com/?apikey=b21437b2&t='+text1
            response=requests.get(url).json()

            pp=PrettyPrinter()
            # pp.pprint(response)
            img_url=response['Poster']
            title=response['Title']
            story=response['Plot']
            rating=response['imdbRating']
            director=response['Director']

            res= {'i_url':img_url,'title':title,'story':story,'rating':rating,'director':director}
            print(res)

        

            return render_template("home.html",res=res)
    except Exception as e:
        print()

        return "<h1>unable to find.....try later</h1>"   
   
    res= {'i_url':'','title':'','story':'','rating':'','director':''}   
    return render_template('home.html',res=res)

@app.route('/about',methods=['GET', 'POST'])
def about():


    # firebase = firebase.FirebaseApplication('https://movies-app-7a60e-default-rtdb.firebaseio.com/', None)
    response= firebase.get('', '')
    top5=list(response['id1'].split(',')) 

   

    return render_template('about.html',res=top5)









 


   

if __name__=='__main__':
    app.run(debug=True)