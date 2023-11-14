from django.db import models


class Bosh(models.Model):
    tg = models.URLField()
    fb = models.URLField()
    youtube = models.URLField()
    logo = models.ImageField(upload_to='Bosh/')
    number = models.IntegerField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='Bosh/')
    data = models.DateField()


class Ramaka(models.Model):
    title = models.TextField()
    photo = models.ImageField(upload_to='Ramaka/')


class Komanda(models.Model):
    photo = models.ImageField(upload_to='Komanda/')
    title = models.TextField()
    data = models.DateField()


class Komanda_info(models.Model):
    name = models.CharField(max_length=200)
    bal = models.IntegerField()
    logo = models.ImageField(upload_to='Komanda_info/')


class Best(models.Model):
    top = models.CharField(max_length=100)
    data = models.DateField()
    Komanda_info = models.ManyToManyField(Komanda_info)


class Video(models.Model):
    photo = models.ImageField(upload_to='Video/')
    name = models.CharField(max_length=200)
    video = models.URLField()


class Reyting(models.Model):
    logo = models.ImageField(upload_to='Reyting/')
    name = models.CharField(max_length=200)
    oyin = models.IntegerField()
    gol = models.IntegerField()
    durrang = models.IntegerField()
    maglubiyat = models.IntegerField()
    tf = models.IntegerField()
    ball = models.IntegerField()


class Player(models.Model):
    photo = models.ImageField(upload_to="Player/")
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    orni = models.CharField(max_length=300)
    game = models.IntegerField()
    start = models.IntegerField()
    sap = models.IntegerField()
    minuts = models.IntegerField()


class Malumot_magazin(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='malumot_magazin/')


class Bozor(models.Model):
    team_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)


class Stadium(models.Model):
    name = models.CharField(max_length=200)
    tex = models.TextField()
    place = models.IntegerField()


class Malumot(models.Model):
    logo = models.ImageField(upload_to='Malumot/')
    number = models.IntegerField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='Malumot/')
    data = models.DateField()
    tg = models.URLField()
    fb = models.URLField()
    youtube = models.URLField()


class Frame(models.Model):
    title = models.TextField()
    photo = models.ImageField(upload_to='frame/')


class Cup(models.Model):
    photo = models.ImageField(upload_to='Cup/')
    title = models.TextField()
    data = models.DateField()


class Jadval_malumot(models.Model):
    name = models.CharField(max_length=200)
    ball = models.IntegerField()
    logo = models.ImageField(upload_to='jadval_malumot/')


class Calendar(models.Model):
    top = models.CharField(max_length=100)
    data = models.DateField()
    jadval_malumot = models.ManyToManyField(Jadval_malumot)


class Baho(models.Model):
    logo = models.ImageField(upload_to='Baho/')
    name = models.CharField(max_length=200)
    play = models.IntegerField()
    gol = models.IntegerField()
    durrang = models.IntegerField()
    defeat = models.IntegerField()
    tf = models.IntegerField()
    ball = models.IntegerField()


class Vide(models.Model):
    photo = models.ImageField(upload_to='Vide/')
    name = models.CharField(max_length=200)
    video = models.URLField()


class Play(models.Model):
    photo = models.ImageField(upload_to="Play/")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    pasition = models.CharField(max_length=200)
    geyms = models.IntegerField()
    start = models.IntegerField()
    sap = models.IntegerField()
    minuts = models.IntegerField()


class Malumot_info(models.Model):
    name = models.CharField(max_length=220)
    photo = models.ImageField(upload_to='malumot_info/')


class Bozar(models.Model):
    photo = models.ImageField(upload_to='Bozar/')
    command_name = models.CharField(max_length=200)
    name = models.CharField(max_length=220)


class Img_stadium(models.Model):
    photo = models.ImageField(upload_to='Img_stadium/')


class Stadion(models.Model):
    name = models.CharField(max_length=220)
    tex = models.TextField()
    size = models.IntegerField()
    sector = models.IntegerField()
    locations = models.CharField(max_length=300)
    number = models.IntegerField()
    photo = models.ManyToManyField(Img_stadium)


class Hamkor(models.Model):
    photo = models.ImageField(upload_to='Hamkor/')


class Team(models.Model):
    name = models.CharField(max_length=220)
    photo = models.ImageField(upload_to='Team/')


class Leadership(models.Model):
    name = models.CharField(max_length=220)
    photo = models.ImageField(upload_to='leadership/')


class Coach(models.Model):
    photo = models.ImageField(upload_to='Coach/')
    name = models.CharField(max_length=220)
    first_name = models.CharField(max_length=220)
    tex = models.TextField()


class Info_club(models.Model):
    tex = models.TextField()
    icon = models.CharField(max_length=200)


class Club(models.Model):
    photo = models.ImageField(upload_to='Club/')
    title = models.CharField(max_length=200)
    info = models.ManyToManyField(Info_club)
    tex = models.TextField()
    photo2 = models.ImageField(upload_to='Club/')


class Advice(models.Model):
    photo = models.ImageField(upload_to='Advice/')
    tex = models.TextField()
    data = models.DateField(auto_now_add=True)


class Akademiya(models.Model):
    name = models.CharField(max_length=200)
    bg_photo = models.ImageField()


class Activities(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField()


class My_shop(models.Model):
    text = models.TextField()
    bg_img = models.ImageField()
    img = models.ImageField()


class Shopping(models.Model):
    photo = models.ImageField()
    title = models.TextField()
    photo_1 = models.ImageField()
    photo_2 = models.ImageField()
    text = models.TextField()


class Img(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=346)


class Maydonm(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()


class Maydon_t(models.Model):
    name = models.CharField(max_length=190)
    text = models.TextField()
    img = models.ImageField()


class Maydon_o(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    photo = models.ImageField()


class Maydon(models.Model):
    name = models.CharField(max_length=130)
    text = models.TextField()
    photo = models.ImageField()