# VirtualLibrary P3Rats

Here is our [project plan](https://padlet.com/ketkic61666/Rats)

### How its made:
##### User Interactions
- [x] Database for sending book recommendations via email
- [X] Random Poem generator (API)
- [x] Database for selling books
- [X] Random Book/Author recommendations

Key Technicals:
- SQL Databases
    - [X] Database for selling books 
    - [x] Database to capture emails 
- API 
    - [X] Pulling data from an api data source
    - [X] Created app route, defined data source in base
    - [X] Each refresh displays a random poem, info about poet, etc.
    - 
- Deployment 
    - [X] Deployed on Raspberry Pi web server
    - [X] Domain name: virtuallibrary.cf 

- Simple Mail Transfer Protocol 
    - [x] Used to send emails to users interested about book recommendations 
    - [x] Used to send receipts to people who purchase books 
- Classes 
    - [X] Used to create random recommendations of authors and books to users
- HTML
    - [X] Used to design the UI and unify the project with a common theme
         - [base.html](https://github.com/adhithin/virtualLibrary/blob/main/templates/base.html) is the jinja template that is being used to integrateall of the pages of the website so that they look the same
         - For example, [home.html](https://github.com/adhithin/virtualLibrary/blob/21857f01f6091627cbeee9748840187f3582c106/templates/home.html#L3) has extended base.html
    - [X] Homepage with book reccomendations, featured author, and recommended genres
         - The homepage HTML code is in [browse.html](https://github.com/adhithin/virtualLibrary/blob/main/templates/browse.html)
         - The [runtime link](virtuallibrary.cf/browse) to the homepage



