from App.Http.Controllers.Controller import Controller

from fastapi import Depends, Form, Security
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from App.Http.Models.User import User
from App.Http.Providers.AuthServiceProvider import AuthServiceProvider
from datetime import datetime

from App.Http.RequestForms.Auth import LoginForm, RegisterForm, Token


class Auth(Controller):

    # def __init__(self):
        # self.db = super().db
        # self.user = User()
        # pass
   
    


    async def login(self, form_data: LoginForm.LoginForm):
        return await AuthServiceProvider().login_for_access_token(form_data)
    
    def register(self, user_form: RegisterForm.RegisterForm):
        if(user_form.password == user_form.c_password):
            password_hash = AuthServiceProvider().get_password_hash(user_form.password)

            payload = {
                'name' : user_form.name,
                'second_name' : user_form.second_name,
                'email' : user_form.email,
                'password' : password_hash,
                'status' : 'active',
                'role' : 'user',
                'deleted_at' : None,
                'created_at' : datetime.now(),
                'updated_at' : None,
            }


            user = User(payload)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)

            return {
                'msg':{
                    'success':'user registered Successfully!',
                },
                'user':user
            }
        
    # async def user(self, token: Token.Token):
    #     return await AuthServiceProvider().get_current_user(token.token)
    # def user(self, token: Token.Token = Depends(AuthServiceProvider.get_current_token)):
    #     # return token
    #     return  AuthServiceProvider().get_current_user(token)

        
