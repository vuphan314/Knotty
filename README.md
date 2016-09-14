<h6>top

# KNOTTY
a computer algebra system for knot theory

## GOAL
to assist mathematicians with symbolic computation
- example: verification of some formulas in these papers (published in the Journal of Knot Theory and Its Ramifications):
	- [(2, 2*p + 1)-torus knot][paperTorus]
	- [figure-eight knot][paperFigure8]

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
- the Knotty webapp
	-	includes:
		- a text box: in which the user can type a source file
		- a button: when clicked will simplify the source file (by invoking the Knotty engine)
		- a preview box: in which the simplified file is shown
	-	is similar to the [SPARC webapp][sparcWeb]

## LINKS
- [kanban][trello]
- [documentation][onedrive]

## HOW TO CONTRIBUTE
Windows Command Prompt example:
```
git clone --recursive https://github.com/vuphan314/CS4365

git checkout brachzach
```

## SUBMODULE
The [generic parser][gitmodules] is developed by [Evgenii Balai][evgenii].

[paperTorus]:
http://www.math.ttu.edu/~rgelca/gs6.pdf
[paperFigure8]:
http://www.math.ttu.edu/~rgelca/jr5.pdf

[sparcWeb]:
http://ec2-52-25-88-7.us-west-2.compute.amazonaws.com/

[trello]:
https://trello.com/b/tCAfkInX
[onedrive]:
https://1drv.ms/f/s!Asl14HFRStFKgZlSAvo01o3toU9ISg

[gitmodules]:
https://github.com/vuphan314/CS4365/blob/master/.gitmodules
[evgenii]:
https://github.com/iensen
