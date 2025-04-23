from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal

class Student(BaseModel):
    name: str = Field(description="The name of the student")
    age: int = Field(gt=0, lt=25, description="The age of the student")
    height: float = Field(gt=0, lt=272, description="The height of the student")
    weight: float = Field(gt=0, description="The weight of the student")
    is_married: Optional[bool] = Field(default=False, description="Whether the student is married or not")
    is_graduated: bool = Field(default=False, description="Whether the student is graduated or not")
    email: Optional[EmailStr] = Field(default=None, description="The email of the student.")
    blood_group: Optional[Literal["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]] = Field(default=None, description="The blood group of the student")
    grade: int = Field(gt=0, lt=13, description="The class in which the student studies")
    section: Optional[Literal["A", "B", "C", "D"]] = Field(default="A", description="The section in which the student studies")
    cgpa: float = Field(ge=0.00, le=4.00, description="The total grade point average of the student.")
    phone_number: Optional[str] = Field(default=None, description="The phone number of the student.")


huzaifa = {
    'name' : "Huzaifa",
    "age" : 22,
    "height" : 176.2,
    "weight" : 59.75,
    "is_married" : False,
    "is_graduated" : True,
    "grade" : 12,
    "section" : "A",
    "cgpa" : 4.00,
    "phone_number" : "0506-1234-56-78"
}

huzaifa = Student(**huzaifa)


print(huzaifa.name)
print(huzaifa.age)
print(huzaifa.height)
print(huzaifa.is_married)
print(huzaifa.email)
print(huzaifa.grade)
print(huzaifa.section)
print(huzaifa.cgpa)
    
json_dict = huzaifa.model_dump_json()
print(json_dict)
