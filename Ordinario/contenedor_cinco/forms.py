from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form
from wtforms.validators import Required

class AnimeSearchForm(FlaskForm):
    title = StringField("Title:", validators= [Required("Please insert data")])    
    epidosdes = StringField("Episodes:", validators= [Required("Please insert data")])    
    Type = StringField("Type:", validators= [Required("Please insert data")])    
    rated = StringField("Rated:", validators= [Required("Please insert data")])    
    image_url = StringField("image_url:", validators= [Required("Please insert data")])    
    score = StringField("Score:", validators= [Required("Please insert data")])    
    synopsis = StringField("Synopsis:", validators= [Required("Please insert data")])    
    airirng = StringField("Airing:", validators= [Required("Please insert data")])    
    members = StringField("Members:", validators= [Required("Please insert data")])    

    submit = SubmitField('Submit')