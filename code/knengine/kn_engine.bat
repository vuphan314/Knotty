goto starting

:looping
    set fold=examples\
    set fil=tmp
    set fils=demo, empty, oneliner, syntax, tmp
    for %%i in (%fil%) do (
        set base=%fold%%%~ni
        set kn=!base!.kn
        set kn_simplified=!base!_simplified.kn
        set txt=!base!_parsed_auto.txt
        set py=!base!_auto.py

        set engine_cmd=%engine_py% !kn!
        set kn_engine_cmd=%kn_engine_py% !kn!
        set kn_parser_cmd=%kn_parser_py% !kn!
        
        REM !engine_cmd!
        REM type !kn_simplified!

        !kn_engine_cmd!
        REM type !py!
        %npp% !py!

        REM !kn_parser_cmd!
        REM !kn_parser_cmd! > !txt! & type !txt!

        echo:
    )
    goto ending

:bundling
    set spec_man=engine_man.spec
    set work_path=%engine_path%build\
    set dist_path=%engine_path%
    set knengine_path=%CD%

    set pyi_makespec=pyi-makespec %engine_py% -F
    set pyi_bundle=pyinstaller %spec_man% --workpath=%work_path% --distpath=%dist_path%

    REM %pyi_makespec%
    REM %pyi_bundle%

    cd %dist_path%
    %engine_exe%
    %engine_exe% examples\demo.kn
    cd %knengine_path%

    goto ending

:starting
    @echo off
    cls
    setlocal enabledelayedexpansion
    
    set npp=notepad++

    set engine_path=..\engine\
    set engine_exe=engine.exe

    set engine_py=engine.py
    set kn_engine_py=kn_engine.py
    set kn_parser_py=kn_parser.py

    goto looping
    REM goto bundling

:ending
    echo:
