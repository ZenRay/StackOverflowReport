**目录**

[TOC]

## 1. 2016 年数据

Column Name --- Survey Question --- Note (if any)

'collector' --- N/A --- Respondent source   数据来源，例如 Facebook、Twitter
'country' --- In what country do you currently reside? --- 地理信息
'un_subregion' --- N/A --- Region inferred by country location (UN region)
'so_region' --- N/A --- Region inferred by country location (semi-arbitrary Stack Overflow region groupings)
'age_range' --- How old are you? 年龄区间
'age_midpoint' --- N/A --- Age inferred by age range 推测年龄
'gender' --- What is your gender? --- Gender provided by respondent	性别
'self_identification' --- What do you consider yourself? (select all that apply)	个人介绍
'occupation' --- Which of the following best describes your occupation?	职位
'occupation_group' --- N/A --- Inferred from occupation  推测职业范围
'experience_range' --- How many years of IT / programming experience do you have? 工作年限
'experience_midpoint' --- N/A --- Inferred from experience_range工作年限
'salary_range' --- What is your annual gross earnings or salary (including bonus) in USD?薪资范围
'salary_midpoint' --- N/A --- Inferred from salary_range
'big_mac_index' --- N/A --- Jan 2016 Big Mac Index for country from: http://www.economist.com/content/big-mac-index  巨无霸指数，相关经济信息需要确认一下

'tech_do' --- Which of the following languages or technologies have you done extensive development with in the last year? (select all that apply)  开发语言

'tech_want' --- Which of the following languages or technologies do you WANT to work with this year? (select all that apply)期望使用开发语言
'aliens' --- Do you believe in aliens? 是否相信外星人
'programming_ability' --- On a scale of 1-10, how would you rate your programming ability? 开发能力评级
'employment_status' --- How would you describe your current employment status?工作状态，全职兼职等等
'industry' --- How would you best describe the industry you currently work in?行业
'company_size_range' --- What is the size of your company?	公司规模
'team_size_range' --- What is the size of your team?团队规模
'women_on_team' --- How many women are on your team?女性开发人员在团队中数量
'remote' --- Do you work remotely? 是否会远程工作
'job_satisfaction' --- How satisfied are you with your current job(s)?  工作满意度
'job_discovery' --- How did you discover your current job? 工作发现渠道
'dev_environment' --- What development environments do you use regularly? (select all that apply) 开发环境
'commit_frequency' --- How frequently do you check-in or commit code? commit 频率
'hobby' --- How much time per week do you spend programming as a hobby, or working on side projects or open-source? 爱好花费时间，
'dogs_vs_cats' --- Dogs or cats? 喜猫还是喜狗
'desktop_os' --- Which desktop operating system do you use most? 桌面系统
'unit_testing' --- Is unit testing worth the effort? 单元测试认知
'rep_range' --- What is your current Stack Overflow reputation?  SO 上荣誉状态
'visit_frequency' --- How frequently do you read Stack Overflow questions or answers? 访问频率
'why_learn_new_tech' --- What is your primary motivation for learning new programming languages or technologies? 学习新语言的驱动力
'education' --- What amount of formal or professional programming training have you received? (select all that apply) 教育，或者学习方式
'open_to_new_job' --- Are you currently looking for a job or open to new opportunities? 新工作意愿
'new_job_value' --- When evaluating a new employment opportunity what's most important to you? (select up to 3) 新工作的工作状态
'job_search_annoyance' --- What annoys you most when searching for a new job? 新工作的烦恼或者问题
'interview_likelihood' --- If you applied to a job at Google, what do you think is the likelihood you would get an interview? Google 得到面试的可能性
'how_to_improve_interview_process' --- How can companies improve the interview process? (select up to 3) 得到面试的方式
'star_wars_vs_star_trek' --- Star Wars or Star Trek? 星球大战和星际迷航
'agree_tech' --- How much do you agree or disagree with the following statements? --- I love the technologies I use at work. 工作中使用技术的意愿
'agree_notice' --- How much do you agree or disagree with the following statements? --- Every day I notice things that can be improved by better software.	关注新事物对目前的影响
'agree_problemsolving' --- How much do you agree or disagree with the following statements? --- I love problem solving.解决问题意愿
'agree_diversity' --- How much do you agree or disagree with the following statements? --- Diversity in the workplace is important.不同工作环境意愿
'agree_adblocker' --- How much do you agree or disagree with the following statements? --- I always use an ad blocker.使用广告阻塞工具的医院
'agree_alcohol' --- How much do you agree or disagree with the following statements? --- I occasionally drink alcohol while coding.编程时喝酒

'agree_loveboss' --- How much do you agree or disagree with the following statements? --- I love my boss.领导赞赏度

'agree_nightcode' --- How much do you agree or disagree with the following statements? --- I love coding late at night. 夜晚编程
'agree_legacy' --- How much do you agree or disagree with the following statements? --- I work with a lot of legacy code. 有效代码
'agree_mars' --- How much do you agree or disagree with the following statements? --- I want to go to Mars right now, even if there's a chance I never come back. 火星探索意愿
'important_variety' --- What's important to you at work? --- Working on a variety of projects 重要性角度
'important_control' --- What's important to you at work? --- Having control over product decisions
'important_sameend' --- What's important to you at work? --- Ending work at the same time every day
'important_newtech' --- What's important to you at work? --- Learning new technologies
'important_buildnew' --- What's important to you at work? --- Building something new
'important_buildexisting' --- What's important to you at work? --- Improving existing applications
'important_promotion' --- What's important to you at work? --- Getting promoted
'important_companymission' --- What's important to you at work? --- Believing strongly in my company's mission
'important_wfh' --- What's important to you at work? --- Working from home
'important_ownoffice' --- What's important to you at work? --- Having my own office
'developer_challenges' --- What are the biggest challenges you face as a developer? (select up to 3)
'why_stack_overflow' --- Why do you use Stack Overflow? (select all that apply)



## 2. 2017 年数据

#### 开发者自我描述信息

1. I am a professional software developer [RESPONDENT] 

2. I’m not a professional developer, but I write code sometimes for my job (e.g. 

   engineering manager, product manager, data analyst, etc.) [RESPONDENT] 

3. I used to code for a living, but I no longer do [RESPONDENT] 

4. I am a student who is learning how to program [RESPONDENT] 

5. None of these 

以下是针对上面的信息涉及到的其他问题

* **Professional** 职业水平。
* **YearsCodedJob** 和 **YearsCodedJobPast** 开发时长——结合 2018 年 yearscoding 和 yearscodingprof。
* **DeveloperType** 职业开发者的开发类型，是多选项。
  * WebDeveloperType 网页开发者最佳描述  职业类型是网页开发的
  * MobileDeveloperType 移动开发平台类型 职业类型是移动开发
* NonDeveloperType 非开发者职业
* **JobSatisfaction** 工作满意度，只能是 software developer。
* 下面的值只能是I used to code for a living, but I no longer do 的开发者，以下 **应当作为换行业分析的角度**
* ExCoderReturn 返回开发工作，
* ExCoderNotForMe 表示Working as a developer just wasn’t for me 
* ExCoderBalance 比坐开发者更能平衡生活和工作I have better work-life balance now than I did as a developer 
* ExCoder10Years 期待更早进入行业？？My career is going the way I thought it would 10 years ago 
* ExCoderBelonged 开发工作归属感
* ExCoderSkills 技能过时I don’t think my coding skills are up to date 
* ExCoderWillNotCode 不会再继续编程 I probably won’t code for a living ever again 
* ExCoderActive 还是活跃的社区开发者 I’m still active in the developer community 
* 
* **LastNewJob** 最近更换工作，条件是前三类开发者
* **ResumePrompted** 最近更新简历原因——2018 年数据是 updatecv
* **Salary** 年薪，条件是前三类开发者。
* Overpaid 对自己在市场的评价 从市场方向来看待个人薪资情况
* ExpectedSalary 期待年薪，这个的条件是学生
* EducationImportant 教育重要性，这个是职业开发者对教育的态度，只能是职业开发者
* **以下不能是前开发者**
* **HaveWorkedLanguage** 和 **WantWorkLanguage** 正在使用和期待使用语言 不能是前开发者
* **HaveWorkedFramework** 和 **WantWorkFramework** 正在使用和期待使用的库
* **HaveWorkedDatabase** 和 **WantWorkDatabase** 正在使用和期待使用的数据库
* **HaveWorkedPlatform** 和 **WantWorkPlatform** 正在使用和期待使用的平台——这里在 2018 年中是独立的开发系统
* 
* **Methodology** 曾经使用的编程方法 不能是学生。
* VersionControl 使用的版本控制工具，不能是前开发者
* **以下是设备满意度，从实际情况来看需要思考从怎么使用这类数据**
* EquipmentSatisfiedMonitors 、EquipmentSatisfiedCPU、EquipmentSatisfiedRAM、EquipmentSatisfiedStorage、EquipmentSatisfiedRW

1. **ProgramHobby** 爱好编程和开源项目，**对分析不起作用**——需要分析一下和 2018 年的 Hobby 之间的数据区别。

2. **Country** 居住国家。

3. University 参加学校项目，**对分析不起作用**

4. **EmploymentStatus** 工作状态，用于分析开发者工作类型，全职、兼职。

   1. HomeRemote 在家或者远程工作频率，这个需要是工作状态是处于有雇佣状态
   2. **CompanySize** 公司人员，这个需要是工作状态是处于有雇佣状态。
   3. **CompanyType** 公司类型，这个需要是工作状态是处于有雇佣状态——2018 年没有该数据
   4. LearnedHiring 当前工作 信息来源，这个需要是工作状态是处于有雇佣状态
   5. InfluenceInternet
      InfluenceWorkstation
      InfluenceHardware
      InfluenceServers
      InfluenceTechStack
      InfluenceDeptTech
      InfluenceVizTools
      InfluenceDatabase
      InfluenceCloud
      InfluenceConsultants
      InfluenceRecruitment
      InfluenceCommunication  影响公司的购买决策方面的内容How much influence do you have on purchasing decisions within your organization for each of the following  

5. **FormalEducation** 最高学历，需要进行分析吗？。

6. **MajorUndergrad** 重要专业，最高学历必须在 Secondary school 之上。

7. YearsProgram 包括学习阶段，编程年限，这个可以用于分析整体编程年限分布

8.  YearsCodedJob 和YearsCodedJobPast ，这两个问题没有弄明白For how many years [have you coded]/[did you code] for a living? 

9. **Gender** 性别。

10. HighestEducationParents 父母受到的最高教育程度 

11. **Race** 人种描述 。

12. 

    

#### 开发者态度和求职

这些都是是否同意的问题，看以下内容是否可以分析出开发者对工作、同事等的态度

1. **ProblemSolving 解决问题态度** 
2. **BuildingThings 创建作为奖励Building things is very rewarding** 
3. **LearningNewTech** 
4. **BoringDetails** 
5. **JobSecurity** 
6. **DiversityImportant** 
7. **AnnoyingUI** 
8. **FriendsDevelopers** 
9. **RightWrongWay** 
10. **UnderstandComputers** 
11. **SeriousWork** 
12. **InvestTimeTools** 
13. **WorkPayCare** 
14. **KinshipDevelopers** 
15. **ChallengeMyself** 
16. **CompetePeers** 
17. ChangeWorld 
18. **以上是一种态度**——对于以上的内容需要判断一下和 2018 年区别
19. **JobSeekingStatus** 当前找工作意愿 。
    1. **下面是当前有意愿找工作的人员的看重选项，这里是否可以分析出找工作的依据**
    2. **AssessJobIndustry**、**AssessJobRole**、**AssessJobExp**、**AssessJobDept**、**AssessJobTech**、**AssessJobProjects**、**AssessJobCompensation**、**AssessJobOffice**、**AssessJobCommute**、**AssessJobRemote**、**AssessJobLeaders**、**AssessJobProfDevel**、**AssessJobDiversity**、**AssessJobProduct**、**AssessJobFinances**
    3. HoursPerWeek 每周花在找工作上的事件，这需要有找工作意愿的人
20. ImportantBenefits 薪资外的补贴重要点 
21. JobProfile 工作状态和建立等保留在哪个网站上 **这里可以分析主要的求职网络渠道**
22. MetricAssess 评价指标Congratulations! The bosses at your new employer, E Corp, are allowing you to choose which metrics will be used to assess your individual performance in your role as a senior developer. Which metrics do you suggest to the E bosses? Please select all that apply. **可以用于分析开发者的看重点**
23. ImportantHiringAlgorithms、ImportantHiringTechExp、ImportantHiringCommunication、ImportantHiringOpenSource、ImportantHiringPMExp、ImportantHiringCompanies、ImportantHiringTitles、ImportantHiringEducation、ImportantHiringRep、ImportantHiringGettingThingsDone 这个是以招聘者的角度来分析需要求职人员的参考点——**这个可以用于分析评估方向**

#### 关于教育的认识观点

1. EducationImportant 教育重要性 
2. **EducationTypes** 学习教育方式 这个是继续教育学习的方式Outside of your formal schooling and education, which of the following have you done? 
   * **SelfTaughtTypes** 自学方式，要求是Participated in online coding competitions (e.g. HackerRank, CodeChef, TopCoder 
   * **TimeAfterBootcamp** bootcamp毕业到工作用多久 要求Participated in a full-time, intensive developer training program (aka “bootcamp”) 



#### 编程习惯和实践

1. ShipIt ——It’s better to ship now and optimize later 
2. OtherPeoplesCode——Maintaining other people’s code is a form of torture 
3. ProjectManagement——Most project management techniques are useless 
4. EnjoyDebugging——I enjoy debugging code 
5. InTheZone——I often get “into the zone” when I’m coding 
6. DifficultCommunication——I have difficulty communicating my ideas to my peers 
7. CollaborateRemote——It’s harder to collaborate with remote peers than those on site 

#### 下面是认为没有必要分析的内容

1. PronounceGIF GIF 发音 
2. ClickyKeys 工作环境-键盘敲击声 机械键盘敲击声
3. **Currency** 使用货币 。
4. TabsSpaces 缩紧使用方式
5. CousinEducation 后辈学习建议 Let’s pretend you have a distant cousin [{null} / named Bob / named Alice]. [They are/ He is / She is] 24 years old, [have/ has/ has] a college degree in a field not related to computer programming, and [have/ has/ has] been working a non-coding job for the last two years. [They want/ he wants/ she wants] your advice on how to switch to a career as a software developer. Which of the following options would you most strongly recommend to [your cousin / Bob / Alice]? Please choose no more than four options. 
6. **WorkStart** 选择每天开始上班的时间 一天八小时上班制的工作起始时间。
7. AuditoryEnvironment 编程中听觉环境 Suppose you're about to start a few hours of coding and have complete control over your auditory environment (music, background noise, etc.). What would you do? 
8. CheckInCode 代码提交频率 Over the last year, how often have you checked-in or committed code? 
9. StackOverflowDescribes
   StackOverflowSatisfaction
   StackOverflowDevices
   StackOverflowFoundAnswer
   StackOverflowCopiedCode
   StackOverflowJobListing
   StackOverflowCompanyPage
   StackOverflowJobSearch
   StackOverflowNewQuestion
   StackOverflowAnswer
   StackOverflowMetaChat
   StackOverflowAdsRelevant
   StackOverflowAdsDistracting
   StackOverflowModeration
   StackOverflowCommunity
   StackOverflowHelpful
   StackOverflowBetter
   StackOverflowWhatDo
   StackOverflowMakeMoney 和 SOF 相关信息可以不用分析
10. 

## 3. 2018 年数据

1. Basic Information
2. Your Work, Education, and Career
3. Technology and Tech Culture
4. Stack Overflow Usage + Community Questions
5. Demographic Information 





## 4. 主题问题

1. 用户侧写

   用户侧写信息，可以参考从 2017 年的调查角度来解释 

   1. Developer attitudes (Q250) 
   2. Job-seeking and compensation (Q410 to Q350)1 
   3. Education and professional development (Q520 to Q550) 
   4. Software development practices (Q710 to Q770) 
   5. Hardware and other tools (Q810 and Q830) 
   6. Stack Overflow usage & attitudes (Q960 to Q980) 

   

2. 扩展问题

   1. 从目前的数据上发现变化，从时间上处理到的变化
   2. 相关性分析，职业、薪资以及开发方向等等之间相关性
   3. 开发语言与期望使用语言的变化
   4. 行业上使用开发语言
   5. 学习驱动类型，钱财探索
   6. 最后的 important 信息，从工作中的期待重要性
   7. 从 2017 年出现了对应的用户 ID，可以考虑以此角度来进行扩展角度分析用户的变化
   8. 工作选择的参考角度，薪资，工作属性等
   9. 在 2017 年的数据中有 ImportantHiring 字段，可以用于分析招聘要求
   10. 2017 年有一个 JobProfile 可以分析常用的找工作平台
   11. MajorUndergrad 这里可以分析一下专业是否存在差异

## 5. 数据处理

1. occupation_group：最好将所有数据的这个 feature 整理到一起进行处理——2016年数据
2. 对于 2016 年数据需要进行处理，例如在 2018 年中新工作期待的选项是数值型的，而 16年是文本描述型的
3. 对所处国家信息可以通过货币信息进行差异判断，但是是作为分析角度还是作为数据处理方式需要进行探讨
4. 2017 年和 2018 年的工作状态字段存在差异
5. 18 年的设备信息为 ErgonomicDevices 需要和 17年进行调整
6. 17年的ProgramHobby 数据是否有必要和2018年的Hobby 作为一起进行合并
7. 17 年的hoursperweek 是否需要和18年 hourscomputer 时间进行合并——这里存在错误，两者不是相同数据
8. 2018 年数据 LanguageDesireNextYear， LanguageWorkedWith 与 2017年数据  HaveWorkedLanguage 和WantWorkFramework
9. 2018 年  PlatformDesireNextYear 和 PlatformWorkedWith 与2017年数据是 have 和want
10. QuestionsConfusing 和 QuestionsInteresting 是 2017 年调查最后一个问题，针对调查反馈
11. 2017 年的 Race 和 2018 年的 RaceEthnicity 数据都是针对人种的，可以合并
12. 2017 年和 2018 年的 Respondent 可能是无信息意义数据，确认是否需要删除
13. 抛弃针对 stackoverflow 的数据，例如对其态度之类？对后续分析不是主要关注点
14. 对调查数据的评价可以丢弃，这也不是分析出发点



## 6. 2018 年的信息

 2018 年的调查数据更系统，用户基本信息——国家及其州区信息，用户的行业等信息；

职业生涯信息——职业状态和后续规划，在 2017 年中也有当前工作满意度和工作选择，工作选择参考点

