from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
      return {"message": "Hello AI510 @ CityU in Summer of 2024 from Teagan Scharlau!"}