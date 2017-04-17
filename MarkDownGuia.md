##### Guía MarkDown by dM #####

Based in --> [https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet)

Markdown es un lenguaje de marcado ligero creado por John Gruber que trata de conseguir la máxima legibilidad
y facilidad de publicación tanto en su forma de entrada como de salida, inspirándose en muchas convenciones existentes
para marcar mensajes de correo electrónico usando texto plano.

Muy usado en los textos descriptores de proyectos de software.

Usando las etiquetas, las podemos probar desde un editor online en --> http://dillinger.io/

###################
##### Headers #####
###################

# H1
## H2
### H3
#### H4
##### H5
###### H6

Xxxxxx
===

Yyyy
---

####################
##### Emphasis #####
####################

Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.

Combined emphasis with **asterisks and _underscores_**.

Strikethrough uses two tildes. ~~Scratch this.~~

#################
##### Lists #####
#################

1. First ordered list item
2. Another item
  * Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
  1. Ordered sub-list
4. And another item.  

   Some text that should be aligned with the above item.

* Unordered list can use asterisks
- Or minuses
+ Or pluses

#################
##### Links #####
#################

// Agregar enlaces al documento, se mostrara un enlace convencional.
[Texto del link](https://link.com)

##################
##### Images #####
##################

Reference-style: 
![alt text][logo]

Here's our logo (hover to see the title text):
Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

#######################################
#### Code and Syntax Highlighting #####
#######################################

Inline `code` has `back-ticks around` it. Indicated the languaje code to colored the syntax

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
print s
print s
```

##################
##### Tables #####
##################

Tables aren't part of the core Markdown spec, but they are part of GFM and Markdown Here supports them. They are an easy way of adding tables to your email -- a task that would otherwise require copy-pasting from another application.

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

The outer pipes (|) are optional, and you don't need to make the raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

###########################
##### Horizontal Rule #####
###########################

Three or more...

---

Hyphens

***

Asterisks

___

Underscores
