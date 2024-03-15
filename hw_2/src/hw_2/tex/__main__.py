import shutil
import hw_2.tex.resources
from .tools import image_to_tex, table_to_tex
from importlib.resources import as_file, files

tex_file = "example.tex"
image_file = "cat.png"

with as_file(files(hw_2.tex.resources).joinpath(image_file)) as resource_file:
    shutil.copy(resource_file, image_file)

def get_tex(content: str) -> str:
    return rf"""
\documentclass{{article}}
\usepackage{{graphicx}}
\begin{{document}}
{content}
\end{{document}}
"""

big_table = [list(range(i*10, i*10+10)) for i in range(5)]  

big_table_tex = table_to_tex(big_table)
small_table_tex = table_to_tex([["Hello", "World"], [42, 4.2]])
one_elem_table_tex = table_to_tex([["."]])
empty_table_tex = table_to_tex([])

image_tex = image_to_tex(image_file)

tex = get_tex(f"""
Big table:    
{big_table_tex}    

Small table:    
{small_table_tex}   

Table with one element:    
{one_elem_table_tex} 


Image:

{image_tex}
    
""")

with open(tex_file, "w") as file:
    file.write(tex)