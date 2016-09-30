goto starting

:body
    set fold=examples\
    set fil=demo
    set fils=demo, empty, oneliner, syntax
    for %%i in (%fils%) do (
        set base=%fold%%%~ni
        set kn=!base!.kn
        set kn_simplified=!base!_simplified.kn
        set txt=!base!_parsed_auto.txt

        set engine_cmd=%engine_py% !kn!
        set kn_engine_cmd=%kn_engine_py% !kn!
        
        echo !base!
        
        !engine_cmd!
        type !kn_simplified!

        REM !kn_engine_cmd!
        REM type !txt!

        echo:
    )
    goto ending

:starting
    @echo off
    cls

    setlocal enabledelayedexpansion

    set engine_py=engine.py
    set kn_engine_py=kn_engine.py

    goto body

:ending
    echo:
