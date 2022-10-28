from landings.api import router as landings_router
from ninja import NinjaAPI

api = NinjaAPI()
api.add_router("/", landings_router)


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


# from landings.models import Landing
# from ninja import ModelSchema


# class LandingSchemaIn(ModelSchema):
#     class Config:
#         model = Landing
#         model_exclude = ["id", "image", "likes", "hates"]


# class LandingSchemaOut(ModelSchema):
#     class Config:
#         model = Landing
#         model_fields = "__all__"


# @api.post("/landings")
# def landings(request, payload: LandingSchemaIn, image: UploadedFile = None):
#     landing = Landing.objects.create(image=image, **payload.dict())
#     return {"id": landing.id}


# @api.get("/landings", response=List[LandingSchemaOut])
# def landings(request):
#     qs = Landing.objects.all()
#     return qs
