from django import forms


class randomForm(forms.Form):
    game_title = forms.ChoiceField(
        choices=[{"C", "coin"}, {"D", "dice"}, {"N", "fandom number"}]
    )


trise = forms.IntegerField(min_value=1, max_value=64)
