from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,RadioField,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
class PostForm(FlaskForm):
    post_title = StringField('Title')
    description = TextAreaField('Description', validators=[Required()])
    submit = SubmitField('Submit')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('write a comment',validators=[Required()])
    submit = SubmitField('comment')