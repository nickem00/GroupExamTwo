---
revision:
    "2023-01-04": "(A, mos) First version."
---
Hints for a healthy team (Part 2)
========================

This is a collection of hints that may make your teamwork go smoother when you have started to work.

[[_TOC_]]



Precondition
------------------------

This text relies on that you read the first part of the "[Hints for a healthy team](./hints-for-a-healthy-team.md)".




Get a good start
------------------------

How to get going with the team work

* Read through spec and agree on your focus
* Sketch an UML diagram
* Agree on classes and larger modules (with several classes)
* Divide work in team - some do more, some do less - that is fine



Create the project structure
------------------------

* Create the directory structure and add the linters
* Start writing the README.md
* Create empty files, but name them so everybody sees the whole picture



Discuss the public interfaces
------------------------

* Create usable but empty classes & methods for the public interfaces
* Do not change the public interface without having a discussion on it, 
    * perhaps GitHub issues would be a great idea



Get going with tests
------------------------

Add the testsuite.

* Add empty test files
* Add testclasses for each testobject
* Add a empty/assertTrue testcase for each class
* Run the testsuite and see it work and pass



Integrate early and often
------------------------

* Integrate for the first time and see that it works
    * Make someone responsible for Main/Shell class that tie it all together into an application?

* Integrate early, at least once a week or when needed
* Do not integrate before each has a passing testsuite
* Integrate by:
    * Copying files
    * All write to the same repo and work in
        * main
        * branches
    * Fork and pull requests from feature branches



About working with Git
------------------------

* Git master & integration manager
    * Setup a git repo for the project
* Perhaps use the available python template to get a quick start
* Decide on how to merge code into main
* GitHub Actions to run the testsuite automatically on each commit