# from fastapi import FastAPI, File, UploadFile,Form
import uvicorn
import jwt
from flask import Flask,request
# from decouple import config
from pydantic import BaseModel




class Item(BaseModel):
    my_value : str

class na_item(BaseModel):
    u_name:str
    pas_wo:str

app = Flask(__name__)

@app.route("/sing_up" ,methods=['GET','POST'])
def sign():
    try:
          name = request.args.get("name")
          pas = request.args.get("pas")
          print(name,pas)
          payload = {
                      "user_id": name,
                      "password": pas,
                  }

          JWT_SECRET = "secret"
          JWT_ALGORITHM = "HS256"
          Hmis_token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

          return {"result": Hmis_token}
    except Exception as e:
          return {"Success": "false", "Result": str(e)}


@app.route("/decode_tock",methods=['GET','POST'])
def tock():

    try:
        my_value = request.args.get("my_value")
        print(my_value)

        token_va = Item(my_value= my_value)
        token = token_va.my_value
        JWT_SECRET = "secret"
        JWT_ALGORITHM = "HS256"
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if decoded_token :
            text = "Welcome to AIMP"
            return {"result": text}
    except Exception as e:
        return { "result":str(e) }
        # return "ok"
    # except Exception as e:
    #         return { "result":str(e) }



if __name__ == '__main__':
    app.run(debug=True)

