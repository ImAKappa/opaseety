# opaseety

[![PyPI - Version](https://img.shields.io/pypi/v/opaseety.svg)](https://pypi.org/project/opaseety)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/opaseety.svg)](https://pypi.org/project/opaseety)

An image guessing game.

-----

## Table of Contents

- [opaseety](#opaseety)
  - [Table of Contents](#table-of-contents)
  - [How to play](#how-to-play)
  - [Contributing](#contributing)
  - [Images](#images)
  - [Installation](#installation)
  - [TODO](#todo)
  - [IDEAS](#ideas)
  - [License](#license)


## How to play

```bash
python opaseety.py 
```

## Contributing

Requires [hatch](https://hatch.pypa.io/latest/), a modern Python project manager.

```
git clone https://github.com/ImAKappa/opaseety.git
```

```
cd opaseety
```

Install pip dependencies and create virtual environment with:

```
hatch shell
```

Run the project using:

```
python .\opaseety\opaseety.py -i .\data\
```

## Images


Lorem Picsum: https://picsum.photos/
    Request specific size: https://picsum.photos/600
    Request specific image: https://picsum.photos/id/21/600 
Blending images: https://www.codespeedy.com/python-pil-image-blend-method/

## Installation

```console
pip install opaseety
```

## TODO

Not in any particular order:

1. Unit tests - currently no unit tests :P
2. Web app - using flask or something, create a simple web app where players can see the blended images, and type in guesses. It records the number of attempts, the list of guesses. It should also show the number of blended images
3. Experiment with different blending techniques? Right now it just blends all images "equally", but doesn't really take into account variations in color, features, etc. In other words, some combinations of images are more difficult than others. That's ok if a lot of people are playing, then each player/team is only really competiting against the population of players. But it's more unbalanced in small group settings where you only present 1-2 blended images per player/team, so you want to make sure the blends are somewhat 'fair' - alternatively, just have every player/team paly against the same set - but that's boring and you can't have other players/teams engage as the audience lest you give away the answers.
4. Update data sources - right now I manually handpick images from https://picsum.photos/. Is there a better (more scalable) way to obtain pictures? There's a REST api for https://picsum.photos/, maybe we could use that to download pictures, although we'd have to be carefully about getting a good variety, not downloding the same/similar pictures over and over again
5. Add `/data` folder to .gitignore. Or maybe rename it to `examples` or something? Only need to push 1-2 example sets of images so contributors can clone and easily run the code. Otherwise, it doesn't make sense to save many sets of images to the repo.

Interesting, but not important:

1. Can we create an "AI" player (like a ResNet or something), i.e. can you beat the bot? Could be an interesting research project, there are a few computer vision models that can detect individual images from a superimposed set of images:

- [Deep Adversarial Decomposition: A Unified Framework for Separating
Superimposed Images (Zhou et al. 2020)](https://openaccess.thecvf.com/content_CVPR_2020/papers/Zou_Deep_Adversarial_Decomposition_A_Unified_Framework_for_Separating_Superimposed_Images_CVPR_2020_paper.pdf), and [GitHub Pytorch repo here](https://github.com/jiupinjia/Deep-adversarial-decomposition)
- [Single Image Layer Separation using Relative Smoothness](https://yu-li.github.io/paper/li_cvpr14_layer.pdf) - this one's only kind of related to the problem

## IDEAS

UI
- [ ] some boxes to check for added difficulty

Skulls

- [ ] another idea, distortions and lens filters
- [ ] also quality 480p pics
- [ ] first thought is colour filter
- [ ] just layer the whole thing w different colour filters, would make it v hard

## License

`opaseety` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
