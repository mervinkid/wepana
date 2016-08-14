# wepana: A Web Page Analyzer

[![Python](https://img.shields.io/badge/Python-3.5-orange.svg?style=flat&maxAge=2592000)](https://www.python.org)
[![License MIT](https://img.shields.io/badge/License-MIT-lightgray.svg?style=flat&maxAge=2592000)](https://opensource.org/licenses/MIT)
[![Release](https://img.shields.io/badge/Release-v0.2.0-lightgray.svg?style=flat&maxAge=2592000)]()

```
 __      _____ _ __   __ _ _ __   __ _
 \ \ /\ / / _ \ '_ \ / _` | '_ \ / _` |
  \ V  V /  __/ |_) | (_| | | | | (_| |
   \_/\_/ \___| .__/ \__,_|_| |_|\__,_|
              |_|
```

Wepana is an analyzer for web page content powered by [Python](https://www.python.org).<br>
It compatible with both python2 and python3. 

## Dependencies

No any third part dependencies.<br> 
Wepana can auto detect the major version of python runtime and use the build in library for feature implementation.

## Features

- Auto load content from url.
- Load content from file.
- Load content from string value.
- Get image urls.
- Get html link src target urls.
- Get meta information.
- Get keyword information.

## Usage

### Installation

```bash
pip install wepana
```

### Sample

```python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
from wepana import WebPageAnalyzer

def foo():
    # load with init
    analyzer = WebPageAnalyzer(url='http://github.com')
    
    # load after init
    analyzer.connect('http://github.com')
    
    # load from file
    analyzer.read_file('/path/to/the/file.html')
    
    # load form text
    analyzer.read_text('text content')
    
    # check status
    if not analyzer.read():
        print('wepana analyzer is not ready.')
        return

    # get title
    analyzer.get_title()
    
    # get keywords
    analyzer.get_keywords()
    
    # get images
    analyzer.get_images()
    
    # get likes
    analyzer.get_links()
    
    # reset analyzer
    analyzer.reset()

if __name__ == '__main__':
    foo()

```

## Contributing

1. Fork it.
2. Create your feature branch. (`$ git checkout feature/my-feature-branch`)
3. Commit your changes. (`$ git commit -am 'What feature I just added.'`)
4. Push to the branch. (`$ git push origin feature/my-feature-branch`)
5. Create a new Pull Request

## Authors

[@Mervin](https://github.com/mofei2816) 

## License

The MIT License (MIT). For detail see [LICENSE](LICENSE).