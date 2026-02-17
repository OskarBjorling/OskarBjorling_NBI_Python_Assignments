class SafeStorage:
    __data = None
    def get(self):
        return self.__data
    def put(self,data):
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda")
x=safe.get()
safe.put("boaorm")
y=safe.get()
print(x,y)