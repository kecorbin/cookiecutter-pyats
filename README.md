cookiecutter-pyats
==============

A cookiecutter to generate pyATS test cases


## usage

```
pip install cookiecutter
cookiecutter https://github.com/kecorbin/cookiecutter-pyats
```


## rationale

This cookiecutter has three objectives.


* ##### Provide a great starting point for ambitious use cases.  
* ##### standardize the look and feel of testscripts
   Create a set of basic guidelines and rules built based-on common software design standards, enforcing modularity, reuseability and debug-ability. Keep in mind that the works of test-automation itself is still software: using software to test software. Thus, good habits goes a long way towards unifying how testcases & libraries are defined, promoting sharing, cross-team collaboration & etc.
* ##### Demonstrate some really cool pyats concepts.
  In doing so, we necessarily add some things which you may or may not need (e.g processors/plugins/etc) for the most part, these don't do much but provide some hooks at key points within the workflow that you may find a usage for. docstrings and comments through the generated code provide guidance on when/why you may want to use them as well as how you would disable or otherwise alter them

## Developing / Testing

we gladly accept pull requests.  
