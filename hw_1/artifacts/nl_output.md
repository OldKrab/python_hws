```bash
> cd src
> touch empty_file
> python -m hw_1.nl empty_file
> echo "one line" > one_line
> python -m hw_1.nl one_line   
     1  one line
> python -m hw_1.nl         
Hi
     1  Hi
it is example
     2  it is example
of work
     3  of work

     4  
> python -m hw_1.nl ../pyproject.toml 
     1  [project]
     2  name = "hw_1"
     3  version = "0.0.1"
     4  dependencies = [
     5      "click==8.1.7",
     6  ]
     7  requires-python = ">=3.11"
     8  
>
```