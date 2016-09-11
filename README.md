# KNOTTY
a computer algebra system for knot theory

## KANBAN BOARD
[Trello][trello]

## HOW TO CONTRIBUTE
Windows Command Prompt example:
```
git clone --recursive https://github.com/vuphan314/CS4365

git checkout brachzach
```

## DESCRIPTION
the Knotty system includes:
- the Knotty language: a programming language for math, specializing in knot theory
- the Knotty engine:
	- receives a source file (in the Knotty language)
		-	example:
			```
			let p(x) = (1 + x) * (x^-1 + 1) - 3

			let c = p(1)
			```
	- returns a simplified file (in the Knotty language)
		-	example:
			```
			let p(x) = x - 1 + x^-1

			let c = 1
			```
- the Knotty webapp includes:
	- a text box: in which the user can type a source file
	- a button: when clicked will simplify the source file (by invoking the Knotty engine)
	- a preview box: in which the simplified file is shown

## SUBMODULE
The [generic parser][genparser] (`code/engine/parser/genparser/`) is developed by Evgenii Balai.

[trello]:
https://trello.com/b/tCAfkInX
[thisRepo]:
https://github.com/vuphan314/CS4365
[genparser]:
https://github.com/iensen/genparser
