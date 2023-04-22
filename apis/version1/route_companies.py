from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.typing import List
from sqlalchemy.orm import Session

from db.repository.companies import create_new_company, retreive_company, list_companies, update_company_by_id, \
    delete_company_by_id
from schemas.companies import CompanyCreate, CompanyShow
from session import get_db

router = APIRouter()


@router.post("/create-company")
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    company = create_new_company(company=company, db=db)
    return company


@router.get("/get/{id}", response_model=CompanyShow)
def read_company(id: int, db: Session = Depends(get_db)):
    company = retreive_company(id=id, db=db)
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"company with this id {id} does not exist")
    return company


@router.get("/all", response_model=List[CompanyShow])
def read_companies(db: Session = Depends(get_db)):
    companies = list_companies(db=db)
    return companies


@router.put("/update/{id}")
def update_company(id: int, company: CompanyCreate, db: Session = Depends(get_db)):
    message = update_company_by_id(id=id, company=company, db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"company with id {id} not found")
    return {"msg": "Successfully updated data."}


@router.delete("/delete/{id}")
def delete_company(id: int, db: Session = Depends(get_db)):
    message = delete_company_by_id(id=id, db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"company with id {id} not found")
    return {"msg": "Successfully deleted."}
