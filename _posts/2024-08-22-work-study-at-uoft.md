---
title: "Work Study Jobs at UofT: Why to Apply, What to Expect, & a Better Way to View Job Postings"
redirect_from:
  - /why-apply-to-uoft-work-study-jobs
description: "UofT's Work Study program is an underappreciated gem for finding part time work as a student; here's why you should apply (and how you can use my redesigned dashboard for viewing jobs)."
author: sadman
date: 2024-08-29 10:34:00 -400
last_modified_at: 2024-08-29 10:34:00 -400
categories: [University, Career]
tags: [university, work, part-time]

pin: true
math: false
mermaid: false
progressBarColor: "#8bd3ca"
hoverColor: "#8bd3ca"
home_image:
  path: assets/img/posts/2024-08-22-work-study-at-uoft/00-thumbnail.svg
  lqip: data:image/webp;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAICAIAAAB/FOjAAAAAwklEQVR4nD2OO1IDQRQD9Zld21QBxbE5GiHnYZ5EsAZlCrolfn5/JbP3JMmMgRv16uN9rQ8db/aLfJCmCEhaAFq0ndnZA2ColCliTDuqJQoi2662bZPMTPZGEXKCTLezlR9bXlig3fZaaK+VFi1KdFfN/AGrJEWSXACuIon2So/iIJ2CaREgVJLLu0hKsk0A1Bnci1txlgdgUCBJ4plFkqRtU5JvxaN4lPf0BI5ySbal6xGfACURlg7w0p/p2f4D/MsvqqODXq1EUkUAAAAASUVORK5CYII=
  alt: "Work Study Jobs at UofT: Why to Apply, What to Expect, & What I Made to Better View Job Postings"
image:
  show: false
  path: assets/img/posts/2024-08-22-work-study-at-uoft/00-thumbnail.png
  alt: "Work Study Jobs at UofT: Why to Apply, What to Expect, & What I Made to Better View Job Postings"

gallery-clnx-jobs:
  - image_path: assets/img/posts/2024-08-22-work-study-at-uoft/03-clnx-home-page.jpg
    alt: "CLNx job board landing page showing options for searching"
    caption: "CLNx job board landing page showing options for searching"
  - image_path: assets/img/posts/2024-08-22-work-study-at-uoft/03-clnx-job-page.jpg
    alt: "CLNx job listings page showing various job postings"
    caption: "CLNx job listings page displaying various job postings"

gallery-clnx-landing:
  - image_path: assets/img/posts/2024-08-22-work-study-at-uoft/02-clnx-landing-page.jpg
    alt: "CLNx landing page before login"
    caption: "CLNx landing page before user login"
  - image_path: assets/img/posts/2024-08-22-work-study-at-uoft/02-clnx-actual-home-page.jpg
    alt: "CLNx home page after user login"
    caption: "CLNx home page after user login"

---

<iframe style="border-radius:12px" src="https://open.spotify.com/embed/episode/5ml4va3CKRiLOHgRibEW24?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

<br>

If you're already familiar with the work study program at UofT then feel free to take a look at the following:

> **There's an easier to view work study jobs for this year** and you can check it out at <br>**<a href="{{ site.baseurl }}/uoft-work-study-2024" target="_blank">sadman.ca/uoft-work-study-2024</a>** (preview below).
{: .prompt-info }

> If you're interested in applying to work study jobs right now *(applications are still open!)* or want to explore what jobs are posted so you can better prepare in the future, then **try taking a look at the preview below or at the dashboard at the link**.

> While work study job postings on CLNx disappear if you don't view them before their respective application deadline, their data is archived on the dashboard so *they remain visible even after their application deadline passes*.

<style>
  .iframe-container {
    overflow: visible;
    position: relative;
    z-index: 9999;
  }

  .iframe-container iframe {
    width: calc(80% + 100px);
    height: 500px;
  }

  @media (min-width: 1300px) {
    .iframe-container iframe {
      transition: 4s ease;
    }

    .iframe-container iframe:hover {
      margin-left: -400px;
      margin-right: -50px;
      width: calc(160%);
      height: 900px;
    }
  }
</style>

<a href="{{ site.baseurl }}/uoft-work-study-2024" target="_blank" class="btn btn-primary mb-1" style="text-decoration: none; color: white;">View Work Study Dashboard</a>
<div id="iframe-container" class="iframe-container" style="background-size: 736px 500px; margin-top: 0;">
  <iframe id="workStudyIframe" src="/uoft-work-study-2024.html" frameborder="0" style="margin-top: 0;" onload="hideBackground()"></iframe>
</div>

<style>
  a.btn.btn-primary.mb-1:hover {
    text-decoration: none;
    color: white;
  }
  .iframe-container {
    margin-top: 0;
  }
  .iframe-container iframe {
    margin-top: 0;
  }
</style>

<script>
  function hideBackground() {
    document.getElementById('iframe-container').style.background = 'none';
  }

  function setThemeBackground() {
    const container = document.getElementById('iframe-container');
    const html = document.documentElement;
    const lightImageUrl = '{{ site.baseurl }}/assets/img/posts/2024-08-22-work-study-at-uoft/01-preview-light.jpg';
    const darkImageUrl = '{{ site.baseurl }}/assets/img/posts/2024-08-22-work-study-at-uoft/01-preview-dark.jpg';

    const isDarkMode = (html.hasAttribute('data-mode') && html.getAttribute('data-mode') === 'dark') ||
                       (!html.hasAttribute('data-mode') && window.matchMedia('(prefers-color-scheme: dark)').matches);

    if (isDarkMode) {
      container.style.background = `url(${darkImageUrl}) no-repeat`;
    } else {
      container.style.background = `url(${lightImageUrl}) no-repeat`;
    }

    container.style.backgroundSize = '746px auto';

    // Send isDarkMode to iframe
    const iframe = document.getElementById('workStudyIframe');
    iframe.contentWindow.postMessage({ isDarkMode }, '*');
  }

  // Set the initial theme background
  setThemeBackground();

  // Listen for changes in the color scheme preference
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', setThemeBackground);
</script>

<br>

## Work Study: (Underappreciated) Part-time <br>Employment for Students

**The work study job program at the University of Toronto (UofT) is an amazing resource for students to get part-time work during their studies**, but I'm surpised at how many fellow students aren't aware of it (many of them first years) or aren't familiar with the breadth of job opportunities offered.

As a student whose very first paid part-time position (that was also technically relevant to my area of study) was a work study job in my first year of post-secondary, I can attest to the value of the program, and I feel that the work experience I was able to get by work study early in my academic career helped out a ton when I was applying to internships and research opportunities later on.

> With over 4000 jobs posted every year for at least the past half decade (i.e. from what I've seen since my freshman year) and a huge variety of positions, **there truly is something for everyone in the work study program.**
{: .prompt-tip }

## What is work study?
Work study or work learn programs offer **part-time on-campus employment opportunities** to enrolled students so they can:
- develop workplace skills & experience
- explore potential career paths
- earn supplemental income

The beauty of work study in my opinion lies in it's **accessibility**: work study jobs are *exclusive* to students at the respective university and there are thousands of jobs posted every year[^1], so it can be **much easier** to land an offer for a position (even if you're a person with limited experience or skills) compared to searching for opportunities on external job boards like LinkedIn or cold-emailing professors to take part in research.

[^1]: at least at the University of Toronto

### Types of Jobs Posted For Work Study

Whether you're in your first year aspiring to start getting involved in a research lab or someone whose looking for a casual service-oriented job (such as a front-desk position or helping out with IT in lecture halls), there's 17 different types of positions available across all three of the UofT campuses (and plenty that are hybrid or remote to accomodate your commute/timetable) including:

| Casual                                | Technical                                             | Office                              |
|---------------------------------------|-------------------------------------------------------|-------------------------------------|
| Art & Design                          | Data Analysis                                         | Lab Coordination and Assistance     |
| Athletics & Sports                    | Technology: Audiovisual, IT, Web Design & Development | Library / Archive                   |
| Coaching / Facilitation               | Finance & Accounting                                  | Office & Administration             |
| Communications / Marketing / Media    | Research: Mixed-Methods                               | Project Coordination and Assistance |
| Student Mentors / Peers / Ambassadors | Research: Qualitative                                 |                                     |
| Events & Programming                  | Research: Quantitative                                |                                     |
| Front Line / Customer Service Support |                                                       |                                     |

### Why apply to work study positions?

In addition to helping you build your work experience, work study positions can also be a gateway to future employment opportunities: a lot of research-based positions can lead to summer research opportunities.

> *The opposite can be true as well*; I know students who started a work study position at a research lab in the summer and were offered part-time contracts to continue working part-time in the following semesters.

While I was employed in my work study position in first year, the professor I worked under actually reached out to me to offer me an extension to my employment for the summer (outside of the work study program). She offered a part-time contract to continue working in the lab (which was great for me because I had just started searching for summer internships and, as any freshman will attest, finding an internship in first year can feel close to impossible).

## Eligibility

> Note that eligibility for work study positions requires **enrolment for whichever semester you intend to work and apply for work study jobs in**. You don't need to be receiving student aid via OSAP or other government loans, but you do need to be taking some minimum number of courses.
{: .prompt-warning }


The specific minimum number of credits/courses you need to be taking in order to meet the definition of enrolment for work study positions can vary between institutions, but for all undergraduate students at the University of Toronto this works out to:

| Requirement                                | Details                                                                                       |
|--------------------------------------------|-----------------------------------------------------------------------------------------------|
| At least 4 courses in Fall/Winter & minimum 1 course in either semester        | 2.0 FCE (full course equivalent) — *a minimum of 0.5 credits in one session & 1.5 credits in the other* |
| At least 1 course in Summer          | 0.5 FCE (full-course equivalents)                                                             |

*There can be concessions to this requirement.* If you're a graduate student, then you just need to be registered in a session in order to be able to do a work study in that session (I'm not well-versed in the particulars of grad studies at UofT, but this probably still entails taking some minimum number of courses). Or if you have a disability or simply need to take a reduced course load due to circumstances beyond your control, you can reach out to the work study department and at the university and request for special accomodation.

***Enrolment is also not the only requirement for eligibility***. Students on a co-op term aren't eligible to apply for work study positions (even if they're taking courses on a part-time basis), and neither are students registered in the Toronto School of Theology (perhaps because their divine calling doesn’t include working at the campus libraries).

> You can read the official eligibility requirements for work study positions at UofT at:
> - [registrar.utoronto.ca/finances-and-funding/work-study-program/review-your-eligibility/](https://registrar.utoronto.ca/finances-and-funding/work-study-program/review-your-eligibility/) (viewable without login)
> - or [clnx.utoronto.ca/myAccount/jobs/work-study/aboutws](https://clnx.utoronto.ca/myAccount/jobs/work-study/aboutws.htm) (requires logging in to CLNx).
{: .prompt-tip }

**But if you're just a run-of-the-mill undergraduate student**—whatever department you may be in—**then you should be good to apply and get hired in any work study job.**

## Pay

This is a bit of a low point: **the pay for work study jobs... isn't great**. Most positions just offer the minimum wage in Ontario (rising to `CAD$17.20` this October 2024) and on top of that you can only work a maximum of `200 hours` in work study positions in the Fall/Winter semesters (`100 hours` for Summer positions).

A large part of this is because the university subsidizes 70% of the pay for work study students, leaving supervisors to cover the remaining 30% (which of course does mean lower risk on the part of staff employing work study students and is a big reason why there are so many professors posting so many work study positions).

Some work study positions do pay more however; in my first work study position the department I worked in topped off the minimum pay with an additional `CAD$3` per hour. Of course, even the minimum pay can be very nice supplementary income: work the maximum number of hours in a single session and you're looking at a pre-tax income `CAD$3440` in the Fall/Winter or `CAD$1720` in the Summer (enough to purchase a high-end laptop for your studies and still have some leftover for splurging elsewhere).

> You don't have to work the maximum number of hours in work study jobs, so depending on the requirements of the position you can keep your supervisor informed of busy periods in your timetable/semester and work fewer hours during those times; **the work study program is designed with putting your education first**, which is why professors and supervisors are more than welcome to accomodate your schedule.
{: .prompt-tip }

## Applying

Work study job postings at the University of Toronto can be viewed & applications can be sent using **CLNx (Career & Co-Curricular Learning Network) at [clnx.utoronto.ca/myAccount/jobs/work-study/wsjobs](https://clnx.utoronto.ca/myAccount/jobs/work-study/wsjobs)**.

CLNx is a catch-all hub for cross-university events & workshops, accessing student resources (such as appointments for activating your student TCard for first years), and access to on/off-campus job boards (one of which is for work study jobs).

<div style="--images-per-row: 3;">
{% include my-gallery.html images=page.gallery-clnx-landing %}
</div>

The dashboard for work study jobs is a bit tucked away under the navigational dropdown[^2] under: `Hamburger Menu on the top-left` `>` `Jobs & Recruitment` `>` `Work Study` `>` `Work Study Jobs`.

[^2]: Which is why every semester you have someone on the university subreddit at [reddit.com/r/uoft](https://reddit.com/r/uoft/) post about how they can't find any work study job postings after the application period opens

You can click on the blue `Search` button to view all posted jobs (that aren't past the application deadline) or one of the options under `Quick Searches` to quickly view jobs expiring today/in the next 10 days, jobs you viewed/applied to previously, or new jobs posted since you last logged in.

<div style="--images-per-row: 3;">
{% include my-gallery.html images=page.gallery-clnx-jobs %}
</div>

![What a job description page looks like on CLNx]({{ site.baseurl }}/assets/img/posts/2024-08-22-work-study-at-uoft/03-example-job.png)
*What a job description page looks like on CLNx*

The work study job board itself is built on a platform by [Orbis Communications](https://orbiscommunications.com) (which, from a cursory glance at their website, appears to build job boards for quite the number of institutions), and while the platform works fine **it's definitely not as easy to use as it could be**.

## Issues with the current work study job board

> The main issue with the work study job board on CLNx is that **viewing & comparing anything more than a handful of work study job postings can quickly become unwieldy**.
{: .prompt-danger }

You have to deal with all of the following:

##### Vague Job Titles
*Many jobs have incredibly vague titles*, such as `"<<VERB or NOUN>> Assistant"` or just plain old `"Research Assistant"`, which means that you basically need to open every individual job to read the description and then understand what they're actually about.

##### Can Only View Job Details After Opening a Job Post
*Clicking on a job posting opens it in a new tab*, which can be slightly annoying but at least means you can jump between multiple job descriptions at the same time. Annoyingly, however, there's no way to save job postings for viewing later on the job description page either (you can shortlist jobs in the listings *after* doing keyword searches or filtering, but not *in the actual page with the job description itself*, which is a rather annoying UX snafu).

##### Automatic Sign Out Timer
There's also an automatic sign out timer, which rather unfortunately not only signs you out after a couple minutes but also redirects any open job postings back to the job board home screen (which is *especially* annoying if you took the time to meticulously open up a whole bunch of job postings). Thankfully there *is* a option to filter jobs that you have already viewed, but that doesn't have any view date filters (e.g. "Viewed today", "Viewed yesterday", etc.) or sorting (e.g. "Order by last viewed") so it shows all job postings that you viewed since the start of the application period.

##### Slow Search
There's also a keyword search function, along with an advanced search option for filtering fields like location (i.e. which campus a job is located, or whether it is hybrid/remote), position type, and more. *Unfortunately* the search is also a bit slow: each individual search takes 1-2 seconds to load, which doesn't sound like much but the consistent interruptions add up over time & can result in compounding frustration if you're trying to look for job postings with specific keywords (such as programming languages or tools you learned about in your courses).

##### Limited Information in Search Results
Adding on to that, while searches for keywords do successfully filter to only show jobs with the matching keyword somewhere in their title, description, or other field, the page listing filtered jobs after searches still only shows the title and department, which means you basically need to either glean the gist of a job from the title or open every individual filtered job to read the description and then understand what they're actually about.

##### Expired Job Postings Become Inaccessible
And finally, once a work study job posting expires (i.e. it is the past it's application deadline), you can't access it unless you viewed it before it expired. Furthermore, once the work study application period ends, all work study job postings are made inaccessible to all students (except for the ones you applied to).

## Building something better

So with all of those considerations at hand, it's safe to say it would be nice if a better design were available. Well, I've actually been archiving the HTML pages of all work study jobs posted every time applications opened since my first year (this isn't exactly something new for me either, I scraped all of my department's 12-16 co-op job postings since the first day I received access in September 2023 and extracted them all to a SQLite database), so I've been able to view the data markup for job postings and think about better ways to display them for a quite a long time.

I've been procrastinating on doing anything about it for the longest time though, so this summer I decided to make the most of those thoughts and design a brand-new easier-to-navigate dashboard to display the work study job postings that are visible on the official CLNx job portal right now (that is, for the 2024-2025 fall/winter semester).

> **The dashboard is live and you can view it at [sadman.ca/uoft-work-study-2024]({{ site.baseurl }}/uoft-work-study-2024)**.
{: .prompt-info }

![Redesigned Work Study Job Dashboard]({{ site.baseurl }}/assets/img/posts/2024-08-22-work-study-at-uoft/04-new-work-study-job-dashboard.png)*Redesigned Work Study Job Dashboard*

![Zoomed-in view of the work study dashboard]({{ site.baseurl }}/assets/img/posts/2024-08-22-work-study-at-uoft/04-zoom-in.png)
*Zoomed-in view of the work study dashboard*

I'll save the technical details for a future post; the gist of backend behind it is that *the raw data was scraped from the CLNx job board* and is displayed on using the incredibly performant [AG Grid library](https://www.ag-grid.com/) (with some additional customization by myself). And in many ways, **it's a lot easier to use for browsing job postings than CLNx.**

> After you've taken a look at jobs on the dashboard, you can just **search for jobs you're interested by their job ID on the CLNx work study dashboard & apply to them directly** (without having to click through hundreds of job postings on CLNx).
{: .prompt-tip}

### Why to use it

Some of the standout features include:
- **Viewing job descriptions & required qualifications on the job listing page itself** (vs. having to open every job in a new tab to view the description on CLNx)
- **Grouping job postings by user-specified fields** (such as position type, department, campus, etc.) to easily see, say, all jobs posted under a specific professor or department
- **Detailed & faster filtering & sorting capabilities**, including setting fine filters such as date ranges or multiple conditional text filters (e.g. "finance AND python", "python OR java OR web", etc.)
- **Quick switching between filters and sort orders**, including viewing jobs expiring soon
- **Viewing expired jobs and their respective job descriptions**
- **Selecting multiple job postings** (using checkboxes) and exporting posting data (including description and application deadline) to .csv or .xlsx files to view/analyze jobs using a tool of your own choice (e.g. Excel, Google Sheets, Python Pandas, etc.)
- **A button to toggle between light and dark themes** :))

At the time of writing, it's been a bit over 2 weeks since work study job applications first opened for the following Fall/Winter semesters, and while it is true that applying early is your best shot at landing a job, there's still plenty of time (almost a month) left until job applications close, so *whether you're a first year student looking to snag your first paying part-time job or in your senior year and looking to build connections with a professor in a lab you're interested in*, **I highly recommend taking a look at the work study jobs out there and consider applying to a few that you might be interested in.**

You never know, you might just land something you love that kickstarts the rest of your career.

-----

-----

-----

## Footnotes