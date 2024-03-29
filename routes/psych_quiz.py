"""users routes"""
from flask import current_app as app, jsonify, request
from models import PsychQuiz, BaseObject, db
from sqlalchemy.sql.expression import func

@app.route('/psych_quiz/<user_id>', methods=['POST', 'GET'])
def create_psych_data(user_id):
    content = request.json
    psych_quiz = PsychQuiz()
    psych_quiz.userID = str(content['userID'])
    psych_quiz.date = str(content['date'])
    psych_quiz.startTime = str(content['startTime'])
    psych_quiz.qnTimeStart = str(content['qnTimeStart'])
    psych_quiz.qnTimeEnd = str(content['qnTimeEnd'])
    psych_quiz.PgFinish_demo = str(content['PgFinish_demo'])
    psych_quiz.PgFinish_OCIR = str(content['PgFinish_OCIR'])
    psych_quiz.PgFinish_BEAQ= str(content['PgFinish_BEAQ'])
    psych_quiz.PgFinish_STAI_Y2 = str(content['PgFinish_STAI_Y2'])
    psych_quiz.PgFinish_BIS11 = str(content['PgFinish_BIS11'])
    psych_quiz.PgFinish_ASI3 = str(content['PgFinish_ASI3'])
    psych_quiz.PgFinish_SDS = str(content['PgFinish_SDS'])
    psych_quiz.PgFinish_IQ_text= str(content['PgFinish_IQ_text'])
    psych_quiz.PgFinish_IQ_image = str(content['PgFinish_IQ_image'])
    psych_quiz.PgRT_demo = str(content['PgRT_demo'])
    psych_quiz.PgRT_OCIR = str(content['PgRT_OCIR'])
    psych_quiz.PgRT_BEAQ = str(content['PgRT_BEAQ'])
    psych_quiz.PgRT_STAI_Y2 = str(content['PgRT_STAI_Y2'])
    psych_quiz.PgRT_BIS11= str(content['PgRT_BIS11'])
    psych_quiz.PgRT_SDS = str(content['PgRT_SDS'])
    psych_quiz.PgRT_ASI3 = str(content['PgRT_ASI3'])
    psych_quiz.PgRT_IQ_text= str(content['PgRT_IQ_text'])
    psych_quiz.PgRT_IQ_image = str(content['PgRT_IQ_image'])
    psych_quiz.age = str(content['age'])
    psych_quiz.gender = str(content['gender'])
    psych_quiz.OCIR = str(content['OCIR'])
    psych_quiz.BEAQ = str(content['BEAQ'])
    psych_quiz.STAI_Y2= str(content['STAI_Y2'])
    psych_quiz.BIS11= str(content['BIS11'])
    psych_quiz.SDS= str(content['SDS'])
    psych_quiz.ASI3= str(content['ASI3'])
    psych_quiz.IQ_1= str(content['IQ_1'])
    psych_quiz.IQ_2= str(content['IQ_2'])
    psych_quiz.IQ_1= str(content['IQ_1'])
    psych_quiz.IQ_2= str(content['IQ_2'])
    psych_quiz.IQ_3= str(content['IQ_3'])
    psych_quiz.IQ_4= str(content['IQ_4'])
    psych_quiz.IQ_5= str(content['IQ_5'])
    psych_quiz.IQ_6= str(content['IQ_6'])
    psych_quiz.IQ_7= str(content['IQ_7'])
    psych_quiz.IQ_8= str(content['IQ_8'])
    psych_quiz.IQimage_1= str(content['IQimage_1'])
    psych_quiz.IQimage_2= str(content['IQimage_2'])
    psych_quiz.IQimage_3= str(content['IQimage_3'])
    psych_quiz.IQimage_4= str(content['IQimage_4'])
    psych_quiz.IQimage_5= str(content['IQimage_5'])
    psych_quiz.IQimage_6= str(content['IQimage_6'])
    psych_quiz.IQimage_7= str(content['IQimage_7'])
    psych_quiz.IQimage_8= str(content['IQimage_8'])

    BaseObject.check_and_save(psych_quiz)
    result = dict({"success": "yes"})
    return jsonify(result)
