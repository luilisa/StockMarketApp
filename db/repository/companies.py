from sqlalchemy.orm import Session

from db.models.companies import Companies
from schemas.companies import CompanyCreate


def create_new_company(db: Session, company: CompanyCreate):
    company = Companies(company_name=company.company_name,
                        symbol=company.symbol,
                        sector=company.sector)
    db.add(company)
    db.commit()
    db.refresh(company)
    return company


def retreive_company(id: int, db: Session):
    item = db.query(Companies).filter(Companies.id == id).first()
    return item


def list_companies(db: Session):
    companies = db.query(Companies).all()  #filter(News.pub_date == datetime.now().date())
    return companies


def update_company_by_id(id: int, company: CompanyCreate, db: Session):
    existing_company = db.query(Companies).filter(Companies.id == id)
    if not existing_company.first():
        return 0
    existing_company.update(company.__dict__)
    db.commit()
    return 1


def delete_company_by_id(id: int, db: Session):
    existing_company = db.query(Companies).filter(Companies.id == id)
    if not existing_company.first():
        return 0
    existing_company.delete(synchronize_session=False)
    db.commit()
    return 1
