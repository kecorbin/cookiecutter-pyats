# Plugins

{{ cookiecutter.project_name }} plugins

The following plugins are defined in [{{ cookiecutter.project_name}}.py]({{ cookiecutter.project_name}}.py)


Plugins


* pre_job - ran before each job
* post_job - ran after each job, take
* pre_task - ran after each task(testscript)
* post_task - ran after each task(testscript)

## Don't cost nothin    

By default, these do very little besides add some noise to the logs, however, they
may come in handy at some point, so we've wired them in for you.


## Documentation

For full documentation on plugins see:

https://pubhub.devnetcloud.com/media/pyats/docs/easypy/plugins.html
