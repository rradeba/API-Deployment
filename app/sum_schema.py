from flask_marshmallow import Marshmallow
from app.sum import Sum

ma = Marshmallow()

class SumSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Sum
    id = ma.auto_field()
    num1 = ma.auto_field()
    num2 = ma.auto_field()
    result = ma.auto_field()


