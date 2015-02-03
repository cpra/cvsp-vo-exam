
"""
This is the script I'll use to ask you questions.
~ Christopher
"""

import random

questions_en = (
    (
        'What factors should be considered when choosing a programming language?',
        'Is there a best programming language? Why (not)?'
    ),
    (
        'What is the relation between image processing and Computer Vision (CV)?',
        'What is the purpose of image processing? Name some examples.'
    ),
    (
        'Why should one not think in terms of algorithms when approaching CV problems?',
        'What is the preferred way to approach CV problems and why?',
        'What are the three steps to model-based CV solutions?',
        'What is the difference between a model and an algorithm?',
        'What is numerical optimization and how do iterative methods work?'
    ),
    (
        'How are images formed? Describe the pinhole camera model.',
        'How does stereo reconstruction work?',
        'What are depth sensors and how do they work?'
    ),
    (
        'What are the three discussed steps of 3D reconstruction?',
        'How does Kinect\'s player pose estimation work?',
        'What is a random forest and how does it work?'
    ),
    (
        'What kinds of object recognition are there and why is it challenging?',
        'How does instance recognition of rigid objects work?',
        'How does Viola & Jones\' face detector work?',
        'How does the bag of words model work and what is it used for?'
    ),
    (
        'What is the limitation of traditional object recognition methods?',
        'What is deep learning and how are such models structured?',
        'What is a convolutional neural network and how is it structured?'
    )
)

questions_de = (
    (
        'Welche Faktoren sollten bei der Wahl einer Programmiersprache beachtet werden?',
        'Gibt es eine beste Programmiersprache? Warum (nicht)?'
    ),
    (
        'Wie stehen Image Processing und Computer Vision (CV) in Zusammenhang?',
        'Was ist der Zweck von Image Processing? Nennen Sie Beispiele.'
    ),
    (
        'Warum soll ein CV Lösungsansatz nicht auf Basis von Algorithmen gewählt werden?',
        'Was ist der bevorzugte Lösungsansatz für CV Problem und warum?',
        'Wie lauten die drei Schritte modellbasierter CV Lösungen?',
        'Was ist der Unterschied zwischen einem Modell und einem Algorithmus?',
        'Was ist numerische Optimierung und wie funktionieren iterative Methoden?'
    ),
    (
        'Wie entstehen Bilder? Beschreiben Sie das Lochkameramodell.',
        'Wie funktioniert Stereo-Rekonstruktion?',
        'Was sind Tiefensensoren und wie funktionieren sie?'
    ),
    (
        'Wie lauten die drei besprochenen Schritte zur 3D Rekonstruktion?',
        'Wie funktioniert die Haltungserkennung der Kinect?',
        'Was ist ein Random Forest und wie funktioniert er?'
    ),
    (
        'Welche Arten der Objekterkennung gibt es? Warum ist Objekterkennung schwierig?',
        'Wie funktioniert die Instanzenerkennung von starren Objekten?',
        'Wie funktioniert Viola & Jones\' Gesichtsdetektor?',
        'Wie funktioniert das Bag of Words Modell und wozu wird es verwendet?'
    ),
    (
        'Was ist die Einschränkung traditioneller Objekterkennungsmethoden?',
        'Was ist Deep Learning und wie sehen solche Modelle aus?',
        'Was ist ein Convolutional Neural Network und wie ist es aufgebaut?'
    )
)

num_questions = 4  # number of questions to ask

random.seed()  # seed rng
categories = sorted(random.sample(range(len(questions_en)), num_questions))  # randomly choose categories

q = input('Specify language ("en" or "de"): ')
questions = questions_en
if q == 'de':
    questions = questions_de

for c in categories:
    qid = random.randint(0, len(questions[c])-1)  # randomly choose question
    print(questions[c][qid])  # print it
    input('')
