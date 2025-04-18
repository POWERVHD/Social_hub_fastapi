from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlmodel import Session, select
from .. import schemas, models, oauth2
from ..database import get_session


router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(get_session), current_user: int = Depends(oauth2.get_current_user)):

    post = db.exec(select(models.Vote).where(models.Post.id == vote.post_id)).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The post with {vote.post_id} Does not exist")


    vote_query = db.exec(select(models.Vote).where(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id))

    found_vote = vote_query.first()
    
    if(vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has already voted on {vote.post_id}")
        
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()

        return {"msg":"Sucessfully Liked"}
    
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist")
        
        db.delete(found_vote)
        db.commit()

        return {"msg": "Sucessfully Unliked"}
