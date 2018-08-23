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
    * Moderately dissatisfied			:	<= 2
    * Slightly dissatisfied 				: 	<= 4
    * Neither satisfied nor dissatisfied	:	= 5
    * Slightly satisfied		:	<=  7
    * Moderately satisfied	:	<= 9
    * Extremely satisfied	:	= 10

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