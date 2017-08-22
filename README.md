# Inventus

Inventus is a spider designed to find subdomains of a specific domain by crawling it and any subdomains it finds. It's a [Scrapy](https://scrapy.org/) spider, meaning it's easily modified and extendable to your needs.

# Demo

[![asciicast](https://asciinema.org/a/PGIeEpEwZTUdgxrolBpCjljHL.png)](https://asciinema.org/a/PGIeEpEwZTUdgxrolBpCjljHL)

# Requirements

 - Linux -- I haven't tested this on Windows.
 - Python 2.7 or Python 3.3+
 - [Scrapy](https://scrapy.org/) 1.4.0 or above.

# Installation

To install Inventus you need to first install [Scrapy](https://scrapy.org/). Once Scrapy is installed, simply clone the repo and you should be good to go.

```
$ git clone https://github.com/nmalcolm/Inventus
```

# Usage

The most basic usage of Inventus is as follows:

```
$ cd Inventus
$ scrapy crawl inventus -a domain=facebook.com
```

This tells Scrapy which spider to use ("inventus" in this case), and passes the domain to the spider. Any subdomains found will be sent to `STDOUT`.

The only other parameter you can pass is `subdomain_limit`. This sets a max limit of subdomains to discover before quitting. The default value is 10000, but isn't a hard limit.

```
$ scrapy crawl inventus -a domain=facebook.com -a subdomain_limit=100
```

# License

Released under the MIT License. See LICENSE.