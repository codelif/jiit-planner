# jiit-planner
Quickly view your upcoming events(lectures, tutorial, etc) at JIIT

## Try it out (in beta)
Visit https://planner.codelif.in

## Development deployment
Clone this repository and cd into it then enter the following commands.
```sh
poetry install
poetry run flask --app jiit_planner run
```

## Roadmap
 - [x] Make the UI uglier
 - [ ] Add support for multiple semesters
 - [ ] Add support for multiple streams (BCA, BBA, etc)
 - [ ] Fix [`jiit-tt-parser`](https://github.com/codelif/jiit-tt-parser)

#### Also checkout the sister project: [`codelif/jiit-tt-parser`](https://github.com/codelif/jiit-tt-parser)
That project contains the actual backend code. `jiit-planner` is a frontend to it.
