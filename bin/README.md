<h6>top

# KNOTTY ENGINE (BINARY)
part of Knotty system

## DESCRIPTION
Windows standalone binary file:
- accepts relative/absolute path to Knotty program
- invocation:
  ```
  $ knotty

  Knotty engine v1.4.0 built 2016-11-13

  usage: knotty [-h] [-f] [-k] Knotty_file

  positional arguments:
    Knotty_file

  optional arguments:
    -h, --help   show this help message and exit
    -f, --force  OVERWRITE existing .py and .tex files
    -k, --keep   keep .py file

  Time taken: 0.01562356948852539 seconds.

  ```
  - possible error:
    ```
    $ knotty
    'knotty' is not recognized as an internal or external command,
    operable program or batch file.

    ```
    - solution:
      ```
      $ "<path_to_knotty_exe>"

      ```
      - example:
        ```
        $ "C:/Users/Vu/Downloads/knotty"

        ```

## USAGE
- download latest [`knotty.exe`][linkReleases]
- move downloaded `knotty.exe` to directory `C:/Windows/`
  (or anywhere else in environment variable `%PATH%`)
- browse directory containing Knotty file
  - example: `../examples/`
- in File Explorer window:
  - click button `File` (top-left corner)
    - click button `Open command prompt`
- in Command Prompt window, enter:
  ```
  knotty -f -k demo.kn

  ```
  - optional tex-to-pdf compilation:
    ```
    latexmk -pdf demo.tex

    latexmk -c demo.tex

    ```

## SOURCE
`../src/`

[linkReleases]:
https://github.com/vuphan314/Knotty/releases
