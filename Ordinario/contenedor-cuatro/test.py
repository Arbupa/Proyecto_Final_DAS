from sqlalchemy.sql.elements import Null


var = Null
if var is not Null:
    print("hay algo")
else:
    print("el valor es nulo")