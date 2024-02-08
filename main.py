from PIL import Image, ImageDraw, ImageFont


# Fonction pour générer une image avec la question et les réponses
def generate_image(question, responses, image_name):
    # Taille de l'image
    image_width = 1080
    image_height = 1080

    # Création de l'image avec fond blanc
    image = Image.new("RGB", (image_width, image_height), "black")

    # Initialisation de l'objet Draw pour dessiner sur l'image
    draw = ImageDraw.Draw(image)

    # Définition de la police
    font = ImageFont.truetype("CormorantInfant-Regular.ttf", 20)  # Modifier le chemin si nécessaire

    # Coordonnées de départ pour la question
    x_question = 540
    y_question = 50

    # Affichage de la question
    draw.text((x_question, y_question), question, fill="white", font=font, align="center")

    # Coordonnées de départ pour les réponses
    x_response = 50
    y_response = 100

    # Affichage des réponses
    for index, response in enumerate(responses, start=1):
        draw.text((x_response, y_response), f"Réponse {index}: {response}", fill="black", font=font)
        y_response += 30

    # Sauvegarde de l'image
    image.save(image_name)

# Exemple d'utilisation
question = "Quelle est la capitale de la France ?"
responses = ["Paris", "Londres", "Berlin"]
solution = "La réponse correcte est Paris."

# Génération de la première image avec la question et les réponses
generate_image(question, responses, "question_responses.png")

# Génération de la deuxième image avec la question, les réponses et la solution
responses_with_solution = responses + [solution]
generate_image(question, responses_with_solution, "question_responses_solution.png")