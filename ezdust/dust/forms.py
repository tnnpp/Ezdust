from django import forms

class PredictForm(forms.Form):
    BANGKOK_DISTRICTS = [
        ('Bang Bon', 'Bang Bon'),
        ('Bang Kapi', 'Bang Kapi'),
        ('Bang Khae', 'Bang Khae'),
        ('Bang Khen', 'Bang Khen'),
        ('Bang Kho Laem', 'Bang Kho Laem'),
        ('Bang Khun Thian', 'Bang Khun Thian'),
        ('Bang Na', 'Bang Na'),
        ('Bang Phlat', 'Bang Phlat'),
        ('Bang Rak', 'Bang Rak'),
        ('Bang Sue', 'Bang Sue'),
        ('Bangkok Noi', 'Bangkok Noi'),
        ('Bangkok Yai', 'Bangkok Yai'),
        ('Bueng Kum', 'Bueng Kum'),
        ('Chatuchak', 'Chatuchak'),
        ('Chom Thong', 'Chom Thong'),
        ('Din Daeng', 'Din Daeng'),
        ('Don Mueang', 'Don Mueang'),
        ('Dusit', 'Dusit'),
        ('Huai Khwang', 'Huai Khwang'),
        ('Khan Na Yao', 'Khan Na Yao'),
        ('Khlong Sam Wa', 'Khlong Sam Wa'),
        ('Khlong San', 'Khlong San'),
        ('Khlong Toei', 'Khlong Toei'),
        ('Lak Si', 'Lak Si'),
        ('Lat Krabang', 'Lat Krabang'),
        ('Lat Phrao', 'Lat Phrao'),
        ('Min Buri', 'Min Buri'),
        ('Nong Chok', 'Nong Chok'),
        ('Nong Khaem', 'Nong Khaem'),
        ('Pathum Wan', 'Pathum Wan'),
        ('Phasi Charoen', 'Phasi Charoen'),
        ('Phaya Thai', 'Phaya Thai'),
        ('Phra Khanong', 'Phra Khanong'),
        ('Phra Nakhon', 'Phra Nakhon'),
        ('Pom Prap Sattru Phai', 'Pom Prap Sattru Phai'),
        ('Prawet', 'Prawet'),
        ('Rat Burana', 'Rat Burana'),
        ('Ratchathewi', 'Ratchathewi'),
        ('Sai Mai', 'Sai Mai'),
        ('Samphanthawong', 'Samphanthawong'),
        ('Saphan Sung', 'Saphan Sung'),
        ('Sathon', 'Sathon'),
        ('Suan Luang', 'Suan Luang'),
        ('Taling Chan', 'Taling Chan'),
        ('Thawi Watthana', 'Thawi Watthana'),
        ('Thon Buri', 'Thon Buri'),
        ('Thung Khru', 'Thung Khru'),
        ('Wang Thonglang', 'Wang Thonglang'),
        ('Watthana', 'Watthana'),
        ('Yan Nawa', 'Yan Nawa'),
    ]

    PLACES = [
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Public Area', 'Public Area')
    ]
    district = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=BANGKOK_DISTRICTS,
        label='District',
        required=True
    )
    place = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=PLACES,
        label='Place',
        required=True
    )
    people_num = forms.IntegerField(
        widget=forms.TextInput(attrs={'type': 'number'}),
        label='People number',
        required=True
    )
