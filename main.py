from fastapi import  FastAPI


app=FastAPI()


@app.get("/hi")
def msg():
    return " msg : ok how can i help u !"