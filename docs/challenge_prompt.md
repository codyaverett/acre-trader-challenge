# AcreTrader Backend Software Engineer Take Home Project 

## A To-Do List Web Service API

### Description
The intention of this task is to assess the candidate’s thinking, experience with web development, and ability to perform web service development tasks. The candidate’s work will be reviewed for code quality, coverage, project structure, scope and complexity of work, etc. Code quality includes concepts such as readability (naming conventions, abstraction practices, adherence to standards and best practices, etc.). Coverage means how comprehensively the work performed addresses the project requirements. Project structure refers to how the code is organized.

## Submission
The candidate should provide access to a public git repository containing the current state of the work submitted. A formatted README.md or some other form of structured instructions for running the project locally should be provided, and should include instructions for testing functionality.

Part of the review process is to verify work authenticity. Using solutions from web searches and standard approaches outlined in documentation is acceptable and appropriate. However, blatant large-scale plagiarization of code bases, tutorials, etc. is grounds for disqualification.

## Technical Interview
AcreTrader developers will review the submitted work independently, and a technical interview may be scheduled to review the work together with the candidate. This interview may include demonstrations of functionality by the candidate, so the candidate should have their local development environment ready for screen sharing. Having an IDE ready will also be beneficial, as it is not uncommon to ask about how a candidate might refactor some code or change some functionality.

## Technical Requirements
AcreTrader back end development is generally performed using Python. Our main services are built using Django. The candidate should use Python for performing the trial work. While Django is not a requirement, demonstrable Django experience is desirable. Competent work in a similar web framework is acceptable and will not implicitly be reviewed negatively.

## Project Details
The service should perform CRUD operations on a database of to-do records. The service will be used privately by one user.

A to-do record should consist of the date and time the record was created, the date and time the to-do is due, the date and time the to-do was done, a description of the to-do, and the status of the to-do.

The service should provide valid and appropriate HTTP responses for the type of API resource request.

### Required
- Create a to-do record by specifying the description and desired date and time of completion.
- Retrieve a list of to-do records.
- Update a to-do record with new values for meaningful fields.
- Delete a to-do record.

### Optional
These additional features would be nice to see, but aren’t necessary for the project review. You’re welcome to ignore them, make an unfinished attempt that can be discussed in the technical interview, or complete them.

- Filtering, searching, and sorting to-do records by meaningful fields.
- Implement some level of authentication, whether at the HTTP, app, or some other level.

### Expectations
Implementation and naming decisions are left to the candidate. AcreTrader developers are less concerned with technologies used than why and how they were used. As one extreme, the candidate may opt to create a barebones service and demonstrate its functionality using curl requests, another extreme example would be a full-fledged Django DRF application with a React frontend. Both approaches can be valid depending on the context of their selection, and the candidate’s ability to participate in a discussion about such decisions is no less important than the quality of the code they produce.

The candidate should feel free to use and show off frameworks, libraries, and ideas that inspire or motivate them, while not feeling forced or expected to implement flashy or cutting-edge solutions if they feel a conservative approach is appropriate. The quality of a given solution is relative to its context and circumstances. Neither approach (or any in between) will implicitly be reviewed as less desirable.
