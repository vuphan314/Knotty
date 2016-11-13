goto starting

:looping
    set fil=skein_T
    set fils=comment, demo, error, oneliner, poly_T, precedence, skein_T, skein_X_i, syntax, tmp
    for %%i in (%fil%) do (
        set base=%examples_path%%%~ni
        set kn_file=!base!.kn
        set tex_file=!base!.tex

        set engine_cmd=%kn_engine% -f -k !kn_file!
        set tex_compile=latexmk -pdf -outdir=%examples_path% !tex_file!

        !engine_cmd!
        REM !tex_compile! & cd %examples_path% & %tex_clean% & cd ..

        echo:
    )
    goto ending

:building
    set spec_man=knotty_man.spec
    set work_path=%bin_path%build/
    set dist_path=%bin_path%
    set src_path=%CD%

    set pyi_makespec=pyi-makespec -F -n knotty %kn_engine%
    set pyi_bundle=pyinstaller %spec_man% --workpath=%work_path% --distpath=%dist_path%

    REM %pyi_makespec%
    %pyi_bundle%

    call "%dist_path%%knotty_exe%"

    goto ending

:starting
    cls
    @echo off
    setlocal enabledelayedexpansion

    set kn_engine=kn_engine.py
    set examples_path=../examples/
    set bin_path=../bin/
    set knotty_exe=knotty.exe

    set npp=notepad++
    set tex_clean=latexmk -c

    REM goto building
    goto looping

:ending
    echo:
