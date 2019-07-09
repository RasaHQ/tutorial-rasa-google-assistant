# Place Finder assistant

This repository contains the code of the Rasa-powered Place Finder assistant.

## Setup and installation

In order to run this assistant, you will need Rasa and a few additional dependencies. You can install them all by running the following command:  

```
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
```  

You also need to install a spaCy English language model. You can install it by running:  

```
python -m spacy download en
```  

## What's in this repository
The repository consists of the following files and directories:  

- **data/nlu_data.md** - training data examples for Rasa NLU model
- **data/stories.md** - training data examples for Rasa Core model
- **actions.py** the code of the custom action used to retrieve data from Google Places API.
- **config.yml** contains the configuration of NLU processing pipeline.
- **ga_credentials.yml** is a file where you should place your Google Places API key.
- **domain.yml** file contains the domain configuration of the assistant.
- **endpoints.yml** contains the webhook configuration for the custom action.
- **ga_connector.py** contains the code of Rasa-Google Assistant connector.
- **credentials.yml** is a file where you have to configure your custom connector.
- **models** is a directory which contains the pretrained models for you to test.


To run this assistant you will need a [Google Place API](https://developers.google.com/places/web-service/get-api-key) key which you should provide inside the credentials.yml file of these directories.

## Let us know how you are getting on!   
If you have any questions regarding this repository, please post them on the [Rasa Community Forum](https://forum.rasa.com)!

