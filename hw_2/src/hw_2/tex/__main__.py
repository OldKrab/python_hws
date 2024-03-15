from .tools import table_to_tex

tex_file = "example.tex"

def get_tex(content: str) -> str:
    return rf"""
\documentclass{{article}}
\begin{{document}}
{content}
\end{{document}}
"""

big_table = [list(range(i*10, i*10+10)) for i in range(5)]  

big_table_tex = table_to_tex(big_table)
small_table_tex = table_to_tex([["Hello", "World"], [42, 4.2]])
one_elem_table_tex = table_to_tex([["."]])
empty_table_tex = table_to_tex([])

tex = get_tex(f"""
Big table:    
{big_table_tex}    

Small table:    
{small_table_tex}   

Table with one element:    
{one_elem_table_tex} 

Empty table:    
{empty_table_tex} 

Image:
Not implemented      
""")

with open(tex_file, "w") as file:
    file.write(tex)