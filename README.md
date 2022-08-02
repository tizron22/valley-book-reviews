# Valley Book Reviews

---

[Click here to view website on Heroku](https://valley-book-reviews.herokuapp.com/)

---

## Table Contents

> 1.  [Overview](#overview)
> 2.  [UX](#ux)
>     1.  [Strategy](#strategy)
>     2.  [Scope](#scope)
>     3.  [Structure](#structure)
>     4.  [Skeleton](#skeleton)
>     5.  [Surface](#surface)
> 3.  [Features](#features)
>     1.  [Existing Features](#existing-features)
>     2.  [Future Feature Considerations](#future-feature-considerations)
> 4.  [Technologies Used](#technologies-used)
> 5.  [Testing](#testing)
> 6.  [Deployment](#deployment)
>     1.  [How this Project was Deployed](#how-this-project-was-deployed)
>     2.  [How to Run this Project in your Browser](#how-to-run-this-project-in-your-browser)
>     3.  [How to Run this Project Locally](#how-to-run-this-project-locally)
> 7.  [Credits](#credits)
>     1.  [Code Snippets](#code-snippets)
>     2.  [Pictures](#pictures)
> 8.  [Acknowledgements](#acknowledgements)
> 9.  [Disclaimer](#disclaimer)

## Overview

**Valley Book Reviews**

Valley Book Reviews is a web application that allows you to create, read, update and delete your own book reviews along side being able to vote on other peoples reviews.

---

# UX

## Strategy

### Stakeholder Requirements

> #### **External Users**
>
> As a user, I would like an app where I'll be able to compare book reviews from other readers have already read and can see which ones are popular among other people. Being able to vote on the reviews or specific books will allow me see which ones are actually popular and recommended rather than just reading a bio from a sellers site which may not be genuie. Having a system where I can create, read, update and delete reviews would allow me to engage with the app.

> #### **Site Owner**
>
> As the site owner, I would like this site to be the go to where book enthusiasts go to either write thier reviews or look for a new recommendation to read. Having a voting system allows users to see others thoughts on certain books where each user can only like or dislike a specific review,

### User Stories

1. `As a potential new user, I would like the site to be easily usable, understandable and user friendly.`
2. `As a new user, I would like to be able to register an account to be able to use the site.`
3. `As a current user, I would like to be able to submit new and vote on exisiting reviews on the site.`
4. `As a returning user, I would like to be able to edit or delete previous reviews that I submitted on the site.`

---

## Scope

### Requirements

> Easy to Navigate and User Friendly
>
> - Straight forward and uncomplicated view.

> Reuseability
>
> - Users must be able to submit, edit, delete and read multiple reviews they've submitted.

> Limited functionality without an account
>
> - Unless users register for an account, they are only able to read reviews and not able to like/dislike reviews.

## Structure

> ### Base Sheet
>
> Includes a nav bar which contains a hamburger menu selector, site name and user account to register or log into the site.
> When the hamburger menu is clicked a side bar shows that allows the user to navigate around the site.
> Includes footer which holds the social media links for the user to connect with us.

> ### index Sheet
>
> Includes a container that holds a welcome message and a random review to intrigue user interest.
> If the user isn't logged in a button will show allowing users to navigate to enable full functionality.

> ### About Sheet
>
> Includes a brief description of what the site is about.

> ### My Reviews Sheet
>
> Includes a section where users are able to submit new reivews.
> The user is also able to review thier previous submissions and either edit, vote or delete them.

> ### All Reviews Sheet
>
> All users who access this sheet is able to see each review that has been submitted.
> Only logged in users are able to vote and see the voting options.

> ### Edit Reviews Sheet
>
> Users are taken to a new sheet where they are able to edit the selected review details before re-submitting it.

> ### Login Sheet
>
> Includes a container where users are able to login after they've registered for an account.

> ### Register Sheet
>
> Includes a container where the user is able to register for an account to fully access the app.

---

## Skeleton

### Wireframes

> - [Base Web Page Wireframe](./valley-book-reviews/static/wireframes/base-web.pdf)
> - [Base Mobile Page Wireframe](./valley-book-reviews/static/wireframes/base-mobile.pdf)
> - [Base Web Menus Page Wireframe](./valley-book-reviews/static/wireframes/base-web-menus.pdf)
> - [Base Mobile Menus Page Wireframe](./valley-book-reviews/static/wireframes/base-mobile-menus.pdf)
> - [Home Content Page Wireframe](./valley-book-reviews/static/wireframes/home-content.pdf)
> - [About Content Page Wireframe](./valley-book-reviews/static/wireframes/about-content.pdf)
> - [My Reviews Content Page Wireframe](./valley-book-reviews/static/wireframes/my-reviews-content.pdf)
> - [All Reviews Content Page Wireframe](./valley-book-reviews/static/wireframes/all-reviews-content.pdf)
> - [My Account Content Page Wireframe](./valley-book-reviews/static/wireframes/my-account-content.pdf)
> - [My Account Register Content Page Wireframe](./valley-book-reviews/static/wireframes/my-account-register-content.pdf)

## Surface

---

## Features

### Existing Features

---

## Technologies Used

> - The project was written in HTML, CSS and JavaScript.
> - The project uses [FontAwesome](https://fontawesome.com/) for the free icons used for web development.
> - The project uses [Bootstrap V5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) for page standardisation, modal functionality and model template.
> - The project was written in [Visual Studio Code IDE](https://code.visualstudio.com/).
> - The project was tested utalising [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extention in VS code.
> - The project uses [GIT](https://git-scm.com/) for verison control and [GitHub](https://github.com/) as a remote repository.
> - The project uses [GitHub Pages](https://pages.github.com/) for hosting the site.
> - The project's wireframes were designed in [Balsamiq](https://balsamiq.com/wireframes/).
> - The project's HTML was validated using [W3C HTML markup validator](https://validator.w3.org/).
> - The project's CSS was validated using [W3C jigsaw CSS validator](https://jigsaw.w3.org/css-validator/).
> - The project's JavaScript was validated using [JS HINT JavaScript validator](https://jshint.com/)
> - The project's performance and accessibility was tested using [Google Chrome's Lighthouse](https://developers.google.com/web/tools/lighthouse) and [WebAim's W.A.V.E](https://wave.webaim.org/).

---

# Testing

> ## Testing Documentation
>
> - The testing documentation can be found here:- [TESTING.md](TESTING.md)

---

# Deployment

> ## How this Project was Deployed

> ## How to Run this Project in your Browser

> ## How to Run this Project Locally

---

## Credits

### Code Snippets

> #### Side Bar
>
> Sample code used from bootstrap website as the template for this website, the code was adapted to suit needs credit for the code is from bootstrap.
>
> - [Get Bootstrap Side Bars Example](https://getbootstrap.com/docs/5.0/examples/sidebars/)

> #### Login & Registering
>
> Some ideas and thought process's from `Arpan Neupane` YouTube channel on how to create flask authentication was used in this project.
>
> - [Python Flask Authentication Tutorial - Learn Flask Login](https://www.youtube.com/watch?v=71EU8gnZqZQ)

### Pictures

> Library Photo
>
> - Photo by [Brasenose College Oxford](https://www.bnc.ox.ac.uk/images/library/Brasenose_College_Library_05.jpg)
>   ) on Goolge Images.

---

# Acknowledgements

---

# Disclaimer

## **This website is for educational purposes only.**

---
