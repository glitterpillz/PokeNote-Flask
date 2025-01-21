from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class MessageForm(FlaskForm):
    receiver = StringField("Receiver Username", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired(), Length(min=1, max=1000)])
    submit = SubmitField("Send Message")