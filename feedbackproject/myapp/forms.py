from django import forms
from myapp.models import feedBack

class StudentForm(forms.ModelForm):
    class Meta:
        model = feedBack
        fields = '__all__'
        # fields = ['name', 'age', 'email', 'course', 'feedback']
        

    def clean_name(self):
        n = self.cleaned_data['name']
        if len(n) <= 3:
            raise forms.ValidationError("Name must be more than 3 characters")
        return n
    def clean_age(self):
        
        
            a = self.cleaned_data['age']
            if a < 0 :
                raise forms.ValidationError("Age cannot be negative")
            return a
    def clean_email(self):
            e = self.cleaned_data['email']
            if not e.endswith('@gmail.com'):
                raise forms.ValidationError("Email must be a gmail address")
            return e
    def clean_course(self):
            c = self.cleaned_data['course']
            if c.lower() not in ['python', 'django', 'data science']:
                raise forms.ValidationError("Courses must be python, django or data Science")
            return c
    def clean_feedback(self):
            c = self.cleaned_data['feedback']
            if len(c) < 10:
                raise forms.ValidationError("Feedback must be at least 10 characters long")
            return c