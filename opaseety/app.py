"""app.py

Main entry point for the Flask app
"""

from flask import Flask, request, render_template
from io import StringIO
from pathlib import Path
from PIL import Image, ImageFilter
import sys

app = Flask(__name__)

effects = {
    
}

def img_filter(img_path: Path) -> None:
    img = Image.open(img_path)
    img = img.filter(ImageFilter.BLUR)
    img.save(img_path)
    return

@app.route("/")
def hello_world():
    return "<p>Opaseety</p>"

@app.route("/set/<int:set_id>", methods=['GET', 'POST'])
def show_set(set_id: int):
    # Look for './data/set<set_id>-final-blend.jpg'
    # if it doesn't exist, recreate it

    if request.method == 'POST':
        print(request.form.getlist('hello'))
        # Apply the image processing filters as needed
        img_filter(Path(f"./opaseety/static/set{set_id}-final-blend.jpg"))
      
    # Make effects globally accessible
    return render_template('set.jinja', set=set_id, effects=['Color', 'Deep Fried', 'Rotate'])