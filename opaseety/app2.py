from pathlib import Path
from nicegui import ui
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
from opaseety.blend import ImageBlend
import matplotlib.pyplot as plt
import numpy as np

class DefaultColours:
    """Default colours provided for deepfrying"""
    red = ((254, 0, 2), (255, 255, 15))
    blue = ((36, 113, 229), (255,) * 3)

class ImageSet:

    SUPPORTED_EFFECTS = ['blur', 'dim', 'grayscale', 'bilevel', 'deepfry']

    def __init__(self):
        self.blend = ImageBlend([])
        self.set_id = None
        self.root = Path("./data")
        self.imgset_dir = None
        self.img_path = None

    def load(self, set_id: int) -> None:
        """Loads a particular set of images"""
        self.set_id = set_id
        self.imgset_dir = self.root/f"set{set_id}"
        self.img_path = self.root/Path(f"set{self.set_id}-final-blend.jpg")
        self.reset()

    def reset(self) -> None:
        """Resets the final blend, essentially removing all effects"""
        imgblend = ImageBlend.load_images(self.imgset_dir)
        blended_image = imgblend.equal_opacity()
        print("RESET")
        
        plt.imsave(self.img_path, blended_image)
        print("SAVE")
    
    def apply_effects(self, effects: list[str]) -> None:
        """Applies effects (blur, rotation, colors) to images"""
        im = Image.open(self.img_path)
        if 'blur' in effects:
            im = im.filter(ImageFilter.BLUR)
        if 'dim' in effects:
            enhancer = ImageEnhance.Brightness(im)
            im = enhancer.enhance(0.5)
        if 'grayscale' in effects:
            im = im.convert('L')
        if 'bilevel' in effects:
            im = im.convert('1')
        if 'deepfry' in effects:
            # Inspired by https://github.com/Ovyerus/deeppyer/blob/master/deeppyer/__init__.py
            im = im.convert('RGB')
            width, height = im.width, im.height
            im = im.resize((int(width ** .75), int(height ** .75)), resample=Image.Resampling.LANCZOS)
            im = im.resize((int(width ** .88), int(height ** .88)), resample=Image.Resampling.BILINEAR)
            im = im.resize((int(width ** .9), int(height ** .9)), resample=Image.Resampling.BICUBIC)
            im = im.resize((width, height), resample=Image.Resampling.BICUBIC)
            im = ImageOps.posterize(im, 8)

            # Generate colour overlay
            r = im.split()[0]
            r = ImageEnhance.Contrast(r).enhance(1.5)
            r = ImageEnhance.Brightness(r).enhance(1.5)

            r = ImageOps.colorize(r, DefaultColours.red[0], DefaultColours.red[1])

            # Overlay red and yellow onto main image and sharpen the hell out of it
            im = Image.blend(im, r, 0.75)
            im = ImageEnhance.Sharpness(im).enhance(100.0)
    
        im.save(self.img_path)

class Command:

    def __init__(self, img_el: ui.image):
        self.imageset = ImageSet()
        self.img_el = img_el
        self.effects = set()
        self.revealed = False
        self.images: list[ui.image] = []

    def update_set(self, set_id: int) -> None:
        self.imageset.load(set_id)

        # Update image
        self.img_el.source = Path(self.imageset.img_path)
        self.img_el.force_reload()

        # Reset state
        self.revealed = False

        # Remove existing images
        for img in self.images:
            img.delete()
        self.images = []

        # Reset checkboxes

    def update_effect_list(self, state: bool, effect: str):
        # Add blur to the imageset
        self.imageset.reset()

        if state:
            self.effects.add(effect)
        else:
            self.effects.remove(effect)

        print(self.effects, effect, state)
        self.imageset.apply_effects(self.effects)

        self.img_el.force_reload()

    def reveal(self):
        """Reveal the answers"""
        if not self.revealed:
            for item in self.imageset.imgset_dir.iterdir():
                self.images.append(ui.image(str(item)).style('width: 600px; height: 600px;'))
            self.revealed = True

# class GUI:
#     """Represents the GUI web interface"""

#     def __init__(self):
        
#         # Components
#         self.effect_checkboxes = []
        
        
#         self.img_answers = []

#         # 
#         self.set_input = []

#         # Buttons
#         self.btn_reveal = []
#         self.btn_update_set = []
    
#     def new(self) -> None:
#         pass


# 1. Visit url /set/#
# 2. Toggle effects - this should dynamically update images, which means need to recreate final-blend from input images
# 3. Timer
# 4. Answer button

if __name__ in {"__main__", "__mp_main__"}:
    command = Command(img_el=None)
    
    ui.label('Opaseety!')

    with ui.row().style('display: flex; width: 100%;'):
        with ui.column().style('position: sticky; top: 0;'):
            # Set ID textbox
            with ui.row():
                txtbox = ui.input(label='Set ID')
                ui.button('Submit', on_click=lambda: command.update_set(txtbox.value))

            # Command & Image element

            img_el = ui.image()
            img_el.style('width: 600px; height: 600px')
            command.img_el = img_el
            
            # Checkboxes
            checkboxes: dict[str, ui.checkbox] = {}
            with ui.row():
                for effect in command.imageset.SUPPORTED_EFFECTS:
                    print(effect)
                    ui.label(effect.title())
                    checkboxes[effect] = ui.checkbox()
                    checkboxes[effect].on('click', lambda e, effect=effect: command.update_effect_list(e.sender.value, effect))
        with ui.column():
            ui.button('Answer', on_click=command.reveal)

    # with ui.splitter().style('width: 100%; height: 100%; display: flex;') as splitter:
    #     with splitter.before:
    #         # Set ID textbox
    #         txtbox = ui.input(label='Set ID')
    #         ui.button('Submit', on_click=lambda: command.update_set(txtbox.value))

    #         # Command & Image element

    #         img_el = ui.image()
    #         img_el.style('width: 500px; height: 500px')
    #         command.img_el = img_el
            
    #         # Checkboxes
    #         checkboxes: dict[str, ui.checkbox] = {}
    #         with ui.row():
    #             for effect in command.imageset.SUPPORTED_EFFECTS:
    #                 print(effect)
    #                 ui.label(effect.title())
    #                 checkboxes[effect] = ui.checkbox()
    #                 checkboxes[effect].on('click', lambda e, effect=effect: command.update_effect_list(e.sender.value, effect))

    #     with splitter.after:
    #         # Answer
    #         ui.button('Answer', on_click=command.reveal)

    ui.run()