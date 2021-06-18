# VirtualLibrary P3Rats

Here is our [project plan](https://padlet.com/ketkic61666/Rats)

### How its made:
##### User Interactions (Items below can be found in the navbar)
- [x] Database for sending book recommendations via email
- [X] Random Poem generator (API)
- [x] Database for selling books
- [X] Random Book/Author recommendations

Key Technicals:
- SQL Databases
    - [X] Database for selling books 
        - Front end to display books in database and help buy the books: [ebook.html](https://github.com/adhithin/virtualLibrary/blob/main/emails/templates/ebooks.html)
        - Back end is here through a blueprint: [app.py](https://github.com/adhithin/virtualLibrary/blob/main/emails/app.py)
    - [x] Database to capture emails 
        - Front end to request emails is here [purchase.html](https://github.com/adhithin/virtualLibrary/blob/main/templates/purchase.html)
        - Back end is here [main.py](https://github.com/adhithin/virtualLibrary/blob/main/main.py)
    - [x] Database for book reviews
        - Front end for user is here [bookreview.html](https://github.com/adhithin/virtualLibrary/blob/main/templates/bookreview.html)
        - Back end is here [main.py](https://github.com/adhithin/virtualLibrary/blob/main/main.py)
- API 
    - [X] Pulling data from an api data source
    - [X] Created app route, defined data source [app.py] (https://github.com/adhithin/virtualLibrary/blob/cd3e7860a0d47bd6b3f0c6ccbef7ebaed7beb4d5/randompoem/app.py#L42)
    - [X] Each refresh displays a random poem, info about poet, etc.

- Simple Mail Transfer Protocol 
    - [x] Used to send emails to users interested about book recommendations 
         - The code (backend) is here, after importing SMTP, on [main.py](https://github.com/adhithin/virtualLibrary/blob/main/main.py)

- Classes 
    - [X] Used to create random recommendations of authors and books to users
         - Python pages for book recomendations and author recomendations are [selection.py](https://github.com/adhithin/virtualLibrary/blob/main/booksearch/selection.py) and [author.py](https://github.com/adhithin/virtualLibrary/blob/main/randompoem/author.py), respectively. 
    - [X] Used to create Pascal's Triangle Simulation
         - Backend python page is [algorithm.py](https://github.com/adhithin/virtualLibrary/blob/main/findabook/algorithm.py). 
         - Frontend html page with user-interactive form is [algorithm.html](https://github.com/adhithin/virtualLibrary/blob/main/findabook/templates/algorithm.html).  
    - [X] Used to simulate factorial expansion
         - Backend python page is [rat.py](https://github.com/adhithin/virtualLibrary/blob/main/booksmart/rat.py). 
         - Frontend html page with user-interactive form is [series.html](https://github.com/adhithin/virtualLibrary/blob/main/booksmart/templates/series.html).   
- Theme
    - [X] Used to design the UI and unify the project with a common theme
         - [base.html](https://github.com/adhithin/virtualLibrary/blob/main/templates/base.html) is the jinja template that is being used to integrateall of the pages of the website so that they look the same
         - For example, [home.html](https://github.com/adhithin/virtualLibrary/blob/21857f01f6091627cbeee9748840187f3582c106/templates/home.html#L3) has extended base.html
    - [X] Page with book reccomendations, featured author, and recommended genres
         - The HTML code for this page is in [browse.html](https://github.com/adhithin/virtualLibrary/blob/main/templates/browse.html)
         - The [runtime link](virtuallibrary.cf/browse) to the recommendation page

- Deployment
    - [X] How it was done
         - The instructions on this [README.md file](https://github.com/nighthawkcoders/flask-idea-homesite) were used to deploy the website
    - [X] Original Domain Name
         - This [Google Doc](https://docs.google.com/document/d/1nODveWp0jBzj4ZpFLgWCWTOXzLAHAPUhAQYmZJ4LhyU/edit?usp=sharing) was used to create the domain name. 



