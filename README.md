# Getting started with BDD in Python

This is an example project demonstrating BDD in Python using Lettuce, you may pull this project and have a try!



**BDD can save Agile**
> - You can’t stay agile without clean code
- You can’t have clean code without refactoring
- You can’t refactor without good automated tests

> _[Matt Wynne, founder fo Cucumber Ltd](https://www.infoq.com/news/2015/03/bdd-save-agile)_



we're going to build a vending machine based on the features provided by customer/BA. we'll use [`Gherkin`](https://github.com/cucumber/cucumber/wiki/Gherkin) as the [`DSL`](http://martinfowler.com/bliki/BusinessReadableDSL.html). 
> With a business-readable DSL, programmers write the code but they show that code frequently to business people who can understand what it means. These customers can then make changes, maybe draft some code, but it's the programmers who make it solid and do the debugging and testing.



### Project info

#### Tools

- Python 2.7.11
- Lettuce 0.2.21


#### BDD Feature files

[vm/test/features](https://github.com/guoliang-dev/bdd-python/tree/master/vm/test/features)

### Q&A
**How to run all BDD tests?**

1. step by step:
  1. navigate to the project-root and install dependencies by: `pip install -r requirements.txt`
  2. install the project locally in '[Development Mode](https://pythonhosted.org/setuptools/setuptools.html#development-mode)'
 ```pip install -e .``` (it creates a special .egg-link file in the deployment directory, that links to your project’s source code)
  2. start testing by:  ```lettuce vm/test```

2. or you may execute the bash script: `bin/install_and_run_at.sh`. it will create a new `virtualenv` and install the app and then start the `lettuce` test. 

**How to config CI job?**

config your Jenkins job with:
```bash
chmod u+x bin/install_and_run_at.sh
bin/install_and_run_at.sh
```

`Post-build` action `Publish JUnit test result report` can be added to show the acceptance test result using `lettucetests.xml`. 
