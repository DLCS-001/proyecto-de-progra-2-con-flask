from flask import Flask, render_template, request, redirect, url_for
import formulario

app = Flask(__name__)

formulario.crear_tabla()


VIDEOS = {
    "Flask": [
        {
            "id": 1,
            "title": "Que es Flask?",
            "description": "Video recomendado",
            "src": "https://drive.google.com/file/d/1aX8fBDX9OjgL-ooYafrZd3Wi-rCT8wfh/view?usp=sharing"
        },
        {
            "id": 2,
            "title": "Introduccion a flask",
            "description": "Video recomendado",
            "src": "https://drive.google.com/file/d/13pQw8BMBLZMj7Fs2qPdZfHmhqoprMJ4c/view?usp=sharing"
        },
        {
            "id": 3,
            "title": "Nuestro primer Hello Desde Flask!",
            "description": "Video recomendado",
            "src": "https://drive.google.com/file/d/1WK5bZP1Ykc9stjHIQ-BXUKMGOGDxSStl/view?usp=sharing"
        },
        {
            "id": 4,
            "title": "Aprende conceptos antes que código",
            "description": "Video recomendado",
            "src": "https://drive.google.com/file/d/1u-w13CmjDpjS406kukER9myPlBIqU1-d/view?usp=sharing"
        }
    ],
    "python": [
        {
            "id": 5,
            "title": "Python en 8 Minutos",
            "description": "Video recomendado",
            "src": "https://drive.google.com/file/d/18FIH-59hwHpAgoPh3qWWcmfL2VgDsP8K/view?usp=sharing"
        },
        {
            "id": 6,
            "title": "Aplicación Web con Python",
            "description": "Video recomendado",
            "src": "https://drive.google.com/file/d/1RuxRnZHFlj3XcZVup293E0WGlu793qES/view?usp=sharing"
        },
        {
            "id": 7,
            "title": "¿Como funciona una aplicacion web?",
            "description": "Video recomendado",
            "src": "https://drive.google.com/file/d/1P6yb6wiCuqoWm0SrA4bAhjMmHWy5OWV8/view"
        },
        {
            "id": 8,
            "title": "¿Qué es una API?",
            "description": "Video recomendado",
            "src": "https://drive.google.com/file/d/1039d18BekjXHMm1einBxZWtuomwxa_fT/view"
        }
    ],
    "anime": [
        {
            "id": 9,
            "title": "Kimetsu No Yaiba",
            "description": "!Estreno¡",
            "src": "https://drive.google.com/file/d/1k0ZI6mz0wa1U1p1blJ_2raY9ecTenBCL/view?usp=sharing"
        },
        {
            "id": 10,
            "title": "Black Clover",
            "description": "!Estreno¡",
            "src": "https://drive.google.com/file/d/1Oe-aHOj3AEaojabDgiZO8TIG_-TOfisV/view?usp=drive_link"
        },
        {
            "id": 11,
            "title": "Jujutsu Kaisen",
            "description": "!Estreno¡",
            "src": "https://drive.google.com/file/d/1MbAbfkutftKvtGfTOOMBRsl1ziqd5kUW/view?usp=drive_link"
        },
        {
            "id": 12,
            "title": "Boku No Hero Academia",
            "description": "!Estreno¡",
            "src": "https://drive.google.com/file/d/1pi2YOTGl5x7l8CjhoXQpcuU2SnYDCIBQ/view?usp=drive_link"
        },
        {
            "id": 13,
            "title": "Re-Zero",
            "description": "!Estreno¡",
            "src": "https://drive.google.com/file/d/1efKJ7ItNGfO-xCd61JeXMiyUlTxghSVM/view?usp=drive_link"
        }
    ]
}


def drive_embed_url(drive_url):
    if "/file/d/" in drive_url:
        file_id = drive_url.split("/file/d/")[1].split("/")[0]
        return f"https://drive.google.com/file/d/{file_id}/preview"
    return drive_url


@app.route("/")
def index():
    
    categories = {}
    for category, vids in VIDEOS.items():
        categories[category] = []
        for v in vids:
            embed = drive_embed_url(v["src"])
            categories[category].append({
                **v,
                "embed_url": embed
            })
    return render_template("index.html", videos=categories)


@app.route("/formulario", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        nombre = request.form["nombre"]
        estrellas = int(request.form["estrellas"])
        experiencia = request.form["experiencia"]

        
        formulario.guardar_valoracion(nombre, estrellas, experiencia)

        return redirect(url_for("gracias"))  

    return render_template("formulario.html")


@app.route("/gracias")
def gracias():
    return "<h2>¡Gracias por enviar tu valoración! </h2><a href='/'>Volver a inicio</a>"


@app.route("/admin/valoraciones")
def ver_valoraciones():
    import sqlite3
    conn = sqlite3.connect("Formulario.db")
    c = conn.cursor()
    c.execute("SELECT nombre, estrellas, experiencia FROM valoraciones ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return render_template("ver_valoraciones.html", valoraciones=data)


if __name__ == "__main__":
    app.run(debug=True)