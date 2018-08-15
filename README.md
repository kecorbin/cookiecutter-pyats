cookiecutter-pyats
==============

A cookiecutter to generate pyATS test cases

## Background
This is a complete pyATS exemplary template, intended to standardize the look
and feel of testscripts across the board, unifying how testcases & libraries
are defined, promoting sharing, cross-team collaboration & etc.

pyATS is a generic test infrastructure open to a wide variety of usages, often
differing from team to team within Cisco. Thus, the use of this template is
optional. The intent is to create a set of basic guidelines and rules built
based-on common software design standards, enforcing modularity, reuseability
and debug-ability. Keep in mind that the works of test-automation itself is
still software: using software to test software. Thus, good habits goes a long
way.

This template goes hand-in-hand with the 'comprehensive' example featured under
your pyATS install folder: both should be copied to your pyATS instance
automatically during installation. The example script is written loosely
following the guidelines in this template, and serves as more of a supplemental
user-guide for the how-tos w.r.t. each script section feature, in addition to
demonstrating this template's structure.

This template only covers the 'templating' portion: eg, what goes where. For
full understanding of how things should be defined and how testscript feature
works, refer to the user guide at:
    http://wwwin-pyats.cisco.com/documentation/html/


    Folder Structure
    ----------------
        <pyats_root>/templates/
        |-- README
        |-- template.py
        |-- variant.py
        |-- job
        |   `-- template_job.py
        |-- etc
        |   `-- template_testbed.yaml
        |-- testcases
        |   |-- __init__.py
        |   `-- template_testcases.py
        `-- libs
            |-- __init__.py
            `-- template_library.py

Each file listed above contains appropriate headers describing their usages.
To use the template, copie the whole template directory to your script directory
and rename accordingly.

Example
-------
    bash$ cp -r $VIRTUAL_ENV/templates/* $VIRTUAL_ENV/xbu_shared/module/script/

--------------------------------------------------------------------------------
