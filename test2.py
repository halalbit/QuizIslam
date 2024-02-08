from PIL import Image, ImageDraw, ImageFont

def get_text_size(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)

def generate_image(question, responses, image_name):
    # Taille de l'image
    image_width = 1080
    image_height = 1080

    # Création de l'image avec fond blanc
    image = Image.new("RGB", (image_width, image_height), "black")

    # Initialisation de l'objet Draw pour dessiner sur l'image
    draw = ImageDraw.Draw(image)

    # Définition de la police
    font = ImageFont.truetype("CormorantInfant-Regular.ttf", 60)  # Modifier le chemin si nécessaire

    # Obtention de la taille du texte de la question
    text_width, text_height = get_text_size(question, font)

    # Calcul de la position pour centrer le texte verticalement
    x_question = 50
    y_question = (image_height - (text_height + len(responses) * 30)) / 2

    # Affichage de la question
    draw.text((x_question, y_question), question, fill="white", font=font)

    # Coordonnées de départ pour les réponses
    x_response = 50
    y_response = y_question + text_height + 20

    # Affichage des réponses
    for index, response in enumerate(responses, start=1):
        draw.text((x_response, y_response), f"Réponse {index}: {response}", fill="black", font=font)
        y_response += 30

    # Sauvegarde de l'image
    image.save(image_name)

# Exemple d'utilisation
question = "Comment s’appelle la source d’eau à la \nMecque qui fut un miracle pour Ismail عليه السلام ?"
responses = ["Paris", "Londres", "Berlin"]
solution = "La réponse correcte est Paris."

# Génération de l'image avec la question et les réponses
generate_image(question, responses, "question_responses.png")

# Génération de l'image avec la question, les réponses et la solution
responses_with_solution = responses + [solution]
generate_image(question, responses_with_solution, "question_responses_solution.png")
