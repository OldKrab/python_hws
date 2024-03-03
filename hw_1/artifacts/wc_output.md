```
> cd src
> touch empty_file
> python -m hw_1.wc empty_file
0 0 0 empty_file
> echo "one line" > one_line
> python -m hw_1.wc one_line    
1 2 9 one_line
> python -m hw_1.wc           
test
   test test  

123
      4       4      25
> python -m hw_1.wc ../pdm.lock ../pyproject.toml ../requirements.txt
  34  113 1250 ../pdm.lock
  10   28  174 ../pyproject.toml
   5   19  128 ../requirements.txt
  49  160 1552 total
>
```