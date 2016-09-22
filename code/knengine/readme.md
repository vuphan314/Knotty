# KNOTTY ENGINE
part of Knotty system

## TEST GUIDE
- automatic unit-testing:
	```
	py kn_tester.py

	```
- manual testing: double-click 
	- `kn_engine.py` 
	- `examples/demo_man.py`

## HOW THE ENGINE WORKS
-	input: source Knotty program
- output: simplified Knotty program
- includes
	-	parser:
		- input: source Knotty program
		- output: Knotty parse-tree (as Python nested list)
	- translator:
		- input: Knotty parse-tree
		- output: Python program that
			-	is equivalent to source Knotty program
			- includes script to generate simplified Knotty program

## FILES
- `kn_engine.py`: Knotty engine
- `kn_tester.py`: unit-tester
- `examples/`: note that
	- suffix `_man`: manually written
	- suffix `_auto`: automatically written
- `knparser/`
	-	`kn_parser.py`: Knotty parser
	- `kn_lexicon.txt`: Knotty parsing-expression lexicon
	- `kn_grammar.txt`: Knotty parsing-expression grammar
- `kntranslator/`:
	-	`kn_lib.py`: Knotty library
