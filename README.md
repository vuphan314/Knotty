<!-- <h6>top -->

# KNOTTY
computer algebra system for knot theory:
assisting mathematicians with symbolic computation

## EXAMPLES
- input [Knotty file][papersKN] ([language specification][specPDF])
- output [TeX file][papersTEX]
  - [PDF file][papersPDF]

## DESCRIPTION
the Knotty system includes:
- the Knotty language: a programming language for math,
  specializing in knot theory
- the Knotty engine:
  - receives a Knotty program
  - returns a TeX program
- the Knotty web application:
  - includes:
    - a text box: in which the user can type
      a Knotty program
    - a button: when clicked will generate a TeX program
      - by invoking the Knotty engine
    - a preview box: in which the TeX program is displayed

## FILES
- `examples/`
- web application:
  - `webapp/`
- engine:
  - `bin/`
  - `src/`
- language:
  - `spec/`

## LINKS
- [web application][linkWebapp]
- videos: [YouTube][linkYouTube]
- GitHub:
  - [releases][linkTags]
  - [issues][linkIssues]
- scrum:
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

    ```
  - directory browsing (Windows Command Prompt):
    ```
    cd/d <parent_dir_of_repo>

    ```
    example: my `<parent_dir_of_repo>` is `D:/github/`
  - repository cloning:
    ```
    git clone --recursive https://github.com/vuphan314/Knotty

    ```
- each following time:
  - directory browsing:
    ```
    cd/d <dir_of_repo>

    ```
    example: my `<dir_of_repo>` is `D:/github/Knotty/`
  - update repository:
    ```
    git pull --recurse-submodules

    ```
  - show tags:
    ```
    git tag -n

    ```
  - browse tag:
    ```
    git checkout tags/<tag>

    ```
    example: latest `<tag>` is `v2.0.0`

## CONTRIBUTORS
- [Vu Phan][linkVu] (regular)
  - language
  - engine
- [Zachariah Grummons][linkZach] (honorary)
  - web application

## ACKNOWLEDGEMENT
- [Git submodules][gitmodules]:
  - [generic parser][genparserSpec]
    - by Evgenii Balai
  - [PyInstaller][pyinstallerHome]
- Python package:
  - [SymPy][sympyHome]
- Knotty language influenced by: LED, SequenceL, Python, SQL
- design document influenced by
  [SE2 Machine Learning Team][teamML]

[specPDF]:
https://github.com/vuphan314/Knotty/blob/master/spec/spec.pdf

[papersKN]:
https://github.com/vuphan314/Knotty/blob/master/examples/papers.kn
[papersTEX]:
https://github.com/vuphan314/Knotty/blob/master/examples/papers.tex
[papersPDF]:
https://github.com/vuphan314/Knotty/blob/master/examples/papers.pdf

[linkVu]:
https://vuphan314.github.io/
[linkZach]:
https://github.com/twibird

[linkYouTube]:
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
