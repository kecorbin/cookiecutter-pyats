# Processors

{{ cookiecutter.project_name }} processors

Currently the following processors are defined in [{{ cookiecutter.project_name}}.py]({{ cookiecutter.project_name}}.py)

* pre_processor
* post_processor
* exception_processor

## Don't cost nothin    

By default, these do very little besides add some noise to the logs, however, they
may come in handy at some point, so we've wired them in for you.

These processors are registered to a testcase by adding a decorator similar
to the following.


```
@aetest.processors(pre=[processors.pre_processor],
                   post=[processors.post_processor],
                   exception=[processors.exception_processor])
class {{ cookiecutter.testcase_class }}(aetest.Testcase):

  ...

```  

For full documentation about processors see:
https://pubhub.devnetcloud.com/media/pyats/docs/aetest/processors.html
