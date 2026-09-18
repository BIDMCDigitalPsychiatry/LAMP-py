import fs from 'node:fs'


const fileName = process.argv[2]

console.log("Processing: ", fileName)

const spec = JSON.parse(fs.readFileSync(fileName, "utf-8"))

spec.components.securitySchemes.OldServer = {
    type: "http",
    scheme: "basic",
}
console.log("SECURITY: ", spec.components.securitySchemes, "\n\n\n")

const newPaths = {}

for (let [pathName, path] of Object.entries(spec.paths)) {
    let newPath = {}
    let newPathName = pathName
    for (let [method, operation] of Object.entries(path)) {
        // Add basic auth to security schemes
        if (operation.security) {
            operation.security.push({"OldServer": []})
        } else {
            operation.security = [{"OldServer": []}]
        }

        // Do not generate client functions for endpoints marked with "x-internal"
        if (!operation["x-internal"]) {
            newPath[method] = operation
        }

        const pythonSettings = operation["x-python-settings"]
        if (pythonSettings) {
            // Set the name of the method to be generated for the sdk
            if (pythonSettings.name) {
                operation.operationId = pythonSettings.name
            }

            // Remove request body type checking. 
            // Useful when the request body can have more than one type which is not supported by generator version 5.3.1
            if (pythonSettings.anyJsonRequestBody) {             
                operation.requestBody.content = {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "additionalProperties": true
                        }
                    }
                }
            }

            if (pythonSettings.replaceResponseContent) {
                for (let [statusCode, replacementType] of Object.entries(pythonSettings.replaceResponseContent)) {
                    operation.responses[statusCode].content = getReponseContentReplacement(replacementType)
                }
            }

            // Replace path parameters with their defined defaults
            if (pythonSettings.pathParameterDefaults) {
                let currentPathName = pathName
                for (let [parameterName, defaultValue] of Object.entries(pythonSettings.pathParameterDefaults)) {
                    console.log(`${currentPathName} => `, currentPathName.replace(`{${parameterName}}`, defaultValue))
                    currentPathName = currentPathName.replace(`{${parameterName}}`, defaultValue)
                    operation.parameters = operation.parameters.filter((param) => !(param.name === parameterName && param.in === "path"))
                }
                newPathName = currentPathName
            }
        }
    }

    if (Object.keys(newPath).length) {
        newPaths[newPathName] = newPath
    }
}

spec.paths = newPaths
console.log(spec)

fs.writeFileSync('./processed_spec.json', JSON.stringify(spec));


function getReponseContentReplacement(replacementType) {
    let schema = replacementType
    if (replacementType === "anyObject") {
        schema = { 
            type: "object",
            additionalProperties: true
        }
    } else if (replacementType === "anyData") {
        schema = {
            type: "object",
            properties: {
                data: {
                    type: "object",
                    additionalProperties: true
                }
            }
        }
    } else if (replacementType === "anyDataList") {
        schema = {
            type: "object",
            properties: {
                data: {
                    type: "array",
                    items: {}
                }
            }
        }
    } else if (replacementType === "any") {
        schema = {}
    }

    return {
        "application/json": {
            "schema": schema
        }
    }
}