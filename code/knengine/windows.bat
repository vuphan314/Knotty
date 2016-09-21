goto starting

:body
    set fold=examples\
    set fil=oneliner
    set fils=demo, demo2, empty, oneliner
    for %%i in (%fil%) do (
        set base=%fold%%%~ni
        set kn=!base!.kn
        set txt=!base!_parsed_auto.txt

        set parse=%kn_engine% !kn!

        REM echo !base!

        !parse!
        type !txt!

    )
    goto ending

:starting
    @echo off
    cls

    setlocal enabledelayedexpansion

    set kn_engine=py kn_engine.py

    goto body

:ending
    echo:
