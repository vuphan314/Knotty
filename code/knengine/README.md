<h6>top

# KNOTTY ENGINE (SOURCE)
part of Knotty system

## TEST GUIDE
- automatic unit-testing:
  ```
  kn_tester.py

  ```
- manual testing:
  ```
  kn_engine.py examples/demo.kn

  ```

## DESCRIPTION
- input: Knotty program
- output: TeX program
- includes:
  - parser:
    - input: Knotty program
    - output: Knotty parse-tree (as Python tuple)
  - translator:
    - input: Knotty parse-tree
    - output: Python program that:
      - is semantically equivalent to Knotty program
      - includes script to generate TeX program

## FILES
- `examples/`:
  - `*.kn` files are manually written
  - other files are generated
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
- prebuilt for Windows: `../engine/`
- to build from source for another OS:
  ```
  pyinstaller engine_man.spec --workpath=../engine/build/ --distpath=../engine/

  ```
