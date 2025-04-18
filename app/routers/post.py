from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import  List, Optional,Literal
from sqlmodel import Session, select, func
from .. import models,schemas, oauth2
from .. database import get_session

from ..models import Post

router = APIRouter(
    prefix = "/posts",
    tags = ["POST"]
)


# @router.get("/", response_model=List[schemas.PostResponse])
@router.get("/", response_model=List[schemas.PostOut])
def get_post(db: Session = Depends(get_session),current_user: int = Depends(oauth2.get_current_user),limit:int = 10, skip: int = 0, search: Optional[str]=""):       # type: ignore

    # cursor.execute("""SELECT * FROM posts""") # Regular RAW SQL fetch
    # posts = cursor.fetchall()
    
    #posts = db.exec(select(models.Post).where(models.Post.owner_id == current_user.id)).all()  # For Only Access the owner posts not all posts
    
    #posts = db.exec(select(models.Post).limit(limit).offset(skip).where(models.Post.title.contains(search))).all()   # For only accessing all the posts without vote

    stmt = (select(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
            .group_by(models.Post.id).limit(limit).offset(skip).where(models.Post.title.contains(search)))
    results = db.exec(stmt).all()


    return results
    


@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(post: Post , db: Session = Depends(get_session),current_user = Depends(oauth2.get_current_user)): # type: ignore


    # cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s,%s,%s) RETURNING * """, (post.title,post.content,post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    
    new_post = models.Post(owner_id=current_user.id , **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post 



@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id :int, db: Session = Depends(get_session),current_user = Depends(oauth2.get_current_user)):

    # cursor.execute(""" SELECT * from posts WHERE id = %s """ , (str(id),))
    # post = cursor.fetchone()

    # post = db.exec(select(models.Post).where(models.Post.id == id)).first()

    post = (select(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
            .where(models.Post.id == id).group_by(models.Post.id))
    
    post_first = db.exec(post).first()

    if not post_first:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} not found")

    return post_first



@router.delete("/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def del_post(id : int, db: Session = Depends(get_session),current_user = Depends(oauth2.get_current_user)):

    # cursor.execute(""" DELETE FROM posts WHERE id = %s returning * """,(str(id),))
    # del_post = cursor.fetchone()
    # conn.commit()

    post = db.exec(select(models.Post).where(models.Post.id == id)).first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    
    db.delete(post)
    db.commit()
        
    return Response(status_code=status.HTTP_204_NO_CONTENT)




@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id: int, updated_post: models.Post, db: Session = Depends(get_session),current_user = Depends(oauth2.get_current_user)):

    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *  """ , 
    #                (post.title, post.content, post.published,str(id),)
    #                )
    # updated_post = cursor.fetchone()
    # conn.commit()

    post_cmd = db.exec(select(models.Post).where(models.Post.id == id)).first()

    if post_cmd == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    if post_cmd.owner_id !=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    
    update_data = updated_post.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(post_cmd, key, value)
    

    db.commit()
    db.refresh(post_cmd)
    
    return post_cmd






