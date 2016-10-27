goto starting

:looping
    set fold=examples/
    set fil=tmp
    set fils=demo, oneliner, precedence, skein_X_i, syntax, tmp
    for %%i in (%fil%) do (
        set base=%fold%%%~ni
        set kn_file=!base!.kn
        set py_file=!base!.py
        set tex_file=!base!.tex

        set engine_cmd=%engine_py% !kn_file!
        set kn_engine_cmd=%kn_engine_py% !kn_file!
        set tex_compile=latexmk -pdf -outdir=%fold% !tex_file!

        !engine_cmd!

        REM !kn_engine_cmd!
        REM %npp% !py_file!
        REM %npp% !tex_file!

        !tex_compile!
        cd %fold% & %tex_clean% & cd ..

        echo:
    )
    goto ending

:building
    set spec_man=engine_man.spec
    set work_path=%engine_path%build\
    set dist_path=%engine_path%
    set knengine_path=%CD%

    set pyi_makespec=pyi-makespec %engine_py% -F
    set pyi_bundle=pyinstaller %spec_man% --workpath=%work_path% --distpath=%dist_path%

    REM %pyi_makespec%
    %pyi_bundle%

    REM cd %dist_path% & %engine_exe% demo.kn & cd %knengine_path%

    goto ending

:starting
    @echo off
    cls
    setlocal enabledelayedexpansion

    set npp=notepad++
    set tex_clean=latexmk -c

    set engine_path=..\engine\
    set engine_exe=engine.exe

    set engine_py=engine.py
    set kn_engine_py=kn_engine.py

    REM goto building
    goto looping

:ending
    echo:
