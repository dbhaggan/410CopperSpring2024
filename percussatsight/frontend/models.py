from django.db import models

# Create your models here.
class User(models.Model):
    # sign up info
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    userName = models.CharField(max_length=255)
    passWord = models.CharField(max_length=255)
    emailAddress = models.CharField(max_length=255)

class Instrument(models.Model):
    # instrument anme
    name = models.CharField(max_length=255)

    # created this if there are intricate percussion families
    family = models.CharField(max_length=255)

class Sheet_Music(models.Model):
    # song/sheet music name
    title = models.CharField(max_length=255)

    # difficulty scale (1-5?)
    difficulty = models.IntegerField()

    # original artist name
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Note(models.Model):
    name = models.CharField(max_length = 2)
    octave = models.IntegerField()  
    duration = models.FloatField()

class Sheet_Music_Note(models.Model):
    sheet_music = models.ForeignKey(Sheet_Music, on_delete = models.CASCADE)
    note = models.ForeignKey(Note, on_delete = models.CASCADE)

class User_Progress(models.Model):
    # user name
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # music played
    sheet_music = models.ForeignKey(Sheet_Music, on_delete=models.CASCADE)

    # music completed
    completed = models.BooleanField(default=False)

    # scores from practice sessions
    score = models.IntegerField()

    # total amount of time played
    timestamp = models.DateTimeField(auto_now_add=True)

class Feedback (models.Model):
    # user name
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # music just played
    sheet_music = models.ForeignKey(Sheet_Music, on_delete=models.CASCADE)

    # algorithmic feedback
    feedback_text = models.TextField()

    # overall rating (1-100?)
    rating = models.IntegerField()

# class Rhythm (models.Model): do we need this? we will have a rhythm api already

class Practice_Session (models.Model):
    # user name
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # time session started
    start_time = models.DateTimeField()

    # time session ended
    end_time = models.DateTimeField()

    # time taken for session
    duration = models.DurationField()