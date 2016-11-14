goto starting

:looping
    set fil=error
    set fils=comment, demo, empty, error, oneliner, poly_T, precedence, skein_T, skein_X_i, syntax, tmp
    for %%i in (%fil%) do (
        set base=%examples_path%%%~ni
        set kn_file=!base!.kn
        set tex_file=!base!.tex

        set kn_cmd=%kn_engine% -f -k !kn_file!
        set tex_compile=latexmk -pdf -outdir=%examples_path% !tex_file!

        !kn_cmd!
        !tex_compile! & cd %examples_path% & %tex_clean% & cd %src_path%

        echo:
    )
    goto ending

:building
    set spec_man=knotty_man.spec
    set work_path=%bin_path%build/

    set pyi_makespec=pyi-makespec -F -n knotty %kn_engine%
    set pyi_bundle=pyinstaller %spec_man% --workpath=%work_path% --distpath=%bin_path%

    REM %pyi_makespec%
    %pyi_bundle%

    call "%bin_path%%kn_exe%"

    goto ending

:starting
    cls
    @echo off
    setlocal enabledelayedexpansion

    set src_path=D:/repos/Knotty/knotty/
    set examples_path=../examples/
    set bin_path=../bin/

    set kn_engine=kn_engine.py
    set kn_exe=knotty.exe

    set tex_clean=latexmk -c

    goto building
    REM goto looping

:ending
    echo:
