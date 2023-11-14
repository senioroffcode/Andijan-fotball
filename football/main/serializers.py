from rest_framework import serializers
from .models import *

class BoshSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bosh
        fields = "__all__"

class RamakaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ramaka
        fields = '__all__'

class KomandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Komanda
        fields = "__all__"

class Komanda_infoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Komanda_info
        fields = "__all__"

class BestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Best
        fields = "__all__"

class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class ReytingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reyting
        fields = "__all__"


class PlayerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class Malumot_magazinSerializers(serializers.ModelSerializer):
    class Meta:
        model = Malumot_magazin
        fields = "__all__"

class BozorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bozor
        fields = "__all__"


class StadiumSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = "__all__"

class MalumotSerializers(serializers.ModelSerializer):
    class Meta:
        model = Malumot
        fields = "__all__"

class FrameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Frame
        fields = "__all__"

class CupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cup
        fields = "__all__"

class Jadval_malumotSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jadval_malumot
        fields = "__all__"

class CalendarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = "__all__"

class BahoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Baho
        fields = "__all__"

class VideSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vide
        fields = "__all__"

class PlaySerializers(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = "__all__"

class Malumot_infoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Malumot_info
        fields = "__all__"


class BozarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bozar
        fields = "__all__"

class Img_stadiumSerializers(serializers.ModelSerializer):
    class Meta:
        model = Img_stadium
        fields = "__all__"

class StadionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stadion
        fields = "__all__"


class HamkorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hamkor
        fields = "__all__"


class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class LeadershipSerializers(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = "__all__"

class CoachSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"

class Info_clubSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info_club
        fields = "__all__"

class ClubSerializers(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"

class AdviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Advice
        fields = "__all__"

class AkademiyaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Akademiya
        fields = "__all__"

class ActivitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = "__all__"

class My_shopSerializers(serializers.ModelSerializer):
    class Meta:
        model = My_shop
        fields = "__all__"

class ShoppingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shopping
        fields = "__all__"

class ImgSerializers(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = "__all__"

class MaydonmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Maydonm
        fields = "__all__"

class Maydon_tSerializers(serializers.ModelSerializer):
    class Meta:
        model = Maydon_t
        fields = "__all__"

class Maydon_oSerializers(serializers.ModelSerializer):
    class Meta:
        model = Maydon_o
        fields = "__all__"

class MaydonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Maydon
        fields = "__all__"

