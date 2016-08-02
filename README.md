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

Wepana is an analyzer for web page content powered by [Python](https://www.python.org).
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

```
pip install wepana
```

### Load

Import analyzer

```
from wepana import WebPageAnalyzer
```

Load from url.

```
# load with init
site = WebPageAnalyzer(url='http://github.com')
# load after init
site.connect('http://github.com')
```

Load from file.

```
analyzer = WebPageAnalyzer()
analyzer.read_file('/path/to/the/file.html')
```

Load from text.

```
analyzer = WebPageAnalyzer()
analyzer.read_text('text content')
```

Check analyzer is ready.

```
analyzer.read()
```

Reset analyzer.

```
analyzer.reset()
```

### Analyze

Get title.

```
analyzer.get_title()
```

Get keywords.

```
analyzer.get_keywords()
```

Get images.

```
analyzer.get_images()
```

Get links.

```
analyzer.get_links()
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