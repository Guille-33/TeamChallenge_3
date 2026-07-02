import os
import getpass
import pandas as pd

movies = pd.read_csv("data/movies_with_overview_and_homepage.csv")


from google import genai

if not os.getenv("GEMINI_API_KEY"):
    os.environ["GEMINI_API_KEY"] = getpass.getpass(
        "Pega aquí tu GEMINI_API_KEY (input oculto): "
    )

print("GEMINI_API_KEY configurada:", "sí" if os.getenv("GEMINI_API_KEY") else "no")

client = genai.Client()
MODEL = "gemini-3-flash-preview"


def summarize_overview_es(overview, title=""):
    overview = overview.strip()
    if not overview:
        raise ValueError("Cadena vacía")
    else:
        return client.models.generate_content(
            model=MODEL,
            contents=f"Resume el siguiente texto en un máximo de 2 frases:\n{overview}"
        ).text
    
movies["overview_es"] = ""
for fila in movies.itertuples():
    if pd.isna(fila.overview) or not str(fila.overview).strip():
        continue                    # me salto filas sin sinopsis
    movies.at[fila.Index, "overview_es"] = summarize_overview_es(str(fila.overview))

movies.to_csv("data/movies_with_overview_and_homepage.csv", index=False)

print(movies)