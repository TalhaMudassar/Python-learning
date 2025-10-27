from pydantic import BaseModel,field_validator,model_validator

class User(BaseModel):
    username : str
    
    @field_validator('username')
    def username_length(cls,v):
        if len(v) < 4:
            raise ValueError("Username must be atleast four character")
        return v 
    
class Sign_up_field(BaseModel):
    password : str
    confirm_password : str
    
    @model_validator(BaseModel)
    def password_match(cls,values):
        if values.password != values.confirm_password:
            raise ValueError("password do not match")
        return values
        