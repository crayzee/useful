from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.app.base.utils import generate

from . import schemas, crud



def create_social_account(db: Session, profile: schemas.SocialAccount):
    if crud.social_account.exists(db, account_id=profile.account_id):
        #raise HTTPException(status_code=400, detail="The account exists")
        account = crud.social_account.get(db, account_id=profile.account_id)
        return account.user
    # TODO add check user exists
    new_user = schemas.UserCreate(
        username=generate.generate_name(profile.account_login),
        email='soc@gmail.com',
        password=generate.generate_pass(),
        first_name='test_name',
        is_active=True, 
        avatar=profile.avatar_url
    )     
    user = crud.user.create(db, schema=new_user)
    prof = profile.dict(exclude={"avatar_url"}) 
    crud.social_account.create(db, schema=prof, user_id=user.id)
    return user