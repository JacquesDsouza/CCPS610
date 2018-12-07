from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired



class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])    
    post_category = StringField('Category', validators=[DataRequired()])
    post_type = StringField('Type', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')