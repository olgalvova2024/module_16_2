import uvicorn
from fastapi import FastAPI, Path


app = FastAPI()

@app.get("/")
async def home_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_page(user_id: int = Path(ge=1, le=100, description = 'Enter your id', example= '1') ):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
async def user_page_info(username: str = Path(max_length=20, min_length=5, description='Enter username', example='UrbanUser'),
                         age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> dict:
    return {"Информация о пользователе. Имя": username, "Возраст": age}

if __name__ == '__main__':
    uvicorn.run('module_16_2:app')
