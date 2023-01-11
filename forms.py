from flask_wtf import FlaskForm
from wtforms import (
    widgets, StringField, SubmitField, EmailField,
    IntegerField, SelectField, SelectMultipleField, TextAreaField
)
from wtforms.validators import DataRequired


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class SurveyForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    gender = SelectField('Ваше гендер',
                            choices=[('Мужчина', 'Мужчина'),
                                     ('Женщина', 'Женщина'),
                                     ('Другое', 'Другое')])
    education = SelectField('Ваше образование',
                            choices=[('детский сад', 'детский сад'), ('9 классов школы', '9 классов школы'),
                                     ('11 классов школы', '11 классов школы'),
                                     ('среднее специальное', 'среднее специальное'),
                                     ('неоконченное высшее', 'неоконченное высшее'),
                                     ('бакалавриат / специалитет', 'бакалавриат / специалитет'),
                                     ('магистратура', 'магистратура'),
                                     ('аспирантура', 'аспирантура'),
                                     ('кандидат наук', 'кандидат наук'),
                                     ('доктор наук', 'доктор наук'),
                                     ]
                            )
    linguistics = SelectField('Вы как-то связаны с лингвистикой?',
                            choices=[('Определённо да', 'Определённо да'),
                                     ('Отчасти', 'Отчасти'),
                                     ('Совсем нет', 'Совсем нет')]
                            )
    {% for question in questions %}

    question1 = SelectField('Сказали бы вы так?',
                            choices=[('Звучит', 'Звучит'),
                                     ('Не звучит', 'Не звучит')])
    submit = SubmitField('Отправить ответы')
