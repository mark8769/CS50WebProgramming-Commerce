from .models import AuctionListing, Categories
from django import forms

# use this when fields are closely related to model fields (e.g. Database driven application)
class ListingForm(forms.ModelForm):
    class Meta:
        model = AuctionListing
        fields = ('auction_title', 'starting_bid', 'auction_description', 'image_url', 'category')
        # all auction listing fields should be used (recommended way for security reasons)
        # https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#selecting-the-fields-to-use
        # fields = '__all__'
        css_dict = {'class': 'form-control'}
        widgets = {
            'auction_title': forms.TextInput(attrs=css_dict),
            'auction_description': forms.Textarea(attrs={'class':'form-control', 'maxlength': '250'}),
            # DecimalField had no attrs field, so caused program not too work. Not form specific field.
            # Sane thing with URLField, not form specific. Also not a "widget".
            # Widget's have the attrs keyword argument, to style with css
            'starting_bid': forms.NumberInput(attrs={'class': 'form-control','min':'5', 'max': '30000'}),
            # there's a pattern attribute for input elements in html, what kind of regex for .jpg,.png,.svg?
            'image_url': forms.URLInput(attrs={'class': 'form-control'})
        }
        # https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
        # need to set a verbose name in models.py for each field, labels no longer working?
        labels = {
            'auction_title': 'Auction Title',
            'auction_description': 'Description',
            'starting_bid': 'Starting Bid',
            'image_url': 'Image Url (.jpg, .png, etc.)',
        }