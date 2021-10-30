# Coding Exercise: Machine Learning Infrastructure Engineer

> **Overjet Confidential**: Please treat this as proprietary information. It is prohibited to distribute or share this test without explicit written permission from **Overjet**.

This is a coding exercise/assessment for Machine Learning (ML) Infrastructure Engineer candidates applying to [Overjet](https://overjet.ai). The goal is to follow the instructions provided here and complete as many of the exercises as possible, within the agreed time limit.

The time limit for this assessment is: `2 hours`.

At the end of 2 hours, please follow the instructions in the [Submit Results](#Submit-Results) section. We will then review your submission and discuss your process during a follow-up interview.

We're looking for creativity and a reflection of your skillset. Thanks!

<!-- MarkdownTOC -->

- [Setup](#setup)
    - [\(Optional\) direnv and pyenv](#optional-direnv-and-pyenv)
    - [Support Links](#support-links)
- [Coding Exercise Goals](#coding-exercise-goals)
    - [Flask App Goals](#flask-app-goals)
    - [Docker and Terraform Goals](#docker-and-terraform-goals)
- [Notes](#notes)
- [Submit Results](#submit-results)

<!-- /MarkdownTOC -->

## Setup

First, this is a Git repository, so please be sure that you have `git` available and configured.

Please commit all code changes however you believe would follow best-practices for professional Software Engineering.

You can assume that this task was given to you as a ticket named `TEST-2020`, so feel free to use that in any commits or branches you may create.

You do not need to use `direnv` or `pyenv`, but they're provided here for convenience. If you want to set them up and use them, go ahead, but don't feel compelled to get them setup. You can skip ahead to focus on the tasks as long as you have Python 3.x, [Docker](https://www.docker.com/get-started), and [Terraform](https://www.terraform.io/downloads.html) available to you.

### (Optional) direnv and pyenv

In this project folder you will find a `.envrc` file and a `.python-version` file, to be used with `direnv` and `pyenv` respectively. These can help provide a local virtual-environment for Python development. Feel free to modify them to use a different version of Python if needed.

To install [direnv](https://direnv.net/) you can use this command or follow the [install instructions](https://direnv.net/docs/installation.html):

```bash
curl -sfL https://direnv.net/install.sh | bash
```

To install [pyenv](https://github.com/pyenv/pyenv) you can use this command from the [pyenv installer](https://github.com/pyenv/pyenv-installer):

```bash
curl https://pyenv.run | bash
```

Or on macOS you can use [brew](https://brew.sh/) to install both -- and follow the `stdout` output to add them to your shell (`bash`, `zsh`, _etc._) config.

### Support Links

- https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
- https://www.cprime.com/resources/blog/docker-on-mac-with-homebrew-a-step-by-step-tutorial/
- https://learn.hashicorp.com/tutorials/terraform/install-cli
- https://varrette.gforge.uni.lu/blog/2019/09/10/using-pyenv-virtualenv-direnv/
- https://medium.com/swlh/setup-and-run-web-app-on-terraform-using-docker-c8e045da8860

## Coding Exercise Goals

These are the main goals of the exercise. You should try to complete these in order, but feel free to jump between them and get as much done as you can.

The overall goal is to have a locally running Docker Image deployed through Terraform (locally, not in any Cloud Service) with a Webserver, where the webpage performs some Machine Learning tasks.

1. Create a dependency management file for your Python code (`requirements.txt`, `poetry`, `pipenv`, _etc._).
2. Edit the `main.py` and create any other Python modules to build-out the features described below, using professional, modern Python 3.x syntax.
3. Create a Dockerfile and build a Docker Image that hosts the webserver and Python Flask app with your updated code.
4. Create a Terraform script (and any other config files) to build a local infrastructure that will run a container based-on the Docker image.

### Flask App Goals

1. Use the `static_files` directory to host the `index.html` file.
2. Use the upload form in the HTML file to upload an image and read that image into your Flask app.
3. Create a function that parses the input image into a Python object (using `PIL`, `Pillow`, or `numpy`).
4. Create a function that takes input arguments (these can be static, or read from the HTML page) for a desired width and height for the image, and resizes the image to that new size.
5. Create a function that returns a randomly positioned, fixed-sized rectangle of pixel values from within the bounds of a given image.
6. Call the function (from step 5) twice to get two random sub-images from the input image.
7. Treat one of the rectangles as "Ground Truth" and the other as "Test Data" -- you can simplify this to just use the grayscale pixel values or select 1 of the color channels. Compare the pixels of the two rectangles from your uploaded image, as if they were Test Data and Ground Truth, by computing a Confusion Matrix and any other test statistics you feel comfortable explaining.
8. Update the HTML file and/or the Flask app to report your comparison statistics and metrics between the two rectangles from the image, by showing them on the webpage. This can be automated after the image upload or triggered by a separate button press or action on the webpage.
9. Similarly, provide a response on the webpage that indicates whether the two rectangles from the image overlap, and by what percentage of the fixed-size area of the rectangle (_i.e._, `100%` overlap means that both `W-by-H` rectangles are centered on the same pixel).
10. (Optional) Show the original image, the resized image, and the two rectangles on the webpage along with the statistics.

Try to complete as many steps as possible -- if you are having trouble with the webapp, please focus on the Python and Machine Learning code. Create as many metrics or measurements as you can for Step 7, in the time allotted, to best show your Machine Learning and Data Science experience.

### Docker and Terraform Goals

1. Host a webserver and the Flask app.
2. Make the Flask app accessible at port `8080` when run locally.
3. Use Terraform with the `terraform-providers/docker` Provider, to run your Docker Image as a container with the specific port exposed.

## Notes

- There is no requirement for unit tests for the Python web-app.
- There is no requirement to upload the Docker image to a container registry.
- There is no requirement to deploy this to a Cloud service, please ensure that it can run in a local development environment.

## Submit Results

At the end of the time period:

- Please make sure you have committed all your changes to the local git repository in this project folder.
- Zip the entire project directory, and email to `<tommy@overjet.ai>`, and CC: `<deepak@overjet.ai>`

You can provide any notes or links you want to share in the email or here in the project directory.
