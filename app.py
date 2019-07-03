import pandas as pd
from flask import Flask, render_template, request

def get_details(state):
    df = pd.read_csv('StateUT_Capitals.csv')
    for i in range(36):
        if df['State/UT'][i].lower() == state:
            str1 = 'Capital is:' +df['Admin_Capital'][i]
            str2 = 'Lagislative Capital :' +df['Legislative_Capital'][i]
            if df['Former_Capital'][i] == 'None':
                str3 = 'No Former Capital'
            else:
                str3 = 'Former Capital is:' +df['Former_Capital'][i]
                return str1, str2, str3
            
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_rsp = request.args.get('msg')
    user_response = user_rsp.lower()
    flag=True
    while(flag==True):
        if(user_response!='bye'):
            if (user_response == 'hi' or user_response == 'hello' or user_response == 'hey'):
                return "ROBO : Hello!"
            else:
                if(user_response=='thanks' or user_response=='thank you' ):
                    flag=False
                    return "ROBO: You are welcome.."
                else:
                    if(user_response != None):
                        st1, st2, st3 = get_details(user_response)
                        return st1 +'\n'+ st2 +'\n'+ st3
                    else:
                        return "ROBO: Nothing Found"
        else:
            flag=False
            return "ROBO: Bye! take care.."

if __name__ == "__main__":
    app.run()