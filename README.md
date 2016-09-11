# CS4365
Knotty: a computer algebra system for knot theory

## KANBAN BOARD
[Trello][trello]

## DESCRIPTION
Knotty system includes:
- Knotty language: a programming language for math, specializing in knot theory
- Knotty engine
	- receives a source file written in Knotty language, such as:
	```
	let p(x) = (1 + x) * (x^-1 + 1) - 3
  
  let c = p(1)
	```
	- returns a target file written in Knotty language, such as:
	```
  let p(x) = x - 1 + x^-1
  
  let c = 1
  ```
- Knotty webapp includes
	- a text box, in which the user can type a source file
	- a button, when clicked will rewrite the source file
	- a preview box, in which the target file is shown

## SUBMODULE
The [generic parser][genparser] (`src/genparser/`) is developed by Evgenii Balai.

[trello]:
https://trello.com/b/tCAfkInX
[genparser]:
https://github.com/iensen/genparser
