


# libraries to build interactive cli
from __future__ import print_function, unicode_literals

# imports for bullet style
from PyInquirer import style_from_dict, Token,  Separator, prompt

# for spawning cli view
from pprint import pprint









# Colour selection

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

# option selection

questions = [
    {
        'type': 'checkbox',
        'message': 'Configure search mode',
        'name': 'Phase 1',
        'choices': [
            Separator('= Search location ='),
            {
                'name': 'Whole disk'
            },
            {
                'name': 'Current directory (Default)',
                'checked': True
            },
            {
                'name': 'Specify path'
            },
            Separator('= File name criteria ='),
            {
                'name': 'Should have same name',
                'checked': True
            },
            {
                'name': 'Irrespective of file name'
            },
            Separator('= File type criteria ='),
            {
                'name': 'Same file type'
            },
            {
                'name': 'All file types'
            },
            {
                'name': 'Include these (Enter explicitly)'
            },
            Separator('= Count ='),
            {
                'name': 'Find one'
            },
            {
                'name': 'Find all',
                #'disabled': 'out of stock'
            },
            {
                'name': 'Set count'
            }
        ],
        'validate': lambda answer: 'Choose appropriate options.' \
            if len(answer) == 0 else True
    }
]



answers = prompt(questions, style=style)
pprint(answers)
