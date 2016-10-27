<h6>top

# ENGINE (BINARY)
part of Knotty system

## DESCRIPTION
Windows standalone binary file `engine.exe`:
- accepts any relative/absolute path
  to any correct Knotty program

## USAGE
- method 1:
  - download [`engine.exe`][engineDownload]
  - move downloaded `engine.exe` to directory `C:/Windows/`
    (or anywhere else in environment variable `%PATH%`)
  - browse directory containing Knotty file
    - example:
      `D:/repos/CS4365/code/engine/examples/`
  - in File Explorer window:
    - click button `File` (top-left corner)
      - click button `Open command prompt`
  - in Command Prompt window, type:
    ```
    engine demo.kn

    ```
- method 2:
  - Command Prompt:
    ```
    cd ./examples/

    call "../engine.exe" demo.kn

    ```
    - optional tex-to-pdf compilation:
      ```
      latexmk -pdf demo.tex

      latexmk -c demo.tex

      ```
- WARNING: the files `demo.(py|tex|pdf)`
  will be OVERWRITTEN/created
  WITHOUT CONFIRMATION

## SOURCE
`../knengine/`

[engineDownload]:
https://github.com/vuphan314/CS4365/blob/master/code/engine/engine.exe?raw=true
