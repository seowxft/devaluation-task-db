"""User model"""
from sqlalchemy import Column, Integer, String, ARRAY, Text

from models.db import Model
from models.base_object import BaseObject


class TaskQuiz(BaseObject, Model):

    id = Column(Integer, primary_key=True)

    userID               = Column(Text(length=10000))
    quizTime             = Column(Text(length=10000))
    taskSession          = Column(Text(length=10000))
    taskSessionTry       = Column(Text(length=10000))
    quizQnNum            = Column(Text(length=10000))
    quizQnRT             = Column(Text(length=10000))
    quizContinDefault    = Column(Text(length=10000))
    quizContin           = Column(Text(length=10000))
    quizConfDefault      = Column(Text(length=10000))
    quizConf             = Column(Text(length=10000))

    def get_id(self):
        return str(self.id)

    def get_user_id(self):
        return str(self.userID)

    def get_trial_time(self):
        return str(self.quizTime)

    def get_task_session(self):
        return str(self.taskSession)

    def get_task_session_try(self):
        return str(self.taskSessionTry)

    def get_quiz_question_no(self):
        return str(self.quizQnNum)

    def get_quiz_rt(self):
        return str(self.quizQnRT)

    def get_contin_def(self):
        return str(self.quizContinDefault)

    def get_contin(self):
        return str(self.quizContin)

    def get_conf_def(self):
        return str(self.quizConfDefault)

    def get_conf(self):
        return str(self.quizConf)

    def errors(self):
        errors = super(TaskQuiz, self).errors()
        return errors