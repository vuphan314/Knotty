<h6>top

# ENGINE (BINARY)

## DESCRIPTION
Windows `engine.exe`:
- accepts any relative/absolute path
  to any syntactically correct Knotty program
- example session with Command Prompt:
  ```
  engine.exe examples/demo.kn

  ```
  - optional tex-to-pdf compilation:
    ```
    cd examples/

    latexmk -pdf demo.tex

    latexmk -c demo.tex

    ```
  - WARNING: the files `demo.(py|tex|pdf)`
    will be OVERWRITTEN/created
    WITHOUT CONFIRMATION

## SOURCE
`../knengine/`
