from typing import List

from django.db.models import Count, Exists, OuterRef
from ipware import get_client_ip
from ninja import ModelSchema, Router

from landings.models import Hate, Landing, Like

router = Router()


class LikeSchemaOut(ModelSchema):
    class Config:
        model = Like
        model_fields = "__all__"


class HateSchemaOut(ModelSchema):
    class Config:
        model = Hate
        model_fields = "__all__"


class LandingSchemaIn(ModelSchema):
    class Config:
        model = Landing
        model_exclude = ["id", "image"]


class LandingSchemaOut(ModelSchema):
    num_likes: int
    num_hates: int
    user_has_liked: bool
    user_has_hated: bool

    # @staticmethod
    # def resolve_likes(obj):
    #     return obj.like_set.count()

    # @staticmethod
    # def resolve_hates(obj):
    #     return obj.like_set.count()

    class Config:
        model = Landing
        model_fields = "__all__"


# @router.post("/landings")
# def create_landing(request, payload: LandingSchemaIn, image: UploadedFile = None):
#     landing = Landing.objects.create(image=image, **payload.dict())
#     return {"id": landing.id}


@router.get("/landings", response=List[LandingSchemaOut])
def list_landings(request):
    client_ip, is_routable = get_client_ip(request)
    print(client_ip)
    qs = (
        Landing.objects.all()
        .annotate(
            user_has_liked=Exists(Like.objects.filter(landing=OuterRef("pk"), ip=client_ip)),
            user_has_hated=Exists(Hate.objects.filter(landing=OuterRef("pk"), ip=client_ip)),
            num_likes=Count("likes", distinct=True),
        )
        .annotate(num_hates=Count("hates", distinct=True))
    )
    return qs


@router.post("/landings/{id}/likes")
def like_landing(request, id: int):
    client_ip, is_routable = get_client_ip(request)
    print(client_ip)
    if Like.objects.filter(landing_id=id, ip=client_ip).exists():
        return {"detail": "이미 좋아요를 누르셨습니다"}
    else:
        Like.objects.create(landing_id=id, ip=client_ip)
    return {"success": True}


@router.post("/landings/{id}/hates")
def hate_landing(request, id: int):
    client_ip, is_routable = get_client_ip(request)
    print(client_ip)
    if Hate.objects.filter(landing_id=id, ip=client_ip).exists():
        return {"detail": "이미 별로요를 누르셨습니다"}
    else:
        Hate.objects.create(landing_id=id, ip=client_ip)
    return {"success": True}


@router.delete("/landings/{id}/likes")
def delete_like_landing(request, id: int):
    client_ip, is_routable = get_client_ip(request)
    print(client_ip)
    if not Like.objects.filter(landing_id=id, ip=client_ip).exists():
        return {"detail": "이미 좋아요를 취소했습니다"}
    else:
        Like.objects.filter(landing_id=id, ip=client_ip).delete()
    return {"success": True}


@router.delete("/landings/{id}/hates")
def delete_hate_landing(request, id: int):
    client_ip, is_routable = get_client_ip(request)
    print(client_ip)
    if not Hate.objects.filter(landing_id=id, ip=client_ip).exists():
        return {"detail": "이미 별로요를 취소했습니다"}
    else:
        Hate.objects.filter(landing_id=id, ip=client_ip).delete()
    return {"success": True}
