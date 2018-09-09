from data_bases.DBManager import DBManager
from data_bases.User import User

DBManager.instance().create()
vasiaUser = User("Vasiliy", "Pypkin", "president", "qwert@gmail.com")
DBManager.instance().session.add(vasiaUser)
ourUser = DBManager.instance().session.query(User).filter_by(name="Vasiliy").first()
print(ourUser)
