import json
import userandsuperuser
def make_question(teacher_number):
    if teacher_number in userandsuperuser.Super_User.total_college_teachers:
        print('Please proceed towards making new questions!!')
        with open('all_questions.json','w') as fo:
            json_file = {}
            while True:
                print("for easy question type 'GK', for hard question type 'Python' and type Stop to stop adding more questions")
                choice_for_level = input('enter your choice  ')
                if choice_for_level == 'GK':
                    content = []
                    count = 1
                    while True:
                        choice = input('IF YOU ENTER 1, GO FORWARD TO MAKING MORE QUESTIONS, IF YOU ENTER 0 STOP MAKING QUESTIONS')
                        if int(choice) == 1:    
                            print('Total questions are -> ',count)
                            dictionary = {}
                            dictionary['question'] = input('Enter the question.')
                            dictionary['options'] = []
                            dictionary['options'].append(input('Enter options A.'))
                            dictionary['options'].append(input('Enter options B.'))
                            dictionary['options'].append(input('Enter options C.'))
                            dictionary['options'].append(input('Enter options D.'))
                            dictionary['answer'] = input('Enter the solution.')
                            content.append(dictionary)
                            count +=1
                        else:
                            print('Your total number of questions are -> ',count)
                            break
                elif choice_for_level == 'Python':
                    hard_content = []
                    count = 1
                    while True:
                        choice = input('IF YOU ENTER 1, GO FORWARD TO MAKING MORE QUESTIONS, IF YOU ENTER 0 STOP MAKING QUESTIONS')
                        if int(choice) == 1:    
                            print('Total questions are -> ',count)
                            dictionary = {}
                            dictionary['question'] = input('Enter the question.')
                            dictionary['options'] = []
                            dictionary['options'].append(input('Enter options A.'))
                            dictionary['options'].append(input('Enter options B.'))
                            dictionary['options'].append(input('Enter options C.'))
                            dictionary['options'].append(input('Enter options D.'))
                            dictionary['answer'] = input('Enter the solution.')
                            hard_content.append(dictionary)
                            count +=1
                        else:
                            print('Your total number of questions are -> ',count)
                            break
                elif choice_for_level == 'Stop':
                    print('questions added successfully')
                    break
                else:
                    print('enter a valid option! ')
            json_file['GK'] = content
            json_file['Python'] = hard_content
            json.dump(json_file,fo)
    else:
        print('YOU ARE NOT A MEMBER OF FACULTY, IF YOU ARE PLEASE ENTER CORRECT ROLL NUMBER.')