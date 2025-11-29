# QOL-scripts
Various CLI automation scripts to make my day-to-day life easier. The purpose of each script is described below.

### timer
A Python executable that sets up a live timer (via the `Rich` library), then runs a specific function (decided by input argument) after the timer ends, offering an option to loop. Currently in baby stages, with plans for ASCII art, streaming RSS feeds / curl input, and running local apps. 

### mapper
In my personal knowledge base, I write courses, books, tutorials, etc with a single dash, and then descriptions of them beneath it, like this:
- (Cornell) Strogatz' Nonlinear Dynamics and Chaos (513 pages, 2018)
	- Prereqs: undergraduate calculus, linear algebra, and ODEs
	- 25 [YT Lectures](https://www.youtube.com/playlist?list=PLbN57C5Zdl6j_qJA-pARJnKsmROzPnO9V) from 2014. 
	- Testimonies:
		- Mentioned a couple times as one of the most fun books to read ([Reddit](https://www.reddit.com/r/math/comments/srueh1/what_are_some_of_your_favorite_textbooks/))
		- The best mathematics book many have ever read ([Reddit](https://www.reddit.com/r/math/comments/n3woj8/comment/gwsw0hi/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button))

I want to be able to develop a map of my knowledge base, which means I need to sort these text blocks into nodes. To start with, I define any text after a single dash to be an entity. Each entity should have its own node, and the details (defined by 2nd or more indents/dashes) can be collapsable inside the node.
Right now, the script only counts entities. This project is my first attempt at writing beautiful Python code; I even used generators. Also first time using `click`, which was a lot nicer than `argparse`.


### calc
A quick Python executable that calculates logarithms, e.g. `calc log 2 8` as Google & Desmos don't have such a feature, and I prefer CLIs over GUIs. Other features include unit conversion for weight, distance, and speed, detailed documentation via `argparse` and error handling.

### pdfTexter
A few lines of Bash that convert my 5GB of PDF textbooks to text, allowing efficient search.
