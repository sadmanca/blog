---
title: 'Analyzing UofT PEY Co-op Job Postings — Part 2: Building a Better Job Postings Dashboard'
redirect_from:
  - /uoft-pey-coop-jobs
  - /uoft-pey-coop-job-postings
  - /analyzing-pey-postings-part-2
description: "Taking 10 MB of UofT PEY Co-op job posting data (2000+ jobs) & displaying postings on a redesigned modern dashboard (so future students have a better idea of what to expect)"
author: sadman
date: 2024-09-11 0:55:00 -400
last_modified_at: 2024-09-11 0:55:00 -400
categories: [Co-op, Data Analysis]
tags: [university, code, python, work, co-op]

pin: true
math: false
mermaid: false
progressBarColor: "#315080"
hoverColor: "#7aaeff"
home_image:
  path: assets/img/posts/2024-09-10-analyzing-pey-postings-part-2/00-thumbnail.svg
  lqip: /9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAIABADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwC/MZPMXZ612OhmX7OPMoor1803R5+B2Z//2Q==
  alt: "Analyzing UofT PEY Co-op Job Postings — Part 2: Building a Better Job Postings Dashboard"
image:
  show: false
  path: assets/img/posts/2024-09-10-analyzing-pey-postings-part-2/00-thumbnail.png
  alt: "Analyzing UofT PEY Co-op Job Postings — Part 2: Building a Better Job Postings Dashboard"

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

> **Check out <a href="{{ site.baseurl }}/uoft-pey-coop-jobs-2023" target="_blank">sadman.ca/uoft-pey-coop-jobs-2023</a> to view all jobs posted for the 12-16 month University of Toronto PEY Co-op program from September 2023 to June 2024**.
{: .prompt-info }

> *The job portal for current PEY Co-op students **opens this September 16**,* so if you're...
> - a 3rd year student looking to get a headstart on preparing your applications for specific positions/companies, or
> - a prospective student who wants to explore what types of jobs are posted (and what companies post co-op jobs)...

> ...then **try taking a look at the preview below or at the dashboard at the link**.

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

<a href="{{ site.baseurl }}/uoft-pey-coop-jobs-2023" target="_blank" class="btn btn-primary mb-1" style="text-decoration: none; color: white;">View UofT PEY Co-op Job Postings (2023-2024) Dashboard</a>
<div id="iframe-container" class="iframe-container" style="background-size: 736px 500px; margin-top: 0;">
  <iframe id="workStudyIframe" src="/uoft-pey-coop-jobs-2023.html" frameborder="0" style="margin-top: 0;" onload="hideBackground()"></iframe>
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

## The UofT PEY Co-op program & why I built this dashboard

The Professional Experience Year (PEY) Co-op program at the University of Toronto (UofT) is a 12-16 month internship program that undergraduate students can take part in after their third year of studies (there's also now a 4-month co-op term in the summer after second year, but I'll leave that topic for future post). The program is a great way to gain work experience, build connections with industry professionals, and get a taste of what it's like to work in a professional setting.

There's a decent amount of information about the PEY Co-op program available online (just check out [the program info page on discover.engineering.utoronto.ca](https://discover.engineering.utoronto.ca/experiential-learning/professional-experience-year-pey/)), along with [countless Reddit threads](https://www.google.com/search?q=uoft+pey+reddit) about the program, but **one thing that's always been unavailable is a full, comprehensive overview of the co-op positions posted on the job portal for students enrolled in the PEY program.**

> That's why I built a dashboard of all the jobs that were posted while I had access to the PEY portal at **<a href="{{ site.baseurl }}/uoft-pey-coop-jobs-2023" target="_blank">sadman.ca/uoft-work-study-2024</a>**.
{: .prompt-info }

As a UofT engineering student who started their 3rd year last fall (and went through the whole job viewing/application process on the PEY portal), this was probably the part of the program that I was the most curious about going into it, so this is my way of making sure that future students have a better idea of what to expect when they go through the PEY Co-op program.

## The gaps this dashboard aims to fill

### What employers are hiring, how many students they're hiring, and what types of jobs are available

There's a fair amount of talk in UofT circles (and on the PEY program's informative web pages) about what some of the biggest PEY Co-op employers are (e.g. AMD, Intel, etc.), but as a student it can still feel apprehensive if you're not aware of approximate numbers or ballpark figures of how many students you can expect different companies to hire.

For example, while I knew that Red Hat was an employer for PEY students, one thing that I didn't expect was for them to only open two positions for the entire academic year in 2023-2024 (and in late November of all months too).

Similarly, AMD—*which in the UofT engineering circles is known to hire lots of electrical & computer engineering (ECE) students*—had 59 separate job postings (with some postings hiring multiple students). Quite the high number, but it's still a bit of a surprise to see the actual number of postings.

Before I got access to the PEY job portal, *I wanted to know what types of jobs were posted, what companies posted jobs, and what the job descriptions were like. I wanted to know what to expect and what I should be preparing for. I wanted to know what the job market was like for students in the PEY program.* I wasn't able to get the most extensive overview of all that back before I had access to the PEY portal, so through this dashboard I wanted to make sure that future students have a better idea of all that.

---

Another bit of a sore spot for the PEY Co-op program is that the majority of positions are in software/hardware development (which is great if you're an electrical/computer engineering or computer science student, but not so much if you're in another discipline).

If you're in fields like civil, mechanical, or mineral engineering, you'll find that there are fewer positions available for you. For mineral engineering students specifically (of which there are really only a handful every year, less than 100 students across all years for almost the last decade or so), a lot of the positions involve travelling to remote locations (which can be a bit of a turn-off for some students), so being aware of things like that can be very helpful for students in those disciplines to find co-op positions best suited for them.

Personally I was quite surprised at the number of hardware development positions available (I was expecting software development positions to completely dominate job postings for ECE/CS students), which I suppose should be good news to future students looking for work in the embedded/FPGA/analog electronics sectors.

### Data that isn't available on the official PEY portal

Finally, one last thing I want to mention is that each job posting on the dashboard has an additional field that *isn't available on the PEY portal*: **the date that each job was posted.**

This is something that I think is very important for students to know about, as it can give you a sense of how the open pool of jobs available at any point in time changes over the course of the fall and winter semesters.

In general, you can expect the number of job postings to peak at the very start of the fall/winter semesters (September/January), and then slowly ramp down over time with some intermittent jumps (usually when a specific company posts a large number of their jobs on some given day).

## Data quality notes
### About data timeliness

One thing to be aware of while you're going through the dashboard is that it's only a snapshot of a single year. I don't have access to any of the jobs that are going to be posted on the (new) PEY portal starting next week September, so I can't update the dashboard with new job postings. The data is from the 2023-2024 academic year, which came off the heels of the COVID-19 pandemic recovering but not completely unscathed. I remember going to the biggest career fair on campus that fall hosted by UofT's Your Next Career Network (YNCN) club, and a common theme through out was how the hiring at companies had ramped down compared to before the pandemic, which meant that they were looking to hire fewer co-op students and correspondingly posted fewer jobs.

From anecdotes I've heard from friends going through PEY right now, I can say that there's a definite effort to ramp the number of co-op students hired back up soon, and so hopefully if you go through the PEY Co-op program sometime in the next few years you should be able to expect an even better job portal compared to the one I went through. I can't say for sure how the jobs posted will change, but it's something to keep in mind when you're looking at the data.

### About data quality

Another thing to bear in mind while you're going through the dashboard: all of the data was obtained by my scraping of HTML pages for each job posting on the PEY portal (you can read about how I did so in my previous part of this series on UofT PEY Co-op jobs [here]({{ site.baseurl }}/posts/analyzing-pey-postings-part-1)). I was definitely in the early stages of figuring out how to save all the scraped data properly back when I first got access to the PEY portal (I had saved similar data for work study postings before, but it was always disorganized and I never got around to properly scraping/analyzing them until fairly [recently]({{ site.baseurl }}/work-study-at-uoft)), but thankfully I had the foresight to mostly organize saved HTML files so that it wasn't a hassle to process all of them at a later date.

## Closing thoughts: let me know what you think

I genuinely hope that this dashboard is helpful to future students in PEY, and even if you're not registered for PEY or studying at the University of Toronto I hope that it gives you a some idea of what the internship/co-op job market is like for undergraduate students (or at least what it was like back when I did my 3rd year of studies). If you have any questions, feel free to ask them in the comments below or reach out to me personally at sadman.hossain(at)mail.utoronto.ca (or on Discord, my personal group chat application of prefernece, at @sadmanca; I'm always lurking on the UofT ECE servers).