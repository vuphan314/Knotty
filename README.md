<h6>top

# KNOTTY
computer algebra system for knot theory

## GOAL
to assist mathematicians with symbolic computation
- example: verification of some formulas in these papers
  (published in the Journal of Knot Theory
  and Its Ramifications):
  - [(2, 2*p + 1)-torus knot][paperTorus]
  - [figure-eight knot][paperFigure8]

## DESCRIPTION
the Knotty system includes:
- the Knotty language: a programming language for math,
  specializing in knot theory
- the Knotty engine:
  - receives a Knotty program
  - returns a TeX program
- the Knotty web application:
  - includes:
    - a text box: in which the user can type a Knotty program
    - a button: when clicked will generate a TeX program
      - by invoking the Knotty engine
    - a preview box: in which the TeX program is displayed

## FILES
`code/`
- `webapp/`: web application
- `engine/`: engine (binary)
- `knengine/`: Knotty engine (source)

## LINKS
- [web application][linkWebapp]
- [demo videos][linkPlaylist]
- GitHub
  - [releases][linkTags]
  - [issues][linkIssues]
- scrum
  - [kanban][linkTrello]
  - [documentation][linkOnedrive]
- [Notepad++ settings for Knotty language][linkNppXml]

## USAGE
- first time:
  - prerequisite installation:
    - [Git][gitDownload]
    - [Python][pythonDownload]
    - optional tex-to-pdf compilation:
      - [TeX Live][texDownload] (~ 2 hours)
      - [Sumatra PDF][sumatraDownload]
  - command-line interface:
    ```
    pip install mpmath

    pip install sympy

    pip install pyinstaller

    ```
  - directory browsing (Windows Command Prompt):
    ```
    cd/d <parent_dir_of_repo>

    ```
    example: my `<parent_dir_of_repo>` is `D:/repos/`
  - repository cloning:
    ```
    git clone --recursive https://github.com/vuphan314/Knotty

    ```
- each following time:
  - directory browsing:
    ```
    cd/d <dir_of_repo>

    ```
    example: my `<dir_of_repo>` is `D:/repos/Knotty/`
  - update repository:
    ```
    git pull --recurse-submodules

    ```
  - show tags:
    ```
    git tag
    
    ```
  - browse tag:
    ```
    git checkout tags/<tag>

    ```
    example: latest `<tag>` is `v1.2.0`

## CONTRIBUTORS
- [Vu Phan][vuCV] (regular)
  - language
  - engine
- Zachariah Grummons (honorary)
  - webapp

## ACKNOWLEDGEMENT
- [Git submodules][gitmodules]:
  - [generic parser][genparserSpec]
    - by Evgenii Balai
- Python packages:
  - [SymPy][sympyHome]
  - [PyInstaller][pyinstallerHome]
- TeX packages:
  - geometry
  - amsmath
  - breqn
- Knotty language influenced by: LED, SequenceL, Python, SQL
- design document influenced by [SE2 Machine Learning Team][teamML]

[paperTorus]:
http://www.math.ttu.edu/~rgelca/gs6.pdf
[paperFigure8]:
http://www.math.ttu.edu/~rgelca/jr5.pdf

[vuCV]:
https://github.com/vuphan314/VU_PHAN/blob/master/README.md#top

[linkPlaylist]:
https://www.youtube.com/playlist?list=PLIJKsTidP3ztqjhlB3Rv1E5hAecfz8VNv
[linkNppXml]:
https://drive.google.com/file/d/0BwTmvmD-2eEwVmgtMFdhMXo4bVk/view?usp=sharing
[linkTags]:
https://github.com/vuphan314/CS4365/releases
[linkIssues]:
https://github.com/vuphan314/CS4365/issues
[linkWebapp]:
http://99.64.48.184/Knotty
[linkTrello]:
https://trello.com/b/tCAfkInX
[linkOnedrive]:
https://1drv.ms/f/s!Asl14HFRStFKgZlSCNCMQ4qIWcOoIg

[gitDownload]:
https://git-scm.com/downloads
[pythonDownload]:
https://www.python.org/downloads/
[texDownload]:
https://www.tug.org/texlive/acquire-netinstall.html
[sumatraDownload]:
https://www.sumatrapdfreader.org/download-free-pdf-viewer.html

[gitmodules]:
https://github.com/vuphan314/CS4365/blob/master/.gitmodules
[genparserSpec]:
https://github.com/iensen/genparser/blob/master/docs/main/astgen.pdf

[sympyHome]:
http://www.sympy.org/en/index.html
[pyinstallerHome]:
http://www.pyinstaller.org/

[teamML]:
https://github.com/ASAAR/SE2-KaggleComp
