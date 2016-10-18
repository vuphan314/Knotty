<h6>top

# KNOTTY
computer algebra system for knot theory

## GOAL
to assist mathematicians with symbolic computation
- example: verification of some formulas in these papers
  (published in the Journal of Knot Theory and
  Its Ramifications):
  - [(2, 2*p + 1)-torus knot][paperTorus]
  - [figure-eight knot][paperFigure8]

## DESCRIPTION
the Knotty system includes:
- the Knotty language: a programming language for math,
  specializing in knot theory
- the Knotty engine:
  - receives a Knotty program
  - returns a TeX program
- the Knotty webapp
  - includes:
    - a text box: in which the user can type a Knotty program
    - a button: when clicked will output a TeX program
      - by invoking the Knotty engine
    - a preview box: in which the TeX program is displayed

## LINKS
- [Notepad++ settings for Knotty language][linkNppXml]
- [tags][linkTags]
- [webapp][linkWebapp]
- [kanban][linkTrello]
- [documentation][linkOnedrive]

## FILES
`code/`
- `engine/`: Knotty engine (binary)
- `knengine/`: Knotty engine (source)
- `webapp/`: Knotty webapp

## SETUP GUIDE
- first time:
  - prerequisite installation:
    - [Git][gitDownload]
    - [Python][pythonDownload]
    - optional tex-to-pdf compilation:
      - [TeX Live][texDownload] (2 hours)
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
    git clone --recursive https://github.com/vuphan314/CS4365

    ```
- each following time:
  - directory browsing:
    ```
    cd/d <dir_of_repo>

    ```
    example: my `<dir_of_repo>` is `D:/repos/CS4365/`
  - update repository:
    ```
    git pull

    ```
  - browse tag:
    ```
    git checkout tags/v1.0.0

    ```

## CONTRIBUTION GUIDE
- switch branch:
  ```
  git checkout branchzach

  ```
- create/change your files
- tell Git:
  ```
  git add --all

  git commit --all --message "say what you did"

  git push

  ```

## ACKNOWLEDGEMENT
- [Git submodule][gitmodules]:
  - [generic parser][genparserSpec]
    - by [Evgenii Balai][evgeniiGithub]
- Python packages:
  - [SymPy][sympyHome]
  - [PyInstaller][pyinstallerHome]

[paperTorus]:
http://www.math.ttu.edu/~rgelca/gs6.pdf
[paperFigure8]:
http://www.math.ttu.edu/~rgelca/jr5.pdf

[linkNppXml]:
https://drive.google.com/file/d/0BwTmvmD-2eEwVmgtMFdhMXo4bVk/view?usp=sharing
[linkTags]:
https://github.com/vuphan314/CS4365/releases
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
[evgeniiGithub]:
https://github.com/iensen

[sympyHome]:
http://www.sympy.org/en/index.html
[pyinstallerHome]:
http://www.pyinstaller.org/
