#!/usr/bin/python3
if __name__ == "__main__":
    import datetime
    import uuid

    class BaseModel:
        def __init__(self, id=None, name=None, my_number=0, *args, **kwargs):
            self.id = id if id is not None else str(uuid.uuid4())
            self.cName = __class__.__name__
            self.name = name
            self.created_at = datetime.datetime.now()
            self.update_at = datetime.datetime.now()
            self.my_number = my_number

        def __str__(self):
            return f"[{self.cName}] ({self.id}) {self.to_dict1()}"

        def save(self):
            self.update_at = datetime.datetime.now()

        def to_dict(self):
            new_dict = {}
            for i in self.__dict__:
                if i == "cName":
                    continue
                new_dict[i] = getattr(self, i)
            new_dict["__class__"] = self.cName
            return new_dict

        def to_dict1(self):
            new_dict = {}
            for i in self.__dict__:
                if i == "cName":
                    continue
                new_dict[i] = getattr(self, i)
            return new_dict

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
