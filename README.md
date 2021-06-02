# VirtualLibrary P3Rats

Here is our [project plan](https://padlet.com/ketkic61666/Rats)

### Progress (6/1/2021)
##### User Interactions
- [ ] Database for sending book recommendations via email
- [X] Random Poem generator (API)
- [ ] Database for selling books
- [X] Random Book/Author recommendations

Key Technicals:
- SQL Databases
    - [X] Database for selling books 
    - [ ] Database to capture emails 
- API 
    - [X] Pulling data from an api data source
    - [X] Created app route, defined data source in base
    - [X] Each refresh displays a random poem, info about poet, etc.
    - 
- Deployment 
    - [X] Deployed on Raspberry Pi web server
    - [X] Domain name: virtuallibrary.cf 

- Simple Mail Transfer Protocol 
    - [ ] Used to send emails to users interested about book recommendations 
    - [ ] Used to send receipts to people who purchase books 
- Classes 
    - [X] Used to create random recommendations of authors and books to users
- HTML
    - [ ] Used to design the UI and unify the project with a common theme
         - still need to create base jinja template and integrate it into the system
         - this is Aditi's next ticket
    - [X] Homepage with book reccomendations, featured author, and recommended genres
         - The homepage HTML code is in [browse.html](https://github.com/adhithin/virtualLibrary/blob/main/templates/browse.html)
         - The [runtime link](virtuallibrary.cf/browse) to the homepage




### MiniLab: Bubble Sort

##### 1. Build individual section into your Scrum Team project for execution.
  * Aditi
    * [Blueprint Integration in main.py](https://github.com/adhithin/virtualLibrary/blob/bcf48349bf3b05f2a85cd7d77828092cfc67c2bb/main.py#L9-L16)
    * [Blueprinted directory](https://github.com/adhithin/virtualLibrary/tree/main/findabook)
  * Ketki
    * [Minilab in Individual Blueprint](https://github.com/adhithin/virtualLibrary/blob/main/randombook/author.py)
  * Dayita
    * [Minilab in Individual Blueprint](https://github.com/adhithin/virtualLibrary/tree/main/booksmart)
##### 2. Build sort using different data types (Characters, Integer, String)
  * Aditi
    * [Specific data type](https://github.com/adhithin/virtualLibrary/blob/a2bad083587955a1caaf59e88bf2d25be3dfc40a/findabook/app.py#L28-L33)
##### 3. Build input screen for different types of data and have action button to sort each type.
  * Aditi
    * [Input in the html form](https://github.com/adhithin/virtualLibrary/blob/25b0e269fcd363cd2c24f0fc158186db484504b0/findabook/templates/bubblesort.html#L9)
##### 4. Display sorted results on screen
  * Aditi
    * [Sorted results are shown as a string](https://github.com/adhithin/virtualLibrary/blob/25b0e269fcd363cd2c24f0fc158186db484504b0/findabook/app.py#L35)
##### 5. Think about using what you learned in your project (evaluate efficiency).  Look up Insertion and Selection Sort.
  * Aditi
    * Insertion sort is when there is a sorted and unsorted list. The algorithm for insertion sort takes each value from the unsorted list and places it in the correct position in the sorted list. 
    * Selection sort finds the smallest values in the list. If they are smaller than the first value in the sorted list, it makes the smaller number index 0 and puches all the other numbers back by 1 index. This process is repeated multiple times until the list is sorted. 
    * Bubble sort is definitely the most efficient sorting method out of all the methods. Selection and Insertion sort take many steps to complete nd the algorithm has to go through the list several times. For a list of small numbers, bubble sort takes the least number of steps compared to the other two sorting methods, and that is why is it more efficient. 

### Minilab: Classes and Objects
##### 1. Use an individual section (blueprint) in your Scrum Team project for Mini Lab definition and execution.
  * Aditi
    * [Blueprint Integration in main.py](https://github.com/adhithin/virtualLibrary/blob/bcf48349bf3b05f2a85cd7d77828092cfc67c2bb/main.py#L9-L16)
    * [Blueprinted directory](https://github.com/adhithin/virtualLibrary/tree/main/findabook)
  * Ketki
    * [Minilab in Individual Blueprint](https://github.com/adhithin/virtualLibrary/blob/main/randombook/author.py)
  * Dayita
    * [Minilab in Individual Blueprint](https://github.com/adhithin/virtualLibrary/tree/main/booksmart)
##### 2. Enhance or Define a Class to manage a complex data set
  * [Aditi](https://github.com/adhithin/virtualLibrary/blob/5ca17adc21b038cb4e19b894eccd5281335134f4/findabook/algorithm.py#L1-L15)
  * [Ketki](https://github.com/adhithin/virtualLibrary/blob/636e747c430eba952dfb3097829fd7fad77de8e6/randombook/author.py#L6-L20)
  * [Dayita](https://github.com/adhithin/virtualLibrary/blob/879a4ea4b46647741f11f94efb0161449bfd07d2/booksmart/rat.py#L6)
##### 3. Create an Object from a Class in Python. 
  * [Aditi](https://github.com/adhithin/virtualLibrary/blob/5ca17adc21b038cb4e19b894eccd5281335134f4/findabook/algorithm.py#L55)
  * [Ketki](https://github.com/adhithin/virtualLibrary/blob/636e747c430eba952dfb3097829fd7fad77de8e6/randombook/author.py#L57-L62)
  * [Dayita](https://github.com/adhithin/virtualLibrary/blob/879a4ea4b46647741f11f94efb0161449bfd07d2/booksmart/rat.py#L7)
##### 4. Display data or enhanced data from this Python Object on Project Web Page using "getters".
  * Aditi
    * [Getters in algorithm.py](https://github.com/adhithin/virtualLibrary/blob/5ca17adc21b038cb4e19b894eccd5281335134f4/findabook/algorithm.py#L33-L63)
    * [display in algorithm.html](https://github.com/adhithin/virtualLibrary/blob/5ca17adc21b038cb4e19b894eccd5281335134f4/findabook/templates/algorithm.html#L21-L30)
    * [Website Link Showing Frontend of Algorithm](http://104.35.27.118/findabook/algo)
  * Ketki
    * [Getters](https://github.com/adhithin/virtualLibrary/blob/5ca17adc21b038cb4e19b894eccd5281335134f4/findabook/algorithm.py#L32-L53)
    * [Data displayed on website](http://104.35.27.118/randombook)
  * Dayita
    * [Getters](https://github.com/adhithin/virtualLibrary/blob/879a4ea4b46647741f11f94efb0161449bfd07d2/booksmart/rat.py#L43)
    * [Data displayed on website](http://104.35.27.118/booksmart)
##### 5. Highlight WOW or insight in doing this project.  (ie Mastery Show adding timing to Class to Displaying it on Web)
  * [Aditi](https://github.com/adhithin/virtualLibrary/blob/5ca17adc21b038cb4e19b894eccd5281335134f4/findabook/algorithm.py#L63): In Mr. M's example, the entire fibonacci sequence is shown. However, in my example, I did not want to show the entire list, I just wanted to show the last number. So I used the getter get_lastnumber to do this. 
  * Ketki: reload the page to get a new author rec each time! 
  * Dayita: Gives you a new sequence each time and has factorials!

### Color Schemes
* #294e54
* For More info about color scemes, visit [https://www.colorhexa.com/294e54](https://www.colorhexa.com/294e54)

