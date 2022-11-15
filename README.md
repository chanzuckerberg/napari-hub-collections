# napari hub collections

This repository contains the content for plugin Collections on the napari hub.

Plugin Collections are sets of plugins from the [napari hub](https://www.napari-hub.org/) curated by fellow community members. A collection might be: 
- A protocol or recipe that shows how to use a set of plugins to complete an image analysis workflow
- A toolkit or pack that helps a napari user get started within a research domain
- An assortment that is defined by another central theme that connects the plugins

Have an idea for a Collection you'd like to share with the napari community? Curate your own Collection following the directions below.

## How to Submit a Collection

Collections can be submitted directly to this repo via a pull request. Download the collection-template.yml file from the [the napari-hub-collections repository](https://github.com/chanzuckerberg/napari-hub-collections) and fill out the fields detailed below for your Collection before making a pull request to add your unique file to the [collections folder](collections). 

***NOTE:*** If you aren't comfortable with Github, email [Dannielle McCarthy](mailto:dmccarthy@chanzuckerberg.com) so that she can facilitate your Collection submission.

* **filename convention:** Use only plain text and dashes in place of spaces in the filename. (e.g. reader-plugins.yaml, electron-microscopy-toolkit.yaml, cell-segmentation-workflow.yaml, etc.) 

* **title:** Human-readable descriptive name of the Collection contents. (e.g. Reader Plugins, Electron Microscopy Toolkit, Cell Segmentation Workflow, etc.) You may use the name to specify if the Collection is a grouping of plugins or an ordered list of plugins for a certain task.

* **updated_date:** The date the Collection was submitted or last updated. This must be in ISO-8601 format within double quotes (e.g. "2022-05-24").

* **summary:** One-sentence overview of the Collection, displayed on the Collection card, to give napari users insight into what the Collection contains and how it will help them. (Max length: 75 characters with spaces)

* **description:** Longer description of the Collection, displayed at the top of the Collection page, to give napari users more background and context on the Collection, what the plugins do, and why it matters. (Max length: 500 characters with spaces)

* **cover_image:** A large image shown at the top of your Collection. Field must be populated with the full file name with the extension (e.g. `national-cancer-institute-lsxKuARrQXI-unsplash.jpg`) of an image in the [images folder](images). Browse the available images or upload your own. If you upload your own image, it should be a minimum of 1440px wide by a minimum of 640px tall (which is an aspect ratio of 9:4). The image’s actual shown aspect ratio will change depending upon the screen width of either the collections umbrella page or the individual collection page where it is viewed. It will range from being shown at the 9:4 aspect ratio on some screen widths of the collections umbrella page, to being shown at approximately 10:1 at its narrowest on the individual collection page (when the screen width is 1440px or greater).

* **plugins:** List of plugins in the Collection with each plugin's PyPI name (e.g. napari-sim-processor) and an optional comment about the plugin to let users know why this plugin matters.

* **curator information:** Information on you to share who created this Collection to the community. You can share your name, title, institution, website, ORCID ID, and links to twitter, GitHub and other relevant websites. 

* (optional) **visibility** Limit the visibility of your Collection on the napari hub. We support three levels of visibility: `public` (the default) means that the collection is available on the list of all Collections, `hidden` means that the collection page is available, but the collection does not show up in the list of collections, and `disabled` means that the collection does not show up on the napari hub

## Mockups

<img width="900" alt="image" src="https://user-images.githubusercontent.com/1245615/171043163-c4371b71-f1b7-480e-a770-b0e67317a68b.png">

<img width="1134" alt="image" src="https://user-images.githubusercontent.com/1245615/171042327-e9ff5a3a-adbf-4046-8dd9-9f97a5c5dacf.png">


## Code of Conduct

This project adheres to the Contributor Covenant [code of conduct](https://github.com/chanzuckerberg/.github/blob/master/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [opensource@chanzuckerberg.com](mailto:opensource@chanzuckerberg.com).

## Reporting Security Issues

If you believe you have found a security issue, please responsibly disclose by contacting us at [security@chanzuckerberg.com](mailto:security@chanzuckerberg.com).
