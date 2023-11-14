from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

@api_view(['GET'])
def get_bosh(request):
       bosh = Bosh.objects.all()
       serialized_data = BoshSerializer(bosh, many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_ramaka(request):
       ramaka = Ramaka.objects.all()
       serialized_data = RamakaSerializer(ramaka, many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_komanda(request):
       komanda = Komanda.objects.all()
       serialized_data = KomandaSerializer(komanda, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_komanda_info(request):
       komanda_info = Komanda_info.objects.all()
       serialized_data = Komanda_infoSerializers(komanda_info, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_best(request):
       best = Best.objects.all()
       serialized_data = BestSerializers(best, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_video(request):
       video = Video.objects.all()
       serialized_data = VideoSerializers(video, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_reyting(request):
       reyting = Reyting.objects.all()
       serialized_data = ReytingSerializers(reyting, many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_player(request):
       player = Player.objects.all()
       serialized_data = PlayerSerializers(player, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_malumot_magazin(request):
       malumot_magazin = Malumot_magazin.objects.all()
       serialized_data = malumot_magazinSerializers(malumot_magazin, many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_bozor(request):
       bozor = Bozor.objects.all()
       serialized_data = BozorSerializers(bozor, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_stadium(request):
       stadium = Stadium.objects.all()
       serialized_data = StadiumSerializers(stadium, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_malumot(request):
       malumot = Malumot.objects.all()
       serialized_data = MalumotSerializers(malumot, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_frame(request):
       frame = Frame.objects.all()
       serialized_data = FrameSerializers(frame, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_cup(request):
       cup = Cup.objects.all()
       serialized_data = CupSerializers(cup, many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_jadval_malumot(request):
       jadval_malumot = Jadval_malumot.objects.all()
       serialized_data = Jadval_malumotSerializers(jadval_malumot, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_calendar(request):
       calendar = Calendar.objects.all()
       serialized_data = CalendarSerializers(calendar, many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_baho(request):
       baho = Baho.objects.all()
       serialized_data = BahoSerializers(baho, many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_vide(request):
       vide = Vide.objects.all()
       serialized_data = VideSerializers(vide, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_play(request):
       play = Play.objects.all()
       serialized_data = PlaySerializers(play, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_malumot_info(request):
       malumot_info = Malumot_info.objects.all()
       serialized_data = malumot_infoSerializers(malumot_info, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_bozar(request):
       bozar = Bozar.objects.all()
       serialized_data = BozarSerializers(bozar, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_img_stadium(request):
       img_stadium = Img_stadium.objects.all()
       serialized_data = Img_stadiumSerializers(img_stadium, many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_stadion(request):
       stadion = Stadion.objects.all()
       serialized_data = StadionSerializers(stadion, many=True).data
       return Response(serialized_data)
@api_view(['GET'])
def get_hamkor(request):
       hamkor = Hamkor.objects.all()
       serialized_data = HamkorSerializers(hamkor, many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_team(request):
       team = Team.objects.all()
       serialized_data = TeamSerializers(team, many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_leadership(request):
       leadership = Leadership.objects.all()
       serialized_data = LeadershipSerializers(leadership, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_coach(request):
       coach = Coach.objects.all()
       serialized_data = CoachSerializers(coach, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_info_club(request):
       info_club = Info_club.objects.all()
       serialized_data = Info_clubSerializers(info_club, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_club(request):
       club = Club.objects.all()
       serialized_data = ClubSerializers(club, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_advice(request):
       advice = Advice.objects.all()
       serialized_data = AdviceSerializers(advice, many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_akademiya(request):
       akademiya = Akademiya.objects.all()
       serialized_data = AkademiyaSerializers(akademiya, many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_activities(request):
       activities = Activities.objects.all()
       serialized_data = ActivitiesSerializers(activities, many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_my_shop(request):
       my_shop = My_shop.objects.all()
       serialized_data = My_shopSerializers(my_shop, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_shopping(request):
       shopping = Shopping.objects.all()
       serialized_data = ShoppingSerializers(shopping, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_img(request):
       img = Img.objects.all()
       serialized_data = ImgSerializers(img, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_maydonm(request):
       maydonm = Maydonm.objects.all()
       serialized_data = MaydonmSerializers(maydonm, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_maydon_t(request):
       maydon_t = Maydon_t.objects.all()
       serialized_data = Maydon_tSerializers(maydon_t, many=True).data
       return Response(serialized_data)


@api_view(['GET'])
def get_maydon_o(request):
       maydon_o = Maydon_o.objects.all()
       serialized_data = Maydon_oSerializers(maydon_o, many=True).data
       return Response(serialized_data)

@api_view(['GET'])
def get_maydon(request):
       maydon = Maydon.objects.all()
       serialized_data = MaydonSerializers(maydon, many=True).data
       return Response(serialized_data)
