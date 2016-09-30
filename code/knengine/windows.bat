goto starting

:looping
    set fold=examples\
    set fil=demo
    set fils=demo, empty, oneliner, syntax
    for %%i in (%fil%) do (
        set base=%fold%%%~ni
        set kn=!base!.kn
        set kn_simplified=!base!_simplified.kn
        set txt=!base!_parsed_auto.txt

        set engine_cmd=%engine_py% !kn!
        set kn_engine_cmd=%kn_engine_py% !kn!

        REM !engine_cmd!
        REM type !kn_simplified!

        REM !kn_engine_cmd!
        REM type !txt!

        echo:
    )
    goto ending

:bundling
    set spec_man=build.spec
    set dist_path=..\dist\
    set knengine_path=%CD%

    set pyi_makespec=pyi-makespec %engine_py% -F
    set pyi_bundle=pyinstaller %spec_man% --workpath=. --dist_path=%distpath%

    %pyi_makespec%
    REM %pyi_bundle%

    REM cd %dist_path%
    REM %engine_exe%
    REM cd %knengine_path%

    goto ending

:starting
    @echo off
    cls
    setlocal enabledelayedexpansion

    set engine_exe=engine.exe
    set engine_py=engine.py
    set kn_engine_py=kn_engine.py

    REM goto looping
    goto bundling

:ending
    echo:
