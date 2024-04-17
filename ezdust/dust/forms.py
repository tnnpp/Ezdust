from django import forms

class PredictForm(forms.Form):
    BANGKOK_DISTRICTS = [
        ('Bang_Bon', 'Bang Bon'),
        ('Bang_Kapi', 'Bang Kapi'),
        ('Bang_Khae', 'Bang Khae'),
        ('Bang_Khen', 'Bang Khen'),
        ('Bang_Kho_Laem', 'Bang Kho Laem'),
        ('Bang_Khun_Thian', 'Bang Khun Thian'),
        ('Bang_Na', 'Bang Na'),
        ('Bang_Phl_at', 'Bang Phlat'),
        ('Bang_Rak', 'Bang Rak'),
        ('Bang_Sue', 'Bang Sue'),
        ('Bangkok_Noi', 'Bangkok Noi'),
        ('Bangkok_Yai', 'Bangkok Yai'),
        ('Bueng_Kum', 'Bueng Kum'),
        ('Chatuchak', 'Chatuchak'),
        ('Chom_Thong', 'Chom Thong'),
        ('Din_Daeng', 'Din Daeng'),
        ('Don_Mueang', 'Don Mueang'),
        ('Dusit', 'Dusit'),
        ('Huai_Khwang', 'Huai Khwang'),
        ('Khan_Na_Yao', 'Khan Na Yao'),
        ('Khlong_Sam_Wa', 'Khlong Sam Wa'),
        ('Khlong_San', 'Khlong San'),
        ('Khlong_Toei', 'Khlong Toei'),
        ('Lak_Si', 'Lak Si'),
        ('Lat_Krabang', 'Lat Krabang'),
        ('Lat_Phrao', 'Lat Phrao'),
        ('Min_Buri', 'Min Buri'),
        ('Nong_Chok', 'Nong Chok'),
        ('Nong_Khaem', 'Nong Khaem'),
        ('Pathum_Wan', 'Pathum Wan'),
        ('Phasi_Charoen', 'Phasi Charoen'),
        ('Phaya_Thai', 'Phaya Thai'),
        ('Phra_Khanong', 'Phra Khanong'),
        ('Phra_Nakhon', 'Phra Nakhon'),
        ('Pom_Prap_Sattru_Phai', 'Pom Prap Sattru Phai'),
        ('Prawet', 'Prawet'),
        ('Rat_Burana', 'Rat Burana'),
        ('Ratchathewi', 'Ratchathewi'),
        ('Sai_Mai', 'Sai Mai'),
        ('Samphanthawong', 'Samphanthawong'),
        ('Saphan_Sung', 'Saphan Sung'),
        ('Sathon', 'Sathon'),
        ('Suan_Luang', 'Suan Luang'),
        ('Taling_Chan', 'Taling Chan'),
        ('Thawi_Watthana', 'Thawi Watthana'),
        ('Thon_Buri', 'Thon Buri'),
        ('Thung_Khru', 'Thung Khru'),
        ('Wang_Thonglang', 'Wang Thonglang'),
        ('Watthana', 'Watthana'),
        ('Yan_Nawa', 'Yan Nawa')
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
