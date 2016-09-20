goto starting

:body
    set fold=examples\
    set fil=demo2
    set fils=demo2, test
    for %%i in (%fil%) do (
        set base=%fold%%%~ni
        set kn=!base!.kn
        set p=!base!.p

        set parse=%genparse% !kn!

        REM !parse!
        !parse! > !p!
        !p!

        goto ending
    )

:starting
    @echo off
    cls

    setlocal enabledelayedexpansion

    set genparserpy=parser\genparser\src\astgen\main.py
    set lexicon=parser\lexicon.txt
    set grammar=parser\grammar.txt

    set genparse=py %genparserpy% %lexicon% %grammar%

    goto body

:ending
