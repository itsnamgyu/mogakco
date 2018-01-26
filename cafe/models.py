from django.db import models

PLUG_STATES = (
        (0, 'None'),
        (1, 'Some'),
        (2, 'Many'))

WIFI_STATES = (
        (0, 'Bad'),
        (1, 'Fine'),
        (2, 'Good'))


class Cafe(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Review(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    plug = models.IntegerField(choices=PLUG_STATES)
    wifi = models.IntegerField(choices=WIFI_STATES)

    def plug_string(self):
        if self.plug == 0:
            return "No plugs :("
        if self.plug == 1:
            return "Some plugs"
        if self.plug == 2:
            return "Lot's of plugs!"

    def wifi_string(self):
        if self.wifi == 0:
            return "Bad wifi"
        if self.wifi == 1:
            return "Okay wifi"
        if self.wifi == 2:
            return "Good wifi"


class Hours(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    # In minutes
    open_weekday = models.IntegerField()
    open_sat = models.IntegerField()
    open_sun = models.IntegerField()
    # In minutes
    close_weekday = models.IntegerField()
    close_sat = models.IntegerField()
    close_sun = models.IntegerField()


class Prices(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    americano = models.IntegerField()
