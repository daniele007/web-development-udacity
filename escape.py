import cgi

# 
# Implement the function escape_html(s), which replaces:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically 
# render your escaped text as the corresponding symbols, 
# but the grading script will still correctly evaluate it.
# 

def escape_html(s):
    for (i, o) in (("&", "&amp;"), # this character has to be replaced before, otherwise it will be replaced many times
                   ("<", "&lt;"),
                   ('"', "&quot;"),
                   (">", "&gt;")):
    
        s = s.replace(i, o)
    # return cgi.escape(s, quote = True) # build-in version
    return s


s = '&:::::: "'
print escape_html(s)