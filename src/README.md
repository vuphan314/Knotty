<h6>top

# KNOTTY ENGINE (SOURCE)
part of Knotty system

## TEST GUIDE
- automatic unit-testing:
  ```
  kn_testing.py

  ```
- manual testing:
  ```
  kn_engine.py -f -k ../examples/demo.kn

  ```

## DESCRIPTION
- input: Knotty program
- output: TeX program
- includes:
  - parsing module:
    - input: Knotty program
    - output: Knotty parse-tree (as Python tuple)
  - translating module:
    - input: Knotty parse-tree
    - output: Python program that:
      - is semantically equivalent to Knotty program
      - includes script to generate TeX program

## FILES
- `kn_testing.py`: unit-testing module
- `kn_engine.py`: Knotty engine
- parsing:
  - `kn_lexicon.txt`: parsing-expression lexicon
  - `kn_grammar.txt`: parsing-expression grammar
  - `kn_parsing.py`: parsing module
- translating:
  - `kn_lib.py`: Knotty library
  - `kn_translating`: translating module

## BINARY
- prebuilt for Windows/Ubuntu: `../bin/`
- to build from source for another OS:
  ```
  python3 pyinstaller/pyinstaller.py knotty_man.spec

  ```
  - if you have successfully built a binary for your OS,
    then please contribute the binary with a pull request
    - we appreciate your help
