import sys
import os

SITE_DATA_PATH = "./Site/data"

project = sys.argv[1]

title = os.path.split(project)[1]

# Wenn der Kreis am Ende eine komische Größe hat, kann man das hier ausgleichen
# Die Länge des Videos sollte nach dem Multiplikator ca. auf 1,5h kommen
duration_factor = 1

with open(os.path.join(project, "motion_shot-avg.txt")) as file:
    shots = [line.strip().split("\t") for line in file if line]
    
shots = [{"motion": float(m), "duration": int(d)*duration_factor*duration_factor} for m, d in shots]

with open(os.path.join(project, "colors.txt")) as file:
    colors = [line.strip().split(", ") for line in file if line]

colors = [[int(x) for x in c] for c in colors]
total = sum(c[3] for c in colors)
colors = [{"rgb": c[:3], "%":c[3]/total} for c in colors]


with open(os.path.join(project, "chapters.txt")) as file:
    chapters = [int(line.strip())*duration_factor for line in file if line]

movie_duration = chapters[-1]

movie = {"colors": colors, "duration": movie_duration*duration_factor}


with open(os.path.join(project, "chapter_colors.txt")) as file:
    chapter_colors = [line.strip() for line in file if line]

chapter_colors = [chapter.split(" _ ") for chapter in chapter_colors]
chapter_colors = [[c.split(", ") for c in colors] for colors in chapter_colors]
chapter_colors = [[[int(c) for c in color] for color in colors] for colors in chapter_colors]
totals = [sum([c[3] for c in color]) for color in chapter_colors]
chapter_colors = [[
    {
        "rgb": c[:3],
        "%": 0.4 * c[3] / totals[i]
    } for c in chapter
]
    for i, chapter in enumerate(chapter_colors)
]

stills_orig = os.listdir(os.path.join(project, "100_stills"))

stills = [x.split("_")[1].split(".")[0] for x in stills_orig]
stills = ["still_%07d.jpg" % (int(x)*duration_factor) for x in stills]
import json
data = {
    "movie": movie, 
    "chapters": chapters, 
    "chaptercolors": chapter_colors, 
    "shots": shots,
    "stills": stills,
    "title": title,
    "height": 105
}

if not os.path.exists(os.path.join(SITE_DATA_PATH, "movies", title)):
    os.mkdir(os.path.join(SITE_DATA_PATH, "movies", title))

with open(os.path.join(SITE_DATA_PATH, "movies", title, "data.json"), "w") as file:
    json.dump(data, file, indent="\t")

# Add Video to List
with open(os.path.join(SITE_DATA_PATH, "movies.json"), "r") as file:
    movies = json.load(file)

with open(os.path.join(SITE_DATA_PATH, "movies.json"), "w") as file:
    movies["movies"].update({title: os.path.join("movies", title, "data.json")})
    json.dump(movies, file, indent="\t")


# Move Stills
import shutil
if not os.path.exists(os.path.join(SITE_DATA_PATH, "movies", title, "stills")):
    os.mkdir(os.path.join(SITE_DATA_PATH, "movies", title, "stills"))

for orig, target in zip(stills_orig, stills):
    # print(t)
    shutil.copy(os.path.join(project, "100_stills", orig), os.path.join(SITE_DATA_PATH, "movies", title, "stills", target))