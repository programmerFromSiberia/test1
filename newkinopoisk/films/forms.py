from django import forms

# форма несвязанная с моделью
class SuggestGenreForm(forms.Form):
    # перечисляем поля формы
    title = forms.CharField(min_length=5, max_length=50, error_messages={'min_length': 'nnnnnoooo!'})  #error_messages={'required': 'нельзя оставлять пустым',
                                           # 'min_length': 'очень malo букв'},  )# CharField поле для заполнения букв CharField(label="Заголовок")
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': '40', 'rows': '10'}), max_length=300, required=False)
    # photo = forms.FileField(required=False)
    # checkbox = forms.BooleanField()
    # list_box = forms.ModelChoiceField(queryset=Films.objects.all())