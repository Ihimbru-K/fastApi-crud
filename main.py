from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from models import Gender, Role, User, UserUpdateRequest


app = FastAPI()


db: list[User] = [


   User(
       id=uuid4(),
       first_name="Che",
       last_name= "John",
       middle_name="Neba",
       gender = Gender.male,
       roles=[Role.student]
    
   ),
   User(
       id=uuid4(),
       first_name="Awasum",
       last_name= "Berenice",
       middle_name="Njua",
       gender = Gender.female,
       roles=[Role.admin, Role.user]
    
   ),
   User(
       id=uuid4(),
       first_name="Tata",
       last_name= "Gloria",
       middle_name="Kah",
       gender = Gender.female,
       roles=[Role.student]
    
   ),
   User(
       id=uuid4(),
       first_name="Shey",
       last_name= "Max",
       middle_name="Neba",
       gender = Gender.male,
       roles=[Role.admin, Role.user]
    
   ),
   User(
       id=uuid4(),
       first_name="Mar",
       last_name= "John",
       middle_name="Chi",
       gender = Gender.male,
       roles=[Role.student]
    
   ),
   User(
       id=uuid4(),
       first_name="Ihimbru",
       last_name= "John",
       middle_name="Kanyimi",
       gender = Gender.male,
       roles=[Role.student]
    
   ),

]





@app.get("/")
async def root():
    return {"Hello": " Kboy"}


@app.get("/api/v1/users")
async def get_Users():
    return db



@app.post("/api/v1/users")
async def add_User(user : User):
    db.append(user)
    return {"id" : user.id}
    


# @app.delete("/api/v1/users/{user_id}")
# async def delete_user(user_id: UUID):
#     for user in db:
#         if user.id == user_id:
#             db.remove(user)
#             return
        


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted successfully"}
    return {"error": "User not found"}




@app.put("/api/v1/users/{user_id}")
async def modify_User(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return {"message": "User updated successfully", "user": user}
    
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exist"
    )
