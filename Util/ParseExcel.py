import openpyxl
import os

parent_directory_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filepath= parent_directory_path + u"\\PageElementLocator\\model.xlsx"

wb = openpyxl.load_workbook(filepath)
login = wb['login']
question = wb['question']
handout = wb['handout']
recordpaper = wb['recordpaper']

class ParseExcel():

    def getlogin_value(self):
        url = login['B1'].value
        loginname = login['B2'].value
        password = login['B3'].value
        dict = {}
        dict['url'] = url
        dict['loginname'] = loginname
        dict['password'] = password
        return dict

    def getquestion_value(self):
        choice_stem = question['B1'].value
        choice_option = question['B2'].value
        choice_answer = question['B3'].value
        choice_analysis =question['B4'].value
        choice_remarks =question['B5'].value

        completion_stem =question['B7'].value
        completion_answer =question['B8'].value
        completion_analysis =question['B9'].value
        completion_remarks =question['B10'].value

        answer_stem =question['B12'].value
        answer_answer =question['B13'].value
        answer_analysis =question['B14'].value
        answer_remarks =question['B15'].value
        dict = {}
        dict['choice_stem'] = choice_stem
        dict['choice_option'] = choice_option
        dict['choice_answer'] = choice_answer
        dict['choice_analysis'] = choice_analysis
        dict['choice_remarks'] = choice_remarks

        dict['completion_stem'] = completion_stem
        dict['completion_answer'] = completion_answer
        dict['completion_analysis'] = completion_analysis
        dict['completion_remarks'] = completion_remarks

        dict['answer_stem'] = answer_stem
        dict['answer_answer'] = answer_answer
        dict['answer_analysis'] = answer_analysis
        dict['answer_remarks'] = answer_remarks
        return dict
