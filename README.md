# jiit-planner
Quickly view your upcoming events(lectures, tutorial, etc) at JIIT

## Try it out (in beta)
Visit https://planner.codelif.in/B5 (here replace B5 with your batch) 

## Development deployment
```sh
poetry run flask --app jiit_planner run
```

## Roadmap
 - [ ] Make the UI uglier
 - [ ] Add support for multiple semesters
 - [ ] Fix [`jiit-tt-parser`](https://github.com/codelif/jiit-tt-parser)

#### Also checkout the sister project: [`codelif/jiit-tt-parser`](https://github.com/codelif/jiit-tt-parser)
That project contains the actual backend code. `jiit-planner` is a frontend to it.
