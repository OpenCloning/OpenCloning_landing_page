# Website

## Running locally

You need to install [hugo](https://gohugo.io/categories/installation/), a command line tool for building static websites.

Once you have hugo installed:

```bash
# Clone the repository
git clone https://github.com/manulera/OpenCloning_landing_page
cd OpenCloning_landing_page

# Install the theme as a submodule
git submodule init
git submodule update

# Then just:
hugo -D serve
```

The site should be live at http://localhost:1313/.

## Contributing

### Content

Content is mostly included in markdown files in the `content` folder. `content/_index.md` is the main page of the site, and the pages of the submenus are in the folders `content/team`, `content/partners`, etc.

The Hugo templates often use the [yaml frontmatter](https://gohugo.io/content-management/front-matter/) to include metadata. It's a section at the top of the file that starts with `---` and ends with `---` and is in yaml format. A good example of this is `content/_index.md`, where there is not actual markdown content, but only metadata.

To modify existing content, simply edit the markdown file.

#### Adding a new page

* Create a new folder in `content/` with the name of the page.
* Add a `_index.md` file to the folder.
* Add the necessary frontmatter to the file (at least `title`).
* Add the page in the navigation menu by editing the `[menu]` section in `hugo.toml`.

#### Adding images and other static files

Put your file in the `static` folder, if it's an image, put it in `static/images`. Then, in the markdown or html files you can reference it using the below path (don't forget the `/` at the beginning!).

```html
<img src="/images/service-3.png">
```

### Formatting and templates

The site uses a theme called [bigspring-light](https://github.com/gethugothemes/bigspring-light-hugo/). The way Hugo themes work is that the default theme files are used, unless you create a new file with the same name in the project folder. For instance, `layouts` contains some html templates for the site that override the ones present in the theme `themes/bigspring-light/layouts`. The same applies to files in `static`, `assets` (contains css for styling), etc.

⚠️**Important:** resist the temptation to modify the theme files. If you need to change the look of the site, do it by copying the file to the root project folder, and modifying the copy.

If you want to add a new template (e.g. the one for the team page), you have to create a new file in the `layouts/_default` folder that matches the name of the page. For instance, to add a new template for the team page (in `content/team/_index.md`), create `layouts/_default/team.html`. See that file for example of how to structure it.

## Content license

The content of this website is licensed [CC BY SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)