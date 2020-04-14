# Python API client for the LAMP Platform.

## Overview

This API client is used to connect to the LAMP Platform from the Python programming language. [Visit our documentation for more information about the LAMP Platform.](https://docs.lamp.digital/)

## Installation
### Prerequisites

Python 3.4+ and `pip`. 
  - You may need root permissions, using `sudo`.
  - Alternatively, to install locally, use `pip --user`.
  - If `pip` is not recognized as a command, use `python3 -m pip`.

### Installation

```sh
pip install LAMP-core
```

### Configuration

Ensure your `server_address` is set correctly. If using the default server, it will be `api.lamp.digital`. Keep your `access_key` (sometimes an email address) and `secret_key` (sometimes a password) private and do not share them with others.

```python
import LAMP
LAMP.connect(access_key, secret_key, server_address)
```

## API Endpoints

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*LAMP.API* | [**query**](docs/APIApi.md#query) | **POST** / | Query the LAMP Database.
*LAMP.API* | [**schema**](docs/APIApi.md#schema) | **GET** / | View the API schema document.
*LAMP.Activity* | [**all**](docs/ActivityApi.md#all) | **GET** /activity | Get the set of all activities.
*LAMP.Activity* | [**all_by_participant**](docs/ActivityApi.md#all_by_participant) | **GET** /participant/{participant_id}/activity | Get all activities for a participant.
*LAMP.Activity* | [**all_by_researcher**](docs/ActivityApi.md#all_by_researcher) | **GET** /researcher/{researcher_id}/activity | Get all activities for a researcher.
*LAMP.Activity* | [**all_by_study**](docs/ActivityApi.md#all_by_study) | **GET** /study/{study_id}/activity | Get all activities in a study.
*LAMP.Activity* | [**create**](docs/ActivityApi.md#create) | **POST** /study/{study_id}/activity | Create a new Activity under the given Study.
*LAMP.Activity* | [**delete**](docs/ActivityApi.md#delete) | **DELETE** /activity/{activity_id} | Delete an Activity.
*LAMP.Activity* | [**update**](docs/ActivityApi.md#update) | **PUT** /activity/{activity_id} | Update an Activity&#39;s settings.
*LAMP.Activity* | [**view**](docs/ActivityApi.md#view) | **GET** /activity/{activity_id} | Get a single activity, by identifier.
*LAMP.ActivityEvent* | [**all_by_participant**](docs/ActivityEventApi.md#all_by_participant) | **GET** /participant/{participant_id}/activity_event | Get all activity events for a participant.
*LAMP.ActivityEvent* | [**all_by_researcher**](docs/ActivityEventApi.md#all_by_researcher) | **GET** /researcher/{researcher_id}/activity_event | Get all activity events for a researcher by participant.
*LAMP.ActivityEvent* | [**all_by_study**](docs/ActivityEventApi.md#all_by_study) | **GET** /study/{study_id}/activity_event | Get all activity events for a study by participant.
*LAMP.ActivityEvent* | [**create**](docs/ActivityEventApi.md#create) | **POST** /participant/{participant_id}/activity_event | Create a new ActivityEvent for the given Participant.
*LAMP.ActivityEvent* | [**delete**](docs/ActivityEventApi.md#delete) | **DELETE** /participant/{participant_id}/activity_event | Delete a ActivityEvent.
*LAMP.ActivitySpec* | [**all**](docs/ActivitySpecApi.md#all) | **GET** /activity_spec | Get all ActivitySpecs registered.
*LAMP.ActivitySpec* | [**create**](docs/ActivitySpecApi.md#create) | **POST** /activity_spec | Create a new ActivitySpec.
*LAMP.ActivitySpec* | [**delete**](docs/ActivitySpecApi.md#delete) | **DELETE** /activity_spec/{activity_spec_name} | Delete an ActivitySpec.
*LAMP.ActivitySpec* | [**update**](docs/ActivitySpecApi.md#update) | **PUT** /activity_spec/{activity_spec_name} | Update an ActivitySpec.
*LAMP.ActivitySpec* | [**view**](docs/ActivitySpecApi.md#view) | **GET** /activity_spec/{activity_spec_name} | View an ActivitySpec.
*LAMP.Credential* | [**create**](docs/CredentialApi.md#create) | **POST** /type/{type_id}/credential | 
*LAMP.Credential* | [**delete**](docs/CredentialApi.md#delete) | **DELETE** /type/{type_id}/credential/{access_key} | 
*LAMP.Credential* | [**list**](docs/CredentialApi.md#list) | **GET** /type/{type_id}/credential | 
*LAMP.Credential* | [**update**](docs/CredentialApi.md#update) | **PUT** /type/{type_id}/credential/{access_key} | 
*LAMP.Participant* | [**all**](docs/ParticipantApi.md#all) | **GET** /participant | Get the set of all participants.
*LAMP.Participant* | [**all_by_researcher**](docs/ParticipantApi.md#all_by_researcher) | **GET** /researcher/{researcher_id}/participant | Get the set of all participants under a single researcher.
*LAMP.Participant* | [**all_by_study**](docs/ParticipantApi.md#all_by_study) | **GET** /study/{study_id}/participant | Get the set of all participants in a single study.
*LAMP.Participant* | [**create**](docs/ParticipantApi.md#create) | **POST** /study/{study_id}/participant | Create a new Participant for the given Study.
*LAMP.Participant* | [**delete**](docs/ParticipantApi.md#delete) | **DELETE** /participant/{participant_id} | Delete a participant AND all owned data or event streams.
*LAMP.Participant* | [**update**](docs/ParticipantApi.md#update) | **PUT** /participant/{participant_id} | Update a Participant&#39;s settings.
*LAMP.Participant* | [**view**](docs/ParticipantApi.md#view) | **GET** /participant/{participant_id} | Get a single participant, by identifier.
*LAMP.Researcher* | [**all**](docs/ResearcherApi.md#all) | **GET** /researcher | Get the set of all researchers.
*LAMP.Researcher* | [**create**](docs/ResearcherApi.md#create) | **POST** /researcher | Create a new Researcher.
*LAMP.Researcher* | [**delete**](docs/ResearcherApi.md#delete) | **DELETE** /researcher/{researcher_id} | Delete a researcher.
*LAMP.Researcher* | [**update**](docs/ResearcherApi.md#update) | **PUT** /researcher/{researcher_id} | Update a Researcher&#39;s settings.
*LAMP.Researcher* | [**view**](docs/ResearcherApi.md#view) | **GET** /researcher/{researcher_id} | Get a single researcher, by identifier.
*LAMP.Sensor* | [**all**](docs/SensorApi.md#all) | **GET** /sensor | Get the set of all sensors.
*LAMP.Sensor* | [**all_by_participant**](docs/SensorApi.md#all_by_participant) | **GET** /participant/{participant_id}/sensor | Get all sensors for a participant.
*LAMP.Sensor* | [**all_by_researcher**](docs/SensorApi.md#all_by_researcher) | **GET** /researcher/{researcher_id}/sensor | Get all sensors for a researcher.
*LAMP.Sensor* | [**all_by_study**](docs/SensorApi.md#all_by_study) | **GET** /study/{study_id}/sensor | View all sensors in a study.
*LAMP.Sensor* | [**create**](docs/SensorApi.md#create) | **POST** /study/{study_id}/sensor | Create a new Sensor under the given Study.
*LAMP.Sensor* | [**delete**](docs/SensorApi.md#delete) | **DELETE** /sensor/{sensor_id} | Delete a Sensor.
*LAMP.Sensor* | [**update**](docs/SensorApi.md#update) | **PUT** /sensor/{sensor_id} | Update an Sensor&#39;s settings.
*LAMP.Sensor* | [**view**](docs/SensorApi.md#view) | **GET** /sensor/{sensor_id} | Get a single sensor, by identifier.
*LAMP.SensorEvent* | [**all_by_participant**](docs/SensorEventApi.md#all_by_participant) | **GET** /participant/{participant_id}/sensor_event | Get all sensor events for a participant.
*LAMP.SensorEvent* | [**all_by_researcher**](docs/SensorEventApi.md#all_by_researcher) | **GET** /researcher/{researcher_id}/sensor_event | Get all sensor events for a researcher by participant.
*LAMP.SensorEvent* | [**all_by_study**](docs/SensorEventApi.md#all_by_study) | **GET** /study/{study_id}/sensor_event | Get all sensor events for a study by participant.
*LAMP.SensorEvent* | [**create**](docs/SensorEventApi.md#create) | **POST** /participant/{participant_id}/sensor_event | Create a new SensorEvent for the given Participant.
*LAMP.SensorEvent* | [**delete**](docs/SensorEventApi.md#delete) | **DELETE** /participant/{participant_id}/sensor_event | Delete a sensor event.
*LAMP.SensorSpec* | [**all**](docs/SensorSpecApi.md#all) | **GET** /sensor_spec | Get all SensorSpecs registered.
*LAMP.SensorSpec* | [**create**](docs/SensorSpecApi.md#create) | **POST** /sensor_spec | Create a new SensorSpec.
*LAMP.SensorSpec* | [**delete**](docs/SensorSpecApi.md#delete) | **DELETE** /sensor_spec/{sensor_spec_name} | Delete an SensorSpec.
*LAMP.SensorSpec* | [**update**](docs/SensorSpecApi.md#update) | **PUT** /sensor_spec/{sensor_spec_name} | Update an SensorSpec.
*LAMP.SensorSpec* | [**view**](docs/SensorSpecApi.md#view) | **GET** /sensor_spec/{sensor_spec_name} | Get a SensorSpec.
*LAMP.Study* | [**all**](docs/StudyApi.md#all) | **GET** /study | Get the set of all studies.
*LAMP.Study* | [**all_by_researcher**](docs/StudyApi.md#all_by_researcher) | **GET** /researcher/{researcher_id}/study | Get the set of studies for a single researcher.
*LAMP.Study* | [**create**](docs/StudyApi.md#create) | **POST** /researcher/{researcher_id}/study | Create a new Study for the given Researcher.
*LAMP.Study* | [**delete**](docs/StudyApi.md#delete) | **DELETE** /study/{study_id} | Delete a study.
*LAMP.Study* | [**update**](docs/StudyApi.md#update) | **PUT** /study/{study_id} | Update the study.
*LAMP.Study* | [**view**](docs/StudyApi.md#view) | **GET** /study/{study_id} | Get a single study, by identifier.
*LAMP.Type* | [**get_attachment**](docs/TypeApi.md#get_attachment) | **GET** /type/{type_id}/attachment/{attachment_key} | 
*LAMP.Type* | [**get_dynamic_attachment**](docs/TypeApi.md#get_dynamic_attachment) | **GET** /type/{type_id}/attachment/dynamic/{attachment_key} | 
*LAMP.Type* | [**list_attachments**](docs/TypeApi.md#list_attachments) | **GET** /type/{type_id}/attachment | 
*LAMP.Type* | [**parent**](docs/TypeApi.md#parent) | **GET** /type/{type_id}/parent | Find the owner(s) of the resource.
*LAMP.Type* | [**set_attachment**](docs/TypeApi.md#set_attachment) | **PUT** /type/{type_id}/attachment/{attachment_key}/{target} | 
*LAMP.Type* | [**set_dynamic_attachment**](docs/TypeApi.md#set_dynamic_attachment) | **PUT** /type/{type_id}/attachment/dynamic/{attachment_key}/{target} | 


## Documentation For Models

 - [AccessCitation](docs/AccessCitation.md)
 - [Activity](docs/Activity.md)
 - [ActivityEvent](docs/ActivityEvent.md)
 - [ActivitySpec](docs/ActivitySpec.md)
 - [Credential](docs/Credential.md)
 - [Document](docs/Document.md)
 - [DurationInterval](docs/DurationInterval.md)
 - [DurationIntervalLegacy](docs/DurationIntervalLegacy.md)
 - [DynamicAttachment](docs/DynamicAttachment.md)
 - [Error](docs/Error.md)
 - [Metadata](docs/Metadata.md)
 - [Participant](docs/Participant.md)
 - [Researcher](docs/Researcher.md)
 - [Sensor](docs/Sensor.md)
 - [SensorEvent](docs/SensorEvent.md)
 - [SensorSpec](docs/SensorSpec.md)
 - [Study](docs/Study.md)
 - [TemporalSlice](docs/TemporalSlice.md)
