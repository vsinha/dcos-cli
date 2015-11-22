# DCOS-CLI Docs and Website

## Run it locally

Ensure you have installed everything listed in the dependencies section before
following the instructions.

### Dependencies

* [Bundler](http://bundler.io/)
* [Node.js](http://nodejs.org/) (for compiling assets)
* Python
* Ruby
* [RubyGems](https://rubygems.org/)

### Instructions

1. Install packages needed to generate the site

    * On Linux:

            $ apt-get install ruby-dev make autoconf nodejs nodejs-legacy python-dev
    * On Mac OS X:
    
            $ brew install node

2. Clone the DCOS-CLI repository

3. Change into the "docs" directory where docs live

        $ cd docs

4. Install Bundler

        $ gem install bundler

5. Install the bundle's dependencies

        $ bundle install

6. Start the web server

        $ bundle exec jekyll serve --watch

7. Visit the site at
   [http://localhost:4000/dcos-cli/](http://localhost:4000/dcos-cli/)

## Deploying the site

1. Clone a separate copy of the DCOS-CLI repo as a sibling of your normal
   DCOS-CLI project directory and name it "dcos-cli-gh-pages".

        $ git clone git@github.com:mesosphere/dcos-cli.git dcos-cli-gh-pages

2. Check out the "gh-pages" branch.

        $ cd /path/to/dcos-cli-gh-pages
        $ git checkout gh-pages

3. Copy the contents of the "docs" directory in master to the root of your
   dcos-cli-gh-pages directory.

        $ cd /path/to/dcos-cli
        $ cp -r docs/** ../dcos-cli-gh-pages

4. Change to the dcos-cli-gh-pages directory, commit, and push the changes

        $ cd /path/to/dcos-cli-gh-pages
        $ git commit . -m "Syncing docs with master branch"
        $ git push
