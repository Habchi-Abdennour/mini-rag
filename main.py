from fastapi import  FastAPI


app=FastAPI()


@app.get("/")
def welcome():
    return " msg : ok how can i help u !"