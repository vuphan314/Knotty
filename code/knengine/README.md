# KNOTTY ENGINE (SOURCE)
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
- input: Knotty program
- output: simplified Knotty program
- includes
  - parser:
    - input: Knotty program
    - output: Knotty parse-tree (as Python nested list)
  - translator:
    - input: Knotty parse-tree
    - output: Python program that
      - is equivalent to Knotty program
      - includes script to generate simplified Knotty program

## FILES
- `examples/`: note that
  - suffix `_man`: manually written
  - suffix `_auto`: automatically written
- `kn_tester.py`: Knotty unit-tester
- `kn_engine.py`: Knotty engine
- parsing:
  - `kn_lexicon.txt`: Knotty parsing-expression lexicon
  - `kn_grammar.txt`: Knotty parsing-expression grammar
  - `kn_parser.py`: Knotty parser
- translating:
  - `kn_lib.py`: Knotty library
  - `kn_translator`: Knotty translator

## BINARY
`../engine/`
