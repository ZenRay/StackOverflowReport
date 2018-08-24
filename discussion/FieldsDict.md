**目录**

针对的内容是接下来需要建立的统计的数据值信息：

1. Professional： 专业状态，包括的信息内容为：

   * Student
   * Professional developer
   * Professional non-developer who sometimes writes code
   * Used to be a professional developer
   * None of these
   * NAN——2018 年数据值

2. Employment：工作状态，2017 年的字段 EmploymentStatus 名称需要修正。包括的信息内容：

   * Employed full-time
   * Independent contractor, freelancer, or self-employed
   * Employed part-time 
   * Not employed, and not looking for work
   * I prefer not to say 
   * Retired

3. University：2018 年的字段为 Student，名称需要修正。包括的信息内容：

   * No
   * Yes, full-time
   * Yes, part-time
   * I prefer not to say

4. FormalEducation：正式受教育情况，注意 2018 年信息修改。包括的信息内容：

   * Bachelor's degree
   * Master's degree
   * Some college/university study without earning a bachelor's degree
   * Secondary school
   * Doctoral degree
   * I prefer not to answer
   * Primary/elementary school
   * Professional degree
   * I never completed any formal education

5. UndergradMajor：大学专业，保留 2017 年和 2018 年数据。但是 2017 年字段名 MajorUndergrad ，要修改。包括信息内容：

   2017 年的信息

   * Computer science or software engineering
   * Computer engineering or electrical/electronics engineering
   * Computer programming or Web development
   * Information technology, networking, or system administration
   * A natural science
   * A non-computer-focused engineering discipline
   * Mathematics or statistics
   * Something else
   * A humanities discipline
   * A business discipline
   * Management information systems
   * Fine arts or performing arts
   * A social science
   * I never declared a major
   * Psychology
   * A health science

   2018 年信息

   * Computer science, computer engineering, or software engineering
   * Another engineering discipline (ex. civil, electrical, mechanical)
   * Information systems, information technology, or system administration
   * A natural science (ex. biology, chemistry, physics)
   * Mathematics or statistics
   * Web development or web design
   * A business discipline (ex. accounting, finance, marketing)
   * A humanities discipline (ex. literature, history, philosophy)
   * A social science (ex. anthropology, psychology, political science)
   * Fine arts or performing arts (ex. graphic design, music, studio art)
   * I never declared a major
   * A health science (ex. nursing, pharmacy, radiology)

6. Gender：性别，字段信息：

   * Male
   * Female
   * NoComment——其他多选项信息

7. SkipMeals：废寝忘食，字段信息

   * Never
   * 1 - 2 times per week
   *   3 - 4 times per week
   *   Daily or almost every day
   * NAN——2017 年没有该数据

8. Race：人种信息，2018 年字段 RaceEthnicity。对于多字段信息，采取了直接取得第一个分号前值。包括字段复选框字段：

   * Black or of African descent 
   * East Asian 
   * Hispanic or Latino/Latina 
   * Middle Eastern 
   * Native American, Pacific Islander, or Indigenous Australian 
   * South Asian 
   * White or of European descent 
   * I don’t know ——只要包括这个数据，变更数据为 NoInfo
   * I prefer not to say ——只要包括这个数据，变更数据为 NoInfo
   * NoInfo——没有明确信息的

9. Age：年龄段，2017 年无该字段，包括字段信息：

   * I prefer not to answer
   *  Under 18 years old
   * 18 - 24 years old
   * 25 - 34 years old
   * 35 - 44 years old
   * 45 - 54 years old
   * 55 - 64 years old
   * 65 years or older 
   * NAN——2017 年无数据

10. Country：国家，包括的是国家信息

11. Salary：薪资，2018 年为 ConvertedSalary 字段名需要修改，连续型数值信息

12. Currency：薪资结算符号，2018 年字段名称为 CurrencySymbol

    * U.S. dollars 
    * Euros 
    * British pounds sterling
    * Japanese yen
    * Chinese yuan renminbi
    * Brazilian reais
    * Indian rupees
    * Mexican pesos
    * South African rands 
    * Swedish kroner
    * Australian dollars
    * Canadian dollars
    * Singapore dollars
    * Russian rubles
    * Swiss francs 
    * Polish złoty
    * Bitcoin
    * other currency:  

13. SalaryType：薪资结算类型，2017 年增加该字段信息值为 Yearly，包括字段信息：

    * Monthly
    * Yearly
    * Weekly

14. CompanySize：公司规模，包括的字段信息

    1. Fewer than 10 employees 
    2. 10 to 19 employees 
    3. 20 to 99 employees 
    4. 100 to 499 employees 
    5. 500 to 999 employees 
    6. 1,000 to 4,999 employees 
    7. 5,000 to 9,999 employees 
    8. 10,000 or more employees 
    9. NoInfo——I don't know 信息 和 I prefer not to answer 信息替换为 NoInfo

15. DeveloperType：开发类型，是以一个复选信息字段，可能包括的字段信息。对于 2017 年和 2018 年的信息存在表达不一致的情况

    ```
    2017年 的信息：
    Web developer                                            
    Mobile developer                                         
    Desktop applications developer                        
    Other                                              
    Embedded applications/devices developer       
    Developer with a statistics or mathematics background 
    Data scientist                                            
    DevOps specialist                                      
    Quality assurance engineer                               
    Database administrator                                   
    Graphics programming                                     
    Machine learning specialist                              
    Systems administrator                                      
    Graphic designer  
    
    2018 年信息
    Back-end developer                     
    Full-stack developer                           
    Mobile developer                                
    Student                                         
    Front-end developer                              
    Desktop or enterprise applications developer    
    Data scientist or machine learning specialist    
    Embedded applications or devices developer     
    QA or test developer                             
    Data or business analyst                          
    C-suite executive (CEO, CTO, etc.)              
    DevOps specialist                               
    Engineering manager                               
    Educator or academic researcher                 
    System administrator                             
    Game or graphics developer                        
    Designer                                          
    Product manager                                  
    Database administrator                           
    ```

16. JobSatisfaction：工作满意度，2017 年和 2018 年数据不一致，修改后保存信息：

    * Extremely dissatisfied				:	= 0
    	 Moderately dissatisfied			:	<= 2
    	 Slightly dissatisfied 				: 	<= 4
    	 Neither satisfied nor dissatisfied	:	= 5
    	 Slightly satisfied		:	<=  7
    	 Moderately satisfied	:	<= 9
    	 Extremely satisfied	:	= 10

    ```
    2017 年数据
    8.0     
    7.0     
    9.0     
    6.0    
    10.0   
    5.0     
    4.0     
    3.0    
    2.0      
    0.0      
    1.0      
    
    2018 年数据
    Moderately satisfied 
    Extremely satisfied  
    Slightly satisfied   
    Slightly dissatisfied   
    Moderately dissatisfied
    Neither satisfied nor dissatisfied
    Extremely dissatisfied      
    ```

17. JobSeekingStatus：求职状态，2018 年的字段名称需要修改（JobSearchStatus）。字段信息如下：

    1. I am actively looking for a job 
    2. I’m not actively looking, but I am open to new opportunities
    3. I am not interested in new job opportunities

18. YearsCoding：编程年限，2017 年中包括了两个字段（YearsCodedJob 与 YearsCodedJobPast）说明了曾经或者过去的的编程年限。为与 2018 年的数据统一，将 2017 年的两个字段统一为一个 YearsCoding（从数据内容上来看，具有可行性—— YearsCodedJobPast 数据量少，可以统一到 YearsCodedJob 作补充数据， 以时间年限上最大的数据作为值。这样说明的是整体有多少编程年限）

       *  Less than a year 
       *  1 to 2 years 
       *  2 to 3 years 
       *  3 to 4 years 
       *  4 to 5 years 
       *  5 to 6 years 
       *  6 to 7 years 
       *  7 to 8 years 
       *  8 to 9 years 
     *  9 to 10 years
    *  11.10 to 11 years
    *  11 to 12 years 
    *  12 to 13 years 
    *  13 to 14 years 
    *  14 to 15 years
    *  15 to 16 years
    *  16 to 17 years
    *  17 to 18 years
    *  18 to 19 years
    *  19 to 20 years
    *  20 or more years 
19. LanguageDesireNextYear ：下一年中期望使用语言，在 2017 年中字段为 WantWorkLanguage，名称存在差异，此外值中存在多余的空格。字段数据值为：
   - Assembly
   - Bash/Shell
   - C
   - C#
   - C++
   - CSS
   - Clojure
   - Cobol
   - CoffeeScript
   - Common Lisp
   - Dart
   - Delphi/Object Pascal
   - Elixir
   - Erlang
   - F#
   - Go
   - Groovy
   - HTML
   - Hack
   - Haskell
   - Java
   - JavaScript
   - Julia
   - Kotlin
   - Lua
   - Matlab
   - Objective-C
   - Ocaml
   - PHP
   - Perl
   - Python
   - R
   - Ruby
   - Rust
   - SQL
   - Scala
   - Smalltalk
   - Swift
   - TypeScript
   - VB.NET
   - VBA
   - Visual Basic 6
20. LanguageWorkedWith：目前正在使用的语言，在 2017 年中字段为 HaveWorkedLanguage，名称存在差异，此外值中存在多余的空格。字段数据值为：
   - Assembly
   - Bash/Shell
   - C
   - C#
   - C++
   - CSS
   - Clojure
   - Cobol
   - CoffeeScript
   - Common Lisp
   - Dart
   - Delphi/Object Pascal
   - Elixir
   - Erlang
   - F#
   - Go
   - Groovy
   - HTML
   - Hack
   - Haskell
   - Java
   - JavaScript
   - Julia
   - Kotlin
   - Lua
   - Matlab
   - Objective-C
   - Ocaml
   - PHP
   - Perl
   - Python
   - R
   - Ruby
   - Rust
   - SQL
   - Scala
   - Smalltalk
   - Swift
   - TypeScript
   - VB.NET
   - VBA
   - Visual Basic 6
21. DatabaseDesireNextYear：下一年期待使用数据库，2017 年的名称为 WantWorkDatabase，字段名称不一致，数据中存在不必要空格。数据值为：
   - Amazon DynamoDB
   - Amazon RDS/Aurora
   - Amazon Redshift
   - Apache HBase
   - Apache Hive
   - Cassandra
   - Elasticsearch
   - Google BigQuery
   - Google Cloud Storage
   - IBM Db2
   - MariaDB
   - Memcached
   - Microsoft Azure (Tables, CosmosDB, SQL, etc)
   - MongoDB
   - MySQL
   - Neo4j
   - Oracle
   - PostgreSQL
   - Redis
   - SQL Server
   - SQLite
22. DatabaseWorkedWith ：当前正在使用的数据库，2017 年的名称为 WantWorkDatabase，字段名称不一致，数据中存在不必要空格。数据值为：
   - Amazon DynamoDB
   - Amazon RDS/Aurora
   - Amazon Redshift
   - Apache HBase
   - Apache Hive
   - Cassandra
   - Elasticsearch
   - Google BigQuery
   - Google Cloud Storage
   - IBM Db2
   - MariaDB
   - Memcached
   - Microsoft Azure (Tables, CosmosDB, SQL, etc)
   - MongoDB
   - MySQL
   - Neo4j
   - Oracle
   - PostgreSQL
   - Redis
   - SQL Server
   - SQLite
23. PlatformWorkedWith ：2017 年字段名称为HaveWorkedPlatform，字段名称不一致，此外存在多余空格。 数据信息为：
   - AWS
   - Amazon Echo
   - Amazon Web Services (AWS)
   - Android
   - Apple Watch or Apple TV
   - Arduino
   - Azure
   - Drupal
   - ESP8266
   - Firebase
   - Gaming console
   - Google Cloud Platform/App Engine
   - Google Home
   - Heroku
   - IBM Cloud or Watson
   - Linux
   - Linux Desktop
   - Mac OS
   - Mainframe
   - Microsoft Azure
   - Predix
   - Raspberry Pi
   - Salesforce
   - Serverless
   - SharePoint
   - Windows Desktop
   - Windows Desktop or Server
   - Windows Phone
   - WordPress
   - iOS
24. PlatformDesireNextYear ：2017 年字段名称为WantWorkPlatform，字段名称不一致，此外存在多余空格。 数据信息为：
   - AWS
   - Amazon Echo
   - Amazon Web Services (AWS)
   - Android
   - Apple Watch or Apple TV
   - Arduino
   - Azure
   - Drupal
   - ESP8266
   - Firebase
   - Gaming console
   - Google Cloud Platform/App Engine
   - Google Home
   - Heroku
   - IBM Cloud or Watson
   - Linux
   - Linux Desktop
   - Mac OS
   - Mainframe
   - Microsoft Azure
   - Predix
   - Raspberry Pi
   - Salesforce
   - Serverless
   - SharePoint
   - Windows Desktop
   - Windows Desktop or Server
   - Windows Phone
   - WordPress
   - iOS