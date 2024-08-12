from django.db import models

class book(models.Model):
        book_id=models.IntegerField(primary_key=True)
        book_name=models.CharField(max_length=255)
        subject=models.CharField(max_length=20)
        author=models.CharField(max_length=230)
        quantity=models.PositiveIntegerField()

class Member(models.Model):
        member_id=models.IntegerField(primary_key=True)
        member_name=models.CharField(max_length=220)
        mobile=models.IntegerField()
        semester=models.IntegerField()
        branch=models.CharField(max_length=30)
class Record(models.Model):
        book=models.ForeignKey(book,on_delete=models.CASCADE)
        Member=models.ForeignKey(Member,on_delete=models.CASCADE)
        issusID=models.IntegerField(primary_key=True)
        issudate=models.DateField()
        returndate=models.DateField()
