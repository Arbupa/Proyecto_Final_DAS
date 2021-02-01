class UniqueVar():
    def __init__(self, last_search) -> None:
        self.last_search = last_search

instan = UniqueVar("")

def hola(instan):
    instan.last_search = "asdasd"
    a = instan.last_search
    return a
def adios(instan):
    b = instan.last_search = "adios"
    return b

print(hola(instan))
print(adios(instan))
print(instan.last_search)    
instan.last_search = ":0"
print(instan.last_search)