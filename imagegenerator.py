from psd_tools import PSDImage
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import simpledialog

def generate_question_image(question, answers, correct_answer_index, question_number):
    # Créer une image de base pour la question
    img = Image.new('RGB', (1080, 1080), color=(153, 204, 204))
    d = ImageDraw.Draw(img)
    taille_de_la_police = 60
    font = ImageFont.truetype("ressources/CormorantInfant-Regular.ttf", taille_de_la_police)
    # Ajouter le numéro de la question dans le cercle 
    d.ellipse([(10,10), (110,110)], fill=(255,255,255))
    d.text((40, 40), str(question_number), fill=(0,0,0), font=font)
    # Ajouter la question
    d.text((87,219), f"{question}", fill=(0,0,0), font=font)

    # Ajouter les réponses
    for i, answer in enumerate(answers):
        d.text((10, 40 + i * 30), f"{chr(65+i)}) {answer}", fill=(0,0,0), font=font)

    # Sauvegarder l'image avec un nom unique pour chaque question
    img.save(f'images/Q{question_number}.png')

def generate_answer_image(correct_answer, justification, question_number):
    # Créer une image de base pour la réponse
    img = Image.new('RGB', (1080, 1080), color=(153, 204, 204))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    # Ajouter la réponse correcte et la justification
    d.text((10,10), f"Réponse correcte à la question {question_number}: {correct_answer}", fill=(0,0,0), font=font)
    if justification:
        d.text((10, 40), f"Justification: {justification}", fill=(0,0,0), font=font)

    # Sauvegarder l'image avec un nom unique pour chaque réponse
    img.save(f'images/R{question_number}.png')

def main():
    # Créer la fenêtre Tkinter
    root = tk.Tk()
    root.withdraw()  # Pour cacher la fenêtre principale

    # Demander le nombre de questions
    num_questions = simpledialog.askinteger("Questions", "Combien de questions souhaitez-vous créer ?", parent=root)

    # Pour chaque question, collecter les données et générer les images
    for i in range(num_questions):
        question = simpledialog.askstring("Question", f"Entrez le texte de la question {i+1} :", parent=root)
        num_answers = simpledialog.askinteger("Réponses", "Combien de réponses possibles ?", parent=root)

        answers = []
        for j in range(num_answers):
            answer = simpledialog.askstring("Réponse", f"Entrez la réponse {chr(65+j)} :", parent=root)
            answers.append(answer)

        correct_answer_index = simpledialog.askinteger("Réponse Correcte", "Quel est le numéro de la réponse correcte ?", parent=root)
        justification = simpledialog.askstring("Justification", "Entrez une justification pour la réponse correcte (facultatif) :", parent=root)

        # Générer les images avec des noms de fichiers uniques
        generate_question_image(question, answers, correct_answer_index, i+1)
        generate_answer_image(answers[correct_answer_index-1], justification, i+1)

main()
