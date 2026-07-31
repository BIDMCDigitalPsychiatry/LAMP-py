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

## Steps to publish LAMP-py:
1. Regenerate the library using the above steps
2. After reviewing, and testing the new package version, merge into main
3. Create a new release on github. Make sure to increment the package version number
4. Verify that the "Publish" github action ran without error