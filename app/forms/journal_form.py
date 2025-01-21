from flask_wtf import FlaskForm
from wtforms import TextAreaField, DateField, BooleanField, StringField
from wtforms.validators import DataRequired, Length

class JournalEntryForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired(), Length(min=1, max=100)],
        render_kw={'placeholder': 'Title...'}
    )

    content = TextAreaField(
        'Content',
        validators=[DataRequired(), Length(min=1, max=2000)],
        render_kw={'placeholder': 'Write your journal entry...'}
    )

    accomplishments = TextAreaField(
        'Accomplishments',
        validators=[Length(max=1000)]
    )

    timestamp = DateField('Date', format='%Y-%m-%d', validators=[])

    photo = StringField('Upload Photo (optional)')

    is_private = BooleanField('Private')