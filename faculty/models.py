from django.db import models
from django.db import connections
from django.core.exceptions import FieldDoesNotExist

# Create your models here.

class Faculty_information(models.Model):
    F_Id = models.CharField(max_length=10,primary_key=True)
    F_Name = models.CharField(max_length=50)
    Pan_no = models.CharField(max_length=50)
    University_Degree = models.CharField(max_length=50)
    Date_of_Receiving_Degree = models.CharField(max_length=50)
    Area_of_Specialization = models.CharField(max_length=500)
    Research_paper_Publications = models.CharField(max_length=10)
    PhD_Guidance = models.CharField(max_length=50)
    Faculty_receiving_PhD = models.CharField(max_length=10)
    Current_Designation = models.CharField(max_length=50)
    Designated_Date = models.CharField(max_length=50)
    Date_of_Joining = models.CharField(max_length=40)
    Association_type = models.CharField(max_length=50)
    Present_Working = models.CharField(max_length=50)
    Date_of_Leaving = models.CharField(max_length=50)
    Is_HOD = models.CharField(max_length=20)
    class Meta:
        db_table ="Faculty_information"


    #def __str__(self):
        #return self.F_Name



class Journals19_20(models.Model):
    J_Id = models.CharField(max_length=10,primary_key=True)
    F_Name = models.CharField(max_length=50)
    Authors = models.CharField(max_length=500)
    Title = models.CharField(max_length=500)
    Vol_No = models.CharField(max_length=50)
    Isssue_No = models.CharField(max_length=50)
    Year = models.CharField(max_length=50)
    Page_No= models.CharField(max_length=500)
    Publisher = models.CharField(max_length=500)
    Indexed_and_Impact_Factor = models.CharField(max_length=50)
    F_Id = models.ForeignKey(Faculty_information, on_delete=models.CASCADE)
    class Meta:
        db_table ="Journals19_20"
    def __repr__(self):
        return f'<Journals19_20: Journals19_20 object ({self.J_Id}, {self.F_Name}, {self.Authors})>'


class Journals18_19(models.Model):
    J_Id = models.CharField(max_length=10,primary_key=True)
    F_Name = models.CharField(max_length=50)
    Authors = models.CharField(max_length=500)
    Title = models.CharField(max_length=500)
    Vol_No = models.CharField(max_length=50)
    Isssue_No = models.CharField(max_length=50)
    Year = models.CharField(max_length=50)
    Page_No= models.CharField(max_length=500)
    Publisher = models.CharField(max_length=500)
    Indexed_and_Impact_Factor = models.CharField(max_length=50)
    F_Id = models.ForeignKey(Faculty_information, on_delete=models.CASCADE)
    class Meta:
        db_table ="Journals18_19"

    def __repr__(self):
        return f'<Journals18_19: Journals18_19 object ({self.J_Id}, {self.F_Name}, {self.Authors})>'

class Journals17_18(models.Model):
    J_Id = models.CharField(max_length=10,primary_key=True)
    F_Name = models.CharField(max_length=50)
    Authors = models.CharField(max_length=500)
    Title = models.CharField(max_length=500)
    Vol_No = models.CharField(max_length=50)
    Isssue_No = models.CharField(max_length=50)
    Year = models.CharField(max_length=50)
    Page_No= models.CharField(max_length=500)
    Publisher = models.CharField(max_length=500)
    Indexed_and_Impact_Factor = models.CharField(max_length=50)
    F_Id = models.ForeignKey(Faculty_information, on_delete=models.CASCADE)
    class Meta:
        db_table ="Journals17_18"

    def __repr__(self):
        return f'<Journals17_18: Journals17_18 object ({self.J_Id}, {self.F_Name}, {self.Authors})>'

class Conference19_20(models.Model):
    Con_Id = models.CharField(max_length=10,primary_key=True)
    F_Name = models.CharField(max_length=50)
    Authors = models.CharField(max_length=500)
    Title = models.CharField(max_length=500)
    Year = models.CharField(max_length=50)
    Vol_Page_No = models.CharField(max_length=50)
    Conference_publication = models.CharField(max_length=500)
    F_Id = models.ForeignKey(Faculty_information, on_delete=models.CASCADE)
    class Meta:
        db_table ="Conference19_20"

    def __repr__(self):
        return f'<Conference19_20: Conference19_20 object ({self.Con_Id}, {self.F_Name}, {self.Authors})>'

class Conference18_19(models.Model):
    Con_Id = models.CharField(max_length=10,primary_key=True)
    F_Name = models.CharField(max_length=50)
    Authors = models.CharField(max_length=500)
    Title = models.CharField(max_length=500)
    Year = models.CharField(max_length=50)
    Vol_Page_No = models.CharField(max_length=50)
    Conference_publication = models.CharField(max_length=500)
    F_Id = models.ForeignKey(Faculty_information, on_delete=models.CASCADE)
    class Meta:
        db_table ="Conference18_19"

    def __repr__(self):
        return f'<Conference18_19: Conference18_19 object ({self.Con_Id}, {self.F_Name}, {self.Authors})>'

class Conference17_18(models.Model):
    Con_Id = models.CharField(max_length=10,primary_key=True)
    F_Name = models.CharField(max_length=50)
    Authors = models.CharField(max_length=500)
    Title = models.CharField(max_length=500)
    Year = models.CharField(max_length=50)
    Vol_Page_No = models.CharField(max_length=50)
    Conference_publication = models.CharField(max_length=500)
    F_Id = models.ForeignKey(Faculty_information, on_delete=models.CASCADE)
    class Meta:
        db_table ="Conference17_18"

    def __repr__(self):
        return f'<Conference17_18: Conference17_18 object ({self.Con_Id}, {self.F_Name}, {self.Authors})>'

class Book_published(models.Model):
    B_Id = models.CharField(max_length=10,primary_key=True)
    F_Name = models.CharField(max_length=50)
    Authors = models.CharField(max_length=500)
    Title = models.CharField(max_length=500)
    Year = models.CharField(max_length=20)
    Publisher = models.CharField(max_length=500)
    class Meta:
        db_table = "Book_published"

    def __repr__(self):
        return f'<Book_published: Book_published object ({self.B_Id}, {self.F_Name}, {self.Authors})>'

class Chapters19_20(models.Model):
    C_Id = models.CharField(max_length=10,primary_key=True)
    F_Name = models.CharField(max_length=50)
    Authors = models.CharField(max_length=500)
    Title = models.CharField(max_length=500)
    Year = models.CharField(max_length=20)
    Vol_Page_No = models.CharField(max_length=50)
    Publication = models.CharField(max_length=100)
    F_Id = models.ForeignKey(Faculty_information, on_delete=models.CASCADE)
    class Meta:
        db_table = "Chapters19_20"

    def __repr__(self):
        return f'<Chapters19_20: Chapters19_20 object ({self.C_Id}, {self.F_Name}, {self.Authors})>'

class Chapters18_19(models.Model):
    C_Id = models.CharField(max_length=10,primary_key=True)
    F_Name = models.CharField(max_length=50)
    Authors = models.CharField(max_length=500)
    Title = models.CharField(max_length=500)
    Year = models.CharField(max_length=20)
    Vol_Page_No = models.CharField(max_length=50)
    Publication = models.CharField(max_length=100)
    F_Id = models.ForeignKey(Faculty_information, on_delete=models.CASCADE)
    class Meta:
        db_table = "Chapters18_19"

    def __repr__(self):
        return f'<Chapters18_19: Chapters18_19 object ({self.C_Id}, {self.F_Name}, {self.Authors})>'

class Chapters17_18(models.Model):
    C_Id = models.CharField(max_length=10,primary_key=True)
    F_Name = models.CharField(max_length=50)
    Authors = models.CharField(max_length=500)
    Title = models.CharField(max_length=500)
    Year = models.CharField(max_length=20)
    Vol_Page_No = models.CharField(max_length=50)
    Publication = models.CharField(max_length=100)
    F_Id = models.ForeignKey(Faculty_information, on_delete=models.CASCADE)
    class Meta:
        db_table = "Chapters17_18"

    def __repr__(self):
        return f'<Chapters17_18: Chapters17_18 object ({self.C_Id}, {self.F_Name}, {self.Authors})>'



class Chapters(models.Model):
    C_Id = models.CharField(max_length=10,primary_key=True)
    F_Name = models.CharField(max_length=50)
    Authors = models.CharField(max_length=500)
    Title = models.CharField(max_length=500)
    Year = models.CharField(max_length=20)
    Vol_Page_No = models.CharField(max_length=50)
    Publication = models.CharField(max_length=100)
    F_Id = models.ForeignKey(Faculty_information, on_delete=models.CASCADE)
    class Meta:
        db_table = "Chapters"

    def __repr__(self):
        return f'<Chapters18_19: Chapters18_19 object ({self.C_Id}, {self.F_Name}, {self.Authors})>'



class Conference(models.Model):
    Con_Id = models.CharField(max_length=10,primary_key=True)
    F_Name = models.CharField(max_length=50)
    Authors = models.CharField(max_length=500)
    Title = models.CharField(max_length=500)
    Year = models.CharField(max_length=50)
    Vol_Page_No = models.CharField(max_length=50)
    Conference_publication = models.CharField(max_length=500)
    F_Id = models.ForeignKey(Faculty_information, on_delete=models.CASCADE)
    class Meta:
        db_table ="Conference"

    def __repr__(self):
        return f'<Conference: Conference object ({self.Con_Id}, {self.F_Name}, {self.Authors})>'



class Journals(models.Model):
    J_Id = models.CharField(max_length=10,primary_key=True)
    F_Name = models.CharField(max_length=50)
    Authors = models.CharField(max_length=500)
    Title = models.CharField(max_length=500)
    Vol_No = models.CharField(max_length=50)
    Isssue_No = models.CharField(max_length=50)
    Year = models.CharField(max_length=50)
    Page_No= models.CharField(max_length=500)
    Publisher = models.CharField(max_length=500)
    Indexed_and_Impact_Factor = models.CharField(max_length=50)
    F_Id = models.ForeignKey(Faculty_information, on_delete=models.CASCADE)
    class Meta:
        db_table ="Journals"

    def __repr__(self):
        return f'<Journals: Journals object ({self.J_Id}, {self.F_Name}, {self.Authors})>'
