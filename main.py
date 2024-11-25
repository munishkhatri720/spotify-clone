from fastapi import FastAPI
from api.v1 import streams


app = FastAPI(debug=True)
app.include_router(streams.router , prefix="/v1/streams")

@app.get('/')
async def home():
    return "Hello World"




if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app' , host="0.0.0.0" , port=8000)

