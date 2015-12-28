# PrettyLog
A way to make your Python logs pretty without disrupting normal logging. Also
outputs to a file if necessary.

## Installation
With the setup.py installation is quite easy.

```sh
$ cd path/to/main/folder
$ pip install .
```

## Basic Usage
1. Create a new PrettyLog object.

  ```python
  import PrettyLog from prettylog
  LOGGING = PrettyLog()
  ```
2. Call functions on PrettyLog with formatted text.

## Built In Functions
`push(message, level="debug")` is the main function for PrettyLog. This pushes
your message to both output streams with the label given (default is "debug").

## Testing
Testing code will be added soon.
