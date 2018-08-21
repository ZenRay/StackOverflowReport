**Contents**

[TOC]

该文件是确认 2017 年和 2018 年两年之间的选择的变量。

## 1. 确认的变量及其信息比对

| 变量名称               | 2017 年                                 | 2018 年                | 注释                                                         | Alvin                                                        |
| ---------------------- | --------------------------------------- | ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Professional           | Professional-Q100                       | Student                | **2017 年和 2018 年名称存在差异，17 年数据是包括了学生 student 和 17 年 university ；18年转换为 university** | 需要探讨：1.是否是学生是一个切入点；2.Professional也可以包含18年的Student |
| Employment             | EmploymentStatus                        | Employment             | 工作状态                                                     |                                                              |
| FormalEducation        | FormalEducation                         | FormalEducation        | 最高学历                                                     |                                                              |
| UndergradMajor         | MajorUndergrad                          | UndergradMajor         | 专业                                                         |                                                              |
| Gender                 | Gender                                  | Gender                 |                                                              |                                                              |
| SkipMeals              |                                         | SkipMeals              | 1                                                            |                                                              |
| Race                   | Race                                    | RaceEthnicity          | 人种描述                                                     | 我记得不是删除这个么，感觉有种族歧视的嫌疑                   |
| Age                    |                                         | Age                    | 1                                                            |                                                              |
| Country                | Country                                 | Country                |                                                              |                                                              |
| Salary                 | Salary - 320                            | ConvertedSalary -P20   | （待确认一下两者是否存在差异）**2017增加salarytype**         | 17年是年薪，18年会选择薪水模式，可能需要转化                 |
| Currency               | Currency -310                           | CurrencySymbol0 -P20   | 2                                                            |                                                              |
|                        |                                         |                        |                                                              |                                                              |
| CompanySize            | CompanySize                             | CompanySize            |                                                              |                                                              |
| DeveloperType          | DeveloperType                           | DevType                | 2                                                            |                                                              |
| JobSatisfaction        | JobSatisfaction                         | JobSatisfaction        |                                                              |                                                              |
| CareerSatisfaction     |                                         | CareerSatisfaction     | 1                                                            |                                                              |
| JobSeekingStatus       | JobSeekingStatus                        | JobSearchStatus        | 2                                                            |                                                              |
| CommunicationTools     |                                         | CommunicationTools     | 1                                                            |                                                              |
|                        |                                         |                        |                                                              | 21年Q628中只问询了去年使用的平台，为什么在schema中还有对明年的期望； |
| HackathonReasons       |                                         | HackathonReasons       | 1                                                            |                                                              |
| YearsCoding            | YearsCodedJob - 175-YearsCodedJobPast - | YearsCoding            | yearsprogram 170 <br /> years codedjob 和 yearsCodedJobPast 数据处理需要精细化，注意缺失值判断 | 我感觉这两个可以合成一个：YearsCodedJob                      |
| LanguageDesireNextYear | WantWorkLanguage                        | LanguageDesireNextYear | 2                                                            |                                                              |
| LanguageWorkedWith     | HaveWorkedLanguage                      | LanguageWorkedWith     | 2                                                            |                                                              |
| DatabaseDesireNextYear | WantWorkDatabase                        | DatabaseDesireNextYear | 2                                                            |                                                              |
| DatabaseWorkedWith     | HaveWorkedDatabase                      | DatabaseWorkedWith     | 2                                                            |                                                              |
| PlatformWorkedWith     | HaveWorkedPlatform                      | PlatformWorkedWith     | 2                                                            |                                                              |
| PlatformDesireNextYear | WantWorkPlatform                        | PlatformDesireNextYear | 2                                                            |                                                              |
| Methodology            | Methodology                             | Methodology            |                                                              |                                                              |
| IDE                    |                                         | IDE                    | 1                                                            |                                                              |
| Hobby                  | ProgramHobby                            | Hobby                  | 2                                                            |                                                              |
| OpenSource             |                                         | OpenSource             | 1，17 年中 programhobby 选项 1 和 3 作为 Hobby，2 和 3 作为  opensource的处理方案 | 17年将爱好和开源合在一起了，整理时虚注意，both为两者都有，no为两者都无 |
| AIDangerous            |                                         | AIDangerous            | 1                                                            |                                                              |
| AIInteresting          |                                         | AIInteresting          | 1                                                            |                                                              |
| AIResponsible          |                                         | AIResponsible          | 1                                                            |                                                              |
| AIFuture               |                                         | AIFuture               | 1                                                            |                                                              |
| AgreeDisagree1         |                                         | AgreeDisagree1         | 1                                                            |                                                              |
| AgreeDisagree2         |                                         | AgreeDisagree2         | 1                                                            |                                                              |
| AgreeDisagree3         |                                         | AgreeDisagree3         | 1                                                            |                                                              |
| WorkStart              | WorkStart                               |                        | 3                                                            | 这两个放在一起好像不合适，WakeTime可以探究，WorkStart好像意义不大 |
| UpdateCV               | ResumePrompted                          | UpdateCV               | 2                                                            |                                                              |
| MetricAssess           | MetricAssess - 481                      |                        | 3 自我评价：用哪些指标来评估高级开发人员的表现               |                                                              |
| LastNewJob             | LastNewJob                              | LastNewJob             |                                                              |                                                              |
| SelfTaughtTypes        | SelfTaughtTypes                         | SelfTaughtTypes        |                                                              |                                                              |
| TimeAfterBootcamp      | TimeAfterBootcamp                       | TimeAfterBootcamp      |                                                              |                                                              |
| EducationTypes         | EducationTypes                          | EducationTypes         |                                                              |                                                              |
| HoursComputer          |                                         | HoursComputer          | 2                                                            |                                                              |
|                        |                                         |                        |                                                              |                                                              |
|                        |                                         |                        |                                                              |                                                              |
|                        |                                         |                        |                                                              |                                                              |
|                        |                                         |                        |                                                              |                                                              |
|                        |                                         |                        |                                                              |                                                              |



**说明：**

* 1 表示的是 2017 年没有该数据，2018 年有
* 2 表示两个字段名称存在差异
* 3 表示 2017 年有数据，而 2018 年没有

### 2. 其他信息作为补充，需要添加到字段中

#### 2.1  Stackoverflow 信息

##### 2.1.1 2017 年

StackOverflowDescribes
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
StackOverflowMakeMoney 

##### 2.1.2 2018 年

StackOverflowRecommend	推荐SO的意愿
StackOverflowVisit	访问SO的频率
StackOverflowHasAccount	有无os账户
StackOverflowParticipate	参加SO活动频率
StackOverflowJobs	使用或访问SO jobs
StackOverflowDevStory	更新so开发人员故事
StackOverflowJobsRecommend	推荐SO
StackOverflowConsiderMember	SO成员
HypotheticalTools1	对假设工具打分_同伴指导系统
HypotheticalTools2	对假设工具打分_编程私人区域
HypotheticalTools3	对假设工具打分_编程博客平台
HypotheticalTools4	对假设工具打分_工作审查平台
HypotheticalTools5	对假设工具打分_职业问答领域

#### 2.2 新工作和求职态度——这个需要整合一下

##### 2.2.1 2017 年

1. **ProblemSolving** 
2. **BuildingThings** 
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
17. **ChangeWorld** 

### 下面是对于新工作的期待，需要将 2018 年相关信息拆分一下，确认能否和下面的内容对应起来

1. **AssessJobIndustry** 
2. **AssessJobRole** 
3. **AssessJobExp** 
4. **AssessJobDept** 
5. **AssessJobTech** 
6. **AssessJobProjects** 
7. **AssessJobCompensation** 
8. **AssessJobOffice** 
9. **AssessJobCommute** 
10. **AssessJobRemote** 
11. **AssessJobLeaders** 
12. **AssessJobProfDevel** 
13. **AssessJobDiversity** 
14. **AssessJobProduct** 
15. **AssessJobFinances**

**ImportantBenefits** ——

1. Stock options 
2. Retirement/pension contributions 
3. Opportunity for an annual bonus 
4. The number of annual days off (vacation, holidays, etc.) 
5. Employer match of charitable contributions 
6. Health benefits 
7. Employer purchase of high-quality equipment (workstation, monitor, etc.) 
8. Private office 
9. Employer sponsorship of professional development (e.g. conference attendance, course enrollment) 
10. Employer sponsorship of education (e.g. tuition reimbursement) 
11. Long-term leave policies (e.g. parental leave, sabbatical) 
12. Number of expected work hours each week 
13. The ability to work from home 
14. Child or elder care benefits 

##### 2.2.2 2018 年

**AssessJob1-10**	新工作重要性角度和薪资待遇判断。
**AssessBenefits1-11**	新工作重要性角度和薪资待遇判断

#### 2.3 作为招聘者会看中哪些点——目前只看见在 2017 年中有数据

1. ImportantHiringAlgorithms
2. ImportantHiringTechExp
3. ImportantHiringCommunication
4. ImportantHiringOpenSource
5. ImportantHiringPMExp
6. ImportantHiringCompanies
7. ImportantHiringTitles
8. ImportantHiringEducation
9. ImportantHiringRep
10. ImportantHiringGettingThingsDone 

### 3. 最终可能分析的角度

#### 3.1 关于侧写可以用到的角度

所有的8，以及：红标

- 对工作和职业的满意情况：JobSatisfaction 、CareerSatisfaction 
- 对潜在工作的评估：AssessJob1
- 对新工作的福利态度：AssessBenefits1
- 主要用那种沟通工具：CommunicationTools
- 有多少接触过线上学习：EducationTypes
- 如何学习的：SelfTaughtTypes
- **毕业多久可以找到工作**：TimeAfterBootcamp——**这个可以定为一个有意思的角度**
- 对广告的态度：AdBlocker
- 对AI的态度：AIDangerous 
- 对SO的态度：StackOverflowRecommend
- 工作时间：HoursComputer—— **2017年缺乏该数据**
- 废寝忘食的敲代码的比例：SkipMeals
- **性别比例**：Gender

#### 3.2 有意思的角度：

- **结合工资探讨是学习编程更久的人工资高还是以编程为工作的人工资高** 

  YearsCoding	加上上学的时间编程了多少年
  YearsCodingProf	以编程为工作多少年了

- **问卷中通过自学或线上学习的人有多少，他们的工作与工资与其他人相比呢**

  EducationTypes	学习教育方式
  SelfTaughtTypes	教授信息方式
  TimeAfterBootcamp	developer training毕业到工作用多久
  HackathonReasons	在线编程和学习的原因

- 当下比较流行（使用人数众多）的语言、数据库、平台、开发环境是什么

  LanguageDesireNextYear	使用其他语言
  LanguageWorkedWith	已使用语言
  DatabaseDesireNextYear	数据库变化
  DatabaseWorkedWith	数据库使用
  PlatformDesireNextYear	接下来的工作平台期待
  PlatformWorkedWith	正在使用工作平台
  FrameworkDesireNextYear	下一年工作的库和工具
  FrameworkWorkedWith	当前工作的扩展库和工具
  IDE	开发环境

- **数据分析师多用什么语言**

  职业DevType+语言LanguageWorkedWith

- 17 年的 MetricsAssess 评估指标 481