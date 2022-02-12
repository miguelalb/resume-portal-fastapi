from app.exceptions import Exc
from sqlalchemy.orm import Session


def create_generic_profile_child(db: Session, model, object_in, profile_id: str):
    model_obj = model(**object_in.dict())
    db.add(model_obj)
    model_obj.profile_id = profile_id
    db.commit()


def delete_generic(db: Session, model, obj_id: str):
    model_obj = db.query(model).filter(model.id == obj_id).first()
    if model_obj is None:
        raise Exc.ObjectNotFoundException("Object")
    db.delete(model_obj)
    db.commit()
