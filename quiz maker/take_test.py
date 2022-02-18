import json
import make_questions
def MCQ(college_rollno):
    # pass
    all_answers = []
    with open('all_questions.json',encoding='utf-8') as fo:
        content = json.load(fo)
        print(content.keys())
        given_input = input("if your choice is 'easy' then easy questions will be given and if your choice is 'hard' hard questions will be given")
        if given_input == 'easy':
            for i in range(len(content['GK'])):
                alpha = 96
                print(content['GK'][i]['question'])
                for j in content['GK'][i]['options']:
                    alpha +=1
                    print(chr(alpha)+')',j)
                solution = input('enter the solution of this question.  ')
                if solution == content['GK'][i]['answer']:
                    print(True)
                    all_answers.append(True)
                else:
                    print(False)
                    all_answers.append(False)
        elif given_input == 'hard':
            for i in range(len(content['Python'])):
                alpha = 96
                print(content['Python'][i]['question'])
                for j in content['Python'][i]['options']:
                    alpha +=1
                    print(chr(alpha)+')',j)
                solution = input('enter the solution of this question.  ')
                if solution == content['Python'][i]['answer']:
                    print(True)
                    all_answers.append(True)
                else:
                    print(False)
                    all_answers.append(False)
        else:
            print('wrong input')
    score = str(len([i for i in all_answers if i == True])) + '/' + str(len(all_answers))
# # making a json file to add all the marks to the file
    with open('marksperstudent.json',encoding='utf-8') as fo:
        content = json.load(fo)
        dictionary = {}
        dictionary[college_rollno] = score
    content.append(dictionary)
    with open('marksperstudent.json','w',encoding='utf-8') as fp:
        json.dump(content,fp)




