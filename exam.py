
"""
This is the script I'll use to ask you questions.
~ Christopher
"""

import random

questions_en = (
    (
        'What is Computer Vision (CV) and why is it important? Name some applications.',
        'What is the purpose of image processing? Briefly describe some image processing operations. What is the relation between image processing and CV?'
    ),
    (
        'Describe how the programming languages we covered in the lecture differ, and what libraries there are for CV-related tasks.',
        'Which factors should be considered when choosing a programming language? Is there a best programming language? Why (not)?'
    ),
    (
        'Explain three things every CV problem consists of and the steps to solving CV problems. Describe and solve an example problem in this manner.',
        'What is a model and what does it do? What kinds of models are there? How is machine learning related to all this?',
        'We covered two approaches to selecting models. What are their differences and when are they applicable?'
    ),
    (
        'What is object recognition and why is it challenging? Explain the taxonomy used in the lecture using own examples.',
        'How does detection of planar rigid objects work? Name some example applications. What are x and w? Which model is applicable and why? Explain how detection can be performed in an automatic manner.',
        'What is the relation between corresponding points on a nonplanar object in two images? How can this relation be used to automatically find correspondences and for estimating 3D coordinates? What must be known for this to work?',
        'Explain the basic idea behind constellation models. Why are they useful and what are they used for? Describe an example application that favors such models, and explain how the model could look like in this application.'
    ),
    (
        'What is the bag of words representation and how is it obtained? Explain the steps necessary to perform classification on this basis.',
        'Explain how face detection works. Which properties are desired? What are Haar features, what do they encode, and why can they be computed so efficiently? What is boosting, how does it work, and how can it be used for face detection?',
        'What is deep learning and what are the motivations for it? How do deep learning models look like? What are Convolutional Neural Networks (CNNs)? Which conditions must apply for CNNs to perform well?',
        'Describe the structure two-layer Perceptrons and their properties. Why are such models not applicable for deep learning? What are convolutional layers? How and why can they be used to realize deep models?'
    )
)

questions_de = (
    (
        'Was ist Computer Vision (CV) und warum ist es wichtig? Nennen Sie Beispielanwendungen.',
        'Was ist der Zweck von Image Processing? Beschreiben Sie kurz verschiedene Image Processing Operationen. Wie stehen Image Processing und CV in Zusammenhang?'
    ),
    (
        'Beschreiben Sie inwiefern sich die in der Vorlesung besprochenen Programmiersprachen voneinander unterscheiden und welche CV Bibliotheken existieren.',
        'Welche Faktoren beeinflussen die Wahl der Programmiersprache? Existiert eine beste Programmiersprache? Warum (nicht)?'
    ),
    (
        'Beschreiben Sie die drei Dinge, aus denen jedes CV Problem besteht, und die in der Vorlesung besprochenen Schritte zur Lösung solcher Probleme. Beschreiben und lösen Sie ein Beispielproblem auf diese Weise.',
        'Was ist ein Modell und welchen Zweck hat es? Welche Arten von Modellen gibt es? Wie steht Machine Learning in Relation dazu?',
        'In der Vorlesung wurden zwei Ansätze zur Wahl von Modellen besprochen. Wie unterscheiden sie sich und wann sind sie zutreffend?'
    ),
    (
        'Was ist Objekterkennung und welche Herausforderungen gibt es? Beschreiben Sie die besprochenen Objekterkennungsarten anhand eigener Beispiele.',
        'Wie können planare und starre Objekte erkannt werden? Nennen Sie Beispielanwendungen. Was beschreiben x und w? Welches Modell ist angemessen? Beschreiben Sie, wie solche Objekte automatisch detektiert werden können.',
        'Wie lautet die Relation zwischen korrespondierenden Punkten auf nicht-planaren Objekten in zwei Bildern? Wie kann diese Relation dazu benutzt werden, um solche Korrespondenzen automatisch zu finden und um 3D Koordinaten zu berechnen? Was muss dazu bekannt sein?',
        'Beschreiben Sie die grundlegende Idee hinter Constellation Models. Warum sind solche Modelle sinnvoll und wozu werden sie verwendet? Beschreiben Sie eine Beispielanwendung und erklären Sie, wie ein solches Modell aussehen könnte.'
    ),
    (
        'Was beschreibt die Bag of Words Repräsentation und wie wird sie berechnet? Erklären Sie die Schritte, die notwendig sind, um damit Bilder zu klassifizieren.',
        'Erklären Sie wie Gesichtserkennung funktioniert. Welche Eigenschaften sind gewünscht? Was sind Haar Features, was beschreiben sie und warum können Sie so effizient berechnet werden? Was ist Boosting, wie funktioniert es und wie kann es zur Gesichtserkennung verwendet werden?',
        'Was ist Deep Learning und was ist der Zweck? Wie sehen Deep Learning Modelle aus? Was sind Convolutional Neural Networks (CNNs)? Welche Bedingungen müssen erfüllt sein, damit CNNs gut funktionieren?',
        'Beschreiben Sie die Struktur eines Perceptrons mit zwei Schichten. Warum sind solche Modelle nicht für Deep Learning geeignet? Was sind Convolutional Layers? Wie und warum können sie verwendet werden um tiefe Modelle zu realisieren?'
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
