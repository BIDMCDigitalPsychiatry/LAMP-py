# LAMP-py

LAMP-py provides a python api client for the LAMP-server api. The python client is generated using OpenApiGenerator.
Do not edit the generated code directly, instead update the api spec from `LAMP-server`, or modify OpenApiGenerator
templates to add or change functionality.

## Steps to regenerate LAMP-py:
1. Copy the current version of the LAMP-server openapi spec into the root directory.
2. Delete the current `lampCore` directory
3. Create a new  `lampCore` directory
4. Copy `.openapi-generator-ignore.sample` into `./lampCore`. Name it `.openapi-generator-ignore`.
5. Run `npm install`
6. Run `npm run process_spec <path to open api spec>`
7. Run `npm run generate`

### The Process Spec Step

In order to maintain compatibility with previous versions of LAMP-py, the process spec step uses custom properties on each route to make changes to the spec before regenerating the client.

`x-internal`: When `true` the route is excluded from the python api client. Most authentication routes should be marked with `x-interal = true`. (Later versions of OpenApiGenerator support this property out of the box, but for now it must be dealt with as part of the process spec step.)

`x-python-settings`: An object with a variety of options properties for customizing the client routes generated.
- `name`: String. Sets the name of the python function used to call the endpoint by overriding the route's `operationId`.
- `pathParameterDefaults`: Replaces a url parameter with provided static value. Should be an object of the form `{"urlParameter": "defaultValue"}`.
- `anyJsonRequestBody`: Boolean. When `true`, do not type check the properties included in the json request body. Allows the python function to accept a regular dictionary rather than requiring an instance of a specific class.
- `replaceResponseContent`: Allows the python client to return regular dictionaries rather than special class instances. An object of the form `{"statusCode": "responseTypeKey"}`. `responseTypeKey` options include:
    - `"anyObject"`: An object with any properties
    - `"anyData"`: An object with the form: `{data: <any json value>}`
    - `"anyDataList"`: An object with the form: `{data: [<any json value>, <any json value>, ...]}`
    - `"any"`: Any json value


## Steps to publish LAMP-py:
1. Regenerate the library using the above steps
2. After reviewing, and testing the new package version, merge into main
3. Create a new release on github. Make sure to increment the package version number
4. Verify that the "Publish" github action ran without error
